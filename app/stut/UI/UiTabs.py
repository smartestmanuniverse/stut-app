#coding: utf-8

from textual.app import ComposeResult
from textual.widgets import TabPane, TabbedContent, Static

from stut.UI.MainUI import MainUI

class TabsMain(Static):
    """ The main Tabs for the application """

    # Key bindings for the application
    BINDINGS = [( "q", "quit", "Quit" )]

    def __init__(self, my_app, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.my_app = my_app
    
    def action_quit(self):
        self.my_app.exit()
    
    def compose(self) -> ComposeResult:
        with TabbedContent():
            with TabPane("Main", id="main"):
                yield MainUI(self.my_app, id="main-ui")


