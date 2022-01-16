from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, RiseInTransition

from Code.py_files.StartPage import StartPage
from Code.py_files.Steps import Steps
from Code.py_files.Scheme import Scheme
from Code.py_files.Metadata import Metadata
from Code.py_files.Notices import Notices


class MyApp(MDApp):
    def __init__(self, **kwargs):
        self.title = "Config maker"
        self.icon = r'Sources\pictures\ico\icon1.ico'
        self.manager = ScreenManager(transition=RiseInTransition())
        super().__init__(**kwargs)

    def build(self):
        self.theme_cls.theme_style = 'Light'
        self.theme_cls.primary_palette = 'DeepPurple'
        self.manager.add_widget(StartPage(name='start_page'))
        self.manager.add_widget(Metadata(name='metadata'))
        self.manager.add_widget(Notices(name='notices'))
        self.manager.add_widget(Scheme(name='scheme'))
        self.manager.add_widget(Steps(name='steps'))
        return self.manager

    def task(self, *args):
        pass
