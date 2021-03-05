import re
import math
import numpy
import vg
from pathlib import Path

class fileLine:
    """A single line from a G-code file"""
    def __init__ (self, lineString):
        self.lineStr = lineString.strip()
        self.newLineStr = ''
        self.newLineLen = 0
        self.newLineRead = 0
        self.lineChunks = self.listChunks(lineString)
        self.charCount = self.length()
        if '(' in lineString:
            self.hasComment = True
        else:
            self.hasComment = False
        if len(lineString.strip()) == 0:
            self.isBlank = True
        else:
            self.isBlank = False
        self.isMove = False
        self.isLinear = False
        self.isIJKArc = False
        self.isRArc = False
        self.isShort = False
        if lineString[0] == '%':
            self.percent = True
        else:
            self.percent = False
        self.f = None
        self.g = None
        self.x = None
        self.y = None
        self.z = None
        self.i = 0
        self.j = 0
        self.k = 0
        self.r = None
        self.plane = None
        self.readTime = None
        self.origMoveTime = None #will be updated during file processing
        self.startPoint = None #will be updated with a point during file processing
        self.endPoint = None #will be updated with a point during file processing
        self.distance = None #will be updated during file processing
        self.dwell = False
        self.idealFeed = 0
        self.finalFeed = 0
        self.modFeedThisLine = False
        self.feedChunkIndex = None
        self.originalLineTime = None
        self.finalLineTime = None

        chunkIndex = 0
        for chunk in self.lineChunks:
            if chunk[0] == 'G':
                if chunk in ['G00','G01','G02','G03','G0','G1','G2','G3']:
                    self.g = int(chunk[1:])
                    self.isMove = True
                    self.isLinear = True
                if chunk in ['G17']: self.plane = 'XY'
                if chunk in ['G18']: self.plane = 'ZX'
                if chunk in ['G19']: self.plane = 'YZ'
            if chunk[0] == 'F':
                self.f = float(chunk[1:])
                #self.feedChunkIndex = chunkIndex #move this from here to a point right before editing the feed rate, after line numbers have been removed
            if chunk[0] == 'X': 
                self.x = float(chunk[1:])
                self.isMove = True
            if chunk[0] == 'Y': 
                self.y = float(chunk[1:])
                self.isMove = True
            if chunk[0] == 'Z': 
                self.z = float(chunk[1:])
                self.isMove = True
            if chunk[0] == 'I':
                self.i = float(chunk[1:])
                self.isIJKArc = True
            if chunk[0] == 'J':
                self.j = float(chunk[1:])
                self.isIJKArc = True
            if chunk[0] == 'K':
                self.k = float(chunk[1:])
                self.isIJKArc = True
            if chunk[0] == 'R': 
                self.r = float(chunk[1:])
                self.isRArc = True
            chunkIndex += 1

    def listChunks(self, lineString): #separate gcode into a list of strings
        if lineString[0] == 'O': #program number        
            chunks = [lineString.rstrip().replace(';','')]
        elif lineString[0] == '(': #comment
            chunks = [lineString.rstrip().replace(';','')]
        else: #disassemble it
            chunks = re.findall(r'[A-Z][^A-Z, ,;]+|[(].+[)]', lineString)
        return chunks

    def length(self):
        return len(self.lineStr)

    def updateWithModals(self, modal):
        if self.g is None: self.g = modal.g
        if modal.g in [0,1]: self.isLinear = True
        #assume that the arc true/false is set because line included I/J/K/R
        if self.f == 0 or self.f is None: self.f = modal.f
        if self.plane is None: self.plane = modal.plane

    def calcDistance(self):
        if self.isMove == True:
            if self.isLinear == True: #find the linear distance between points
                self.distance = round(math.sqrt((self.endPoint.x-self.startPoint.x)**2+(self.endPoint.y-self.startPoint.y)**2+(self.endPoint.z-self.startPoint.z)**2), 4)
            elif self.isIJKArc == True: #find the arc distance using IJK
                #boop the coordinates into vectors
                if self.g == 2: #G02 is clockwise
                    vec2 = numpy.array([self.startPoint.x - self.i, self.startPoint.y - self.j, self.startPoint.z - self.k])
                    vec1 = numpy.array([self.endPoint.x - self.i, self.endPoint.y - self.j, self.endPoint.z - self.k])
                else: #counterclockwise
                    vec1 = numpy.array([self.startPoint.x - self.i, self.startPoint.y - self.j, self.startPoint.z - self.k])
                    vec2 = numpy.array([self.endPoint.x - self.i, self.endPoint.y - self.j, self.endPoint.z - self.k])

                #find the radius
                #Old: radius = round(math.sqrt((self.endPoint.x - self.i)**2 + (self.endPoint.y - self.j)**2 + (self.endPoint.z - self.k)**2), 4)
                #need to figure out the center point instead of the offset
                radius = round(math.sqrt((self.endPoint.x - self.startPoint.x - self.i)**2 + (self.endPoint.y - self.startPoint.y - self.j)**2 + (self.endPoint.z - self.startPoint.z - self.k)**2), 4)

                if self.startPoint == self.endPoint: #this is a complete circle
                    self.distance = round(2*numpy.pi*radius, 4)
                else:
                    #calculate the angle based on the plane
                    if self.plane == 'XY':
                        angle = vg.signed_angle(vec1, vec2, look=vg.basis.z)
                    elif self.plane == 'ZX':
                        angle = vg.signed_angle(vec1, vec2, look=vg.basis.y)
                    elif self.plane == 'YZ':
                        angle = vg.signed_angle(vec1, vec2, look=vg.basis.x)

                    #negative angle indicates obtuse
                    if angle < 0:
                        angle += 360
                    self.distance = round(2*numpy.pi*radius*(angle/360),4)
            else: #find the arc distance using R (not implemented yet)
                pass

        else:
            self.distance = None

    def csvLine(self):

        #"Original Line,New Line,Start Point,End Point,Distance,Read Time,Move Time,Dwell,Short"
        list = ['"' + self.lineStr + '"', '"' + self.newLineStr + '"', self.startPoint.string(), self.endPoint.string(), str(self.distance), str(self.f), str(self.readTime), str(self.origMoveTime), str(self.originalLineTime), str(self.isShort), str(self.dwell), str(self.idealFeed), str(self.newLineRead), str(self.finalLineTime), str(self.finalFeed), str(self.modFeedThisLine)]
        s = ','.join(list) + '\n'
        return s

