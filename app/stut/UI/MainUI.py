#coding: utf-8

from textual.app import ComposeResult
from textual.widgets import Label, Static
from textual.containers import Horizontal, Vertical
from textual.widgets import Input, Button
from stut.UI.MessagesScrollable import MessagesScrollable
from textual import events


class InputTextMessage(Input):
    def __init__(self, my_app, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.my_app = my_app
        self.value = ""
        self.placeholder = "Zone de saisie de texte"
        
    def on_key(self, event: events.Key) -> None:
        pass


class MainUI(Static):
    def __init__(self, my_app, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.my_app = my_app
        self.messages_area = MessagesScrollable(self.my_app, id="messages_area")
        self.input_field = InputTextMessage(self.my_app, id="input_field")
        self.submit_button = Button("Valider", id="submit_button", classes="send_button")

    async def on_button_pressed(self, event: Button.Pressed) -> None:
        text = self.input_field.value
        
        # Vider le champ de saisie
        self.input_field.value = ""

        # Ajouter le message dans la zone de messages
        await self.messages_area.add_message(text)


    def compose(self) -> ComposeResult:
        yield Vertical(
            Horizontal(self.messages_area, id="output_zone"),
            Horizontal(Label("~~~~"), id="status_chat_zone"),
            Horizontal(
                self.input_field,
                self.submit_button,
                id="input_zone"
            ),
            id="main_content"
        )




