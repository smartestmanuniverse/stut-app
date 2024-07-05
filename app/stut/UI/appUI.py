#coding: utf-8

from textual.app import ComposeResult
from textual.containers import  Vertical
from textual.widgets import Static

class AppUI(Static):
        def __init__(self, my_app, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.my_app = my_app
            
        def compose(self) -> ComposeResult:
            

            yield Vertical(
                
                id="app_ui"
            )