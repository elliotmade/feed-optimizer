import wx
import feed_ui as ui
import main_process

def printAttributes(object):
    attrs = vars(object)
    print(''.join("%s: %s \n" % item for item in attrs.items()))

class elliotConfig: #object to store all configuration variables for the main process
    #need to make a duplicate for storing default values, give the class a copy method and use a copy for the one sent to the processing function
    inPath = ''
    outPath = 'sample files\\test-output.txt'
    outCsv = True
    outCsvPath = 'sample files\output-csv.csv'
    eob = ';'
    rLineNum = False
    renumber = True
    numInc = 10
    rComments = True
    rBlankLines = True
    rSpaces = False
    rShortLines = False
    rTrailingZeroes = True
    shortThreshold = .001
    optimizeFeed = False
    increaseFeed = False
    feedCeiling = 77
    reduceFeed = False
    optimizePercent = 100 #0 to whatever whole number
    diffThreshold = .5 #done smallest feed rate to change for

    optimizeType = 0 #0 for memory, 1 for drip feed
    memLineMs = 100     #base time to process a line (blocks/lines per second that the control does, regardless of length)
    memCharMs = 4       #additional time per character in a line 300 char/sec for fanuc 6m tape reader?
    tapeLineMs = 200
    tapeCharMs = 8


class elliotFrame(ui.main_frame):
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
            self.feed_percent_text.Enable()
            self.optimize_type_radio.Enable()
        else:
            self.increase_feed_checkbox.Disable()
            self.reduce_feed_checkbox.Disable()
            self.feed_limit_text.Disable()
            self.feed_percent_text.Disable()
            self.optimize_type_radio.Disable()

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
        if cf.optimizeFeed == False: #negate the values of some selections that are disabled
            cf.increaseFeed == False
            cf.optimizePercent = 100
        else:
            cf.increaseFeed = self.increase_feed_checkbox.GetValue()
            if cf.reduceFeed == True:
                cf.optimizePercent = int(self.feed_percent_text.GetValue())
            else:
                cf.optimizePercent = 100
        
        cf.feedCeiling = float(self.feed_limit_text.GetValue())
        #cf.minTimeSaving = 300 #don't bother increasing the feed rate if it saves less than this, to preserve file size (milliseconds) (not implemented yet)

        cf.diffThreshold = float(self.small_feed_diff_text.GetValue()) #done smallest feed rate to change for #not in UI yet

        cf.optimizeType = self.optimize_type_radio.GetSelection()
        cf.memLineMs = int(self.mem_block_text.GetValue())
        cf.memCharMs = int(self.mem_char_text.GetValue())
        cf.tapeLineMs = int(self.drip_block_text.GetValue())
        cf.tapeCharMs = int(self.drip_char_text.GetValue())
        

    def write_form_config(self, inConfig): #write a config object into the form
        self.input_text.SetValue(inConfig.inPath)
        self.output_text.SetValue(inConfig.outPath)
        self.csv_text.SetValue(inConfig.outCsvPath)
        self.eob_text.SetValue(inConfig.eob)
        self.optimize_feed_checkbox.SetValue(inConfig.optimizeFeed)
        self.increase_feed_checkbox.SetValue(inConfig.increaseFeed)
        self.feed_limit_text.SetValue(str(inConfig.feedCeiling))
        self.reduce_feed_checkbox.SetValue(inConfig.reduceFeed)
        self.feed_percent_text.SetValue(str(inConfig.optimizePercent))
        self.csv_checkbox.SetValue(inConfig.outCsv)

        self.mem_block_text.SetValue(str(inConfig.memLineMs))
        self.mem_char_text.SetValue(str(inConfig.memCharMs))
        self.drip_block_text.SetValue(str(inConfig.tapeLineMs))
        self.drip_char_text.SetValue(str(inConfig.tapeCharMs))
        self.small_feed_diff_text.SetValue(str(inConfig.diffThreshold))
        self.linenum_increment_text.SetValue(str(inConfig.numInc))


    def go(self, event): #read the state of all inputs, then kick off the main process
        self.read_form_config()
        
        out_result = main_process.process_files(cf)
        print('Options Used:')
        printAttributes(cf)

        printAttributes(out_result)
        print('Original  : ' + str(out_result.inFileTime // 1000) + ' Seconds')
        print('New       : ' + str(out_result.outFileTime // 1000) + ' Seconds')
        print('Difference: ' + str((out_result.outFileTime - out_result.inFileTime) // 1000) + ' Seconds')


if __name__ == '__main__':
    app = wx.App()
    frame = elliotFrame(None)
    frame.Show(True)
    defaultConfig = elliotConfig() #create a default configuration object
    frame.write_form_config(defaultConfig) #and write it to the form
    frame.optimize_enable(None)
    frame.csv_enable(None)
    #import wx.lib.inspection
    #wx.lib.inspection.InspectionTool().Show()
    
    cf = elliotConfig()
    app.MainLoop()

