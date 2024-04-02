import pygame
from pygame.locals import *

pygame.init()
pygame.mixer.init()
pygame.display.init()

wrong = pygame.mixer.Sound('LIE.mp3')
right = pygame.mixer.Sound('CORRECT.mp3')

logo = pygame.image.load("logo.png")
logotroll = pygame.image.load("logotroll.png")
logo1 = pygame.image.load("logo1.png")
logo2 = pygame.image.load("logo2.png")
logo3 = pygame.image.load("logo3.png")
logo4 = pygame.image.load("logo4.png")
pygame.display.set_icon(logo)

pygame.display.set_caption("projet JO")

def draw_text(text,font,text_col,x,y,loc):
    img = font.render(text,True,text_col)
    loc.blit(img,(x,y))

fenetre = pygame.display.set_mode((1280, 720))
text_font_p = pygame.font.Font("arial.ttf",30,bold = True,italic = True)
text_font_g = pygame.font.Font("arial.ttf",90,bold = True,italic = True)
background = pygame.image.load("blanc.jpg").convert()
bonneRep = pygame.image.load('bonneReponse.png').convert_alpha()
backArrow = pygame.image.load('back.png').convert_alpha()
mauvaiseRep = pygame.image.load('mauvaiseReponse.png').convert_alpha()
boutonpng = pygame.image.load('bouton.png').convert()
boutoncarrepng = pygame.image.load('boutoncarre.png').convert()
perso = pygame.image.load("dingoofygauche.png").convert_alpha()
perso2 = pygame.image.load("forest.png").convert_alpha()
piste = pygame.image.load("Pistedeski.png").convert()
piste2 = pygame.image.load("Pistedehaie.png").convert()
pistex = 0
haie = pygame.image.load("haie.png").convert_alpha()
lolol = pygame.image.load("lolol.png").convert_alpha()
tropheeor = pygame.image.load("or.png").convert_alpha()
tropheeargent = pygame.image.load("argent.png").convert_alpha()

score = 0
menu = True
scnaide = False
scnaide2 = False
scnpiste = False
scnhaie = False
q1 = False
q2 = False
q3 = False
q4 = False
q5 = False
q6 = False
q7 = False
q8 = False
q9 = False
q10 = False
q11 = False
q12 = False
q13 = False
posX = 600
posY = 30
repq1 = True
repq2 = True
repq3 = True
repq4 = True
repq5 = True
repq6 = True
repq7 = True
repq8 = True
repq9 = True
repq10 = True
repq11 = True
repq12 = True
scorex = 1080
bq1 = False
bq2 = False
bq3 = False
bq4 = False
bq5 = False
bq6 = False
bq7 = False
bq8 = False
bq9 = False
bq10 = False
bq11 = False
bq12 = False
bq13 = False
brepq1 = True
brepq2 = True
brepq3 = True
brepq4 = True
brepq5 = True
brepq6 = True
brepq7 = True
brepq8 = True
brepq9 = True
brepq10 = True
brepq11 = True
brepq12 = True
jumping = False
up = False
down = False
haieX = 0
vitesse = .2
trophee1 = 0
trophee2 = 0

def start():
    fenetre.blit(background,(0,0))
    bouton1 = pygame.Surface((200,50))
    bouton2 = pygame.Surface((200,50))
    bouton3 = pygame.Surface((200,50))
    bouton1.blit(boutonpng,(0,0))
    bouton2.blit(boutonpng,(0,0))
    bouton3.blit(boutonpng,(0,0))
    draw_text('Jouer Hiver',text_font_p,(0,0,0),20,7,bouton1)
    if trophee1 == 1:
        fenetre.blit(tropheeargent,(750,290))
    elif trophee1 == 2:
        fenetre.blit(tropheeor,(750,290))
    draw_text('Quitter',text_font_p,(0,0,0),50,7,bouton2)
    if trophee2 == 1:
        fenetre.blit(tropheeargent,(750,390))
    elif trophee2 == 2:
        fenetre.blit(tropheeor,(750,390))
    draw_text('Jouer Été',text_font_p,(0,0,0),35,7,bouton3)
    fenetre.blit(bouton1,(540,300))
    fenetre.blit(bouton2,(540,500))
    fenetre.blit(bouton3,(540,400))
    draw_text('PROJET',text_font_p,(0,0,0),580,20,fenetre)
    if trophee1 == 2 and trophee2 == 2 :
        draw_text('Bien Joué !',text_font_p,(0,0,0),200,300,fenetre)
        draw_text('Vous avez obtenu un score ',text_font_p,(0,0,0),100,400,fenetre)
        draw_text('parfait à chaque mini-jeu !',text_font_p,(0,0,0),110,450,fenetre)
    elif trophee1 >= 1 and trophee2 >= 1 :
        draw_text('Bravo !',text_font_p,(0,0,0),225,300,fenetre)
        draw_text('Vous avez gagné à chaque',text_font_p,(0,0,0),100,400,fenetre)
        draw_text('mini-jeu ! Maintenant, essayez ',text_font_p,(0,0,0),70,450,fenetre)
        draw_text('de faire un score parfait !',text_font_p,(0,0,0),115,500,fenetre)

    pygame.display.update()

start()

def aide():
    fenetre.blit(background,(0,0))
    bouton1 = pygame.Surface((200,50))
    bouton1.blit(boutonpng,(0,0))
    draw_text('OK',text_font_p,(0,0,0),80,7,bouton1)
    fenetre.blit(bouton1,(540,500))
    draw_text('Comment jouer :',text_font_p,(0,0,0),540,20,fenetre)
    draw_text('Utilisez Q et D pour déplacer le skieur et passez les portes.',text_font_p,(0,0,0),100,200,fenetre)
    draw_text('Les touches ne peuvent pas être maintenues.',text_font_p,(0,0,0),100,250,fenetre)
    draw_text('Faites au moins 7 pour gagner, 12 pour un score parfait.',text_font_p,(0,0,0),100,350,fenetre)
    pygame.display.update()

def aide2():
    fenetre.blit(background,(0,0))
    bouton1 = pygame.Surface((200,50))
    bouton1.blit(boutonpng,(0,0))
    draw_text('OK',text_font_p,(0,0,0),80,7,bouton1)
    fenetre.blit(bouton1,(540,500))
    draw_text('Comment jouer :',text_font_p,(0,0,0),540,20,fenetre)
    draw_text('Utilisez Espace pour sauter au dessus des haies.',text_font_p,(0,0,0),100,200,fenetre)
    draw_text('Faites au moins 7 pour gagner, 12 pour un score parfait.',text_font_p,(0,0,0),100,300,fenetre)

def pistedeski():
    global posX,posY,scorecolor,score,scorex
    fenetre.blit(piste,(0,0))
    fenetre.blit(perso,(posX,posY))
    retour = pygame.Surface((50,50))
    retour.blit(boutoncarrepng,(0,0))
    retour.blit(backArrow,(0,0))
    fenetre.blit(retour,(10,10))
    if score<7:
        scorecolor=(255,0,0)
    if score>6:
        scorecolor=(0,255,0)
    if score >9:
        scorex = 1030
    if score ==12:
        scorecolor=(255,191,0)
    draw_text(f'{score}/12',text_font_g,scorecolor,scorex,10,fenetre)

def coursehaie():
    global posX,posY,scorecolor,score,scorex,pistex,haieX,vitesse
    if pistex < -1280:
        pistex = 0
    fenetre.blit(piste2,(pistex,0))
    fenetre.blit(haie,(800-haieX,450))
    fenetre.blit(haie,(1600-haieX,450))
    fenetre.blit(haie,(2400-haieX,450))
    fenetre.blit(haie,(3200-haieX,450))
    fenetre.blit(haie,(4000-haieX,450))
    fenetre.blit(haie,(4800-haieX,450))
    fenetre.blit(haie,(5600-haieX,450))
    fenetre.blit(haie,(6400-haieX,450))
    fenetre.blit(haie,(7200-haieX,450))
    fenetre.blit(haie,(8000-haieX,450))
    fenetre.blit(haie,(8800-haieX,450))
    fenetre.blit(haie,(9600-haieX,450))
    fenetre.blit(perso2,(posX,posY))
    retour = pygame.Surface((50,50))
    retour.blit(boutoncarrepng,(0,0))
    retour.blit(backArrow,(0,0))
    fenetre.blit(retour,(10,10))
    if score<7:
        scorecolor=(255,0,0)
    if score>6:
        scorecolor=(0,255,0)
    if score >9:
        scorex = 1030
    if score ==12:
        scorecolor=(255,191,0)
    draw_text(f'{score}/12',text_font_g,scorecolor,scorex,10,fenetre)
    pistex += -.1
    haieX += vitesse
    vitesse += .00005

def ques1():
    fenetre.blit(background,(0,0))
    bouton1 = pygame.Surface((50,50))
    bouton2 = pygame.Surface((50,50))
    bouton3 = pygame.Surface((50,50))
    bouton4 = pygame.Surface((50,50))
    bouton1.blit(boutoncarrepng,(0,0))
    bouton2.blit(boutoncarrepng,(0,0))
    bouton3.blit(boutoncarrepng,(0,0))
    bouton4.blit(boutoncarrepng,(0,0))
    draw_text('A',text_font_p,(0,0,0),15,7,bouton1)
    draw_text('B',text_font_p,(0,0,0),15,7,bouton2)
    draw_text('C',text_font_p,(0,0,0),15,7,bouton3)
    draw_text('D',text_font_p,(0,0,0),15,7,bouton4)
    fenetre.blit(bouton1,(100,300))
    fenetre.blit(bouton2,(100,400))
    fenetre.blit(bouton3,(100,500))
    fenetre.blit(bouton4,(100,600))
    draw_text('Question 1 :',text_font_p,(0,0,0),580,20,fenetre)
    draw_text("Parmi ces sports, lequel n'est pas une épreuve aux Jeux Olympiques ?",text_font_p,(0,0,0),100,100,fenetre)
    draw_text('Formule 1',text_font_p,(0,0,0),200,307,fenetre)
    draw_text('BasketBall',text_font_p,(0,0,0),200,407,fenetre)
    draw_text('Golf',text_font_p,(0,0,0),200,507,fenetre)
    draw_text('Lancé de javelot',text_font_p,(0,0,0),200,607,fenetre)
    pygame.display.update()

def ques2():
    fenetre.blit(background,(0,0))
    bouton1 = pygame.Surface((50,50))
    bouton2 = pygame.Surface((50,50))
    bouton3 = pygame.Surface((50,50))
    bouton4 = pygame.Surface((50,50))
    bouton1.blit(boutoncarrepng,(0,0))
    bouton2.blit(boutoncarrepng,(0,0))
    bouton3.blit(boutoncarrepng,(0,0))
    bouton4.blit(boutoncarrepng,(0,0))
    draw_text('A',text_font_p,(0,0,0),15,7,bouton1)
    draw_text('B',text_font_p,(0,0,0),15,7,bouton2)
    draw_text('C',text_font_p,(0,0,0),15,7,bouton3)
    draw_text('D',text_font_p,(0,0,0),15,7,bouton4)
    fenetre.blit(bouton1,(100,300))
    fenetre.blit(bouton2,(100,400))
    fenetre.blit(bouton3,(100,500))
    fenetre.blit(bouton4,(100,600))
    draw_text('Question 2 :',text_font_p,(0,0,0),580,20,fenetre)
    draw_text("En quelles saisons ont lieu les Jeux Olympiques ?",text_font_p,(0,0,0),100,100,fenetre)
    draw_text('Été et Automne',text_font_p,(0,0,0),200,307,fenetre)
    draw_text('Printemps et Hiver',text_font_p,(0,0,0),200,407,fenetre)
    draw_text('Été et Hiver',text_font_p,(0,0,0),200,507,fenetre)
    draw_text('Automne et Printemps',text_font_p,(0,0,0),200,607,fenetre)
    pygame.display.update()

