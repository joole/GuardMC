# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Dec 21 2016)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import json

###########################################################################
## Class LoginDialog
###########################################################################

class LoginDialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"【守护模拟测试客户端】", pos = wx.DefaultPosition, size = wx.Size( 231,242 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.Size( 231,242 ), wx.Size( 231,242 ) )
		
		fgSizer1 = wx.FlexGridSizer( 0, 2, 0, 10 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_ALL )
		
		self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, u"服务器地址", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )
		fgSizer1.Add( self.m_staticText12, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_txtCtrl_ServerAddr = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.m_txtCtrl_ServerAddr.SetMinSize( wx.Size( 100,-1 ) )
		self.m_txtCtrl_ServerAddr.SetMaxSize( wx.Size( 100,-1 ) )
		
		fgSizer1.Add( self.m_txtCtrl_ServerAddr, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText13 = wx.StaticText( self, wx.ID_ANY, u"服务器端口", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )
		fgSizer1.Add( self.m_staticText13, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_textCtrl_ServerPort = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.m_textCtrl_ServerPort.SetMinSize( wx.Size( 100,-1 ) )
		self.m_textCtrl_ServerPort.SetMaxSize( wx.Size( 100,-1 ) )
		
		fgSizer1.Add( self.m_textCtrl_ServerPort, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText14 = wx.StaticText( self, wx.ID_ANY, u"组织ID", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14.Wrap( -1 )
		fgSizer1.Add( self.m_staticText14, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_textCtrl_OrgID = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.m_textCtrl_OrgID.SetMinSize( wx.Size( 100,-1 ) )
		self.m_textCtrl_OrgID.SetMaxSize( wx.Size( 100,-1 ) )
		
		fgSizer1.Add( self.m_textCtrl_OrgID, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText15 = wx.StaticText( self, wx.ID_ANY, u"用户UID", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText15.Wrap( -1 )
		fgSizer1.Add( self.m_staticText15, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_textCtrl_Uid = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.m_textCtrl_Uid.SetMinSize( wx.Size( 100,-1 ) )
		self.m_textCtrl_Uid.SetMaxSize( wx.Size( 100,-1 ) )
		
		fgSizer1.Add( self.m_textCtrl_Uid, 0, wx.ALL, 5 )
		
		self.m_staticText16 = wx.StaticText( self, wx.ID_ANY, u"用户密码", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText16.Wrap( -1 )
		fgSizer1.Add( self.m_staticText16, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_textCtrl_Pwd = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), wx.TE_PASSWORD )
		self.m_textCtrl_Pwd.SetMinSize( wx.Size( 100,-1 ) )
		self.m_textCtrl_Pwd.SetMaxSize( wx.Size( 100,-1 ) )
		
		fgSizer1.Add( self.m_textCtrl_Pwd, 0, wx.ALL, 5 )
		
		self.m_btnClose = wx.Button( self, wx.ID_ANY, u"取消", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.m_btnClose, 0, wx.ALL, 5 )
		
		self.m_btnLogin = wx.Button( self, wx.ID_ANY, u"登陆", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.m_btnLogin, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.SetSizer( fgSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_INIT_DIALOG, self.OnInitDialog )
		self.m_btnClose.Bind( wx.EVT_BUTTON, self.OnBtnCloseClick )
		self.m_btnLogin.Bind( wx.EVT_BUTTON, self.OnBtnLoginClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnInitDialog( self, event ):
		config = None
		with open("config.json", "r") as load_f:
			config = json.load(load_f)

		self.m_txtCtrl_ServerAddr.SetLabelText(config["server_addr"])
		self.m_textCtrl_ServerPort.SetLabelText(str(config["server_port"]))
		self.m_textCtrl_OrgID.SetLabelText(str(config["server_org"]))
		self.m_textCtrl_Uid.SetLabelText(str(config["user_name"]))
		self.m_textCtrl_Pwd.SetLabelText(str(config["user_pwd"]))
	
	def OnBtnCloseClick( self, event ):
		self.Close()
		event.Skip()
	
	def OnBtnLoginClick( self, event ):
		event.Skip()
	