class point:
    def __init__ (self, x = 0, y = 0, z = 0):
        self.x = x
        self.y = y
        self.z = z

    def __add__ (self, point):
        self.x += point.x
        self.y += point.y
        self.z += point.z
        return self

    def __str__ (self):
        out = 'X' + str(self.x) + ' Y' + str(self.y) + ' Z' + str(self.y)
        return out

    def string(self):
        out = 'X' + str(self.x) + ' Y' + str(self.y) + ' Z' + str(self.y)
        return out

class modal: #use to store the state of modals and position we care about
    g = 0
    f = 0
    x = 0
    y = 0
    z = 0
    plane = 'XY'
    abs = True #incremental = false

    def update(self, line): #given a line, update the internal states
        if line.g is not None: self.g = line.g
        if line.f is not None: self.f = line.f
        if line.plane is not None: self.plane = line.plane

        #positions
        self.x = line.endPoint.x
        self.y = line.endPoint.y
        self.z = line.endPoint.z

class result:
    inFileSize = 0
    inFileLines = 0
    inFileTime = 0
    outFileSize = 0
    outFileLines = 0
    outFileTime = 0
    shortMoves = 0
    dwellLines = 0
    distance = 0

def calcReadTime(charCount, c):
    return (charCount * c.charMs) + c.lineMs

def calcMoveTime(distance, feed):
    if distance == 0 or feed == 0 or distance is None: time = 0
    else: time = round(distance / feed * 60 * 1000) #assume feed is always in units per minute
    return time

def getEndPoint(modal, line):
    if modal.abs == True: #absolute
        if line.x is None: 
            tempX = modal.x 
        else: 
            tempX = line.x
        if line.y is None: 
            tempY = modal.y 
        else: 
            tempY = line.y
        if line.z is None: 
            tempZ = modal.z 
        else: 
            tempZ = line.z
    else: #incremental
        if line.x is None: 
            tempX += modal.x 
        else: 
            tempX += line.x
        if line.y is None: 
            tempY += modal.y 
        else: 
            tempY += line.y
        if line.z is None: 
            tempZ += modal.z 
        else: 
            tempZ += line.z
    endPoint = point(tempX, tempY, tempZ)
    return endPoint

def lineToString(chunks, c, num = 0): #transform a list of chunks into a single string
    #c is the configuration object
    counter = 0
    outString = ''
    for chunk in chunks:
        chunk = chunk.strip()
        
        if c.rTrailingZeroes == True and chunk.find('.') >= 0:
            outString += str(chunk).rstrip('0')
        elif c.rComments == True and chunk[0] == '(':
            pass
        else:
            outString += str(chunk)
        
        if c.rSpaces == False and counter + 1 < len(chunks):
            outString += ' '
        
        if counter + 1 == len(chunks) and c.eob != '' and len(outString.strip()) > 0:
            outString += c.eob
        
        counter += 1
        
    return outString

def calcIdealFeed(distance, time): #calculate feed rate units per minute given distance and time in milliseconds
    idealFeed = round(distance / (time/1000/60),1)
    return idealFeed

