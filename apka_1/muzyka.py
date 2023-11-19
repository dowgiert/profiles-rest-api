from kivy.config import Config
from pytube import YouTube

# simplifies working with some widget properties
from kivymd.uix.relativelayout import MDRelativeLayout

# is argument that you put in class generaly xD
from kivymd.app import MDApp

# Label widget is for rendering text
# widżet- podstawowy elementu graficznego
from kivy.uix.label import Label
# TextInput widget provides a box for editable plain text.
from kivy.uix.textinput import TextInput
# providing images
from kivy.uix.image import Image
# providing buttons
from kivy.uix.button import Button
# for example we importing kivy.uix.button to not import whole kivy

# we can window size with it
from kivy.core.window import Window

Window.size = (500, 700)


class MyApp(MDApp):
    def build(self):
        layout = MDRelativeLayout(
            md_bg_color=[235/255, 158/255, 185/255])  # MDRelativeLayouts- simplifies layout

        # size_hint służy do określania wielkości
        # jest też width_hint oraz height_hint
        self.image = Image(  # to stretch young leosia you have to allow_stretch=True amd leep_ratio=False
            source='C:/Users/Dowgiertos/Desktop/apki/apka_1/Young_Leosia.jpg', allow_stretch=True, keep_ratio=False,  size_hint_y=0.5,
            size_hint_x=1, pos_hint={'center_x': 0.5,
                                     'center_y': 0.75}, color=[235/255, 158/255, 185/255])

        self.youtubelink = Label(halign='center', valign='middle', pos_hint={'center_y': 0.57},
                                 text='[color=ee33ff]I love[/color]\n[color=ee33ff]Young Leosia[/color]', markup=True, font_size='40sp')

        self.linkinput = TextInput(text="", pos_hint={'center_x': 0.5, 'center_y': 0.47},
                                   size_hint=(1, None), height=48,
                                   font_size=29, foreground_color=(0, .5, 0),
                                   font_name="Comic")

        self.button = Button(text="Button", pos_hint={
                             'center_x': 0.5, 'center_y': 0.39}, size_hint_y=0.1, size_hint_x=0.3, color='ee33ff', background_color="pink")

        layout.add_widget(self.image)
        layout.add_widget(self.youtubelink)
        layout.add_widget(self.linkinput)
        layout.add_widget(self.button)

        return layout


if __name__ == '__main__':
    MyApp().run()
