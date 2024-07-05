#coding: utf-8

from textual.app import ComposeResult
from textual.containers import  Vertical
from textual.widgets import Static

from stut.UI.UiTabs import TabsMain

class AppUI(Static):
        def __init__(self, my_app, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.my_app = my_app
            
        def compose(self) -> ComposeResult:
            self.tabs = TabsMain(self.my_app, id="tabs")

            yield Vertical(
                self.tabs
                , id="app_ui"
            )