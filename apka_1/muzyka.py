import time

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

from functools import partial

Window.size = (500, 700)


class MyApp(MDApp):

    def getLinkInfo(self, event, widndow):
        self.link = self.linkinput.text
        self.yt = YouTube(self.link)

        self.views = str(self.yt.views)
        self.length = str(self.yt.length)
        print(f"views is {self.views}.")
        print(f"Length is {self.length}.")

        self.viewsLabel.text = "Amount of views: " + self.views
        self.lengthLabel.text = "Length is seconds: " + self.length

        self.downloadButton.pos_hint={'center_x': 0.5, 'center_y':0.1}


    def download(self, event, layout):
        self.ys = self.yt.streams.get_highest_resolution()

        print("Downloading")

        self.ys.download('C:/Users/karol/OneDrive/Pulpit/apki/yd_down_manager')

        print("Download complete :)")
        time.sleep(1000)
        exit()


    def build(self):
        layout = MDRelativeLayout(
            md_bg_color=[235/255, 158/255, 185/255])  # MDRelativeLayouts- simplifies layout

        # size_hint służy do określania wielkości
        # jest też width_hint oraz height_hint
        self.image = Image(  # to stretch young leosia you have to allow_stretch=True amd leep_ratio=False
            source='Young_Leosia.jpg', allow_stretch=True, keep_ratio=False,  size_hint_y=0.5,
            size_hint_x=1, pos_hint={'center_x': 0.5,
                                     'center_y': 0.75}, color=[235/255, 158/255, 185/255])

        self.youtubelink = Label(halign='center', valign='middle', pos_hint={'center_y': 0.57},
                                 text='[color=ee33ff]I love[/color]\n[color=ee33ff]Young Leosia[/color]', markup=True, font_size='40sp')

        self.linkinput = TextInput(text="", pos_hint={'center_x': 0.5, 'center_y': 0.47},
                                   size_hint=(1, None), height=48,
                                   font_size=29, foreground_color=(0, .5, 0),
                                   font_name="Comic")

        self.linkbutton = Button(text="Get Link", pos_hint={
                             'center_x': 0.5, 'center_y': 0.39}, size_hint_y=0.1, size_hint_x=0.3, color='ee33ff', background_color="pink")

        self.linkbutton.bind(on_press = partial(self.getLinkInfo,layout))

        self.viewsLabel = Label(text="", pos_hint={
                             'center_x': 0.5, 'center_y': 0.28}, font_size='20sp')

        self.lengthLabel = Label(text="", pos_hint={
                             'center_x': 0.5, 'center_y': 0.17}, font_size='20sp')
        
        self.downloadButton = Button(text = 'Download', pos_hint={'center_x': 0.5, 'center_y': 20},
                                     size_hint=(.2,.1), size=(75,75), font_name= 'Comic',
                                     bold = True, font_size = 24, background_color=(0,1,0))
        
        self.downloadButton.bind(on_press = partial(self.download, layout))
        

        layout.add_widget(self.image)
        layout.add_widget(self.youtubelink)
        layout.add_widget(self.linkinput)
        layout.add_widget(self.linkbutton)
        layout.add_widget(self.viewsLabel)
        layout.add_widget(self.lengthLabel)

        layout.add_widget(self.downloadButton)

        return layout


if __name__ == '__main__':
    MyApp().run()
