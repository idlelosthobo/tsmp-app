import wx

MENU_LIST = [
    {
        'name': '&File',
        'item_list': [
            {
                'label': 'Clear Data',
                'description': 'Clear all open data',
                'event': wx.EVT_MENU,
                'handler': 'on_open_folder'
            },
            {
                'label': 'Open Folder',
                'description': 'Open a folder with MP3s',
                'event': wx.EVT_MENU,
                'handler': 'on_open_folder'
            }
        ]
    },
    {
        'name': '&Help',
        'item_list': [
            {
                'label': 'Howto',
                'description': 'how to use this program',
                'event': wx.EVT_MENU,
                'handler': 'on_open_folder'
            },
        ]
    }
]
