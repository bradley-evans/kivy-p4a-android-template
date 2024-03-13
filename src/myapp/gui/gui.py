import kivy


from kivy.app import App
from kivy.uix.label import Label


from myapp.utils.logging import log_generator
log = log_generator(__name__)


class AppGui(App):

    def build(self):
        return Label(text='myapp: hello world')


def gui():
    log.info(f"hello world")
    AppGui().run()

