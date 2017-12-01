# primeiro programa que eu aprendi com o João Bueno fera
# pygame.org/docs/

import pygame
import random

W, H = 800, 600

tela = pygame.display.set_mode((W, H), pygame.FULLSCREEN)

def sorteia():
    r = random.randrange(0, 256, 127)
    g = random.randrange(0, 256, 127)
    b = random.randrange(0, 256, 127)
    return (r, g, b)

def desenha(tamanho):
    for y in range(0, H, tamanho):
        for x in range(0, W, tamanho):
            pygame.draw.rect (tela, sorteia(), (x, y, tamanho, tamanho))

def principal():
    tamanho = 100
    while True:
        eventos = pygame.event.get()
        for evento in eventos:
            if evento.type == pygame.QUIT:
                return
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    return
                if evento.key == pygame.K_LEFT:
                    tamanho = tamanho - 10
                if evento.key == pygame.K_RIGHT:
                    tamanho = tamanho + 10
        desenha(tamanho)
        pygame.display.flip()
        pygame.time.delay(100)

try:
    principal()
finally:
    pygame.quit()
