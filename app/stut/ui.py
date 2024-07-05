#!/env/bin/python3
#coding: utf-8

import logging
from textual.app import App, ComposeResult
from textual.widgets import Header, Footer
from textual.logging import TextualHandler
from textual.containers import Container

from stut.UI.appUI import AppUI
from stut.audio import device_audio_recorder as darec

logging.basicConfig(
    level="NOTSET",
    handlers=[TextualHandler()],
)

class StutApp(App):
    """ The main application class """

    # Textual-CSS files to load
    CSS_PATH = ["UI/styles/app.tcss"]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        yield Container(
            AppUI(self, id="app_ui")
            , id="app_interface"
        )

        
