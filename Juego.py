import pygame
import sys
import random
pygame.init()

Ancho=700
Alto=500

screen=pygame.display.set_mode((Ancho, Alto))
player_pos =(pygame.Vector2(screen.get_width() / 2,478))
objeto_pos= [(random.randint(0, 660)),0]
objeto_pos1= [(random.randint(0, 660)),0]
objeto_pos2= [0,(random.randint(23, 479))]
objeto_pos3= [669,(random.randint(23, 479))]
game_over=False
inicio=False

clock = pygame.time.Clock()
dt = 0
Font=pygame.font.SysFont("Minecraft",40)
background=pygame.image.load(r"C:\Users\6305\Downloads\fondo.png").convert()
menuinicio=pygame.image.load(r"C:\Users\6305\Downloads\MenuInicio.png").convert()
menuinicio2=pygame.image.load(r"C:\Users\6305\Downloads\Thank You (1).png").convert()
menufinal=pygame.image.load(r"C:\Users\6305\Downloads\Good.png").convert()

def detectar_colision(player_pos, objeto_pos):
    px, py = player_pos
    ox, oy = objeto_pos
    distance = ((px - ox) ** 2 + (py - oy) ** 2) ** 0.5
    return distance < 35

def detectar_colision(player_pos, objeto_pos1):
    px, py = player_pos
    ox1, oy1 = objeto_pos1
    distance = ((px - ox1) ** 2 + (py - oy1) ** 2) ** 0.5
    return distance < 35

def detectar_colision(player_pos, objeto_pos2):
    px, py = player_pos
    ox2, oy2 = objeto_pos2
    distance = ((px - ox2) ** 2 + (py - oy2) ** 2) ** 0.5
    return distance < 35

def detectar_colision(player_pos, objeto_pos3):
    px, py = player_pos
    ox3, oy3 = objeto_pos3
    distance = ((px - ox3) ** 2 + (py - oy3) ** 2) ** 0.5
    return distance < 35

while not inicio:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
    screen.blit(menuinicio, (0,0))
    game_over=True
    pygame.display.set_caption("Menu👻")
    pygame.display.update()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        inicio=True
        game_over=False

pygame.mixer.music.load(r"C:\Users\6305\Downloads\y2mate.com - Plants vs Zombies Soundtrack Pool Stage.mp3")
pygame.mixer.music.load(r"C:\Users\6305\Downloads\y2mate.com - Plants vs Zombies Soundtrack Zomboss Stage.mp3")
pygame.mixer.music.play(-1)

startt=pygame.time.get_ticks()
while game_over==False:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
    pygame.display.set_caption("Esquiva👻")
    screen.fill("white")
    screen.blit(background, (0,0))
    actual=pygame.time.get_ticks()
    Timer=(actual-startt)//1000
    Puntos=(actual-startt)//100
    Time=Font.render("TIME",0,(0,0,0))
    Score=Font.render("SCORE",0,(0,0,0))
    cronometro=Font.render(str(Timer),0,(0,0,0))
    screen.blit(cronometro,(47,45))
    screen.blit(Time,(10,10))
    screen.blit(Score,(550,10))
    Scorer=Font.render(str(Puntos),0,(0,0,0))
    screen.blit(Scorer,(590,45))
    pygame.draw.circle(screen, "green", player_pos, 25)
    if Timer >=1:
        pygame.draw.circle(screen, "red", objeto_pos, 25)
        if detectar_colision(player_pos, objeto_pos):
            game_over = True    
    if Timer >=5: 
        pygame.draw.circle(screen, "red", objeto_pos1, 25)
        if detectar_colision(player_pos, objeto_pos1):
            game_over = True
    if Timer >=10:    
        pygame.draw.circle(screen, "red", objeto_pos2, 35)
        if detectar_colision(player_pos, objeto_pos2):
            game_over = True
    if Timer >=15:    
        pygame.draw.circle(screen, "red", objeto_pos3, 35)
        if detectar_colision(player_pos, objeto_pos3):
            game_over = True

    pygame.display.update()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 400 * dt
    if keys[pygame.K_s]:
        player_pos.y += 400 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 400 * dt
    if keys[pygame.K_d]:
        player_pos.x += 400 * dt

    if Timer >=1:
        if objeto_pos[1]>=0 and objeto_pos[1] < 500:
            objeto_pos[1] +=12
        else:
            objeto_pos[1]=0
            objeto_pos[0]=random.randint(26,668)
    if Timer >=7:
        if objeto_pos1[1]>=0 and objeto_pos1[1] < 500:
            objeto_pos1[1] +=12
        else:
            objeto_pos1[1]=0
            objeto_pos1[0]=random.randint(29,668)
    
    if Timer >=14:
        if objeto_pos2[0]>=0 and objeto_pos2[0] < 676:
            objeto_pos2[0] +=12
        else:
            objeto_pos2[0]=0
            objeto_pos2[1]=random.randint(23,479)
    if Timer >=20:
        if objeto_pos3[0]>=0 and objeto_pos3[0] < 676:
            objeto_pos3[0] -=12
        else:
            objeto_pos3[0]=675
            objeto_pos3[1]=random.randint(23,479)

    if player_pos.x <= 27:
        player_pos.x =28
    if player_pos.x >=668:
        player_pos.x =667
    if player_pos.y <=29:
        player_pos.y =30
    if player_pos.y >=470:
        player_pos.y =469

    if detectar_colision(player_pos,objeto_pos):
        game_over = True
    pygame.display.flip()
    dt = clock.tick(60) / 1000

while inicio==True and game_over==True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
    screen.fill("black")
    screen.blit(menufinal, (0,0))
    Puntaje=Font.render(str(Puntos),0,(251,42,171))
    screen.blit(Puntaje,(490,270))
    Tempo=Font.render(str(Timer),0,(90,221,225))
    screen.blit(Tempo,(170,270))
    pygame.display.set_caption("Final👻")
    pygame.display.update()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:    
        pygame.quit()