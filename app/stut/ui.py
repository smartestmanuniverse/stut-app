#!/env/bin/python3
#coding: utf-8

import logging
from textual.app import App, ComposeResult
from textual.widgets import Header, Footer
from textual.containers import Vertical, Horizontal, VerticalScroll, HorizontalScroll, Container
from textual import events
from textual.logging import TextualHandler


logging.basicConfig(
    level="NOTSET",
    handlers=[TextualHandler()],
)

class StutApp(App):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
