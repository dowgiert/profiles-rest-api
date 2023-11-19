from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.app import App


class MyApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')

        # Background text
        self.background_text = TextInput(
            text='Hello, Kivy!', readonly=True, multiline=True)
        self.layout.add_widget(self.background_text)

        # Button to clear background text
        self.clear_button = Button(text='Clear Text', on_press=self.clear_text)
        self.layout.add_widget(self.clear_button)

        return self.layout

    def clear_text(self, instance):
        # Remove the background text and replace it with an editable TextInput
        self.layout.remove_widget(self.background_text)
        self.user_input = TextInput(multiline=True)
        self.layout.add_widget(self.user_input)


if __name__ == '__main__':
    MyApp().run()
