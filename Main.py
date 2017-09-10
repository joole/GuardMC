import wx
import wx.xrc
import LoginDialog
import NdUser



if __name__ == '__main__':
	app = wx.App(False)
	
	login_dlg = LoginDialog.LoginDialog(None)
	login_dlg.Show()
	app.MainLoop()
	