def ques3():
    fenetre.blit(background,(0,0))
    bouton1 = pygame.Surface((50,50))
    bouton2 = pygame.Surface((50,50))
    bouton3 = pygame.Surface((50,50))
    bouton4 = pygame.Surface((50,50))
    bouton1.blit(boutoncarrepng,(0,0))
    bouton2.blit(boutoncarrepng,(0,0))
    bouton3.blit(boutoncarrepng,(0,0))
    bouton4.blit(boutoncarrepng,(0,0))
    draw_text('A',text_font_p,(0,0,0),15,7,bouton1)
    draw_text('B',text_font_p,(0,0,0),15,7,bouton2)
    draw_text('C',text_font_p,(0,0,0),15,7,bouton3)
    draw_text('D',text_font_p,(0,0,0),15,7,bouton4)
    fenetre.blit(bouton1,(100,300))
    fenetre.blit(bouton2,(100,400))
    fenetre.blit(bouton3,(100,500))
    fenetre.blit(bouton4,(100,600))
    draw_text('Question 3 :',text_font_p,(0,0,0),580,20,fenetre)
    draw_text("D'où viennent les jeux Olympique ?",text_font_p,(0,0,0),100,100,fenetre)
    draw_text('Des États-Unis',text_font_p,(0,0,0),200,307,fenetre)
    draw_text('De Grèce Antique',text_font_p,(0,0,0),200,407,fenetre)
    draw_text('De Rome',text_font_p,(0,0,0),200,507,fenetre)
    draw_text("D'Angleterre",text_font_p,(0,0,0),200,607,fenetre)
    pygame.display.update()

def ques4():
    fenetre.blit(background,(0,0))
    bouton1 = pygame.Surface((50,50))
    bouton2 = pygame.Surface((50,50))
    bouton3 = pygame.Surface((50,50))
    bouton4 = pygame.Surface((50,50))
    bouton1.blit(boutoncarrepng,(0,0))
    bouton2.blit(boutoncarrepng,(0,0))
    bouton3.blit(boutoncarrepng,(0,0))
    bouton4.blit(boutoncarrepng,(0,0))
    draw_text('A',text_font_p,(0,0,0),15,7,bouton1)
    draw_text('B',text_font_p,(0,0,0),15,7,bouton2)
    draw_text('C',text_font_p,(0,0,0),15,7,bouton3)
    draw_text('D',text_font_p,(0,0,0),15,7,bouton4)
    fenetre.blit(bouton1,(100,300))
    fenetre.blit(bouton2,(100,400))
    fenetre.blit(bouton3,(100,500))
    fenetre.blit(bouton4,(100,600))
    draw_text('Question 4 :',text_font_p,(0,0,0),580,20,fenetre)
    draw_text("Lequel de ces pays n'a jamais accueilli les Jeux Olympiques ?",text_font_p,(0,0,0),100,100,fenetre)
    draw_text('France',text_font_p,(0,0,0),200,307,fenetre)
    draw_text('Japon',text_font_p,(0,0,0),200,407,fenetre)
    draw_text('Angleterre',text_font_p,(0,0,0),200,507,fenetre)
    draw_text('Pologne',text_font_p,(0,0,0),200,607,fenetre)
    pygame.display.update()

def ques5():
    fenetre.blit(background,(0,0))
    bouton1 = pygame.Surface((50,50))
    bouton2 = pygame.Surface((50,50))
    bouton3 = pygame.Surface((50,50))
    bouton4 = pygame.Surface((50,50))
    bouton1.blit(boutoncarrepng,(0,0))
    bouton2.blit(boutoncarrepng,(0,0))
    bouton3.blit(boutoncarrepng,(0,0))
    bouton4.blit(boutoncarrepng,(0,0))
    draw_text('A',text_font_p,(0,0,0),15,7,bouton1)
    draw_text('B',text_font_p,(0,0,0),15,7,bouton2)
    draw_text('C',text_font_p,(0,0,0),15,7,bouton3)
    draw_text('D',text_font_p,(0,0,0),15,7,bouton4)
    fenetre.blit(bouton1,(100,300))
    fenetre.blit(bouton2,(100,400))
    fenetre.blit(bouton3,(100,500))
    fenetre.blit(bouton4,(100,600))
    draw_text('Question 5 :',text_font_p,(0,0,0),580,20,fenetre)
    draw_text("Lequel de ces pays n'a aucune médaille Olympique ?",text_font_p,(0,0,0),100,100,fenetre)
    draw_text('Italie',text_font_p,(0,0,0),200,307,fenetre)
    draw_text('Angola',text_font_p,(0,0,0),200,407,fenetre)
    draw_text('Chine',text_font_p,(0,0,0),200,507,fenetre)
    draw_text('Allemagne',text_font_p,(0,0,0),200,607,fenetre)
    pygame.display.update()

def ques6():
    fenetre.blit(background,(0,0))
    bouton1 = pygame.Surface((50,50))
    bouton2 = pygame.Surface((50,50))
    bouton3 = pygame.Surface((50,50))
    bouton4 = pygame.Surface((50,50))
    bouton1.blit(boutoncarrepng,(0,0))
    bouton2.blit(boutoncarrepng,(0,0))
    bouton3.blit(boutoncarrepng,(0,0))
    bouton4.blit(boutoncarrepng,(0,0))
    draw_text('A',text_font_p,(0,0,0),15,7,bouton1)
    draw_text('B',text_font_p,(0,0,0),15,7,bouton2)
    draw_text('C',text_font_p,(0,0,0),15,7,bouton3)
    draw_text('D',text_font_p,(0,0,0),15,7,bouton4)
    fenetre.blit(bouton1,(100,300))
    fenetre.blit(bouton2,(100,400))
    fenetre.blit(bouton3,(100,500))
    fenetre.blit(bouton4,(100,600))
    draw_text('Question 6 :',text_font_p,(0,0,0),580,20,fenetre)
    draw_text("Combien de pays seront représentés aux JO de 2024 ?",text_font_p,(0,0,0),100,100,fenetre)
    draw_text('155',text_font_p,(0,0,0),200,307,fenetre)
    draw_text('297',text_font_p,(0,0,0),200,407,fenetre)
    draw_text('206',text_font_p,(0,0,0),200,507,fenetre)
    draw_text('103',text_font_p,(0,0,0),200,607,fenetre)
    pygame.display.update()

def ques7():
    fenetre.blit(background,(0,0))
    bouton1 = pygame.Surface((50,50))
    bouton2 = pygame.Surface((50,50))
    bouton3 = pygame.Surface((50,50))
    bouton4 = pygame.Surface((50,50))
    bouton1.blit(boutoncarrepng,(0,0))
    bouton2.blit(boutoncarrepng,(0,0))
    bouton3.blit(boutoncarrepng,(0,0))
    bouton4.blit(boutoncarrepng,(0,0))
    draw_text('A',text_font_p,(0,0,0),15,7,bouton1)
    draw_text('B',text_font_p,(0,0,0),15,7,bouton2)
    draw_text('C',text_font_p,(0,0,0),15,7,bouton3)
    draw_text('D',text_font_p,(0,0,0),15,7,bouton4)
    fenetre.blit(bouton1,(100,300))
    fenetre.blit(bouton2,(100,400))
    fenetre.blit(bouton3,(100,500))
    fenetre.blit(bouton4,(100,600))
    draw_text('Question 7 :',text_font_p,(0,0,0),580,20,fenetre)
    draw_text("Quelle ville n'a jamais accueilli les Jeux Olympiques d'hiver ?",text_font_p,(0,0,0),100,100,fenetre)
    draw_text('Reykjavik',text_font_p,(0,0,0),200,307,fenetre)
    draw_text('Oslo',text_font_p,(0,0,0),200,407,fenetre)
    draw_text('Sapporo',text_font_p,(0,0,0),200,507,fenetre)
    draw_text('Pékin',text_font_p,(0,0,0),200,607,fenetre)
    pygame.display.update()

def ques8():
    fenetre.blit(background,(0,0))
    bouton1 = pygame.Surface((50,50))
    bouton2 = pygame.Surface((50,50))
    bouton3 = pygame.Surface((50,50))
    bouton4 = pygame.Surface((50,50))
    bouton1.blit(boutoncarrepng,(0,0))
    bouton2.blit(boutoncarrepng,(0,0))
    bouton3.blit(boutoncarrepng,(0,0))
    bouton4.blit(boutoncarrepng,(0,0))
    draw_text('A',text_font_p,(0,0,0),15,7,bouton1)
    draw_text('B',text_font_p,(0,0,0),15,7,bouton2)
    draw_text('C',text_font_p,(0,0,0),15,7,bouton3)
    draw_text('D',text_font_p,(0,0,0),15,7,bouton4)
    fenetre.blit(bouton1,(100,300))
    fenetre.blit(bouton2,(100,400))
    fenetre.blit(bouton3,(100,500))
    fenetre.blit(bouton4,(100,600))
    draw_text('Question 8 :',text_font_p,(0,0,0),580,20,fenetre)
    draw_text("Quelle nation a remporté le plus grand nombre de médailles d'or lors des",text_font_p,(0,0,0),100,100,fenetre)
    draw_text("Jeux Olympiques d'Hiver de 2018 à Pyeongchang ?",text_font_p,(0,0,0),100,150,fenetre)
    draw_text('Allemagne',text_font_p,(0,0,0),200,307,fenetre)
    draw_text('États-Unis',text_font_p,(0,0,0),200,407,fenetre)
    draw_text('Norvège',text_font_p,(0,0,0),200,507,fenetre)
    draw_text('Canada',text_font_p,(0,0,0),200,607,fenetre)
    pygame.display.update()

def ques9():
    fenetre.blit(background,(0,0))
    bouton1 = pygame.Surface((50,50))
    bouton2 = pygame.Surface((50,50))
    bouton3 = pygame.Surface((50,50))
    bouton4 = pygame.Surface((50,50))
    bouton1.blit(boutoncarrepng,(0,0))
    bouton2.blit(boutoncarrepng,(0,0))
    bouton3.blit(boutoncarrepng,(0,0))
    bouton4.blit(boutoncarrepng,(0,0))
    draw_text('A',text_font_p,(0,0,0),15,7,bouton1)
    draw_text('B',text_font_p,(0,0,0),15,7,bouton2)
    draw_text('C',text_font_p,(0,0,0),15,7,bouton3)
    draw_text('D',text_font_p,(0,0,0),15,7,bouton4)
    fenetre.blit(bouton1,(100,300))
    fenetre.blit(bouton2,(100,400))
    fenetre.blit(bouton3,(100,500))
    fenetre.blit(bouton4,(100,600))
    draw_text('Question 9 :',text_font_p,(0,0,0),580,20,fenetre)
    draw_text("Dans quelle discipline sportive les athlètes effectuent-ils des sauts et des",text_font_p,(0,0,0),100,100,fenetre)
    draw_text("acrobaties en l'air avant de descendre une pente enneigée ?",text_font_p,(0,0,0),100,150,fenetre)
    draw_text('Snowboard',text_font_p,(0,0,0),200,307,fenetre)
    draw_text('Ski freestyle',text_font_p,(0,0,0),200,407,fenetre)
    draw_text('Saut à ski',text_font_p,(0,0,0),200,507,fenetre)
    draw_text('Ski alpin',text_font_p,(0,0,0),200,607,fenetre)
    pygame.display.update()

def ques10():
    fenetre.blit(background,(0,0))
    bouton1 = pygame.Surface((50,50))
    bouton2 = pygame.Surface((50,50))
    bouton3 = pygame.Surface((50,50))
    bouton4 = pygame.Surface((50,50))
    bouton1.blit(boutoncarrepng,(0,0))
    bouton2.blit(boutoncarrepng,(0,0))
    bouton3.blit(boutoncarrepng,(0,0))
    bouton4.blit(boutoncarrepng,(0,0))
    draw_text('A',text_font_p,(0,0,0),15,7,bouton1)
    draw_text('B',text_font_p,(0,0,0),15,7,bouton2)
    draw_text('C',text_font_p,(0,0,0),15,7,bouton3)
    draw_text('D',text_font_p,(0,0,0),15,7,bouton4)
    fenetre.blit(bouton1,(100,300))
    fenetre.blit(bouton2,(100,400))
    fenetre.blit(bouton3,(100,500))
    fenetre.blit(bouton4,(100,600))
    draw_text('Question 10 :',text_font_p,(0,0,0),580,20,fenetre)
    draw_text("Quelle ville a accueilli les premiers Jeux Olympiques d'Hiver en 1924 ?",text_font_p,(0,0,0),100,100,fenetre)
    draw_text('Innsbruck',text_font_p,(0,0,0),200,307,fenetre)
    draw_text('Lake Placid',text_font_p,(0,0,0),200,407,fenetre)
    draw_text('Saint-Moritz',text_font_p,(0,0,0),200,507,fenetre)
    draw_text('Chamonix-Mont-Blanc',text_font_p,(0,0,0),200,607,fenetre)
    pygame.display.update()

