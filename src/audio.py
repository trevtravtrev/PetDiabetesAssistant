import pygame
from os.path import dirname, abspath, join
import os


class TextToSpeech:
    pass


def play_sound(sound_file, volume):
    os.putenv('SDL_AUDIODRIVER', 'alsa')
    os.putenv('SDL_AUDIODEV', '/dev/audio')
    sound_filepath = join(dirname(abspath(__file__)), "sounds", sound_file)

    pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=4096)
    pygame.mixer.music.set_volume(volume)
    pygame.mixer.music.load(sound_filepath)
    pygame.mixer.music.play()