def calcFinalFeed(line, prevFeed, c): #using the configuration options, figure out the right feed rate

    if line.idealFeed == 0: #if there was no ideal feed, this may be a non-move, just inherit the previous one
        finalFeed = prevFeed

    elif c.increaseFeed == True: #if increasing is allowed, do it
        if line.idealFeed > c.feedCeiling: #limit it to the ceiling
            finalFeed = c.feedCeiling
        else: #or just use it as is
            finalFeed = line.idealFeed

    else: #otherwise decrease only
        if line.idealFeed < line.f: #if the new feed is smaller, use it
            finalFeed = line.idealFeed
        else: #just use the original feed
            finalFeed = line.f
    
    if c.minFeed == True: #if there is a floor, lift up any smaller ones to that level
        if finalFeed < c.minFeedLimit:
            finalFeed = c.minFeedLimit

    if c.reduceFeed == True: #if there is a multiplier, do it
        finalFeed *= round(c.optimizePercent/100,1)

    #then compare it to the previous line, and don't bother changing if it's too close
    if abs(finalFeed - prevFeed) < c.diffThreshold:
        finalFeed = prevFeed

    return finalFeed

def getFeedChunkIndex(line):
    #locate the feed chunk if it exists in this line
    chunkCounter = 0
    chunkIndex = None
    for chunk in line.lineChunks:
        if chunk[0] == 'F': chunkIndex = chunkCounter
        chunkCounter += 1
    
    return chunkIndex

