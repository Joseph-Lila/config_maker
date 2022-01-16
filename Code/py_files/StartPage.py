from kivy.uix.gridlayout import GridLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import MDScreen
from functools import partial
from plyer import filechooser
from kivymd.toast import toast
from Code.py_files.Notification import Notification
from Code.py_files.MyConfig import MyConfig
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class StartPage(MDScreen):
    dialog = None
    note = Notification(dialog)

    def __init__(self, **kw):
        super().__init__(**kw)
        self.file_manager_answer = '?'
        self.my_config = MyConfig()

    def __draw_shadow__(self, origin, end, context=None):
        pass

    def __choose_dir_using_manager(self, *args):
        try:
            path = filechooser.choose_dir()[0]
        except:
            self.note.universal_note('You didn\'t choose directory!', [])
            return False
        toast(path)
        self.file_manager_answer = path
        return True

    def __choose_file_using_manager(self, *args):
        try:
            path = filechooser.open_file()[0]
        except:
            self.note.universal_note('You didn\'t choose file!', [])
            return False
        toast(path)
        self.file_manager_answer = path
        return True

    def save(self, *args):
        if self.__choose_file_using_manager():
            self.note.universal_note('File was saved successfully!', [])

    def edit_one(self, *args):
        if self.__choose_file_using_manager():
            new_title = self.file_manager_answer.split('/')
            if len(new_title) == 1:
                new_title = new_title[0].split('\\')
            new_title = new_title[-1]
            new_title = new_title[:new_title.find('.')]
            self.__set_toolbar_title(new_title)
            self.my_config.load_data_by_path(self.file_manager_answer)

    def create_new(self, *args):
        if self.__choose_dir_using_manager():
            self.note.note_with_container(
                [self.__get_dialog_construction_for_file_creation()],
                'Enter file name...',
                (.9, .6)
            )

    def __set_toolbar_title(self, title):
        self.ids.tool_bar.title = title

    def __get_dialog_construction_for_file_creation(self):
        main_cont = MDBoxLayout(height='100dp',
                                orientation='vertical',
                                size_hint_y=None
                                )
        cont = GridLayout(
            rows=2,
            cols=1,
        )
        input_filed = TextInput(font_size=30, write_tab=False, multiline=False)
        ok_btn = Button(text='Ok')
        clear_btn = Button(text='Clear')
        ok_btn.bind(on_press=partial(self.__create_file, self.file_manager_answer + '/', input_filed))
        clear_btn.bind(on_press=partial(self.__clear_text_input, input_filed))
        answers = GridLayout(cols=2, rows=1)
        answers.add_widget(ok_btn)
        answers.add_widget(clear_btn)
        cont.add_widget(input_filed)
        cont.add_widget(answers)
        main_cont.add_widget(cont)
        return main_cont

    def __create_file(self, path, txt_input, *args):
        try:
            my_file = open(path + txt_input.text, "w+")
            my_file.close()
            self.__set_toolbar_title(txt_input.text)
            self.note.dialog_close()
        except Exception as ex:
            pass

    @staticmethod
    def __clear_text_input(txt_input, *args):
        txt_input.text = ''
