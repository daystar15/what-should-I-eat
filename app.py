from os.path import dirname
from os.path import join
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from openAPI import *

kv_file = 'test.kv'
Builder.load_file(join(dirname(__file__), kv_file))


class RootLayout(FloatLayout):
    def button01_clicked(self):
        # Label 위젯의 text_size를 (width, None)으로 설정하여 화면 너비에 맞게 자동으로 줄바꿈되도록 만듭니다.
        # 이때 width 값을 적절하게 조절해야 합니다.
        self.sid.text_size = (self.sid.width, None)
        self.sid.text = result


class MainApp(App):
    def build(self):
        return RootLayout()


def main():
    MainApp().run()


if __name__ == "__main__":
    main()