def process_files(c):
    curModal = modal()
    lines = []
    inFile = open(c.inPath)
    out_results = result()
    outNumber = 0
    
    #First loop: the input file
    curLine = 0
    tempTime = 0
    for inLine in inFile:
        #create a line object
        lines.append(fileLine(inLine))
        
        #determine the start point
        if curLine == 0:
            lines[curLine].startPoint = point()
        else:
            lines[curLine].startPoint = lines[curLine - 1].endPoint
        #determine the end point
        lines[curLine].endPoint = getEndPoint(curModal, lines[curLine])
        
        #update the modal.  position should be the endpoint of the current line
        curModal.update(lines[curLine])

        #update the line to complete it with some things from the modal
        lines[curLine].updateWithModals(curModal)

        #calculate the distance
        lines[curLine].calcDistance()
        if lines[curLine].distance is not None and lines[curLine].distance < c.shortThreshold: lines[curLine].isShort = True

        #calculate the read time
        lines[curLine].readTime = calcReadTime(lines[curLine].charCount, c)
        lines[curLine].newLineRead = lines[curLine].readTime
        
        #calculate the travel time
        if lines[curLine].distance:
            lines[curLine].origMoveTime = calcMoveTime(lines[curLine].distance, lines[curLine].f)

        #sum up the total time for the original file
        if lines[curLine].origMoveTime is not None and lines[curLine].readTime is not None:
            tempTime = max(lines[curLine].origMoveTime, lines[curLine].readTime)
        elif lines[curLine].origMoveTime is not None:
            tempTime = lines[curLine].origMoveTime
        elif lines[curLine].readTime is not None:
            tempTime = lines[curLine].readTime
        else:
             tempTime += 0   

        out_results.inFileTime += tempTime
        lines[curLine].originalLineTime = tempTime


        #end of loop
        curLine += 1
    
    #Close the input file
    out_results.inFileSize = Path(c.inPath).stat().st_size
    out_results.inFileLines = curLine
    inFile.close()

    #Create the output file(s)
    outFile = open(c.outPath, 'w')
    if c.outCsv == True:
        csvOut = open(c.outCsvPath, 'w')
        csvOut.write('Original Line,New Line,Start Point,End Point,Distance,Original Feed,Original Read Time,Original Line Time,Move Time,Short,Dwell,Maximum Feed,New Read Time,Final Line Time,Final Feed,Modify Feed On This Line?\n')
    
    #second loop: calculate the best feed rate and output a file
    curOutLine = 0
    outLineCount = 0
    prevFinalFeed = 0
    for outLine in lines:
        
        print(outLineCount) #for debugging

        #inherit the feed from the previous line before starting (it will be overwritten if necessary)
        lines[curOutLine].finalFeed = prevFinalFeed

        #skip the line if it is blank and should be removed
        if outLine.isBlank == True and c.rBlankLines == True:
            pass
        elif outLine.percent == True:
            outFile.write('%\n')
            outLineCount += 1
        else:
        
            #do whatever is needed with the line numbers
            if c.rLineNum == True and outLine.isBlank == False: #remove them
                for chunk in lines[curOutLine].lineChunks:
                    if chunk[0] == 'N': lines[curOutLine].lineChunks.remove(chunk)
            elif c.renumber == True and outLine.isBlank == False and lines[curOutLine].lineChunks[0][0] != 'O': #Replace or add numbers
                if lines[curOutLine].lineChunks[0][0] == 'N': #replace this chunk with a new one (Assume it is the first chunk, this could lead to bugs)
                    lines[curOutLine].lineChunks[0] = 'N' + str(outNumber)
                    outNumber += c.numInc
                else: #add a new chunk
                    lines[curOutLine].lineChunks.insert(0, 'N' + str(outNumber))
                    outNumber += c.numInc
                    
            
            #create the new line with basic optimizations
            lines[curOutLine].newLineStr = lineToString(outLine.lineChunks, c)
            lines[curOutLine].newLineLen = len(lines[curOutLine].newLineStr.strip())
            lines[curOutLine].newLineRead = calcReadTime(lines[curOutLine].newLineLen, c)
            if len(lines[curOutLine].newLineStr.strip()) == 0:
                lines[curOutLine].isBlank == True
            
            #compare the time required for the current move to the time required to have the next one ready 
            accumulatedReadTime = 0
            if outLine.isMove == True and outLine.distance > 0 and curOutLine < len(lines):

                #find the minimum time for this move - to prevent dwelling
                
                #look forward to the next line that moves and figure out how much read time is needed
                nextOutLine = curOutLine + 1
                while nextOutLine < len(lines) and lines[nextOutLine].isMove == False:
                    accumulatedReadTime += lines[nextOutLine].newLineRead
                    nextOutLine += 1
                else: 
                    if nextOutLine < len(lines):
                        accumulatedReadTime += lines[nextOutLine].newLineRead

                #calculate the fastest feed rate for this line before starving
                lines[curOutLine].idealFeed = calcIdealFeed(outLine.distance, accumulatedReadTime)
                #note if the original feed was too high
                if accumulatedReadTime > lines[curOutLine].origMoveTime: lines[curOutLine].dwell = True

                #make changes to the feed rate if desired
                if c.optimizeFeed == True:
                    #figure out the best feed rate
                    tempFeed = calcFinalFeed(outLine, prevFinalFeed, c)
                    lines[curOutLine].finalFeed = tempFeed
                    lines[curOutLine].feedChunkIndex = getFeedChunkIndex(lines[curOutLine])

                    #compare it to the previous rate and determine if a new one needs to be appended to the string
                    if tempFeed != prevFinalFeed: 
                        lines[curOutLine].modFeedThisLine = True
                        #if there is and F chunk, replace it
                        if lines[curOutLine].feedChunkIndex is not None:
                            lines[curOutLine].lineChunks.pop(lines[curOutLine].feedChunkIndex)
                            lines[curOutLine].lineChunks.append('F' + str(tempFeed).rstrip('0').lstrip('0'))
                        #otherwise append one
                        else:
                            lines[curOutLine].lineChunks.append('F' + str(tempFeed).rstrip('0').lstrip('0'))

                    elif lines[curOutLine].feedChunkIndex is not None: #no feed change from previous line, check if there was an existing F and remove it
                        del lines[curOutLine].lineChunks[lines[curOutLine].feedChunkIndex]

                    #then regenerate the new line string
                    lines[curOutLine].newLineStr = lineToString(lines[curOutLine].lineChunks, c)

                else:
                    lines[curOutLine].finalFeed = outLine.f

            prevFinalFeed = lines[curOutLine].finalFeed

            #double check the new string just in case it became blank
            if len(outLine.newLineStr) == 0: lines[curOutLine].isBlank = True
          

            #calculate the final time for the line, greater of read or travel
            out_results.outFileTime += max(calcReadTime(len(outLine.newLineStr), c), calcMoveTime(outLine.distance, lines[curOutLine].finalFeed))

            #also add it back to the line to be printed in the CSV
            lines[curOutLine].finalLineTime = max(calcReadTime(len(outLine.newLineStr), c), calcMoveTime(outLine.distance, lines[curOutLine].finalFeed))

            #write the output file
            if c.rBlankLines == True and lines[curOutLine].isBlank == True:
                pass
            else:
                outFile.write(outLine.newLineStr + '\n')
                outLineCount += 1

            #write a CSV if required
            if c.outCsv == True: csvOut.write(outLine.csvLine())

        #record some stats
        if lines[curOutLine].dwell == True: out_results.dwellLines += 1
        if lines[curOutLine].isShort == True: out_results.shortMoves += 1


        curOutLine += 1
        
    outFile.close()
    if c.outCsv == True: csvOut.close()

    #summarize some values for feedback
    out_results.outFileSize = Path(c.outPath).stat().st_size
    out_results.outFileLines = outLineCount    
    return out_results
