import wx
import feed_ui as ui
import main_process

def printAttributes(object):
    attrs = vars(object)
    print(''.join("%s: %s \n" % item for item in attrs.items()))

class appConfig: #object to store all configuration variables for the main process
    #need to make a duplicate for storing default values, give the class a copy method and use a copy for the one sent to the processing function
    inPath = ''
    outPath = 'sample_files\\test-output.txt'
    outCsv = True
    outCsvPath = 'sample_files\debug_output.csv'
    eob = ';'
    rLineNum = False
    renumber = False
    numInc = 10
    rComments = False
    rBlankLines = False
    rSpaces = False
    rShortLines = False
    rTrailingZeroes = True
    shortThreshold = .001
    optimizeFeed = False
    increaseFeed = False
    feedCeiling = 77
    reduceFeed = False
    optimizePercent = 100 #0 to whatever whole number
    minFeed = False
    minFeedLimit = .25
    diffThreshold = .5  #done smallest feed rate to change for

    optimizeType = 0    #0 for memory, 1 for drip feed

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
        else:
            self.increase_feed_checkbox.Disable()
            self.reduce_feed_checkbox.Disable()
            self.feed_limit_text.Disable()
            self.reduce_feed_slider.Disable()
            self.min_feed_checkbox.Disable()
            self.min_feed_text.Disable()

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
       
        lineOption = self.linenum_radio.GetSelection()
        if lineOption == 0:
            cf.rLineNum = False
            cf.renumber = False
        elif lineOption == 1:
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
        
    def write_form_config(self, inConfig): #write a config object into the form
        self.input_text.SetValue(inConfig.inPath)
        self.output_text.SetValue(inConfig.outPath)
        self.csv_text.SetValue(inConfig.outCsvPath)
        self.eob_text.SetValue(inConfig.eob)
        self.optimize_feed_checkbox.SetValue(inConfig.optimizeFeed)
        self.increase_feed_checkbox.SetValue(inConfig.increaseFeed)
        self.feed_limit_text.SetValue(str(inConfig.feedCeiling))
        self.reduce_feed_checkbox.SetValue(inConfig.reduceFeed)
        self.reduce_feed_slider.SetValue(inConfig.optimizePercent)
        self.csv_checkbox.SetValue(inConfig.outCsv)

        self.time_block_slider.SetValue(inConfig.lineMs)
        self.time_char_slider.SetValue(inConfig.charMs * 10)
        self.small_feed_diff_text.SetValue(str(inConfig.diffThreshold))
        self.linenum_increment_text.SetValue(str(inConfig.numInc))
        self.min_feed_checkbox.SetValue(inConfig.minFeed)
        self.min_feed_text.SetValue(str(inConfig.minFeedLimit))

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

    def go(self, event): #read the state of all inputs, then kick off the main process
        self.read_form_config()
        
        out_result = main_process.process_files(cf)
        print('Options Used:')
        printAttributes(cf)

        printAttributes(out_result)
        print('Original  : ' + str(out_result.inFileTime // 1000) + ' Seconds')
        print('New       : ' + str(out_result.outFileTime // 1000) + ' Seconds')
        print('Difference: ' + str((out_result.outFileTime - out_result.inFileTime) // 1000) + ' Seconds')
        self.write_results(out_result, cf)

if __name__ == '__main__':
    app = wx.App()
    frame = appFrame(None)
    frame.Show(True)
    defaultConfig = appConfig() #create a default configuration object
    frame.write_form_config(defaultConfig) #and write it to the form
    frame.optimize_enable(None)
    frame.csv_enable(None)
    
    cf = appConfig()
    app.MainLoop()

