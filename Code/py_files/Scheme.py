from kivymd.uix.screen import MDScreen
from Code.py_files.Notification import Notification


class Scheme(MDScreen):
    dialog = None
    note = Notification(dialog)

    def __init__(self, **kw):
        super().__init__(**kw)

    def __draw_shadow__(self, origin, end, context=None):
        pass

    def go_back(self, *args):
        self.manager.current = 'start_page'
