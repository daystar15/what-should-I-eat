from os.path import dirname
from os.path import join
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from openAPI import result

kv_file = 'test.kv'
Builder.load_file(join(dirname(__file__), kv_file))


class RootLayout(FloatLayout):
    def button01_clicked(self):
        self.sid.text = 'Clicked'


class MainApp(App):
    def build(self):
        return RootLayout()


def main():
    MainApp().run()


if __name__ == "__main__":
    main()