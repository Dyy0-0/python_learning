# -*- coding: utf-8 -*-

#############################Import package##############################################
                                                                                       #
import wx                                                                              #
import wx.xrc                                                                          #               
import re                                                                              #
import os    
from KeywordPage import *                                                                       #
#############################Import package##############################################
## Class MyFrame1
###########################################################################

#########头#############
class MyApp(wx.App):
 
	pass
#########头#############


# the class to get a method to get the LOG_path and Page_path and in the textural space !
class FileDropTarget(wx.FileDropTarget):
	def __init__(self, window):
		wx.FileDropTarget.__init__(self)
		self.window = window
 
	def OnDropFiles(self,  x,  y, fileNames): 
		self.window.SetValue(str(fileNames)) 


# The windows program , 2 testctrl and one button 
class MyFrame1 ( wx.Frame ):
	
	wildcard = '文本文件(*.txt)|*.txt|所有文件(*.*)|*.*'
	global ans1
	
	def __init__( self, parent , id):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = "扎斯特读易特", pos = wx.DefaultPosition, size = wx.Size( 500 ,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"LOG", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.m_staticText1.Wrap( -1 )

		self.m_staticText1.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.m_staticText1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )

		bSizer1.Add( self.m_staticText1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )

		self.LOG_path = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, size =(300, 60))
		bSizer1.Add( self.LOG_path, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"PAGE", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.m_staticText2.Wrap( -1 )

		self.m_staticText2.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.m_staticText2.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )

		bSizer1.Add( self.m_staticText2, 0, wx.ALL|wx.EXPAND, 5 )

		self.PAGE_path = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, size =(300, 60))
		bSizer1.Add( self.PAGE_path, 0, wx.ALL|wx.EXPAND, 5 )

		self.GOtoSearch = wx.Button( self, wx.ID_ANY, u"GOtoSearch", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.GOtoSearch, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		
		
		
		
		# Connect Events
		self.GOtoSearch.Bind( wx.EVT_BUTTON, self.get_the_LOg_PAGe_path )
		
		dropTarget = FileDropTarget(self.LOG_path)
		dropTarget2 = FileDropTarget(self.PAGE_path)
		self.LOG_path.SetDropTarget( dropTarget )
		self.PAGE_path.SetDropTarget( dropTarget2 )
		

		

	def __del__( self ):
		pass

		

		
	# def OnOpen(self, event):     ##测试 1：          ans1和ans2  可以赋值 及 可以调用其地址 
		# ans1 = self.LOG_path.GetValue()
		# ans2 = self.PAGE_path.GetValue()
		# if ans1 != ''and ans2 !='':
			# dlg = wx.FileDialog(self, message='打开文件', 
								# defaultDir='',
								# defaultFile='', 
								# wildcard=self.wildcard, 
								# style=wx.FD_OPEN)
			# if dlg.ShowModal() == wx.ID_OK:
				# file = dlg.GetPath()
				# print(file)
				# dlg.Destroy()         
		
	# Virtual event handlers, overide them in your derived class, this is first step and total def in the program 
	# I think we should code else defs in this def 
	# using it to take else def done form the buttom is OK
	def get_the_LOg_PAGe_path( self, event ):
		# ans1 is the LOG_path ,asn2 is the PAGE_path
		global ans1 ,ans2
		ans1 = self.LOG_path.GetValue()
		ans2 = self.PAGE_path.GetValue()
		# if 'KeywordPage' in ans1:
			
		# 	search_go()
		# 	write_ana_log()

########python can read this so wo didn't need to fromat it 
		# if ans1 != '' and ans2 != '':

		# 	with open('log-key.txt' ,'a') as tttt:
		# 		# Fromate the path to use it in python 
		ans1 = ans1.split("'")
		ans1 = ans1[1]
		# 		ans1 = eval(repr(ans1).replace('\\\\', '\\'))
		# 		ans1 = eval(repr(ans1).replace( '\\','/'))
		# 		ans1 = eval(repr(ans1).replace( '//','/'))
		ans2 = ans2.split("'")
		ans2 = ans2[1]
		# 		ans2 = ans2.split("\\\\")
		# 		ans2 = ans2[-1]
		# 		tttt.write(ans2)
		if ans1 != '' and ans2 != '':
			if 'KeywordPage' in ans2 :
				search_go(ans1)
				write_ana_log()

				# get the page Path ps. the page doc need in  the same file import LOG

				# ans2 = eval(repr(ans2).replace('\\\\', '\\'))
				# ans2 = eval(repr(ans2).replace( '\\','/'))
				# ans2 = eval(repr(ans2).replace( '//','/'))


############调用文件##############
app=MyApp()
frame=MyFrame1(parent=None,id=-1)
frame.Show(True)
app.MainLoop() 
############调用文件##############