def ques11():
    fenetre.blit(background,(0,0))
    bouton1 = pygame.Surface((50,50))
    bouton2 = pygame.Surface((50,50))
    bouton3 = pygame.Surface((50,50))
    bouton4 = pygame.Surface((50,50))
    bouton1.blit(boutoncarrepng,(0,0))
    bouton2.blit(boutoncarrepng,(0,0))
    bouton3.blit(boutoncarrepng,(0,0))
    bouton4.blit(boutoncarrepng,(0,0))
    draw_text('A',text_font_p,(0,0,0),15,7,bouton1)
    draw_text('B',text_font_p,(0,0,0),15,7,bouton2)
    draw_text('C',text_font_p,(0,0,0),15,7,bouton3)
    draw_text('D',text_font_p,(0,0,0),15,7,bouton4)
    fenetre.blit(bouton1,(100,300))
    fenetre.blit(bouton2,(100,400))
    fenetre.blit(bouton3,(100,500))
    fenetre.blit(bouton4,(100,600))
    draw_text('Question 11 :',text_font_p,(0,0,0),580,20,fenetre)
    draw_text("Lequel de ces pays ne possède aucune médaille Olympique ?",text_font_p,(0,0,0),100,100,fenetre)
    draw_text('Ouzbékistan',text_font_p,(0,0,0),200,307,fenetre)
    draw_text('Zambie',text_font_p,(0,0,0),200,407,fenetre)
    draw_text('Burkina Faso',text_font_p,(0,0,0),200,507,fenetre)
    draw_text('République Démocratique du Congo',text_font_p,(0,0,0),200,607,fenetre)
    pygame.display.update()


def ques12():
    fenetre.blit(background,(0,0))
    bouton1 = pygame.Surface((50,50))
    bouton2 = pygame.Surface((50,50))
    bouton3 = pygame.Surface((50,50))
    bouton4 = pygame.Surface((50,50))
    bouton1.blit(boutoncarrepng,(0,0))
    bouton2.blit(boutoncarrepng,(0,0))
    bouton3.blit(boutoncarrepng,(0,0))
    bouton4.blit(boutoncarrepng,(0,0))
    draw_text('A',text_font_p,(0,0,0),15,7,bouton1)
    draw_text('B',text_font_p,(0,0,0),15,7,bouton2)
    draw_text('C',text_font_p,(0,0,0),15,7,bouton3)
    draw_text('D',text_font_p,(0,0,0),15,7,bouton4)
    fenetre.blit(bouton1,(100,300))
    fenetre.blit(bouton2,(100,400))
    fenetre.blit(bouton3,(100,500))
    fenetre.blit(bouton4,(100,600))
    draw_text('Question 12 :',text_font_p,(0,0,0),580,20,fenetre)
    draw_text("Lequel de ces logos est celui des Jeux Olympiques ?",text_font_p,(0,0,0),100,100,fenetre)
    fenetre.blit(logo3,(200,297))
    fenetre.blit(logo4,(200,397))
    fenetre.blit(logo2,(200,497))
    fenetre.blit(logo1,(200,597))
    pygame.display.update()

def bques1():
    fenetre.blit(background,(0,0))
    bouton1 = pygame.Surface((50,50))
    bouton2 = pygame.Surface((50,50))
    bouton3 = pygame.Surface((50,50))
    bouton4 = pygame.Surface((50,50))
    bouton1.blit(boutoncarrepng,(0,0))
    bouton2.blit(boutoncarrepng,(0,0))
    bouton3.blit(boutoncarrepng,(0,0))
    bouton4.blit(boutoncarrepng,(0,0))
    draw_text('A',text_font_p,(0,0,0),15,7,bouton1)
    draw_text('B',text_font_p,(0,0,0),15,7,bouton2)
    draw_text('C',text_font_p,(0,0,0),15,7,bouton3)
    draw_text('D',text_font_p,(0,0,0),15,7,bouton4)
    fenetre.blit(bouton1,(100,300))
    fenetre.blit(bouton2,(100,400))
    fenetre.blit(bouton3,(100,500))
    fenetre.blit(bouton4,(100,600))
    draw_text('Question 1 :',text_font_p,(0,0,0),580,20,fenetre)
    draw_text("Laquelle de ces courses n'existe pas aux JO ?",text_font_p,(0,0,0),100,100,fenetre)
    draw_text('100m',text_font_p,(0,0,0),200,307,fenetre)
    draw_text('200m',text_font_p,(0,0,0),200,407,fenetre)
    draw_text('500m',text_font_p,(0,0,0),200,507,fenetre)
    draw_text('800m',text_font_p,(0,0,0),200,607,fenetre)
    pygame.display.update()

def bques2():
    fenetre.blit(background,(0,0))
    bouton1 = pygame.Surface((50,50))
    bouton2 = pygame.Surface((50,50))
    bouton3 = pygame.Surface((50,50))
    bouton4 = pygame.Surface((50,50))
    bouton1.blit(boutoncarrepng,(0,0))
    bouton2.blit(boutoncarrepng,(0,0))
    bouton3.blit(boutoncarrepng,(0,0))
    bouton4.blit(boutoncarrepng,(0,0))
    draw_text('A',text_font_p,(0,0,0),15,7,bouton1)
    draw_text('B',text_font_p,(0,0,0),15,7,bouton2)
    draw_text('C',text_font_p,(0,0,0),15,7,bouton3)
    draw_text('D',text_font_p,(0,0,0),15,7,bouton4)
    fenetre.blit(bouton1,(100,300))
    fenetre.blit(bouton2,(100,400))
    fenetre.blit(bouton3,(100,500))
    fenetre.blit(bouton4,(100,600))
    draw_text('Question 2 :',text_font_p,(0,0,0),580,20,fenetre)
    draw_text("Quel ville acceuillera les Jeux Olympiques de 2024 ?",text_font_p,(0,0,0),100,100,fenetre)
    draw_text('Paris',text_font_p,(0,0,0),200,307,fenetre)
    draw_text('Madrid',text_font_p,(0,0,0),200,407,fenetre)
    draw_text('New York',text_font_p,(0,0,0),200,507,fenetre)
    draw_text('Séoul',text_font_p,(0,0,0),200,607,fenetre)
    pygame.display.update()

def bques3():
    fenetre.blit(background,(0,0))
    bouton1 = pygame.Surface((50,50))
    bouton2 = pygame.Surface((50,50))
    bouton3 = pygame.Surface((50,50))
    bouton4 = pygame.Surface((50,50))
    bouton1.blit(boutoncarrepng,(0,0))
    bouton2.blit(boutoncarrepng,(0,0))
    bouton3.blit(boutoncarrepng,(0,0))
    bouton4.blit(boutoncarrepng,(0,0))
    draw_text('A',text_font_p,(0,0,0),15,7,bouton1)
    draw_text('B',text_font_p,(0,0,0),15,7,bouton2)
    draw_text('C',text_font_p,(0,0,0),15,7,bouton3)
    draw_text('D',text_font_p,(0,0,0),15,7,bouton4)
    fenetre.blit(bouton1,(100,300))
    fenetre.blit(bouton2,(100,400))
    fenetre.blit(bouton3,(100,500))
    fenetre.blit(bouton4,(100,600))
    draw_text('Question 3 :',text_font_p,(0,0,0),580,20,fenetre)
    draw_text("Qui détient le record du 100m ?",text_font_p,(0,0,0),100,100,fenetre)
    draw_text('Usain Bolt',text_font_p,(0,0,0),200,307,fenetre)
    draw_text('Carl Lewis',text_font_p,(0,0,0),200,407,fenetre)
    draw_text('Donovan Bailey',text_font_p,(0,0,0),200,507,fenetre)
    draw_text("Asafa Powell",text_font_p,(0,0,0),200,607,fenetre)
    pygame.display.update()

def bques4():
    fenetre.blit(background,(0,0))
    bouton1 = pygame.Surface((50,50))
    bouton2 = pygame.Surface((50,50))
    bouton3 = pygame.Surface((50,50))
    bouton4 = pygame.Surface((50,50))
    bouton1.blit(boutoncarrepng,(0,0))
    bouton2.blit(boutoncarrepng,(0,0))
    bouton3.blit(boutoncarrepng,(0,0))
    bouton4.blit(boutoncarrepng,(0,0))
    draw_text('A',text_font_p,(0,0,0),15,7,bouton1)
    draw_text('B',text_font_p,(0,0,0),15,7,bouton2)
    draw_text('C',text_font_p,(0,0,0),15,7,bouton3)
    draw_text('D',text_font_p,(0,0,0),15,7,bouton4)
    fenetre.blit(bouton1,(100,300))
    fenetre.blit(bouton2,(100,400))
    fenetre.blit(bouton3,(100,500))
    fenetre.blit(bouton4,(100,600))
    draw_text('Question 4 :',text_font_p,(0,0,0),580,20,fenetre)
    draw_text("Quel est le record du monde de saut en hauteur ?",text_font_p,(0,0,0),100,100,fenetre)
    draw_text('3.5m',text_font_p,(0,0,0),200,307,fenetre)
    draw_text('2m',text_font_p,(0,0,0),200,407,fenetre)
    draw_text('2.45m',text_font_p,(0,0,0),200,507,fenetre)
    draw_text('1.73m',text_font_p,(0,0,0),200,607,fenetre)
    pygame.display.update()

def bques5():
    fenetre.blit(background,(0,0))
    bouton1 = pygame.Surface((50,50))
    bouton2 = pygame.Surface((50,50))
    bouton3 = pygame.Surface((50,50))
    bouton4 = pygame.Surface((50,50))
    bouton1.blit(boutoncarrepng,(0,0))
    bouton2.blit(boutoncarrepng,(0,0))
    bouton3.blit(boutoncarrepng,(0,0))
    bouton4.blit(boutoncarrepng,(0,0))
    draw_text('A',text_font_p,(0,0,0),15,7,bouton1)
    draw_text('B',text_font_p,(0,0,0),15,7,bouton2)
    draw_text('C',text_font_p,(0,0,0),15,7,bouton3)
    draw_text('D',text_font_p,(0,0,0),15,7,bouton4)
    fenetre.blit(bouton1,(100,300))
    fenetre.blit(bouton2,(100,400))
    fenetre.blit(bouton3,(100,500))
    fenetre.blit(bouton4,(100,600))
    draw_text('Question 5 :',text_font_p,(0,0,0),580,20,fenetre)
    draw_text("Quel est la longueur d'une piste de course ?",text_font_p,(0,0,0),100,100,fenetre)
    draw_text('1km',text_font_p,(0,0,0),200,307,fenetre)
    draw_text('400m',text_font_p,(0,0,0),200,407,fenetre)
    draw_text('2km',text_font_p,(0,0,0),200,507,fenetre)
    draw_text('800m',text_font_p,(0,0,0),200,607,fenetre)
    pygame.display.update()

def bques6():
    fenetre.blit(background,(0,0))
    bouton1 = pygame.Surface((50,50))
    bouton2 = pygame.Surface((50,50))
    bouton3 = pygame.Surface((50,50))
    bouton4 = pygame.Surface((50,50))
    bouton1.blit(boutoncarrepng,(0,0))
    bouton2.blit(boutoncarrepng,(0,0))
    bouton3.blit(boutoncarrepng,(0,0))
    bouton4.blit(boutoncarrepng,(0,0))
    draw_text('A',text_font_p,(0,0,0),15,7,bouton1)
    draw_text('B',text_font_p,(0,0,0),15,7,bouton2)
    draw_text('C',text_font_p,(0,0,0),15,7,bouton3)
    draw_text('D',text_font_p,(0,0,0),15,7,bouton4)
    fenetre.blit(bouton1,(100,300))
    fenetre.blit(bouton2,(100,400))
    fenetre.blit(bouton3,(100,500))
    fenetre.blit(bouton4,(100,600))
    draw_text('Question 6 :',text_font_p,(0,0,0),580,20,fenetre)
    draw_text("Quel sport voit les concurrents s'affronter dans une arène circulaire avant comme ",text_font_p,(0,0,0),100,100,fenetre)
    draw_text("objectif de faire chuter leur adversaire sur le dos ou les épaules ?",text_font_p,(0,0,0),100,150,fenetre)
    draw_text('Judo',text_font_p,(0,0,0),200,307,fenetre)
    draw_text('Taekwondo',text_font_p,(0,0,0),200,407,fenetre)
    draw_text('Lutte',text_font_p,(0,0,0),200,507,fenetre)
    draw_text('Boxe',text_font_p,(0,0,0),200,607,fenetre)
    pygame.display.update()

