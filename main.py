from kivy.core.window import Window
from Code.py_files.MyApp import MyApp
from kivy.lang import Builder


Builder.load_file("Code/kv_files/start_page.kv")
Builder.load_file("Code/kv_files/steps.kv")
Builder.load_file("Code/kv_files/notices.kv")
Builder.load_file("Code/kv_files/scheme.kv")
Builder.load_file("Code/kv_files/metadata.kv")


def main():
    Window.maximize()
    MyApp().run()


if __name__ == "__main__":
    main()
