import pygame

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Music Player")

songs = ["song1.mp3", "song2.mp3", "song3.mp3"]
current_song = 0

pygame.mixer.music.load(songs[current_song])

running = True
while running:
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pygame.mixer.music.pause() if pygame.mixer.music.get_busy() else pygame.mixer.music.unpause()
            elif event.key == pygame.K_s:
                pygame.mixer.music.stop()
            elif event.key in (pygame.K_RIGHT, pygame.K_LEFT):
                current_song = (current_song + (1 if event.key == pygame.K_RIGHT else -1)) % len(songs)
                pygame.mixer.music.load(songs[current_song])
                pygame.mixer.music.play()

    pygame.display.flip()

pygame.quit()