def bques7():
    fenetre.blit(background,(0,0))
    bouton1 = pygame.Surface((50,50))
    bouton2 = pygame.Surface((50,50))
    bouton3 = pygame.Surface((50,50))
    bouton4 = pygame.Surface((50,50))
    bouton1.blit(boutoncarrepng,(0,0))
    bouton2.blit(boutoncarrepng,(0,0))
    bouton3.blit(boutoncarrepng,(0,0))
    bouton4.blit(boutoncarrepng,(0,0))
    draw_text('A',text_font_p,(0,0,0),15,7,bouton1)
    draw_text('B',text_font_p,(0,0,0),15,7,bouton2)
    draw_text('C',text_font_p,(0,0,0),15,7,bouton3)
    draw_text('D',text_font_p,(0,0,0),15,7,bouton4)
    fenetre.blit(bouton1,(100,300))
    fenetre.blit(bouton2,(100,400))
    fenetre.blit(bouton3,(100,500))
    fenetre.blit(bouton4,(100,600))
    draw_text('Question 7 :',text_font_p,(0,0,0),580,20,fenetre)
    draw_text("Quel sport exige que les athlètes courrent, sautent, et lancent dans une série ",text_font_p,(0,0,0),100,100,fenetre)
    draw_text("d'épreuves combinées ?",text_font_p,(0,0,0),100,150,fenetre)
    draw_text('Athlétisme',text_font_p,(0,0,0),200,307,fenetre)
    draw_text('Cyclisme sur piste',text_font_p,(0,0,0),200,407,fenetre)
    draw_text('Badminton',text_font_p,(0,0,0),200,507,fenetre)
    draw_text('Pentathlon moderne',text_font_p,(0,0,0),200,607,fenetre)
    pygame.display.update()

def bques8():
    fenetre.blit(background,(0,0))
    bouton1 = pygame.Surface((50,50))
    bouton2 = pygame.Surface((50,50))
    bouton3 = pygame.Surface((50,50))
    bouton4 = pygame.Surface((50,50))
    bouton1.blit(boutoncarrepng,(0,0))
    bouton2.blit(boutoncarrepng,(0,0))
    bouton3.blit(boutoncarrepng,(0,0))
    bouton4.blit(boutoncarrepng,(0,0))
    draw_text('A',text_font_p,(0,0,0),15,7,bouton1)
    draw_text('B',text_font_p,(0,0,0),15,7,bouton2)
    draw_text('C',text_font_p,(0,0,0),15,7,bouton3)
    draw_text('D',text_font_p,(0,0,0),15,7,bouton4)
    fenetre.blit(bouton1,(100,300))
    fenetre.blit(bouton2,(100,400))
    fenetre.blit(bouton3,(100,500))
    fenetre.blit(bouton4,(100,600))
    draw_text('Question 8 :',text_font_p,(0,0,0),580,20,fenetre)
    draw_text("Laquelle de ces disciplines n'est pas pratiquée aux Jeux Olympiques ?",text_font_p,(0,0,0),100,100,fenetre)
    draw_text('Saut à la perche',text_font_p,(0,0,0),200,307,fenetre)
    draw_text('Saut à la corde',text_font_p,(0,0,0),200,407,fenetre)
    draw_text('Saut en hauteur',text_font_p,(0,0,0),200,507,fenetre)
    draw_text('saut en longueur',text_font_p,(0,0,0),200,607,fenetre)
    pygame.display.update()

def bques9():
    fenetre.blit(background,(0,0))
    bouton1 = pygame.Surface((50,50))
    bouton2 = pygame.Surface((50,50))
    bouton3 = pygame.Surface((50,50))
    bouton4 = pygame.Surface((50,50))
    bouton1.blit(boutoncarrepng,(0,0))
    bouton2.blit(boutoncarrepng,(0,0))
    bouton3.blit(boutoncarrepng,(0,0))
    bouton4.blit(boutoncarrepng,(0,0))
    draw_text('A',text_font_p,(0,0,0),15,7,bouton1)
    draw_text('B',text_font_p,(0,0,0),15,7,bouton2)
    draw_text('C',text_font_p,(0,0,0),15,7,bouton3)
    draw_text('D',text_font_p,(0,0,0),15,7,bouton4)
    fenetre.blit(bouton1,(100,300))
    fenetre.blit(bouton2,(100,400))
    fenetre.blit(bouton3,(100,500))
    fenetre.blit(bouton4,(100,600))
    draw_text('Question 9 :',text_font_p,(0,0,0),580,20,fenetre)
    draw_text("Qu'est-ce que le pentathlon moderne ?",text_font_p,(0,0,0),100,100,fenetre)
    draw_text('De la course en pentalon',text_font_p,(0,0,0),200,307,fenetre)
    draw_text('Un sprint sur 500m',text_font_p,(0,0,0),200,407,fenetre)
    draw_text("Une épreuve constituée d'escrime, de natation, d'équitation,",text_font_p,(0,0,0),200,482,fenetre)
    draw_text(" de tir à l'arc, et de relai",text_font_p,(0,0,0),200,532,fenetre)
    draw_text("Une épreuve constituée d'escrime, de natation, d'équitation,",text_font_p,(0,0,0),200,582,fenetre)
    draw_text(" de tir, et de course à pied",text_font_p,(0,0,0),200,632,fenetre)
    pygame.display.update()

def bques10():
    fenetre.blit(background,(0,0))
    bouton1 = pygame.Surface((50,50))
    bouton2 = pygame.Surface((50,50))
    bouton3 = pygame.Surface((50,50))
    bouton4 = pygame.Surface((50,50))
    bouton1.blit(boutoncarrepng,(0,0))
    bouton2.blit(boutoncarrepng,(0,0))
    bouton3.blit(boutoncarrepng,(0,0))
    bouton4.blit(boutoncarrepng,(0,0))
    draw_text('A',text_font_p,(0,0,0),15,7,bouton1)
    draw_text('B',text_font_p,(0,0,0),15,7,bouton2)
    draw_text('C',text_font_p,(0,0,0),15,7,bouton3)
    draw_text('D',text_font_p,(0,0,0),15,7,bouton4)
    fenetre.blit(bouton1,(100,300))
    fenetre.blit(bouton2,(100,400))
    fenetre.blit(bouton3,(100,500))
    fenetre.blit(bouton4,(100,600))
    draw_text('Question 10 :',text_font_p,(0,0,0),580,20,fenetre)
    draw_text("Quelle est la devise des Jeux Olympiques ?",text_font_p,(0,0,0),100,100,fenetre)
    draw_text('Liberté, Égalité, Fraternité',text_font_p,(0,0,0),200,307,fenetre)
    draw_text('Plus vite, plus haut, plus fort - ensemble',text_font_p,(0,0,0),200,407,fenetre)
    draw_text('Luttons ensemble contre les inégalites',text_font_p,(0,0,0),200,507,fenetre)
    draw_text('Égalité, Respect, Motivation',text_font_p,(0,0,0),200,607,fenetre)
    pygame.display.update()

def bques11():
    fenetre.blit(background,(0,0))
    bouton1 = pygame.Surface((50,50))
    bouton2 = pygame.Surface((50,50))
    bouton3 = pygame.Surface((50,50))
    bouton4 = pygame.Surface((50,50))
    bouton1.blit(boutoncarrepng,(0,0))
    bouton2.blit(boutoncarrepng,(0,0))
    bouton3.blit(boutoncarrepng,(0,0))
    bouton4.blit(boutoncarrepng,(0,0))
    draw_text('A',text_font_p,(0,0,0),15,7,bouton1)
    draw_text('B',text_font_p,(0,0,0),15,7,bouton2)
    draw_text('C',text_font_p,(0,0,0),15,7,bouton3)
    draw_text('D',text_font_p,(0,0,0),15,7,bouton4)
    fenetre.blit(bouton1,(100,300))
    fenetre.blit(bouton2,(100,400))
    fenetre.blit(bouton3,(100,500))
    fenetre.blit(bouton4,(100,600))
    draw_text('Question 11 :',text_font_p,(0,0,0),580,20,fenetre)
    draw_text("Quel athlète a remporté le plus grand nombre de médailles d'or individuelles",text_font_p,(0,0,0),100,100,fenetre)
    draw_text(" aux Jeux olympiques d'été ?",text_font_p,(0,0,0),100,150,fenetre)
    draw_text('Michael Phelps',text_font_p,(0,0,0),200,307,fenetre)
    draw_text('Carl Lewis',text_font_p,(0,0,0),200,407,fenetre)
    draw_text('Usain Bolt',text_font_p,(0,0,0),200,507,fenetre)
    draw_text('Larisa Latynina',text_font_p,(0,0,0),200,607,fenetre)
    pygame.display.update()

def bques12():
    fenetre.blit(background,(0,0))
    bouton1 = pygame.Surface((50,50))
    bouton2 = pygame.Surface((50,50))
    bouton3 = pygame.Surface((50,50))
    bouton4 = pygame.Surface((50,50))
    bouton1.blit(boutoncarrepng,(0,0))
    bouton2.blit(boutoncarrepng,(0,0))
    bouton3.blit(boutoncarrepng,(0,0))
    bouton4.blit(boutoncarrepng,(0,0))
    draw_text('A',text_font_p,(0,0,0),15,7,bouton1)
    draw_text('B',text_font_p,(0,0,0),15,7,bouton2)
    draw_text('C',text_font_p,(0,0,0),15,7,bouton3)
    draw_text('D',text_font_p,(0,0,0),15,7,bouton4)
    fenetre.blit(bouton1,(100,300))
    fenetre.blit(bouton2,(100,400))
    fenetre.blit(bouton3,(100,500))
    fenetre.blit(bouton4,(100,600))
    draw_text('Question 12 :',text_font_p,(0,0,0),580,20,fenetre)
    draw_text("Dans quelle discipline sportive les États-Unis n'ont-ils jamais remporté de médaille d'or aux Jeux olympiques d'été ?",text_font_p,(0,0,0),100,100,fenetre)
    draw_text("Tir à l'arc",text_font_p,(0,0,0),200,307,fenetre)
    draw_text('Badminton',text_font_p,(0,0,0),200,407,fenetre)
    draw_text('Escrime',text_font_p,(0,0,0),200,507,fenetre)
    draw_text('Rugby à VII',text_font_p,(0,0,0),200,607,fenetre)
    pygame.display.update()

running = True

