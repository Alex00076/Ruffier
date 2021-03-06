# Модуль, в котором описан бегунок
from kivy.properties import NumericProperty, BooleanProperty
from kivy.uix.button import Button
from kivy.animation import Animation 
from kivy.uix.boxlayout import BoxLayout
from kivy.core.audio import SoundLoader

class Runner(BoxLayout):
    value = NumericProperty(0)
    finished = BooleanProperty(False)
    def __init__(self, total = 10, steptime = 1.5, autorepeat = True, btext = "Приседания", **params):
        super().__init__(**params)  

        self.total = total
        self.autorepeat = autorepeat
        self.btext = btext
        self.animation = (Animation(pos_hint = {'top':0.1}, duration = steptime / 2)) + (Animation(pos_hint = {'top':1.0}, duration = steptime / 2))
        self.animation.repeat = True
        self.animation.on_progress = self.next
        self.btn =Button(size_hint = (1,0.1), pos_hint ={'top':1.0})
        self.add_widget(self.btn)

    def start(self):
        self.value = 0
        self.finished =False
        self.btn.text = self.btext
        if self.autorepeat:
            self.animation.repeat = True
        self.animation.start(self.btn)


    def next(self, widget, step):
        if step == 1.0:
            sound = SoundLoader.load('Sound_19349.mp3')
            self.value += 1
            if sound:
                sound.play()
            if self.value >= self.total:
                self.animation.repeat = False
                self.finished = True
