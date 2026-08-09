import pygame,sys,Tablero

pygame.init()
screen = pygame.display.set_mode((800,400))
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    tablero = Tablero.init()
    Tablero.draw(tablero, screen)
    clock.tick(60)
pygame.quit()
sys.exit()