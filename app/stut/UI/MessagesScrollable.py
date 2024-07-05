#coding: utf-8

from time import monotonic

from textual.app import ComposeResult
from textual.reactive import reactive
from textual.widgets import Label, Static
from textual.containers import Container
from textual.containers import ScrollableContainer
from textual.widgets import Label

class Message(Container):
    start_time = reactive(monotonic)
    time = reactive(0.0)

    def __init__(self, my_app, text_message, sender_name, from_classe, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.my_app = my_app
        self.label_message = Label(f"{text_message}", classes=f"label_message {from_classe}")
        self.label_message.border_title = f"<{sender_name}>"

    def on_mount(self) -> None:
        """Event handler called when widget is added to the app."""
        self.set_interval(1 / 60, self.update_time)

    def update_time(self) -> None:
        """Method to update the time to the current time."""
        self.time = monotonic() - self.start_time

    def watch_time(self, time: float) -> None:
        """Called when the time attribute changes."""
        minutes, seconds = divmod(time, 60)
        hours, minutes = divmod(minutes, 60)
        self.label_message.border_subtitle = f"{hours:02.0f}:{minutes:02.0f}:{seconds:05.2f}"

    def compose(self) -> ComposeResult:
        yield self.label_message


class MessagesScrollable(Static):
    def __init__(self, my_app, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.my_app = my_app
        self.messages = []
        self.message = None
        
    async def add_message(self, message, sender_name="me", from_classe="from_me"):
        self.message = Message(self.my_app, message, sender_name, from_classe)
        self.messages.append(self.message)
        self.query_one("#messages_scrollable").mount(self.message)

    def compose(self) -> ComposeResult:
        yield ScrollableContainer(
            Label("Messages", classes="ui_label_header"),
            id="messages_scrollable"
        )