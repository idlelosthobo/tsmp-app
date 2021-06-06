import wx

from tsmp.gui.panels import Mp3Panel
from tsmp.gui.menus import MENU_LIST


class MainFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='Traveling Salesman Problem Tool')
        self.panel = Mp3Panel(self)
        self.create_menu_bar()
        self.create_status_bar()
        self.create_tool_bar()
        self.Show()

    def create_menu_bar(self):
        menu_bar = wx.MenuBar()

        for menu in MENU_LIST:
            new_menu = wx.Menu()

            for item in menu['item_list']:
                new_menu_item = new_menu.Append(wx.ID_ANY, item['label'], item['description'])

                self.Bind(
                    event=item['event'],
                    handler=self.__getattribute__(item['handler']),
                    source=new_menu_item,
                )

            menu_bar.Append(new_menu, menu['name'])

        self.SetMenuBar(menu_bar)

    def create_status_bar(self):
        status_bar = wx.StatusBar(self)

        status_bar.SetStatusText('Information')

        self.SetStatusBar(status_bar)

    def create_tool_bar(self):
        tool_bar = wx.ToolBar(self)

        qtool = tool_bar.AddTool(wx.ID_ANY, 'Quit', 'Quit')
        tool_bar.Realize()

        self.Bind(wx.EVT_TOOL, self.OnQuit, qtool)

        self.SetSize((350, 250))
        self.SetTitle('Simple toolbar')
        self.Centre()

        self.SetToolBar(tool_bar)

    def on_open_folder(self, event):
        title = "Choose a directory:"
        dlg = wx.DirDialog(self, title, style=wx.DD_DEFAULT_STYLE)
        if dlg.ShowModal() == wx.ID_OK:
            self.panel.update_mp3_listing(dlg.GetPath())
        dlg.Destroy()