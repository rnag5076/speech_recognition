import pygame
import time

pygame.mixer.init()
pygame.display.init()
screen = pygame.display.set_mode ( ( 420 , 240 ) )

playlist = list()
playlist.append("C:/Users/MUJ/Desktop/songs/07 - Tera Yaar Hoon Main.mp3")
playlist.append("C:/Users/MUJ/Desktop/songs/Besabriyaan - 320Kbps.mp3")
playlist.append("C:/Users/MUJ/Desktop/songs/linkin park-leave out all the rest.mp3")

pygame.mixer.music.load ( playlist.pop() ) 
pygame.mixer.music.queue ( playlist.pop() )
pygame.mixer.music.set_endevent ( pygame.USEREVENT )
pygame.mixer.music.play()   

running = True
while running:
   for event in pygame.event.get():
      if event.type == pygame.USEREVENT: 
         if len ( playlist ) > 0:      
            pygame.mixer.music.queue ( playlist.pop() )
