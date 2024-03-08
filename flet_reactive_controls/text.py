# Python(Flet)でリアクティブなUIを作る方法を考える
# https://qiita.com/ForestMountain1234/items/64edacd5275c1ce4c943

from .state import StateProperty, bind_props, get_prop_value
import flet as ft

class ReactiveText(ft.UserControl):
    def __init__(self, text: StateProperty[str], size: StateProperty[int] = 17):
        super().__init__()
        self.control = ft.Text('')
        self.text = text
        self.size = size

        self.set_props()
        bind_props([self.text, self.size], lambda: self.update())#自動でデータバインディング

    def set_props(self):
        self.control.value = get_prop_value(self.text)#通常の変数かStateかを判断して値を取得
        self.control.size  = get_prop_value(self.size)

    def update(self):
        self.set_props()
        self.control.update()

    def build(self):
        return self.control