while running:
    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                menu = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    pos = pygame.mouse.get_pos()
                    if pos[0] >= 540 and  pos[0] <= 740 and pos[1] >= 300 and pos[1] <= 350:
                        posX = 600
                        posY = 30
                        aide()
                        menu = False
                        scnaide = True
                    if pos[0] >= 540 and  pos[0] <= 740 and pos[1] >= 400 and pos[1] <= 450:
                        posX = 600
                        posY = 30
                        aide2()
                        menu = False
                        scnaide2 = True
                    if pos[0] >= 540 and  pos[0] <= 740 and pos[1] >= 500 and pos[1] <= 550:
                        pygame.quit()
                        menu = False
        pygame.display.update()

    while scnaide:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                scnaide = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    pos = pygame.mouse.get_pos()
                    if pos[0] >= 540 and  pos[0] <= 740 and pos[1] >= 500 and pos[1] <= 550:
                        posX = 600
                        posY = 30
                        score = 0
                        pistedeski()
                        scnaide = False
                        scnpiste = True
        pygame.display.update()

    while scnaide2:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                scnaide = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    pos = pygame.mouse.get_pos()
                    if pos[0] >= 540 and  pos[0] <= 740 and pos[1] >= 500 and pos[1] <= 550:
                        posX = 200
                        posY = 350
                        haieX = 0
                        score = 0
                        coursehaie()
                        scnaide2 = False
                        scnhaie = True
        pygame.display.update()

    while scnpiste:
        for event in pygame.event.get():
            if event.type == QUIT:
                ruuning = False
                pygame.quit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    pos = pygame.mouse.get_pos()
                    if pos[0] >= 10 and  pos[0] <= 60 and pos[1] >= 10 and pos[1] <= 60:
                        menu = True
                        scnpiste = False
                        repq1 = True
                        repq2 = True
                        repq3 = True
                        repq4 = True
                        repq5 = True
                        repq6 = True
                        repq7 = True
                        repq8 = True
                        repq9 = True
                        repq10 = True
                        repq11 = True
                        repq12 = True
                        score = 0
                        start()
                        pygame.display.update()
            if event.type == KEYDOWN:
                if event.key == pygame.K_q:
                    posX = posX-20
                    perso = pygame.image.load("dingoofygauche.png").convert_alpha()
                if event.key == pygame.K_d:
                    posX = posX+20
                    perso = pygame.image.load("dingoofydroit.png").convert_alpha()
        if posX>720 and posX<750 and posY>75 and posY<116 and repq1:
            repq1 = False
            q1 = True
            scnpiste = False
            ques1()
            pygame.display.update()
        if posX>490 and posX<530 and posY>100 and posY<140 and repq2:
            repq2 = False
            q2 = True
            scnpiste = False
            ques2()
            pygame.display.update()
        if posX>750 and posX<780 and posY>140 and posY<180 and repq3:
            repq3 = False
            q3 = True
            scnpiste = False
            ques3()
            pygame.display.update()
        if posX>450 and posX<480 and posY>170 and posY<210 and repq4:
            repq4 = False
            q4 = True
            scnpiste = False
            ques4()
            pygame.display.update()
        if posX>760 and posX<800 and posY>210 and posY<250 and repq5:
            repq5 = False
            q5 = True
            scnpiste = False
            ques5()
            pygame.display.update()
        if posX>420 and posX<460 and posY>230 and posY<270 and repq6:
            repq6 = False
            q6 = True
            scnpiste = False
            ques6()
            pygame.display.update()
        if posX>800 and posX<840 and posY>270 and posY<310 and repq7:
            repq7 = False
            q7 = True
            scnpiste = False
            ques7()
            pygame.display.update()
        if posX>410 and posX<450 and posY>300 and posY<340 and repq8:
            repq8 = False
            q8 = True
            scnpiste = False
            ques8()
            pygame.display.update()
        if posX>820 and posX<870 and posY>330 and posY<380 and repq9:
            repq9 = False
            q9 = True
            scnpiste = False
            ques9()
            pygame.display.update()
        if posX>340 and posX<390 and posY>370 and posY<420 and repq10:
            repq10 = False
            q10 = True
            scnpiste = False
            ques10()
            pygame.display.update()
        if posX>840 and posX<900 and posY>420 and posY<480 and repq11:
            repq11 = False
            q11 = True
            scnpiste = False
            ques11()
            pygame.display.update()
        if posX>320 and posX<370 and posY>450 and posY<510 and repq12:
            pygame.display.set_icon(logotroll)
            repq12 = False
            q12 = True
            scnpiste = False
            ques12()
            pygame.display.update()
        posY += .015
        if posY>580:
            posY=580
            if score < 7:
                draw_text('Perdu !',text_font_g,(255,0,0),520,300,fenetre)
                repq1 = True
                repq2 = True
                repq3 = True
                repq4 = True
                repq5 = True
                repq6 = True
                repq7 = True
                repq8 = True
                repq9 = True
                repq10 = True
                repq11 = True
                repq12 = True
                score = 0
                pygame.display.update()
                pygame.time.wait(2000)
                posX = 600
                posY = 30
            elif score < 12:
                draw_text('Gagné !',text_font_g,(0,255,0),500,300,fenetre)
                pygame.display.update()
                pygame.time.wait(2000)
                scnpiste = False
                menu = True
                if trophee1 != 2 :
                    trophee1 = 1
                start()
            elif score == 12:
                draw_text('Score Parfait !',text_font_g,(255,191,0),370,300,fenetre)
                pygame.display.update()
                pygame.time.wait(2000)
                scnpiste = False
                menu = True
                trophee1 = 2
                start()
        if posX<270 or posX>1040:
            posX = 600
            posY = 30
            draw_text('Sortie de piste',text_font_g,(0,0,0),360,120,fenetre)
            fenetre.blit(lolol,(540,260))
            repq1 = True
            repq2 = True
            repq3 = True
            repq4 = True
            repq5 = True
            repq6 = True
            repq7 = True
            repq8 = True
            repq9 = True
            repq10 = True
            repq11 = True
            repq12 = True
            score = 0
            pygame.display.update()
            pygame.time.wait(1000)
        elif scnpiste:
            pistedeski()
            pygame.display.update()

    while q1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                q1 = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    pos = pygame.mouse.get_pos()

                    if pos[0] >= 100 and  pos[0] <= 150 and pos[1] >= 300 and pos[1] <= 350:
                        score += 1
                        right.play()
                        fenetre.blit(bonneRep,(600,300))
                        pygame.display.update()
                        pygame.time.wait(1000)
                        scnpiste = True
                        q1 = False
                        pistedeski()

                    if pos[0] >= 100 and  pos[0] <= 150 and pos[1] >= 400 and pos[1] <= 450:
                        wrong.play()
                        fenetre.blit(mauvaiseRep,(600,300))
                        pygame.display.update()
                        pygame.time.wait(1000)
                        scnpiste = True
                        q1 = False
                        pistedeski()

                    if pos[0] >= 100 and  pos[0] <= 150 and pos[1] >= 500 and pos[1] <= 550:
                        wrong.play()
                        fenetre.blit(mauvaiseRep,(600,300))
                        pygame.display.update()
                        pygame.time.wait(1000)
                        scnpiste = True
                        q1 = False
                        pistedeski()

                    if pos[0] >= 100 and  pos[0] <= 150 and pos[1] >= 600 and pos[1] <= 650:
                        wrong.play()
                        fenetre.blit(mauvaiseRep,(600,300))
                        pygame.display.update()
                        pygame.time.wait(1000)
                        scnpiste = True
                        q1 = False
                        pistedeski()

    while q2:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                q2 = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    pos = pygame.mouse.get_pos()

                    if pos[0] >= 100 and  pos[0] <= 150 and pos[1] >= 300 and pos[1] <= 350:
                        wrong.play()
                        fenetre.blit(mauvaiseRep,(600,300))
                        pygame.display.update()
                        pygame.time.wait(1000)
                        scnpiste = True
                        q2 = False
                        pistedeski()

                    if pos[0] >= 100 and  pos[0] <= 150 and pos[1] >= 400 and pos[1] <= 450:
                        wrong.play()
                        fenetre.blit(mauvaiseRep,(600,300))
                        pygame.display.update()
                        pygame.time.wait(1000)
                        scnpiste = True
                        q2 = False
                        pistedeski()

                    if pos[0] >= 100 and  pos[0] <= 150 and pos[1] >= 500 and pos[1] <= 550:
                        score += 1
                        right.play()
                        fenetre.blit(bonneRep,(600,300))
                        pygame.display.update()
                        pygame.time.wait(1000)
                        scnpiste = True
                        q2 = False
                        pistedeski()

                    if pos[0] >= 100 and  pos[0] <= 150 and pos[1] >= 600 and pos[1] <= 650:
                        wrong.play()
                        fenetre.blit(mauvaiseRep,(600,300))
                        pygame.display.update()
                        pygame.time.wait(1000)
                        scnpiste = True
                        q2 = False
                        pistedeski()

    while q3:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                q3 = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    pos = pygame.mouse.get_pos()

                    if pos[0] >= 100 and  pos[0] <= 150 and pos[1] >= 300 and pos[1] <= 350:
                        wrong.play()
                        fenetre.blit(mauvaiseRep,(600,300))
                        pygame.display.update()
                        pygame.time.wait(1000)
                        scnpiste = True
                        q3 = False
                        pistedeski()

                    if pos[0] >= 100 and  pos[0] <= 150 and pos[1] >= 400 and pos[1] <= 450:
                        score += 1
                        right.play()
                        fenetre.blit(bonneRep,(600,300))
                        pygame.display.update()
                        pygame.time.wait(1000)
                        scnpiste = True
                        q3 = False
                        pistedeski()

                    if pos[0] >= 100 and  pos[0] <= 150 and pos[1] >= 500 and pos[1] <= 550:
                        wrong.play()
                        fenetre.blit(mauvaiseRep,(600,300))
                        pygame.display.update()
                        pygame.time.wait(1000)
                        scnpiste = True
                        q3 = False
                        pistedeski()

                    if pos[0] >= 100 and  pos[0] <= 150 and pos[1] >= 600 and pos[1] <= 650:
                        wrong.play()
                        fenetre.blit(mauvaiseRep,(600,300))
                        pygame.display.update()
                        pygame.time.wait(1000)
                        scnpiste = True
                        q3 = False
                        pistedeski()

    while q4:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                q4 = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    pos = pygame.mouse.get_pos()

                    if pos[0] >= 100 and  pos[0] <= 150 and pos[1] >= 300 and pos[1] <= 350:
                        wrong.play()
                        fenetre.blit(mauvaiseRep,(600,300))
                        pygame.display.update()
                        pygame.time.wait(1000)
                        scnpiste = True
                        q4 = False
                        pistedeski()

                    if pos[0] >= 100 and  pos[0] <= 150 and pos[1] >= 400 and pos[1] <= 450:
                        wrong.play()
                        fenetre.blit(mauvaiseRep,(600,300))
                        pygame.display.update()
                        pygame.time.wait(1000)
                        scnpiste = True
                        q4 = False
                        pistedeski()


                    if pos[0] >= 100 and  pos[0] <= 150 and pos[1] >= 500 and pos[1] <= 550:
                        wrong.play()
                        fenetre.blit(mauvaiseRep,(600,300))
                        pygame.display.update()
                        pygame.time.wait(1000)
                        scnpiste = True
                        q4 = False
                        pistedeski()

                    if pos[0] >= 100 and  pos[0] <= 150 and pos[1] >= 600 and pos[1] <= 650:
                        score += 1
                        right.play()
                        fenetre.blit(bonneRep,(600,300))
                        pygame.display.update()
                        pygame.time.wait(1000)
                        scnpiste = True
                        q4 = False
                        pistedeski()

    while q5:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                q5 = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    pos = pygame.mouse.get_pos()

                    if pos[0] >= 100 and  pos[0] <= 150 and pos[1] >= 300 and pos[1] <= 350:
                        wrong.play()
                        fenetre.blit(mauvaiseRep,(600,300))
                        pygame.display.update()
                        pygame.time.wait(1000)
                        scnpiste = True
                        q5 = False
                        pistedeski()

                    if pos[0] >= 100 and  pos[0] <= 150 and pos[1] >= 400 and pos[1] <= 450:
                        score += 1
                        right.play()
                        fenetre.blit(bonneRep,(600,300))
                        pygame.display.update()
                        pygame.time.wait(1000)
                        scnpiste = True
                        q5 = False
                        pistedeski()


                    if pos[0] >= 100 and  pos[0] <= 150 and pos[1] >= 500 and pos[1] <= 550:
                        wrong.play()
                        fenetre.blit(mauvaiseRep,(600,300))
                        pygame.display.update()
                        pygame.time.wait(1000)
                        scnpiste = True
                        q5 = False
                        pistedeski()

                    if pos[0] >= 100 and  pos[0] <= 150 and pos[1] >= 600 and pos[1] <= 650:
                        wrong.play()
                        fenetre.blit(mauvaiseRep,(600,300))
                        pygame.display.update()
                        pygame.time.wait(1000)
                        scnpiste = True
                        q5 = False
                        pistedeski()

    while q6:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                q6 = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    pos = pygame.mouse.get_pos()

                    if pos[0] >= 100 and  pos[0] <= 150 and pos[1] >= 300 and pos[1] <= 350:
                        wrong.play()
                        fenetre.blit(mauvaiseRep,(600,300))
                        pygame.display.update()
                        pygame.time.wait(1000)
                        scnpiste = True
                        q6 = False
                        pistedeski()

                    if pos[0] >= 100 and  pos[0] <= 150 and pos[1] >= 400 and pos[1] <= 450:
                        wrong.play()
                        fenetre.blit(mauvaiseRep,(600,300))
                        pygame.display.update()
                        pygame.time.wait(1000)
                        scnpiste = True
                        q6 = False
                        pistedeski()

                    if pos[0] >= 100 and  pos[0] <= 150 and pos[1] >= 500 and pos[1] <= 550:
                        score += 1
                        right.play()
                        fenetre.blit(bonneRep,(600,300))
                        pygame.display.update()
                        pygame.time.wait(1000)
                        scnpiste = True
                        q6 = False
                        pistedeski()

                    if pos[0] >= 100 and  pos[0] <= 150 and pos[1] >= 600 and pos[1] <= 650:
                        wrong.play()
                        fenetre.blit(mauvaiseRep,(600,300))
                        pygame.display.update()
                        pygame.time.wait(1000)
                        scnpiste = True
                        q6 = False
                        pistedeski()

    while q7:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                q7 = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    pos = pygame.mouse.get_pos()

                    if pos[0] >= 100 and  pos[0] <= 150 and pos[1] >= 300 and pos[1] <= 350:
                        score += 1
                        right.play()
                        fenetre.blit(bonneRep,(600,300))
                        pygame.display.update()
                        pygame.time.wait(1000)
                        scnpiste = True
                        q7 = False
                        pistedeski()

                    if pos[0] >= 100 and  pos[0] <= 150 and pos[1] >= 400 and pos[1] <= 450:
                        wrong.play()
                        fenetre.blit(mauvaiseRep,(600,300))
                        pygame.display.update()
                        pygame.time.wait(1000)
                        scnpiste = True
                        q7 = False
                        pistedeski()

                    if pos[0] >= 100 and  pos[0] <= 150 and pos[1] >= 500 and pos[1] <= 550:
                        wrong.play()
                        fenetre.blit(mauvaiseRep,(600,300))
                        pygame.display.update()
                        pygame.time.wait(1000)
                        scnpiste = True
                        q7 = False
                        pistedeski()

                    if pos[0] >= 100 and  pos[0] <= 150 and pos[1] >= 600 and pos[1] <= 650:
                        wrong.play()
                        fenetre.blit(mauvaiseRep,(600,300))
                        pygame.display.update()
                        pygame.time.wait(1000)
                        scnpiste = True
                        q7 = False
                        pistedeski()

    while q8:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                q8 = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    pos = pygame.mouse.get_pos()

                    if pos[0] >= 100 and  pos[0] <= 150 and pos[1] >= 300 and pos[1] <= 350:
                        wrong.play()
                        fenetre.blit(mauvaiseRep,(600,300))
                        pygame.display.update()
                        pygame.time.wait(1000)
                        scnpiste = True
                        q8 = False
                        pistedeski()

                    if pos[0] >= 100 and  pos[0] <= 150 and pos[1] >= 400 and pos[1] <= 450:
                        wrong.play()
                        fenetre.blit(mauvaiseRep,(600,300))
                        pygame.display.update()
                        pygame.time.wait(1000)
                        scnpiste = True
                        q8 = False
                        pistedeski()

                    if pos[0] >= 100 and  pos[0] <= 150 and pos[1] >= 500 and pos[1] <= 550:
                        score += 1
                        right.play()
                        fenetre.blit(bonneRep,(600,300))
                        pygame.display.update()
                        pygame.time.wait(1000)
                        scnpiste = True
                        q8 = False
                        pistedeski()

                    if pos[0] >= 100 and  pos[0] <= 150 and pos[1] >= 600 and pos[1] <= 650:
                        wrong.play()
                        fenetre.blit(mauvaiseRep,(600,300))
                        pygame.display.update()
                        pygame.time.wait(1000)
                        scnpiste = True
                        q8 = False
                        pistedeski()

    while q9:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                q9 = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    pos = pygame.mouse.get_pos()

                    if pos[0] >= 100 and  pos[0] <= 150 and pos[1] >= 300 and pos[1] <= 350:
                        wrong.play()
                        fenetre.blit(mauvaiseRep,(600,300))
                        pygame.display.update()
                        pygame.time.wait(1000)
                        scnpiste = True
                        q9 = False
                        pistedeski()

                    if pos[0] >= 100 and  pos[0] <= 150 and pos[1] >= 400 and pos[1] <= 450:
                        score += 1
                        right.play()
                        fenetre.blit(bonneRep,(600,300))
                        pygame.display.update()
                        pygame.time.wait(1000)
                        scnpiste = True
                        q9 = False
                        pistedeski()

                    if pos[0] >= 100 and  pos[0] <= 150 and pos[1] >= 500 and pos[1] <= 550:
                        wrong.play()
                        fenetre.blit(mauvaiseRep,(600,300))
                        pygame.display.update()
                        pygame.time.wait(1000)
                        scnpiste = True
                        q9 = False
                        pistedeski()

                    if pos[0] >= 100 and  pos[0] <= 150 and pos[1] >= 600 and pos[1] <= 650:
                        wrong.play()
                        fenetre.blit(mauvaiseRep,(600,300))
                        pygame.display.update()
                        pygame.time.wait(1000)
                        scnpiste = True
                        q9 = False
                        pistedeski()

    while q10:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                q10 = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    pos = pygame.mouse.get_pos()

                    if pos[0] >= 100 and  pos[0] <= 150 and pos[1] >= 300 and pos[1] <= 350:
                        wrong.play()
                        fenetre.blit(mauvaiseRep,(600,300))
                        pygame.display.update()
                        pygame.time.wait(1000)
                        scnpiste = True
                        q10 = False
                        pistedeski()

                    if pos[0] >= 100 and  pos[0] <= 150 and pos[1] >= 400 and pos[1] <= 450:
                        wrong.play()
                        fenetre.blit(mauvaiseRep,(600,300))
                        pygame.display.update()
                        pygame.time.wait(1000)
                        scnpiste = True
                        q10 = False
                        pistedeski()

                    if pos[0] >= 100 and  pos[0] <= 150 and pos[1] >= 500 and pos[1] <= 550:
                        wrong.play()
                        fenetre.blit(mauvaiseRep,(600,300))
                        pygame.display.update()
                        pygame.time.wait(1000)
                        scnpiste = True
                        q10 = False
                        pistedeski()

                    if pos[0] >= 100 and  pos[0] <= 150 and pos[1] >= 600 and pos[1] <= 650:
                        score += 1
                        right.play()
                        fenetre.blit(bonneRep,(600,300))
                        pygame.display.update()
                        pygame.time.wait(1000)
                        scnpiste = True
                        q10 = False
                        pistedeski()

    while q11:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                q11 = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    pos = pygame.mouse.get_pos()

                    if pos[0] >= 100 and  pos[0] <= 150 and pos[1] >= 300 and pos[1] <= 350:
                        wrong.play()
                        fenetre.blit(mauvaiseRep,(600,300))
                        pygame.display.update()
                        pygame.time.wait(1000)
                        scnpiste = True
                        q11 = False
                        pistedeski()


                    if pos[0] >= 100 and  pos[0] <= 150 and pos[1] >= 400 and pos[1] <= 450:
                        wrong.play()
                        fenetre.blit(mauvaiseRep,(600,300))
                        pygame.display.update()
                        pygame.time.wait(1000)
                        scnpiste = True
                        q11 = False
                        pistedeski()

                    if pos[0] >= 100 and  pos[0] <= 150 and pos[1] >= 500 and pos[1] <= 550:
                        wrong.play()
                        fenetre.blit(mauvaiseRep,(600,300))
                        pygame.display.update()
                        pygame.time.wait(1000)
                        scnpiste = True
                        q11 = False
                        pistedeski()

                    if pos[0] >= 100 and  pos[0] <= 150 and pos[1] >= 600 and pos[1] <= 650:
                        score += 1
                        right.play()
                        fenetre.blit(bonneRep,(600,300))
                        pygame.display.update()
                        pygame.time.wait(1000)
                        scnpiste = True
                        q11 = False
                        pistedeski()

    while q12:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                q12 = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    pos = pygame.mouse.get_pos()

                    if pos[0] >= 100 and  pos[0] <= 150 and pos[1] >= 300 and pos[1] <= 350:
                        wrong.play()
                        fenetre.blit(mauvaiseRep,(600,300))
                        pygame.display.update()
                        pygame.time.wait(1000)
                        scnpiste = True
                        q12 = False
                        pistedeski()
                        pygame.display.set_icon(logo)

                    if pos[0] >= 100 and  pos[0] <= 150 and pos[1] >= 400 and pos[1] <= 450:
                        score += 1
                        right.play()
                        fenetre.blit(bonneRep,(600,300))
                        pygame.display.update()
                        pygame.time.wait(1000)
                        scnpiste = True
                        q12 = False
                        pistedeski()
                        pygame.display.set_icon(logo)


                    if pos[0] >= 100 and  pos[0] <= 150 and pos[1] >= 500 and pos[1] <= 550:
                        wrong.play()
                        fenetre.blit(mauvaiseRep,(600,300))
                        pygame.display.update()
                        pygame.time.wait(1000)
                        scnpiste = True
                        q12 = False
                        pistedeski()
                        pygame.display.set_icon(logo)

                    if pos[0] >= 100 and  pos[0] <= 150 and pos[1] >= 600 and pos[1] <= 650:
                        wrong.play()
                        fenetre.blit(mauvaiseRep,(600,300))
                        pygame.display.update()
                        pygame.time.wait(1000)
                        scnpiste = True
                        q12 = False
                        pistedeski()
                        pygame.display.set_icon(logo)

    while scnhaie:
        for event in pygame.event.get():
            if event.type == QUIT:
                ruuning = False
                pygame.quit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    pos = pygame.mouse.get_pos()
                    if pos[0] >= 10 and  pos[0] <= 60 and pos[1] >= 10 and pos[1] <= 60:
                        menu = True
                        scnhaie = False
                        brepq1 = True
                        brepq2 = True
                        brepq3 = True
                        brepq4 = True
                        brepq5 = True
                        brepq6 = True
                        brepq7 = True
                        brepq8 = True
                        brepq9 = True
                        brepq10 = True
                        brepq11 = True
                        brepq12 = True
                        score = 0
                        start()
                        pygame.display.update()
            if event.type == KEYDOWN:
                if event.key == pygame.K_SPACE and jumping == False:
                    jumping = True
                    up = True
                    jumptime = 0
        if haieX > 650 and brepq1:
            if posY < 250 :
                brepq1 = False
                bq1 = True
                scnhaie = False
                bques1()
                pygame.display.update()
            else :
                draw_text('Perdu !',text_font_g,(255,0,0),520,300,fenetre)
                brepq1 = True
                brepq2 = True
                brepq3 = True
                brepq4 = True
                brepq5 = True
                brepq6 = True
                brepq7 = True
                brepq8 = True
                brepq9 = True
                brepq10 = True
                brepq11 = True
                brepq12 = True
                score = 0
                pygame.display.update()
                pygame.time.wait(2000)
                haieX = 0
                vitesse = .2
        if haieX > 1450 and brepq2:
            if posY < 250 :
                brepq2 = False
                bq2 = True
                scnhaie = False
                bques2()
                pygame.display.update()
            else :
                draw_text('Perdu !',text_font_g,(255,0,0),520,300,fenetre)
                brepq1 = True
                brepq2 = True
                brepq3 = True
                brepq4 = True
                brepq5 = True
                brepq6 = True
                brepq7 = True
                brepq8 = True
                brepq9 = True
                brepq10 = True
                brepq11 = True
                brepq12 = True
                score = 0
                pygame.display.update()
                pygame.time.wait(2000)
                haieX = 0
                vitesse = .2
        if haieX > 2250 and brepq3:
            if posY < 250 :
                brepq3 = False
                bq3 = True
                scnhaie = False
                bques3()
                pygame.display.update()
            else :
                draw_text('Perdu !',text_font_g,(255,0,0),520,300,fenetre)
                brepq1 = True
                brepq2 = True
                brepq3 = True
                brepq4 = True
                brepq5 = True
                brepq6 = True
                brepq7 = True
                brepq8 = True
                brepq9 = True
                brepq10 = True
                brepq11 = True
                brepq12 = True
                score = 0
                pygame.display.update()
                pygame.time.wait(2000)
                haieX = 0
                vitesse = .2
        if haieX > 3050 and brepq4:
            if posY < 250 :
                brepq4 = False
                bq4 = True
                scnhaie = False
                bques4()
                pygame.display.update()
            else :
                draw_text('Perdu !',text_font_g,(255,0,0),520,300,fenetre)
                brepq1 = True
                brepq2 = True
                brepq3 = True
                brepq4 = True
                brepq5 = True
                brepq6 = True
                brepq7 = True
                brepq8 = True
                brepq9 = True
                brepq10 = True
                brepq11 = True
                brepq12 = True
                score = 0
                pygame.display.update()
                pygame.time.wait(2000)
                haieX = 0
                vitesse = .2
        if haieX > 3850 and brepq5:
            if posY < 250 :
                brepq5 = False
                bq5 = True
                scnhaie = False
                bques5()
                pygame.display.update()
            else :
                draw_text('Perdu !',text_font_g,(255,0,0),520,300,fenetre)
                brepq1 = True
                brepq2 = True
                brepq3 = True
                brepq4 = True
                brepq5 = True
                brepq6 = True
                brepq7 = True
                brepq8 = True
                brepq9 = True
                brepq10 = True
                brepq11 = True
                brepq12 = True
                score = 0
                pygame.display.update()
                pygame.time.wait(2000)
                haieX = 0
                vitesse = .2
        if haieX > 4650 and brepq6:
            if posY < 250 :
                brepq6 = False
                bq6 = True
                scnhaie = False
                bques6()
                pygame.display.update()
            else :
                draw_text('Perdu !',text_font_g,(255,0,0),520,300,fenetre)
                brepq1 = True
                brepq2 = True
                brepq3 = True
                brepq4 = True
                brepq5 = True
                brepq6 = True
                brepq7 = True
                brepq8 = True
                brepq9 = True
                brepq10 = True
                brepq11 = True
                brepq12 = True
                score = 0
                pygame.display.update()
                pygame.time.wait(2000)
                haieX = 0
                vitesse = .2
        if haieX > 5450 and brepq7:
            if posY < 250 :
                brepq7 = False
                bq7 = True
                scnhaie = False
                bques7()
                pygame.display.update()
            else :
                draw_text('Perdu !',text_font_g,(255,0,0),520,300,fenetre)
                brepq1 = True
                brepq2 = True
                brepq3 = True
                brepq4 = True
                brepq5 = True
                brepq6 = True
                brepq7 = True
                brepq8 = True
                brepq9 = True
                brepq10 = True
                brepq11 = True
                brepq12 = True
                score = 0
                pygame.display.update()
                pygame.time.wait(2000)
                haieX = 0
                vitesse = .2
        if haieX > 6250 and brepq8:
            if posY < 250 :
                brepq8 = False
                bq8 = True
                scnhaie = False
                bques8()
                pygame.display.update()
            else :
                draw_text('Perdu !',text_font_g,(255,0,0),520,300,fenetre)
                brepq1 = True
                brepq2 = True
                brepq3 = True
                brepq4 = True
                brepq5 = True
                brepq6 = True
                brepq7 = True
                brepq8 = True
                brepq9 = True
                brepq10 = True
                brepq11 = True
                brepq12 = True
                score = 0
                pygame.display.update()
                pygame.time.wait(2000)
                haieX = 0
                vitesse = .2
        if haieX > 7050 and brepq9:
            if posY < 250 :
                brepq9 = False
                bq9 = True
                scnhaie = False
                bques9()
                pygame.display.update()
            else :
                draw_text('Perdu !',text_font_g,(255,0,0),520,300,fenetre)
                brepq1 = True
                brepq2 = True
                brepq3 = True
                brepq4 = True
                brepq5 = True
                brepq6 = True
                brepq7 = True
                brepq8 = True
                brepq9 = True
                brepq10 = True
                brepq11 = True
                brepq12 = True
                score = 0
                pygame.display.update()
                pygame.time.wait(2000)
                haieX = 0
                vitesse = .2
        if haieX > 7850 and brepq10:
            if posY < 250 :
                brepq10 = False
                bq10 = True
                scnhaie = False
                bques10()
                pygame.display.update()
            else :
                draw_text('Perdu !',text_font_g,(255,0,0),520,300,fenetre)
                brepq1 = True
                brepq2 = True
                brepq3 = True
                brepq4 = True
                brepq5 = True
                brepq6 = True
                brepq7 = True
                brepq8 = True
                brepq9 = True
                brepq10 = True
                brepq11 = True
                brepq12 = True
                score = 0
                pygame.display.update()
                pygame.time.wait(2000)
                haieX = 0
                vitesse = .2
        if haieX > 8650 and brepq11:
            if posY < 250 :
                brepq11 = False
                bq11 = True
                scnhaie = False
                bques11()
                pygame.display.update()
            else :
                draw_text('Perdu !',text_font_g,(255,0,0),520,300,fenetre)
                brepq1 = True
                brepq2 = True
                brepq3 = True
                brepq4 = True
                brepq5 = True
                brepq6 = True
                brepq7 = True
                brepq8 = True
                brepq9 = True
                brepq10 = True
                brepq11 = True
                brepq12 = True
                score = 0
                pygame.display.update()
                pygame.time.wait(2000)
                haieX = 0
                vitesse = .2
        if haieX > 9450 and brepq12:
            if posY < 250 :
                brepq12 = False
                bq12 = True
                scnhaie = False
                bques12()
                pygame.display.update()
        if jumping :
            if posY > 150 and up :
                posY += -vitesse
            elif posY <= 350 :
                up = False
                posY += vitesse
            if scnhaie :
                coursehaie()
                pygame.display.update()
            if posY > 350:
                posY = 350
                jumping = False
                coursehaie()
                pygame.display.update()
        elif scnhaie:
            coursehaie()
            pygame.display.update()
        if haieX > 10000:
            if score < 7:
                draw_text('Perdu !',text_font_g,(255,0,0),520,300,fenetre)
                brepq1 = True
                brepq2 = True
                brepq3 = True
                brepq4 = True
                brepq5 = True
                brepq6 = True
                brepq7 = True
                brepq8 = True
                brepq9 = True
                brepq10 = True
                brepq11 = True
                brepq12 = True
                score = 0
                pygame.display.update()
                pygame.time.wait(2000)
                haieX = 0
                vitesse = .2
            elif score < 12:
                draw_text('Gagné !',text_font_g,(0,255,0),500,300,fenetre)
                pygame.display.update()
                pygame.time.wait(2000)
                scnhaie = False
                menu = True
                if trophee2 != 2 :
                    trophee2 = 1
                start()
                vitesse = .2
            elif score == 12:
                draw_text('Score Parfait !',text_font_g,(255,191,0),370,300,fenetre)
                pygame.display.update()
                pygame.time.wait(2000)
                scnhaie = False
                menu = True
                trophee2 = 2
                start()
                vitesse = .2

    while bq1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                bq1 = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    pos = pygame.mouse.get_pos()

                    if pos[0] >= 100 and  pos[0] <= 150 and pos[1] >= 300 and pos[1] <= 350:
                        wrong.play()
                        fenetre.blit(mauvaiseRep,(600,300))
                        pygame.display.update()
                        pygame.time.wait(1000)
                        scnhaie = True
                        bq1 = False
                        coursehaie()

                    if pos[0] >= 100 and  pos[0] <= 150 and pos[1] >= 400 and pos[1] <= 450:
                        wrong.play()
                        fenetre.blit(mauvaiseRep,(600,300))
                        pygame.display.update()
                        pygame.time.wait(1000)
                        scnhaie = True
                        bq1 = False
                        coursehaie()

                    if pos[0] >= 100 and  pos[0] <= 150 and pos[1] >= 500 and pos[1] <= 550:
                        score += 1
                        right.play()
                        fenetre.blit(bonneRep,(600,300))
                        pygame.display.update()
                        pygame.time.wait(1000)
                        scnhaie = True
                        bq1 = False
                        coursehaie()

                    if pos[0] >= 100 and  pos[0] <= 150 and pos[1] >= 600 and pos[1] <= 650:
                        wrong.play()
                        fenetre.blit(mauvaiseRep,(600,300))
                        pygame.display.update()
                        pygame.time.wait(1000)
                        scnhaie = True
                        bq1 = False
                        coursehaie()

    while bq2:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                bq2 = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    pos = pygame.mouse.get_pos()

                    if pos[0] >= 100 and  pos[0] <= 150 and pos[1] >= 300 and pos[1] <= 350:
                        score += 1
                        right.play()
                        fenetre.blit(bonneRep,(600,300))
                        pygame.display.update()
                        pygame.time.wait(1000)
                        scnhaie = True
                        bq2 = False
                        coursehaie()

                    if pos[0] >= 100 and  pos[0] <= 150 and pos[1] >= 400 and pos[1] <= 450:
                        wrong.play()
                        fenetre.blit(mauvaiseRep,(600,300))
                        pygame.display.update()
                        pygame.time.wait(1000)
                        scnhaie = True
                        bq2 = False
                        coursehaie()

                    if pos[0] >= 100 and  pos[0] <= 150 and pos[1] >= 500 and pos[1] <= 550:
                        wrong.play()
                        fenetre.blit(mauvaiseRep,(600,300))
                        pygame.display.update()
                        pygame.time.wait(1000)
                        scnhaie = True
                        bq2 = False
                        coursehaie()

                    if pos[0] >= 100 and  pos[0] <= 150 and pos[1] >= 600 and pos[1] <= 650:
                        wrong.play()
                        fenetre.blit(mauvaiseRep,(600,300))
                        pygame.display.update()
                        pygame.time.wait(1000)
                        scnhaie = True
                        bq2 = False
                        coursehaie()

    while bq3:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                bq3 = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    pos = pygame.mouse.get_pos()

                    if pos[0] >= 100 and  pos[0] <= 150 and pos[1] >= 300 and pos[1] <= 350:
                        score += 1
                        right.play()
                        fenetre.blit(bonneRep,(600,300))
                        pygame.display.update()
                        pygame.time.wait(1000)
                        scnhaie = True
                        bq3 = False
                        coursehaie()

                    if pos[0] >= 100 and  pos[0] <= 150 and pos[1] >= 400 and pos[1] <= 450:
                        wrong.play()
                        fenetre.blit(mauvaiseRep,(600,300))
                        pygame.display.update()
                        pygame.time.wait(1000)
                        scnhaie = True
                        bq3 = False
                        coursehaie()

                    if pos[0] >= 100 and  pos[0] <= 150 and pos[1] >= 500 and pos[1] <= 550:
                        wrong.play()
                        fenetre.blit(mauvaiseRep,(600,300))
                        pygame.display.update()
                        pygame.time.wait(1000)
                        scnhaie = True
                        bq3 = False
                        coursehaie()

                    if pos[0] >= 100 and  pos[0] <= 150 and pos[1] >= 600 and pos[1] <= 650:
                        wrong.play()
                        fenetre.blit(mauvaiseRep,(600,300))
                        pygame.display.update()
                        pygame.time.wait(1000)
                        scnhaie = True
                        bq3 = False
                        coursehaie()

    while bq4:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                bq4 = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    pos = pygame.mouse.get_pos()

                    if pos[0] >= 100 and  pos[0] <= 150 and pos[1] >= 300 and pos[1] <= 350:
                        wrong.play()
                        fenetre.blit(mauvaiseRep,(600,300))
                        pygame.display.update()
                        pygame.time.wait(1000)
                        scnhaie = True
                        bq4 = False
                        coursehaie()

                    if pos[0] >= 100 and  pos[0] <= 150 and pos[1] >= 400 and pos[1] <= 450:
                        wrong.play()
                        fenetre.blit(mauvaiseRep,(600,300))
                        pygame.display.update()
                        pygame.time.wait(1000)
                        scnhaie = True
                        bq4 = False
                        coursehaie()


                    if pos[0] >= 100 and  pos[0] <= 150 and pos[1] >= 500 and pos[1] <= 550:
                        score += 1
                        right.play()
                        fenetre.blit(bonneRep,(600,300))
                        pygame.display.update()
                        pygame.time.wait(1000)
                        scnhaie = True
                        bq4 = False
                        coursehaie()

                    if pos[0] >= 100 and  pos[0] <= 150 and pos[1] >= 600 and pos[1] <= 650:
                        wrong.play()
                        fenetre.blit(mauvaiseRep,(600,300))
                        pygame.display.update()
                        pygame.time.wait(1000)
                        scnhaie = True
                        bq4 = False
                        coursehaie()

    while bq5:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                bq5 = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    pos = pygame.mouse.get_pos()

                    if pos[0] >= 100 and  pos[0] <= 150 and pos[1] >= 300 and pos[1] <= 350:
                        wrong.play()
                        fenetre.blit(mauvaiseRep,(600,300))
                        pygame.display.update()
                        pygame.time.wait(1000)
                        scnhaie = True
                        bq5 = False
                        coursehaie()

                    if pos[0] >= 100 and  pos[0] <= 150 and pos[1] >= 400 and pos[1] <= 450:
                        score += 1
                        right.play()
                        fenetre.blit(bonneRep,(600,300))
                        pygame.display.update()
                        pygame.time.wait(1000)
                        scnhaie = True
                        bq5 = False
                        coursehaie()


                    if pos[0] >= 100 and  pos[0] <= 150 and pos[1] >= 500 and pos[1] <= 550:
                        wrong.play()
                        fenetre.blit(mauvaiseRep,(600,300))
                        pygame.display.update()
                        pygame.time.wait(1000)
                        scnhaie = True
                        bq5 = False
                        coursehaie()

                    if pos[0] >= 100 and  pos[0] <= 150 and pos[1] >= 600 and pos[1] <= 650:
                        wrong.play()
                        fenetre.blit(mauvaiseRep,(600,300))
                        pygame.display.update()
                        pygame.time.wait(1000)
                        scnhaie = True
                        bq5 = False
                        coursehaie()

    while bq6:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                bq6 = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    pos = pygame.mouse.get_pos()

                    if pos[0] >= 100 and  pos[0] <= 150 and pos[1] >= 300 and pos[1] <= 350:
                        wrong.play()
                        fenetre.blit(mauvaiseRep,(600,300))
                        pygame.display.update()
                        pygame.time.wait(1000)
                        scnhaie = True
                        bq6 = False
                        coursehaie()

                    if pos[0] >= 100 and  pos[0] <= 150 and pos[1] >= 400 and pos[1] <= 450:
                        wrong.play()
                        fenetre.blit(mauvaiseRep,(600,300))
                        pygame.display.update()
                        pygame.time.wait(1000)
                        scnhaie = True
                        bq6 = False
                        coursehaie()

                    if pos[0] >= 100 and  pos[0] <= 150 and pos[1] >= 500 and pos[1] <= 550:
                        score += 1
                        right.play()
                        fenetre.blit(bonneRep,(600,300))
                        pygame.display.update()
                        pygame.time.wait(1000)
                        scnhaie = True
                        bq6 = False
                        coursehaie()

                    if pos[0] >= 100 and  pos[0] <= 150 and pos[1] >= 600 and pos[1] <= 650:
                        wrong.play()
                        fenetre.blit(mauvaiseRep,(600,300))
                        pygame.display.update()
                        pygame.time.wait(1000)
                        scnhaie = True
                        bq6 = False
                        coursehaie()

    while bq7:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                bq7 = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    pos = pygame.mouse.get_pos()

                    if pos[0] >= 100 and  pos[0] <= 150 and pos[1] >= 300 and pos[1] <= 350:
                        score += 1
                        right.play()
                        fenetre.blit(bonneRep,(600,300))
                        pygame.display.update()
                        pygame.time.wait(1000)
                        scnhaie = True
                        bq7 = False
                        coursehaie()

                    if pos[0] >= 100 and  pos[0] <= 150 and pos[1] >= 400 and pos[1] <= 450:
                        wrong.play()
                        fenetre.blit(mauvaiseRep,(600,300))
                        pygame.display.update()
                        pygame.time.wait(1000)
                        scnhaie = True
                        bq7 = False
                        coursehaie()

                    if pos[0] >= 100 and  pos[0] <= 150 and pos[1] >= 500 and pos[1] <= 550:
                        wrong.play()
                        fenetre.blit(mauvaiseRep,(600,300))
                        pygame.display.update()
                        pygame.time.wait(1000)
                        scnhaie = True
                        bq7 = False
                        coursehaie()

                    if pos[0] >= 100 and  pos[0] <= 150 and pos[1] >= 600 and pos[1] <= 650:
                        wrong.play()
                        fenetre.blit(mauvaiseRep,(600,300))
                        pygame.display.update()
                        pygame.time.wait(1000)
                        scnhaie = True
                        bq7 = False
                        coursehaie()

    while bq8:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                bq8 = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    pos = pygame.mouse.get_pos()

                    if pos[0] >= 100 and  pos[0] <= 150 and pos[1] >= 300 and pos[1] <= 350:
                        wrong.play()
                        fenetre.blit(mauvaiseRep,(600,300))
                        pygame.display.update()
                        pygame.time.wait(1000)
                        scnhaie = True
                        bq8 = False
                        coursehaie()

                    if pos[0] >= 100 and  pos[0] <= 150 and pos[1] >= 400 and pos[1] <= 450:
                        score += 1
                        right.play()
                        fenetre.blit(bonneRep,(600,300))
                        pygame.display.update()
                        pygame.time.wait(1000)
                        scnhaie = True
                        bq8 = False
                        coursehaie()

                    if pos[0] >= 100 and  pos[0] <= 150 and pos[1] >= 500 and pos[1] <= 550:
                        wrong.play()
                        fenetre.blit(mauvaiseRep,(600,300))
                        pygame.display.update()
                        pygame.time.wait(1000)
                        scnhaie = True
                        bq8 = False
                        coursehaie()

                    if pos[0] >= 100 and  pos[0] <= 150 and pos[1] >= 600 and pos[1] <= 650:
                        wrong.play()
                        fenetre.blit(mauvaiseRep,(600,300))
                        pygame.display.update()
                        pygame.time.wait(1000)
                        scnhaie = True
                        bq8 = False
                        coursehaie()

    while bq9:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                bq9 = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    pos = pygame.mouse.get_pos()

                    if pos[0] >= 100 and  pos[0] <= 150 and pos[1] >= 300 and pos[1] <= 350:
                        wrong.play()
                        fenetre.blit(mauvaiseRep,(600,300))
                        pygame.display.update()
                        pygame.time.wait(1000)
                        scnhaie = True
                        bq9 = False
                        coursehaie()

                    if pos[0] >= 100 and  pos[0] <= 150 and pos[1] >= 400 and pos[1] <= 450:
                        wrong.play()
                        fenetre.blit(mauvaiseRep,(600,300))
                        pygame.display.update()
                        pygame.time.wait(1000)
                        scnhaie = True
                        bq9 = False
                        coursehaie()

                    if pos[0] >= 100 and  pos[0] <= 150 and pos[1] >= 500 and pos[1] <= 550:
                        wrong.play()
                        fenetre.blit(mauvaiseRep,(600,300))
                        pygame.display.update()
                        pygame.time.wait(1000)
                        scnhaie = True
                        bq9 = False
                        coursehaie()

                    if pos[0] >= 100 and  pos[0] <= 150 and pos[1] >= 600 and pos[1] <= 650:
                        score += 1
                        right.play()
                        fenetre.blit(bonneRep,(600,300))
                        pygame.display.update()
                        pygame.time.wait(1000)
                        scnhaie = True
                        bq9 = False
                        coursehaie()

    while bq10:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                bq10 = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    pos = pygame.mouse.get_pos()

                    if pos[0] >= 100 and  pos[0] <= 150 and pos[1] >= 300 and pos[1] <= 350:
                        wrong.play()
                        fenetre.blit(mauvaiseRep,(600,300))
                        pygame.display.update()
                        pygame.time.wait(1000)
                        scnhaie = True
                        bq10 = False
                        coursehaie()

                    if pos[0] >= 100 and  pos[0] <= 150 and pos[1] >= 400 and pos[1] <= 450:
                        score += 1
                        right.play()
                        fenetre.blit(bonneRep,(600,300))
                        pygame.display.update()
                        pygame.time.wait(1000)
                        scnhaie = True
                        bq10 = False
                        coursehaie()

                    if pos[0] >= 100 and  pos[0] <= 150 and pos[1] >= 500 and pos[1] <= 550:
                        wrong.play()
                        fenetre.blit(mauvaiseRep,(600,300))
                        pygame.display.update()
                        pygame.time.wait(1000)
                        scnhaie = True
                        bq10 = False
                        coursehaie()

                    if pos[0] >= 100 and  pos[0] <= 150 and pos[1] >= 600 and pos[1] <= 650:
                        wrong.play()
                        fenetre.blit(mauvaiseRep,(600,300))
                        pygame.display.update()
                        pygame.time.wait(1000)
                        scnhaie = True
                        bq10 = False
                        coursehaie()

    while bq11:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                bq11 = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    pos = pygame.mouse.get_pos()

                    if pos[0] >= 100 and  pos[0] <= 150 and pos[1] >= 300 and pos[1] <= 350:
                        wrong.play()
                        fenetre.blit(mauvaiseRep,(600,300))
                        pygame.display.update()
                        pygame.time.wait(1000)
                        scnhaie = True
                        bq11 = False
                        coursehaie()


                    if pos[0] >= 100 and  pos[0] <= 150 and pos[1] >= 400 and pos[1] <= 450:
                        wrong.play()
                        fenetre.blit(mauvaiseRep,(600,300))
                        pygame.display.update()
                        pygame.time.wait(1000)
                        scnhaie = True
                        bq11 = False
                        coursehaie()

                    if pos[0] >= 100 and  pos[0] <= 150 and pos[1] >= 500 and pos[1] <= 550:
                        score += 1
                        right.play()
                        fenetre.blit(bonneRep,(600,300))
                        pygame.display.update()
                        pygame.time.wait(1000)
                        scnhaie = True
                        bq11 = False
                        coursehaie()

                    if pos[0] >= 100 and  pos[0] <= 150 and pos[1] >= 600 and pos[1] <= 650:
                        wrong.play()
                        fenetre.blit(mauvaiseRep,(600,300))
                        pygame.display.update()
                        pygame.time.wait(1000)
                        scnhaie = True
                        bq11 = False
                        coursehaie()

    while bq12:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                bq12 = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    pos = pygame.mouse.get_pos()

                    if pos[0] >= 100 and  pos[0] <= 150 and pos[1] >= 300 and pos[1] <= 350:
                        wrong.play()
                        fenetre.blit(mauvaiseRep,(600,300))
                        pygame.display.update()
                        pygame.time.wait(1000)
                        scnhaie = True
                        bq12 = False
                        coursehaie()

                    if pos[0] >= 100 and  pos[0] <= 150 and pos[1] >= 400 and pos[1] <= 450:
                        wrong.play()
                        fenetre.blit(mauvaiseRep,(600,300))
                        pygame.display.update()
                        pygame.time.wait(1000)
                        scnhaie = True
                        bq12 = False
                        coursehaie()

                    if pos[0] >= 100 and  pos[0] <= 150 and pos[1] >= 500 and pos[1] <= 550:
                        wrong.play()
                        fenetre.blit(mauvaiseRep,(600,300))
                        pygame.display.update()
                        pygame.time.wait(1000)
                        scnhaie = True
                        bq12 = False
                        coursehaie()

                    if pos[0] >= 100 and  pos[0] <= 150 and pos[1] >= 600 and pos[1] <= 650:
                        score += 1
                        right.play()
                        fenetre.blit(bonneRep,(600,300))
                        pygame.display.update()
                        pygame.time.wait(1000)
                        scnhaie = True
                        bq12 = False
                        coursehaie()


    pygame.display.update()

pygame.quit()