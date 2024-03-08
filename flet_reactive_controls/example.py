import flet as ft
from .text import ReactiveText
from .state import State, ReactiveState

text = State('')
class InfoAria(ft.UserControl):
    def __init__(self):
        super().__init__(self)
        self.text_len = ReactiveState(lambda: f'文字数:{len(text.get())}', [text])
        self.text_val = ReactiveState(lambda: f'テキストボックスに「{text.get()}」と入力されています。', [text])

    def build(self):
        return ft.Column([ReactiveText(self.text_len), ReactiveText(self.text_val)])

def main(page: ft.Page):

    page.title = "Flet Reactive Control Example"
    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationDestination(icon=ft.icons.EXPLORE, label="Explore"),
            ft.NavigationDestination(icon=ft.icons.COMMUTE, label="Commute"),
            ft.NavigationDestination(
                icon=ft.icons.BOOKMARK_BORDER,
                selected_icon=ft.icons.BOOKMARK,
                label="Explore",
            ),
        ]
    )
    page.add(ft.Column([ft.TextField(on_change=lambda e: text.set(e.control.value)), InfoAria()]))



# ft.app(target=main)
ft.app(main, view=ft.AppView.WEB_BROWSER)