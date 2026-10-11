from textual.app import App, ComposeResult
from textual.containers import HorizontalGroup, VerticalScroll
from textual.widgets import Header, Footer, Button, Label

class Todo(HorizontalGroup):
    def compose(self)->ComposeResult:
        yield Button("☐", id="todo-check", variant="default")
        yield Label("This is a todo task")

class ToDoList(App): # type: ignore
    CSS_PATH = "todolist.tcss"
    BINDINGS = [("ctrl+q", "quit", "Quit App")] 

    def compose(self)->ComposeResult:
        yield Header()
        yield Footer()
        yield VerticalScroll(Todo(), Todo(), Todo(), id="todos")

if __name__ == "__main__": 
    app = ToDoList()
    app.run()