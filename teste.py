import pygame
pygame.init()
pygame.display.set_mode((200,100))
pygame.mixer.music.load('Musica.mp3')
pygame.mixer.music.play(1)
pygame.mixer.music.stop()
