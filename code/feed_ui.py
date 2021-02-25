# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class main_frame
###########################################################################

class main_frame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"elliotmade Feed Rate Optimizer", pos = wx.DefaultPosition, size = wx.Size( 600,500 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		actual_main_sizer = wx.BoxSizer( wx.VERTICAL )

		self.actual_main_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		main_sizer = wx.BoxSizer( wx.VERTICAL )

		self.main_notebook = wx.Notebook( self.actual_main_panel, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,400 ), 0 )
		self.tab_main = wx.Panel( self.main_notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL, u"Main" )
		self.tab_main.SetToolTip( u"Using the speed input on the 'Machine Settings' tab, find the best feed rate for executing the program from control memory or drip feed" )

		main_main_sizer = wx.BoxSizer( wx.VERTICAL )

		self.m_staticline4 = wx.StaticLine( self.tab_main, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		main_main_sizer.Add( self.m_staticline4, 0, wx.EXPAND |wx.ALL, 5 )

		main_input_sizer = wx.BoxSizer( wx.HORIZONTAL )

		input_button_sizer = wx.BoxSizer( wx.VERTICAL )

		self.input_button = wx.Button( self.tab_main, wx.ID_ANY, u"Input FIle", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		input_button_sizer.Add( self.input_button, 0, wx.ALL, 5 )


		main_input_sizer.Add( input_button_sizer, 1, wx.EXPAND, 5 )

		input_text_sizer = wx.BoxSizer( wx.VERTICAL )

		self.input_text = wx.TextCtrl( self.tab_main, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 400,-1 ), 0 )
		input_text_sizer.Add( self.input_text, 0, wx.ALL, 5 )


		main_input_sizer.Add( input_text_sizer, 1, wx.EXPAND, 5 )


		main_main_sizer.Add( main_input_sizer, 1, wx.EXPAND, 5 )

		main_output_sizer = wx.BoxSizer( wx.HORIZONTAL )

		output_button_sizer = wx.BoxSizer( wx.VERTICAL )

		self.output_button = wx.Button( self.tab_main, wx.ID_ANY, u"Output File", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		output_button_sizer.Add( self.output_button, 0, wx.ALL, 5 )


		main_output_sizer.Add( output_button_sizer, 1, wx.EXPAND, 5 )

		output_text_sizer = wx.BoxSizer( wx.VERTICAL )

		self.output_text = wx.TextCtrl( self.tab_main, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 400,-1 ), 0 )
		output_text_sizer.Add( self.output_text, 0, wx.ALL, 5 )


		main_output_sizer.Add( output_text_sizer, 1, wx.EXPAND, 5 )


		main_main_sizer.Add( main_output_sizer, 1, wx.EXPAND, 5 )

		self.m_staticline2 = wx.StaticLine( self.tab_main, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		main_main_sizer.Add( self.m_staticline2, 0, wx.EXPAND |wx.ALL, 5 )

		main_feed_sizer = wx.BoxSizer( wx.VERTICAL )

		feed_group_sizer = wx.BoxSizer( wx.HORIZONTAL )

		feed_check_sizer = wx.BoxSizer( wx.VERTICAL )

		feed_optimize_sizer = wx.BoxSizer( wx.HORIZONTAL )

		self.optimize_feed_checkbox = wx.CheckBox( self.tab_main, wx.ID_ANY, u"Optimize Feed Rate", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.optimize_feed_checkbox.SetToolTip( u"Enable changing of feed rate.  Disabling this allows you to use other optimizations on the 'File Settings' tab without changing feed rates.  Enabling this will cause feed rates to be reduced on lines that would cause the cutter to dwell" )

		feed_optimize_sizer.Add( self.optimize_feed_checkbox, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


		feed_check_sizer.Add( feed_optimize_sizer, 1, wx.EXPAND, 5 )

		feed_increase_sizer = wx.BoxSizer( wx.HORIZONTAL )

		self.increase_feed_checkbox = wx.CheckBox( self.tab_main, wx.ID_ANY, u"Increase Feed Rate", wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		self.increase_feed_checkbox.SetToolTip( u"Increase feed rates on lines that are not bottlenecked by the control, up to the point that the cutter will dwell or the limit input here, whichever is smaller" )

		feed_increase_sizer.Add( self.increase_feed_checkbox, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.m_staticText1 = wx.StaticText( self.tab_main, wx.ID_ANY, u"Limit:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		feed_increase_sizer.Add( self.m_staticText1, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.feed_limit_text = wx.TextCtrl( self.tab_main, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.feed_limit_text.SetToolTip( u"Maximum feed rate allowed when increasing feed on a line.  Set this to the best feed for your tool, useful if your settings were lower than ideal in your CAM output" )

		feed_increase_sizer.Add( self.feed_limit_text, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


		feed_check_sizer.Add( feed_increase_sizer, 1, wx.EXPAND, 5 )

		feed_min_sizer = wx.BoxSizer( wx.HORIZONTAL )

		self.min_feed_checkbox = wx.CheckBox( self.tab_main, wx.ID_ANY, u"Minimum Feed Rate", wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		self.min_feed_checkbox.SetToolTip( u"Floor for optimized feed rate.  This is a shortcut to avoid hopeless small feed rates for hopelessly short moves that would always cause dwelling.  May allow a machine with lookeahead to move smoothly through." )

		feed_min_sizer.Add( self.min_feed_checkbox, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.min_feed_label = wx.StaticText( self.tab_main, wx.ID_ANY, u"Limit:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.min_feed_label.Wrap( -1 )

		feed_min_sizer.Add( self.min_feed_label, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.min_feed_text = wx.TextCtrl( self.tab_main, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.min_feed_text.SetToolTip( u"Maximum feed rate allowed when increasing feed on a line.  Set this to the best feed for your tool, useful if your settings were lower than ideal in your CAM output" )

		feed_min_sizer.Add( self.min_feed_text, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


		feed_check_sizer.Add( feed_min_sizer, 1, wx.EXPAND, 5 )

		feed_reduce_sizer = wx.BoxSizer( wx.HORIZONTAL )

		self.reduce_feed_checkbox = wx.CheckBox( self.tab_main, wx.ID_ANY, u"Modify All Feed Rates (%)", wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		self.reduce_feed_checkbox.SetToolTip( u"Modify all feed rates by this amount.  Example: set to 50 to increase the range of adjustment possible with manual feed override before causing the cutter to dwell." )

		feed_reduce_sizer.Add( self.reduce_feed_checkbox, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.reduce_feed_slider = wx.Slider( self.tab_main, wx.ID_ANY, 100, 1, 200, wx.DefaultPosition, wx.Size( 150,-1 ), wx.SL_HORIZONTAL|wx.SL_VALUE_LABEL )
		feed_reduce_sizer.Add( self.reduce_feed_slider, 0, wx.ALL, 5 )


		feed_check_sizer.Add( feed_reduce_sizer, 1, wx.EXPAND, 5 )

		small_feed_diff_sizer = wx.BoxSizer( wx.HORIZONTAL )

		self.small_feed_desc = wx.StaticText( self.tab_main, wx.ID_ANY, u"Skip changes smaller than:", wx.DefaultPosition, wx.Size( 230,-1 ), 0 )
		self.small_feed_desc.Wrap( -1 )

		small_feed_diff_sizer.Add( self.small_feed_desc, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.small_feed_diff_text = wx.TextCtrl( self.tab_main, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.small_feed_diff_text.SetToolTip( u"This will reduce the number of feed rate changes by omitting them if they are very close to the previous line" )

		small_feed_diff_sizer.Add( self.small_feed_diff_text, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


		feed_check_sizer.Add( small_feed_diff_sizer, 1, wx.EXPAND, 5 )


		feed_check_sizer.Add( ( 0, 80), 1, wx.EXPAND, 5 )


		feed_group_sizer.Add( feed_check_sizer, 1, wx.EXPAND, 5 )


		main_feed_sizer.Add( feed_group_sizer, 1, wx.EXPAND, 5 )


		main_main_sizer.Add( main_feed_sizer, 1, wx.EXPAND, 5 )


		self.tab_main.SetSizer( main_main_sizer )
		self.tab_main.Layout()
		main_main_sizer.Fit( self.tab_main )
		self.main_notebook.AddPage( self.tab_main, u"Main", True )
		self.tab_file = wx.Panel( self.main_notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.tab_file.SetToolTip( u"Remove or re-number program lines" )

		file_main_sizer = wx.BoxSizer( wx.VERTICAL )

		file_line_sizer = wx.BoxSizer( wx.HORIZONTAL )

		linenum_radioChoices = [ u"Do Nothing", u"Remove", u"Re-number" ]
		self.linenum_radio = wx.RadioBox( self.tab_file, wx.ID_ANY, u"Line Numbers", wx.DefaultPosition, wx.DefaultSize, linenum_radioChoices, 1, wx.RA_SPECIFY_ROWS )
		self.linenum_radio.SetSelection( 0 )
		file_line_sizer.Add( self.linenum_radio, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.linenum_label = wx.StaticText( self.tab_file, wx.ID_ANY, u"Increment:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.linenum_label.Wrap( -1 )

		file_line_sizer.Add( self.linenum_label, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.linenum_increment_text = wx.TextCtrl( self.tab_file, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.linenum_increment_text.SetToolTip( u"When renumbering the file, increase the N number by this increment.  Default is 1" )

		file_line_sizer.Add( self.linenum_increment_text, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


		file_main_sizer.Add( file_line_sizer, 1, wx.EXPAND, 5 )

		self.m_staticline5 = wx.StaticLine( self.tab_file, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		file_main_sizer.Add( self.m_staticline5, 0, wx.EXPAND |wx.ALL, 5 )

		file_remove_sizer = wx.BoxSizer( wx.VERTICAL )

		self.remove_spaces_checkbox = wx.CheckBox( self.tab_file, wx.ID_ANY, u"Remove Spaces", wx.DefaultPosition, wx.DefaultSize, 0 )
		file_remove_sizer.Add( self.remove_spaces_checkbox, 0, wx.ALL, 5 )

		self.remove_blanks_checkbox = wx.CheckBox( self.tab_file, wx.ID_ANY, u"Remove Blank Lines", wx.DefaultPosition, wx.DefaultSize, 0 )
		file_remove_sizer.Add( self.remove_blanks_checkbox, 0, wx.ALL, 5 )

		self.remove_comments_checkbox = wx.CheckBox( self.tab_file, wx.ID_ANY, u"Remove Comments", wx.DefaultPosition, wx.DefaultSize, 0 )
		file_remove_sizer.Add( self.remove_comments_checkbox, 0, wx.ALL, 5 )

		self.remove_zeroes_checkbox = wx.CheckBox( self.tab_file, wx.ID_ANY, u"Remove Trailing Zeroes", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.remove_zeroes_checkbox.SetToolTip( u"Remove trailing zeros, but preserve decimal points" )

		file_remove_sizer.Add( self.remove_zeroes_checkbox, 0, wx.ALL, 5 )


		file_main_sizer.Add( file_remove_sizer, 1, wx.EXPAND, 5 )

		file_eob_sizer = wx.BoxSizer( wx.HORIZONTAL )

		self.eob_label = wx.StaticText( self.tab_file, wx.ID_ANY, u"End Of Block:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.eob_label.Wrap( -1 )

		file_eob_sizer.Add( self.eob_label, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.eob_text = wx.TextCtrl( self.tab_file, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.eob_text.SetToolTip( u"This is used at the end of each line, semicolon or blank are common examples" )

		file_eob_sizer.Add( self.eob_text, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


		file_main_sizer.Add( file_eob_sizer, 1, wx.EXPAND, 5 )


		self.tab_file.SetSizer( file_main_sizer )
		self.tab_file.Layout()
		file_main_sizer.Fit( self.tab_file )
		self.main_notebook.AddPage( self.tab_file, u"File Settings", False )
		self.tab_machine = wx.Panel( self.main_notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		machine_main_sizer = wx.BoxSizer( wx.VERTICAL )

		time_block_sizer = wx.BoxSizer( wx.VERTICAL )

		self.time_block_slider = wx.Slider( self.tab_machine, wx.ID_ANY, 100, 1, 200, wx.DefaultPosition, wx.Size( 400,-1 ), wx.SL_HORIZONTAL|wx.SL_VALUE_LABEL )
		time_block_sizer.Add( self.time_block_slider, 0, wx.ALL, 5 )

		self.m_staticText121 = wx.StaticText( self.tab_machine, wx.ID_ANY, u"Block time factor: This is a fixed amount of time required for the control to process a block.  It is static overhead that does not vary with line length.  On this slider one notch is roughly equivalent to 1 millisecond.\n\nExamples:\nFanuc 6mb: 100\nYasnac MX2: 30", wx.DefaultPosition, wx.Size( -1,120 ), 0 )
		self.m_staticText121.Wrap( -1 )

		time_block_sizer.Add( self.m_staticText121, 0, wx.ALL, 5 )


		machine_main_sizer.Add( time_block_sizer, 1, wx.EXPAND, 5 )

		self.m_staticline41 = wx.StaticLine( self.tab_machine, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		machine_main_sizer.Add( self.m_staticline41, 0, wx.EXPAND |wx.ALL, 5 )

		time_char_sizer = wx.BoxSizer( wx.VERTICAL )

		self.time_char_slider = wx.Slider( self.tab_machine, wx.ID_ANY, 80, 0, 200, wx.DefaultPosition, wx.Size( 400,-1 ), wx.SL_HORIZONTAL|wx.SL_VALUE_LABEL )
		time_char_sizer.Add( self.time_char_slider, 0, wx.ALL, 5 )

		self.m_staticText14 = wx.StaticText( self.tab_machine, wx.ID_ANY, u"Character time factor: This is the amount of time required per character in a block.  This accounts for the impact of the character count on a program line.  On this slider one notch is roughly equivalent to .1 milliseconds.\n\nExamples:\nFanuc 6mb: 80\nYasnac MX2: 30", wx.DefaultPosition, wx.Size( -1,120 ), 0 )
		self.m_staticText14.Wrap( -1 )

		time_char_sizer.Add( self.m_staticText14, 0, wx.ALL, 5 )


		machine_main_sizer.Add( time_char_sizer, 1, wx.EXPAND, 5 )


		self.tab_machine.SetSizer( machine_main_sizer )
		self.tab_machine.Layout()
		machine_main_sizer.Fit( self.tab_machine )
		self.main_notebook.AddPage( self.tab_machine, u"Machine Settings", False )
		self.tab_advanced = wx.Panel( self.main_notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		advanced_main_sizer = wx.BoxSizer( wx.VERTICAL )

		advanced_button_sizer = wx.BoxSizer( wx.HORIZONTAL )

		self.save_settings_button = wx.Button( self.tab_advanced, wx.ID_ANY, u"Save Settings", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.save_settings_button.SetToolTip( u"Save settings as a new default" )

		advanced_button_sizer.Add( self.save_settings_button, 0, wx.ALL, 5 )

		self.restore_settings_button = wx.Button( self.tab_advanced, wx.ID_ANY, u"Restore Settings", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.restore_settings_button.SetToolTip( u"Restore saved default settings" )

		advanced_button_sizer.Add( self.restore_settings_button, 0, wx.ALL, 5 )


		advanced_main_sizer.Add( advanced_button_sizer, 1, wx.EXPAND, 5 )

		bSizer40 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText17 = wx.StaticText( self.tab_advanced, wx.ID_ANY, u"CSV output provides some additional details of the original and new files, useful for debugging, also analyzing and comparing files to dial in your post processor.", wx.DefaultPosition, wx.Size( -1,50 ), 0 )
		self.m_staticText17.Wrap( 500 )

		bSizer40.Add( self.m_staticText17, 0, wx.ALL, 5 )

		file_csv_sizer = wx.BoxSizer( wx.HORIZONTAL )

		self.csv_checkbox = wx.CheckBox( self.tab_advanced, wx.ID_ANY, u"CSV Output", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.csv_checkbox.SetToolTip( u"Output the program to a CSV.  Useful for debugging or analyzing the results" )

		file_csv_sizer.Add( self.csv_checkbox, 0, wx.ALL, 5 )

		self.csv_button = wx.Button( self.tab_advanced, wx.ID_ANY, u"Select", wx.DefaultPosition, wx.DefaultSize, 0 )
		file_csv_sizer.Add( self.csv_button, 0, wx.ALL, 5 )

		self.csv_text = wx.TextCtrl( self.tab_advanced, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 400,-1 ), 0 )
		file_csv_sizer.Add( self.csv_text, 0, wx.ALL, 5 )


		bSizer40.Add( file_csv_sizer, 1, wx.EXPAND, 5 )


		advanced_main_sizer.Add( bSizer40, 1, wx.EXPAND, 5 )


		self.tab_advanced.SetSizer( advanced_main_sizer )
		self.tab_advanced.Layout()
		advanced_main_sizer.Fit( self.tab_advanced )
		self.main_notebook.AddPage( self.tab_advanced, u"Advanced", False )
		self.tab_results = wx.Panel( self.main_notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		results_main_sizer = wx.BoxSizer( wx.VERTICAL )

		self.result_text = wx.TextCtrl( self.tab_results, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 600,300 ), wx.TE_MULTILINE )
		results_main_sizer.Add( self.result_text, 0, wx.ALL, 5 )


		self.tab_results.SetSizer( results_main_sizer )
		self.tab_results.Layout()
		results_main_sizer.Fit( self.tab_results )
		self.main_notebook.AddPage( self.tab_results, u"Result", False )
		self.tab_help = wx.Panel( self.main_notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		help_main_sizer = wx.BoxSizer( wx.VERTICAL )

		image_sizer_1 = wx.BoxSizer( wx.VERTICAL )


		help_main_sizer.Add( image_sizer_1, 1, wx.EXPAND, 5 )


		self.tab_help.SetSizer( help_main_sizer )
		self.tab_help.Layout()
		help_main_sizer.Fit( self.tab_help )
		self.main_notebook.AddPage( self.tab_help, u"Help", False )

		main_sizer.Add( self.main_notebook, 1, wx.EXPAND |wx.ALL, 5 )

		main_bottom_sizer = wx.BoxSizer( wx.VERTICAL )

		self.go_button = wx.Button( self.actual_main_panel, wx.ID_ANY, u"Go", wx.DefaultPosition, wx.DefaultSize, 0 )
		main_bottom_sizer.Add( self.go_button, 0, wx.ALL, 5 )


		main_sizer.Add( main_bottom_sizer, 1, wx.EXPAND, 5 )


		self.actual_main_panel.SetSizer( main_sizer )
		self.actual_main_panel.Layout()
		main_sizer.Fit( self.actual_main_panel )
		actual_main_sizer.Add( self.actual_main_panel, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( actual_main_sizer )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.input_button.Bind( wx.EVT_BUTTON, self.browse_input )
		self.output_button.Bind( wx.EVT_BUTTON, self.browse_output )
		self.optimize_feed_checkbox.Bind( wx.EVT_CHECKBOX, self.optimize_enable )
		self.save_settings_button.Bind( wx.EVT_BUTTON, self.readFormWriteFile )
		self.restore_settings_button.Bind( wx.EVT_BUTTON, self.readConfig )
		self.csv_checkbox.Bind( wx.EVT_CHECKBOX, self.csv_enable )
		self.csv_button.Bind( wx.EVT_BUTTON, self.browse_csv )
		self.go_button.Bind( wx.EVT_BUTTON, self.go )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def browse_input( self, event ):
		event.Skip()

	def browse_output( self, event ):
		event.Skip()

	def optimize_enable( self, event ):
		event.Skip()

	def readFormWriteFile( self, event ):
		event.Skip()

	def readConfig( self, event ):
		event.Skip()

	def csv_enable( self, event ):
		event.Skip()

	def browse_csv( self, event ):
		event.Skip()

	def go( self, event ):
		event.Skip()


