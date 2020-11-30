"""
My first application
"""
import requests
import toga
from toga.style.pack import COLUMN, ROW, CENTER, Pack



# 

class Browser(toga.App):
    def startup(self):
        self.main_window = toga.MainWindow(title=self.name)
        self.webview = toga.WebView(style=Pack(flex=1))
        self.url_input = toga.TextInput(
            initial='https://beeware.org/',
            style=Pack(flex=1)
        )
        box = toga.Box(
            children=[
                toga.Box(
                    children=[
                        self.url_input,
                        toga.Button('Go', on_press=self.load_page, style=Pack(width=50, padding_left=5)),
                    ],
                    style=Pack(
                        direction=ROW,
                        alignment=CENTER,
                        padding=5,
                    )
                ),
                self.webview,
            ],
            style=Pack(
                direction=COLUMN
            )
        )
        self.main_window.content = box
        self.webview.url = self.url_input.value
        # Show the main window
        self.main_window.show()
        def load_page(self, widget):
            self.webview.url = self.url_input.value


def main():
    return Browser('Graze', 'org.beeware.graze')
# class HelloWorld(toga.App):
#     def startup(self):
#         r = requests.get('https://taco-food-api.herokuapp.com/api/v1/category/1')
#         main_box = toga.Box(style=Pack(direction=COLUMN))

#         name_label = toga.Label(
#             r.json(),
#             style=Pack(padding=(0, 5))
#         )
#         self.name_input = toga.TextInput(style=Pack(flex=1))

#         name_box = toga.Box(style=Pack(direction=ROW, padding=5))
#         name_box.add(name_label)
#         name_box.add(self.name_input)

#         button = toga.Button(
#             'Say Hello!',
#             on_press=self.say_hello,
#             style=Pack(padding=5)
#         )
#         text = toga.Label(
#             r.json(),
#             style=Pack(padding=(0, 5))
#         )

#         main_box.add(name_box)
#         main_box.add(button)
#         main_box.add(text)

#         self.main_window = toga.MainWindow(title=self.formal_name)
#         self.main_window.content = main_box
#         self.main_window.show()

#     def say_hello(self, widget):
#         print("Hello", self.name_input.value)

# def main():
#     return HelloWorld()
