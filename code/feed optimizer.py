import wx
import feed_ui as ui
import main_process
import configparser
import os

def printAttributes(object):
    attrs = vars(object)
    print(''.join("%s: %s \n" % item for item in attrs.items()))

class appConfig: #object to store all configuration variables for the main process
    #need to make a duplicate for storing default values, give the class a copy method and use a copy for the one sent to the processing function
    inPath = ''
    outPath = ''
    outCsv = True
    outCsvPath = ''
    eob = ';'
    lineOption = 0
    rLineNum = False
    renumber = False
    numInc = 10
    rComments = False
    rBlankLines = False
    rSpaces = False
    rTrailingZeroes = True
    shortThreshold = .001
    optimizeFeed = False
    increaseFeed = False
    feedCeiling = 77
    reduceFeed = False
    optimizePercent = 100
    minFeed = False
    minFeedLimit = .25
    diffThreshold = .3 

    lineMs = 100
    charMs = 8

class appFrame(ui.main_frame):
    #constructor
    def __init__(self,parent):
        #initialize parent class
        ui.main_frame.__init__(self,parent)

    def browse_input(self, event):
        wildcard = '*.txt;*.nc'
        with wx.FileDialog(None, "Choose a file", wildcard=wildcard, style=wx.FD_OPEN) as dialog:
            if dialog.ShowModal() == wx.ID_OK:
                self.input_text.SetValue(dialog.GetPath())

    def browse_output(self, event):
        wildcard = '*.txt;*.nc'
        with wx.FileDialog(None, "Choose a file", wildcard=wildcard, style=wx.FD_OPEN) as dialog:
            if dialog.ShowModal() == wx.ID_OK:
                self.output_text.SetValue(dialog.GetPath())

    def browse_csv(self, event):
        wildcard = '*.csv'
        with wx.FileDialog(None, "Choose a file", wildcard=wildcard, style=wx.FD_OPEN) as dialog:
            if dialog.ShowModal() == wx.ID_OK:
                self.csv_text.SetValue(dialog.GetPath())

    def optimize_enable(self, event):
        if self.optimize_feed_checkbox.GetValue() == True:
            self.increase_feed_checkbox.Enable()
            self.reduce_feed_checkbox.Enable()
            self.feed_limit_text.Enable()
            self.reduce_feed_slider.Enable()
            self.min_feed_checkbox.Enable()
            self.min_feed_text.Enable()
            self.small_feed_diff_text.Enable()
            self.small_feed_desc.Enable()
        else:
            self.increase_feed_checkbox.Disable()
            self.reduce_feed_checkbox.Disable()
            self.feed_limit_text.Disable()
            self.reduce_feed_slider.Disable()
            self.min_feed_checkbox.Disable()
            self.min_feed_text.Disable()
            self.small_feed_diff_text.Disable()
            self.small_feed_desc.Disable()

    def csv_enable(self, event):
        if self.csv_checkbox.GetValue() == True:
            self.csv_button.Enable()
            self.csv_text.Enable()
        else:
            self.csv_button.Disable()
            self.csv_text.Disable()

    def read_form_config(self): #read all the inputs into a config object
        cf.inPath = self.input_text.GetValue()
        cf.outPath = self.output_text.GetValue()
        cf.outCsv = self.csv_checkbox.GetValue()
        cf.outCsvPath = self.csv_text.GetValue()
        cf.eob = self.eob_text.GetValue()
       
        cf.lineOption = self.linenum_radio.GetSelection()
        if cf.lineOption == 0:
            cf.rLineNum = False
            cf.renumber = False
        elif cf.lineOption == 1:
            cf.rLineNum = True
            cf.renumber = False
        else:
            cf.rLineNum = False
            cf.renumber = True
        cf.numInc = int(self.linenum_increment_text.GetValue())

        cf.rSpaces = self.remove_spaces_checkbox.GetValue()
        cf.rComments = self.remove_comments_checkbox.GetValue()
        cf.rBlankLines = self.remove_blanks_checkbox.GetValue()
        cf.rTrailingZeroes = self.remove_zeroes_checkbox.GetValue()
        #cf.rShortLines = False not on UI yet
        #cf.shortThreshold = .001 #done-
        cf.optimizeFeed = self.optimize_feed_checkbox.GetValue()
        cf.reduceFeed = self.reduce_feed_checkbox.GetValue()
        cf.minFeed = self.min_feed_checkbox.GetValue()
        if cf.optimizeFeed == False: #negate the values of some selections that are disabled
            cf.increaseFeed == False
            cf.optimizePercent = 100
            cf.minFeed == False
        else:
            cf.increaseFeed = self.increase_feed_checkbox.GetValue()
            if cf.reduceFeed == True:
                cf.optimizePercent = int(self.reduce_feed_slider.GetValue())
            else:
                cf.optimizePercent = 100
            if cf.minFeed == True:
                cf.minFeedLimit = float(self.min_feed_text.GetValue())
        
        cf.feedCeiling = float(self.feed_limit_text.GetValue())
        #cf.minTimeSaving = 300 #don't bother increasing the feed rate if it saves less than this, to preserve file size (milliseconds) (not implemented yet)
        cf.diffThreshold = float(self.small_feed_diff_text.GetValue()) #done smallest feed rate to change for #not in UI yet
        cf.lineMs = int(self.time_block_slider.GetValue())
        cf.charMs = int(self.time_char_slider.GetValue() / 10)
        return cf

    def write_form_config(self, inConfig): #write a config object into the form
        self.input_text.SetValue(inConfig.inPath)
        self.output_text.SetValue(inConfig.outPath)
        self.csv_checkbox.SetValue(inConfig.outCsv)
        self.csv_text.SetValue(inConfig.outCsvPath)

        self.optimize_feed_checkbox.SetValue(inConfig.optimizeFeed)
        self.increase_feed_checkbox.SetValue(inConfig.increaseFeed)
        self.feed_limit_text.SetValue(str(inConfig.feedCeiling))
        self.reduce_feed_checkbox.SetValue(inConfig.reduceFeed)
        self.reduce_feed_slider.SetValue(inConfig.optimizePercent)
        self.min_feed_checkbox.SetValue(inConfig.minFeed)
        self.min_feed_text.SetValue(str(inConfig.minFeedLimit))
        self.small_feed_diff_text.SetValue(str(inConfig.diffThreshold))
        
        self.remove_blanks_checkbox.SetValue(inConfig.rBlankLines)
        self.remove_comments_checkbox.SetValue(inConfig.rComments)
        self.remove_spaces_checkbox.SetValue(inConfig.rSpaces)
        self.remove_zeroes_checkbox.SetValue(inConfig.rTrailingZeroes)
        self.linenum_increment_text.SetValue(str(inConfig.numInc))
        self.eob_text.SetValue(inConfig.eob)
        self.linenum_radio.SetSelection(inConfig.lineOption)
        
        self.time_block_slider.SetValue(inConfig.lineMs)
        self.time_char_slider.SetValue(inConfig.charMs * 10)

    def write_results(self, result, config): #print out the contents of the result object
        #first clear the text
        self.result_text.Clear()
        self.result_text.AppendText('Input File:\t\t\t' + config.inPath +'\n')
        self.result_text.AppendText('Output File:\t\t' + config.outPath +'\n')
        self.result_text.AppendText('\n')
        self.result_text.AppendText('Original File Size:\t\t' + str(round(result.inFileSize/1024,1)) + ' kb\n')
        self.result_text.AppendText('Original File Lines:\t\t' + str(result.inFileLines) + '\n')
        self.result_text.AppendText('Original Estimated Time:\t' + str(round(result.inFileTime/60)) + ' seconds\n')
        self.result_text.AppendText('\n')
        self.result_text.AppendText('Short moves under ' + str(config.shortThreshold) + ':\t' + str(result.shortMoves) + '\n')
        self.result_text.AppendText('Lines causing dwell:\t\t' + str(result.dwellLines) + '\n')
        self.result_text.AppendText('\n')
        self.result_text.AppendText('New File Size:\t\t' + str(round(result.outFileSize/1024,1)) + ' kb\n')
        self.result_text.AppendText('New File Lines:\t\t' + str(result.outFileLines) + '\n')
        self.result_text.AppendText('New Estimated Time:\t\t' + str(round(result.outFileTime/60)) + ' seconds\n')
        self.result_text.AppendText('\n')
        self.result_text.AppendText('Time Difference:\t\t' + str((result.outFileTime - result.inFileTime) // 1000) + ' seconds\n')

        self.main_notebook.ChangeSelection(4)

    def readConfig(self, c): #find and open a config file, or if it doesn't exist, create it with the defaults
        config = configparser.ConfigParser()
        if not os.path.exists('settings.ini'):
            self.writeConfig(c)
        else: #read the file
            config.read('settings.ini')
            c.inPath = config['FILES']['InputFile']
            c.outPath = config['FILES']['OutputFile']
            c.outCsv = config['FILES'].getboolean('CSVOutput')
            c.outCsvPath = config['FILES']['CSVFile']

            c.optimizeFeed = config['FEED'].getboolean('Optimize_Enabled')
            c.increaseFeed = config['FEED'].getboolean('Increase_Enabled')
            c.feedCeiling = float(config['FEED']['Max_Feed'])
            c.reduceFeed = config['FEED'].getboolean('Modify_Feed_Enabled')
            c.optimizePercent = int(config['FEED']['Modify_Feed_Percent'])
            c.minFeed = config['FEED'].getboolean('Min_Feed_Enabled')
            c.minFeedLimit = float(config['FEED']['Min_Feed'])
            c.diffThreshold = float(config['FEED']['Diff_Threshold'])

            c.lineOption = int(config['FILE_OPTIONS']['Line_Number_Option'])
            c.numInc = int(config['FILE_OPTIONS']['Line_Number_Increment'])
            c.rBlankLines = config['FILE_OPTIONS'].getboolean('Remove_Blank_Lines')
            c.rComments = config['FILE_OPTIONS'].getboolean('Remove_Comments')
            c.rSpaces = config['FILE_OPTIONS'].getboolean('Remove_Spaces')
            c.rTrailingZeroes = config['FILE_OPTIONS'].getboolean('Remove_Trailing_Zeroes')
            c.eob = config['FILE_OPTIONS']['End_of_block']

            c.lineMs = int(config['OTHER']['Block_time_factor'])
            c.charMs = int(config['OTHER']['Char_time_factor'])
            c.shortThreshold = float(config['OTHER']['Short_move_threshold'])

            self.write_form_config(c)

        return c

    def writeConfig(self, c): #write a configuration file
        config = configparser.ConfigParser()
        config['FILES'] = {}
        config['FILES']['InputFile'] = c.inPath
        config['FILES']['OutputFile'] = c.outPath
        config['FILES']['CSVOutput'] = str(c.outCsv)
        config['FILES']['CSVFile'] = c.outCsvPath
        
        config['FEED'] = {}
        config['FEED']['Optimize_Enabled'] = str(c.optimizeFeed)
        config['FEED']['Increase_Enabled'] = str(c.increaseFeed)
        config['FEED']['Max_Feed'] = str(c.feedCeiling)
        config['FEED']['Modify_Feed_Enabled'] = str(c.reduceFeed)
        config['FEED']['Modify_Feed_Percent'] = str(c.optimizePercent)
        config['FEED']['Min_Feed_Enabled'] = str(c.minFeed)
        config['FEED']['Min_Feed'] = str(c.minFeedLimit)
        config['FEED']['Diff_Threshold'] = str(c.diffThreshold)

        config['FILE_OPTIONS'] = {}
        config['FILE_OPTIONS']['Line_Number_Option'] = str(c.lineOption) #Figure out how to deal with the radio button
        config['FILE_OPTIONS']['Line_Number_Increment'] = str(c.numInc)
        config['FILE_OPTIONS']['Remove_Blank_Lines'] = str(c.rBlankLines)
        config['FILE_OPTIONS']['Remove_Comments'] = str(c.rComments)
        config['FILE_OPTIONS']['Remove_Spaces'] = str(c.rSpaces)
        config['FILE_OPTIONS']['Remove_Trailing_Zeroes'] = str(c.rTrailingZeroes)
        config['FILE_OPTIONS']['End_of_block'] = c.eob

        config['OTHER'] = {}
        config['OTHER']['Block_time_factor'] = str(c.lineMs)
        config['OTHER']['Char_time_factor'] = str(c.charMs)
        config['OTHER']['Short_move_threshold'] = str(c.shortThreshold)

        with open('settings.ini', 'w') as configfile:
            config.write(configfile)

    def readFormWriteFile(self, event):
        c = self.read_form_config()
        self.writeConfig(c)
        
    def go(self, event): #read the state of all inputs, then kick off the main process
        self.read_form_config()
        
        out_result = main_process.process_files(cf)
        #print('Options Used:')
        #printAttributes(cf)

        #printAttributes(out_result)
        self.write_results(out_result, cf)

    def calcFactors(self, event): #read the calculator inputs, update some things for an output
        dist = float(self.calc_distance_text.GetValue())
        feed1 = float(self.calc_feed1_text.GetValue())
        feed2 = float(self.calc_feed2_text.GetValue())
        char1 = int(self.calc_char1_text.GetValue())
        char2 = int(self.calc_char2_text.GetValue())
        
        ms1 = dist/feed1*60000
        ms2 = dist/feed2*60000
        timeDiff = abs(ms1 - ms2)
        charDiff = abs(char1 - char2)

        msPerChar = round(timeDiff / charDiff, 1)
        msPerLine = round(ms1 - (char1 * msPerChar), 1)

        if msPerLine < 0: msPerLine = 0 #there are situations where you can have negative time per block, need to figure that out

        self.line_result.SetValue(str(msPerLine))
        self.char_result.SetValue(str(msPerChar * 10))
        
if __name__ == '__main__':
    app = wx.App()
    frame = appFrame(None)
    frame.Show(True)
    cf = frame.readConfig(appConfig())

    frame.write_form_config(cf) #and write it to the form
    frame.optimize_enable(None)
    frame.csv_enable(None)
    
    app.MainLoop()

