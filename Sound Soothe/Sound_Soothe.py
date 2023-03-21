import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.audio import SoundLoader
from kivy.uix.image import Image
from kivy.animation import Animation
from kivy.uix.gridlayout import GridLayout

class SplashScreen(Screen):
    def __init__(self, **kwargs):
        super(SplashScreen, self).__init__(**kwargs)
        self.bg = Image(source='splash_bg.png', allow_stretch=True, keep_ratio=False)
        self.text = Label(text="SoundSoothe", font_size=32, color=(0, 0, 0, 1), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        self.add_widget(self.bg)
        self.add_widget(self.text)

        self.anim = Animation(opacity=0, duration=3)
        self.anim.bind(on_complete=self.change_screen)
        self.anim.start(self.bg)
        self.anim.start(self.text)

    def change_screen(self, *args):
        self.manager.current = 'main'

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', spacing=10, padding=[50, 50, 50, 50])

        title = Label(text="Select a sound to relax:", font_size=24)
        layout.add_widget(title)

        grid = GridLayout(cols=2, spacing=10, size_hint=(1, 0.6), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        for sound_type in ['harp', 'guitar', 'piano', 'nature']:
            button_layout = BoxLayout(orientation='vertical', spacing=2)
            button = Button(text='', size_hint=(1, 1))
            button.background_normal = f'{sound_type}_icon.png'
            button.bind(on_release=self.change_screen)
            label = Label(text=sound_type.capitalize(), font_size=14)
            button_layout.add_widget(button)
            button_layout.add_widget(label)
            grid.add_widget(button_layout)
        layout.add_widget(grid)

        self.add_widget(layout)

    def change_screen(self, instance):
        sound_type = instance.parent.children[0].text.lower()
        self.manager.current = sound_type

class SoundScreen(Screen):
    def __init__(self, sound_file, **kwargs):
        super(SoundScreen, self).__init__(**kwargs)
        self.sound = SoundLoader.load(sound_file)
        self.sound.loop = True
        self.sound.stop()

        layout = BoxLayout(orientation='vertical', spacing=10)

        image = Image(source=f"{self.name}_large_image.png", size_hint=(1, 0.7), allow_stretch=True, keep_ratio=False)
        layout.add_widget(image)

        play_button = Button(text="Play", size_hint=(1, 0.1))
        play_button.bind(on_release=self.toggle_play_pause)
        layout.add_widget(play_button)

        back_button = Button(text="Go Back", size_hint=(1, 0.1))
        back_button.bind(on_release=self.go_back)
        layout.add_widget(back_button)

        self.add_widget(layout)

    def toggle_play_pause(self, instance):
        if self.sound.state == 'play':
            self.sound.stop()
            instance.text = "Play"
        else:
            self.sound.play()
            instance.text = "Pause"

    def on_enter(self, *args):
        self.sound.stop()

    def go_back(self, instance):
        self.sound.stop()
        self.manager.current = 'main'

    def on_leave(self, *args):
        self.sound.stop()


class SoundSootheApp(App):
    title = 'SoundSoothe'

    def build(self):
        sm = ScreenManager()

        splash_screen = SplashScreen(name='splash')
        sm.add_widget(splash_screen)

        main_screen = MainScreen(name='main')
        sm.add_widget(main_screen)

        for sound_type in ['harp', 'guitar', 'piano', 'nature']:
            sound_screen = SoundScreen(name=sound_type, sound_file=f"{sound_type}.mp3")
            sm.add_widget(sound_screen)

        return sm

if __name__ == '__main__':
    SoundSootheApp().run()

   
