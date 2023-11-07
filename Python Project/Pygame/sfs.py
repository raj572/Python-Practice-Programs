import pygame
pygame.init()
red=(255,0,0)
white=(255,255,255)
black=(0,0,0)

gd=pygame.display.set_mode((500,700))
pygame.display.update()
x=300
y=200

game_over=False

while game_over==False:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_over=True
        if event.type==pygame.KEYDOWN:
            if event.type==pygame.K_LEFT:
                x-=10
            elif event.type==pygame.K_RIGHT:
                x+=10

    gd.fill(white)
    pygame.draw.rect(gd,red,[300,200,50,50])
    pygame.display.update()
pygame.quit()
quit()