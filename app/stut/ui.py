#!/env/bin/python3
#coding: utf-8

import logging
from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Static, Input, Button
from textual.logging import TextualHandler
from textual.containers import Container
from textual.screen import Screen

from stut.UI.appUI import AppUI
from stut.audio import device_audio_recorder as darec

logging.basicConfig(
    level="NOTSET",
    handlers=[TextualHandler()],
)



class BSOD(Screen):

    # Bindings to handle key presses
    BINDINGS = [("escape", "app.pop_screen", "Pop screen")]

    def compose(self) -> ComposeResult:
        yield Static(" Login ", id="title")
        yield Container(
            Input(placeholder="Username", id="username_field"),
            Input(placeholder="Password", id="password_field"),
            Button("Login", id="login_button")
            , id="login_form"
        )
        

class StutApp(App):
    """ The main application class """

    # Textual-CSS files to load
    CSS_PATH = ["UI/styles/app.tcss", "UI/styles/screen01.tcss"]

    SCREENS = {"bsod": BSOD()}

    # Bindings to handle key presses
    BINDINGS = [("b", "push_screen('bsod')", "BSOD")]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_mount(self) -> None:
        self.push_screen('bsod')

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        yield Container(
            AppUI(self, id="app_ui")
            , id="app_interface"
        )

        
