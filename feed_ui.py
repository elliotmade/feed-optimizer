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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"elliotmade Feed Rate Optimizer", pos = wx.DefaultPosition, size = wx.Size( 850,650 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		actual_main_sizer = wx.BoxSizer( wx.VERTICAL )

		self.actual_main_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		main_sizer = wx.BoxSizer( wx.VERTICAL )

		self.main_notebook = wx.Notebook( self.actual_main_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.tab_main = wx.Panel( self.main_notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL, u"Main" )
		self.tab_main.SetToolTip( u"Using the speed input on the 'Machine Settings' tab, find the best feed rate for executing the program from control memory or drip feed" )

		main_main_sizer = wx.BoxSizer( wx.VERTICAL )

		self.m_staticline4 = wx.StaticLine( self.tab_main, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		main_main_sizer.Add( self.m_staticline4, 0, wx.EXPAND |wx.ALL, 5 )

		main_input_sizer = wx.BoxSizer( wx.HORIZONTAL )

		self.input_button = wx.Button( self.tab_main, wx.ID_ANY, u"Input FIle", wx.DefaultPosition, wx.DefaultSize, 0 )
		main_input_sizer.Add( self.input_button, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.input_text = wx.TextCtrl( self.tab_main, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 400,-1 ), 0 )
		main_input_sizer.Add( self.input_text, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


		main_main_sizer.Add( main_input_sizer, 1, wx.EXPAND, 5 )

		main_output_sizer = wx.BoxSizer( wx.HORIZONTAL )

		self.output_button = wx.Button( self.tab_main, wx.ID_ANY, u"Output File", wx.DefaultPosition, wx.DefaultSize, 0 )
		main_output_sizer.Add( self.output_button, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.output_text = wx.TextCtrl( self.tab_main, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 400,-1 ), 0 )
		main_output_sizer.Add( self.output_text, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


		main_main_sizer.Add( main_output_sizer, 1, wx.EXPAND, 5 )

		self.m_staticline2 = wx.StaticLine( self.tab_main, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		main_main_sizer.Add( self.m_staticline2, 0, wx.EXPAND |wx.ALL, 5 )

		main_feed_sizer = wx.BoxSizer( wx.VERTICAL )

		feed_group_sizer = wx.BoxSizer( wx.HORIZONTAL )

		feed_check_sizer = wx.BoxSizer( wx.VERTICAL )

		self.optimize_feed_checkbox = wx.CheckBox( self.tab_main, wx.ID_ANY, u"Optimize Feed Rate", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.optimize_feed_checkbox.SetValue(True)
		self.optimize_feed_checkbox.SetToolTip( u"Enable changing of feed rate.  Disabling this allows you to use other optimizations on the 'File Settings' tab without changing feed rates.  Enabling this will cause feed rates to be reduced on lines that would cause the cutter to dwell" )

		feed_check_sizer.Add( self.optimize_feed_checkbox, 0, wx.ALL, 5 )

		feed_increase_sizer = wx.BoxSizer( wx.HORIZONTAL )

		self.increase_feed_checkbox = wx.CheckBox( self.tab_main, wx.ID_ANY, u"Increase Feed Rate", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.increase_feed_checkbox.SetToolTip( u"Increase feed rates on lines that are not bottlenecked by the control, up to the point that the cutter will dwell or the limit input here, whichever is smaller" )

		feed_increase_sizer.Add( self.increase_feed_checkbox, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.m_staticText1 = wx.StaticText( self.tab_main, wx.ID_ANY, u"Limit:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		feed_increase_sizer.Add( self.m_staticText1, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.feed_limit_text = wx.TextCtrl( self.tab_main, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.feed_limit_text.SetToolTip( u"Maximum feed rate allowed when increasing feed on a line.  Set this to the best feed for your tool, useful if your settings were lower than ideal in your CAM output" )

		feed_increase_sizer.Add( self.feed_limit_text, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


		feed_check_sizer.Add( feed_increase_sizer, 1, wx.EXPAND, 5 )

		feed_reduce_sizer = wx.BoxSizer( wx.HORIZONTAL )

		self.reduce_feed_checkbox = wx.CheckBox( self.tab_main, wx.ID_ANY, u"Reduce Feed Rates", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.reduce_feed_checkbox.SetToolTip( u"Reduce all feed rates by this amount.  Example: set to 50 to increase the range of adjustment possible with manual feed override before causing the cutter to dwell." )

		feed_reduce_sizer.Add( self.reduce_feed_checkbox, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.m_staticText3 = wx.StaticText( self.tab_main, wx.ID_ANY, u"Percent (whole number):", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )

		feed_reduce_sizer.Add( self.m_staticText3, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.feed_percent_text = wx.TextCtrl( self.tab_main, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.feed_percent_text.SetToolTip( u"100 = no change, 50 = decrease by half, 200 = double" )

		feed_reduce_sizer.Add( self.feed_percent_text, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


		feed_check_sizer.Add( feed_reduce_sizer, 1, wx.EXPAND, 5 )


		feed_group_sizer.Add( feed_check_sizer, 1, wx.EXPAND, 5 )

		feed_optimize_type_sizer = wx.BoxSizer( wx.VERTICAL )

		optimize_type_radioChoices = [ u"Memory", u"Drip-feed" ]
		self.optimize_type_radio = wx.RadioBox( self.tab_main, wx.ID_ANY, u"Optimize Feed For:", wx.DefaultPosition, wx.DefaultSize, optimize_type_radioChoices, 1, wx.RA_SPECIFY_COLS )
		self.optimize_type_radio.SetSelection( 0 )
		feed_optimize_type_sizer.Add( self.optimize_type_radio, 0, wx.ALL|wx.EXPAND, 5 )


		feed_group_sizer.Add( feed_optimize_type_sizer, 1, wx.EXPAND, 5 )


		main_feed_sizer.Add( feed_group_sizer, 1, wx.EXPAND, 5 )


		main_main_sizer.Add( main_feed_sizer, 1, wx.EXPAND, 5 )

		self.m_staticline3 = wx.StaticLine( self.tab_main, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		main_main_sizer.Add( self.m_staticline3, 0, wx.EXPAND |wx.ALL, 5 )

		main_go_sizer = wx.BoxSizer( wx.HORIZONTAL )

		self.go_button = wx.Button( self.tab_main, wx.ID_ANY, u"Go", wx.DefaultPosition, wx.DefaultSize, 0 )
		main_go_sizer.Add( self.go_button, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


		main_main_sizer.Add( main_go_sizer, 1, wx.EXPAND, 5 )


		self.tab_main.SetSizer( main_main_sizer )
		self.tab_main.Layout()
		main_main_sizer.Fit( self.tab_main )
		self.main_notebook.AddPage( self.tab_main, u"Main", True )
		self.tab_file = wx.Panel( self.main_notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.tab_file.SetToolTip( u"Remove or re-number program lines" )

		file_main_sizer = wx.BoxSizer( wx.VERTICAL )

		file_csv_sizer = wx.BoxSizer( wx.HORIZONTAL )

		self.csv_checkbox = wx.CheckBox( self.tab_file, wx.ID_ANY, u"CSV Output", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.csv_checkbox.SetToolTip( u"Output the program to a CSV.  Useful for debugging or analyzing the results" )

		file_csv_sizer.Add( self.csv_checkbox, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.csv_button = wx.Button( self.tab_file, wx.ID_ANY, u"Select", wx.DefaultPosition, wx.DefaultSize, 0 )
		file_csv_sizer.Add( self.csv_button, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.csv_text = wx.TextCtrl( self.tab_file, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 400,-1 ), 0 )
		file_csv_sizer.Add( self.csv_text, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


		file_main_sizer.Add( file_csv_sizer, 1, wx.EXPAND, 5 )

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

		self.mem_label = wx.StaticText( self.tab_machine, wx.ID_ANY, u"Memory:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.mem_label.Wrap( -1 )

		machine_main_sizer.Add( self.mem_label, 0, wx.ALL, 5 )

		machine_mem_sizer = wx.BoxSizer( wx.HORIZONTAL )

		mem_label_sizer = wx.BoxSizer( wx.VERTICAL )

		self.mem_block_label = wx.StaticText( self.tab_machine, wx.ID_ANY, u"Block Read Time", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.mem_block_label.Wrap( -1 )

		mem_label_sizer.Add( self.mem_block_label, 0, wx.ALL, 5 )

		self.mem_char_label = wx.StaticText( self.tab_machine, wx.ID_ANY, u"Character Read Time", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.mem_char_label.Wrap( -1 )

		mem_label_sizer.Add( self.mem_char_label, 0, wx.ALL, 5 )


		machine_mem_sizer.Add( mem_label_sizer, 1, wx.EXPAND, 5 )

		mem_text_sizer = wx.BoxSizer( wx.VERTICAL )

		self.mem_block_text = wx.TextCtrl( self.tab_machine, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		mem_text_sizer.Add( self.mem_block_text, 0, wx.ALL, 5 )

		self.mem_char_text = wx.TextCtrl( self.tab_machine, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		mem_text_sizer.Add( self.mem_char_text, 0, wx.ALL, 5 )


		machine_mem_sizer.Add( mem_text_sizer, 1, wx.EXPAND, 5 )


		machine_main_sizer.Add( machine_mem_sizer, 1, wx.EXPAND, 5 )

		self.m_staticline1 = wx.StaticLine( self.tab_machine, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		machine_main_sizer.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )

		self.drip_label = wx.StaticText( self.tab_machine, wx.ID_ANY, u"Drip Feed:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.drip_label.Wrap( -1 )

		machine_main_sizer.Add( self.drip_label, 0, wx.ALL, 5 )

		drip_label_sizer1 = wx.BoxSizer( wx.HORIZONTAL )

		drip_label_sizer = wx.BoxSizer( wx.VERTICAL )

		self.drip_block_label = wx.StaticText( self.tab_machine, wx.ID_ANY, u"Block Read Time", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.drip_block_label.Wrap( -1 )

		drip_label_sizer.Add( self.drip_block_label, 0, wx.ALL, 5 )

		self.drip_char_label = wx.StaticText( self.tab_machine, wx.ID_ANY, u"Character Read Time", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.drip_char_label.Wrap( -1 )

		drip_label_sizer.Add( self.drip_char_label, 0, wx.ALL, 5 )


		drip_label_sizer1.Add( drip_label_sizer, 1, wx.EXPAND, 5 )

		drip_text_sizer = wx.BoxSizer( wx.VERTICAL )

		self.drip_block_text = wx.TextCtrl( self.tab_machine, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		drip_text_sizer.Add( self.drip_block_text, 0, wx.ALL, 5 )

		self.drip_char_text = wx.TextCtrl( self.tab_machine, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		drip_text_sizer.Add( self.drip_char_text, 0, wx.ALL, 5 )


		drip_label_sizer1.Add( drip_text_sizer, 1, wx.EXPAND, 5 )


		machine_main_sizer.Add( drip_label_sizer1, 1, wx.EXPAND, 5 )


		self.tab_machine.SetSizer( machine_main_sizer )
		self.tab_machine.Layout()
		machine_main_sizer.Fit( self.tab_machine )
		self.main_notebook.AddPage( self.tab_machine, u"Machine Settings", False )
		self.tab_advanced = wx.Panel( self.main_notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		advanced_main_sizer = wx.BoxSizer( wx.VERTICAL )

		advanced_button_sizer = wx.BoxSizer( wx.VERTICAL )

		self.save_settings_button = wx.Button( self.tab_advanced, wx.ID_ANY, u"Save Settings", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.save_settings_button.SetToolTip( u"Not implemented yet" )

		advanced_button_sizer.Add( self.save_settings_button, 0, wx.ALL, 5 )

		self.restore_settings_button = wx.Button( self.tab_advanced, wx.ID_ANY, u"Restore Settings", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.restore_settings_button.SetToolTip( u"Not implemented yet" )

		advanced_button_sizer.Add( self.restore_settings_button, 0, wx.ALL, 5 )

		small_feed_diff_sizer = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText12 = wx.StaticText( self.tab_advanced, wx.ID_ANY, u"Do not change feed rate for differences less than:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )

		small_feed_diff_sizer.Add( self.m_staticText12, 0, wx.ALL, 5 )

		self.small_feed_diff_text = wx.TextCtrl( self.tab_advanced, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.small_feed_diff_text.SetToolTip( u"This will reduce the number of feed rate changes by omitting them if they are very close to the previous line" )

		small_feed_diff_sizer.Add( self.small_feed_diff_text, 0, wx.ALL, 5 )


		advanced_button_sizer.Add( small_feed_diff_sizer, 1, wx.EXPAND, 5 )


		advanced_main_sizer.Add( advanced_button_sizer, 1, wx.EXPAND, 5 )


		self.tab_advanced.SetSizer( advanced_main_sizer )
		self.tab_advanced.Layout()
		advanced_main_sizer.Fit( self.tab_advanced )
		self.main_notebook.AddPage( self.tab_advanced, u"Advanced", False )
		self.tab_help = wx.Panel( self.main_notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		help_main_sizer = wx.BoxSizer( wx.VERTICAL )

		image_sizer_1 = wx.BoxSizer( wx.VERTICAL )


		help_main_sizer.Add( image_sizer_1, 1, wx.EXPAND, 5 )


		self.tab_help.SetSizer( help_main_sizer )
		self.tab_help.Layout()
		help_main_sizer.Fit( self.tab_help )
		self.main_notebook.AddPage( self.tab_help, u"Help", False )

		main_sizer.Add( self.main_notebook, 1, wx.EXPAND |wx.ALL, 5 )


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
		self.go_button.Bind( wx.EVT_BUTTON, self.go )
		self.csv_checkbox.Bind( wx.EVT_CHECKBOX, self.csv_enable )
		self.csv_button.Bind( wx.EVT_BUTTON, self.browse_csv )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def browse_input( self, event ):
		event.Skip()

	def browse_output( self, event ):
		event.Skip()

	def optimize_enable( self, event ):
		event.Skip()

	def go( self, event ):
		event.Skip()

	def csv_enable( self, event ):
		event.Skip()

	def browse_csv( self, event ):
		event.Skip()


