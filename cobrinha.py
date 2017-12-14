from copy import copy
import pygame
 
SIZE = W, H = (800, 600)
BLOCK = W / 32
 
def init():
    global screen
    screen = pygame.display.set_mode(SIZE)
 
def process_keys(keys, pos):
    if keys[pygame.K_RIGHT]:
        pos[0] += BLOCK
        if pos[0] >= W:
            pos[0] = 0
    if keys[pygame.K_LEFT]:
        pos[0] -= BLOCK
        if pos[0] < 0:
            pos[0] = W - BLOCK
    if keys[pygame.K_DOWN]:
        pos[1] += BLOCK
        if pos[1] >= H:
            pos[1] = 0
    if keys[pygame.K_UP]:
        pos[1] -= BLOCK
        if pos[1] < 0:
            pos[1] = H - BLOCK
 
 
def main():
    pos = [0, 0]
    body = [pos, ]
    max_length = 7
    while True:
        event = pygame.event.get()
        for event in event:
            if event.type == pygame.QUIT:
                return
 
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            return
        process_keys(keys, pos)
        body.insert(0, copy(pos))

        if len(body) > max_length:
            end = body.pop()
            pygame.draw.rect(screen, (0, 0, 0), (end[0], end[1], BLOCK, BLOCK))

        pygame.draw.rect(screen, (255, 0, 0), (pos[0], pos[1], BLOCK, BLOCK))
 
        old_pos = copy(pos)
 
        pygame.display.flip()
        pygame.time.delay(30)
 
try:
    init()
    main()
finally:
    pygame.quit()
