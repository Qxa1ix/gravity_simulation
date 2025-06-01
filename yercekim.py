

import pygame
from pygame import MOUSEMOTION, MOUSEBUTTONDOWN

pygame.init()

w=pygame.display.set_mode((1200,700))
fps=60
saat=pygame.time.Clock()
ball_cord=[600,350]
ball=pygame.draw.circle(w,(200,20,200),ball_cord,30)

gravity=20




drag=False

d=True
while d:
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            d=False

        if i.type==pygame.MOUSEBUTTONDOWN:
            x, y = i.pos
            dx = x - ball_cord[0]
            dy = y - ball_cord[1]
            cc = dx ** 2 + dy ** 2
            if cc < 30 ** 2:
                drag=True
        if i.type==pygame.MOUSEBUTTONUP:
            drag=False
        if i.type == MOUSEMOTION and drag:
            ball_cord=list(i.pos)

    if drag==False and ball_cord[1]<660:
        ball_cord[1] += gravity

    w.fill((0, 0, 0))
    ball = pygame.draw.circle(w, (200, 20, 200), ball_cord, 30)
    pygame.display.update()
    saat.tick(fps)
