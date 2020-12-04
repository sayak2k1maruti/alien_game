import pygame

import time

import random

pygame.init()

display_width = 800
display_height=600

black = (0,0,0)
white = (255,255,255)
red = (200,0,0)
green = (0,200,0)

bright_red=(255,0,0)
bright_green=(0,255,0)
car_width = 60

pause = False
#crash = True
gameDisplay = pygame.display.set_mode((display_width,display_height))

pygame.display.set_caption('A bit Racey')

clock = pygame.time.Clock()

carImg = pygame.image.load("../ship.png")

pygame.display.set_icon(carImg)


def things_dodged(count):
    font=pygame.font.SysFont(None,25)
    text = font.render("dodged "+ str(count),True,black)
    gameDisplay.blit(text , (0,0))


def things(thingx , thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color,[thingx , thingy, thingw, thingh])

def car(x,y):
    gameDisplay.blit(carImg,(x,y))

def text_objects(text,font):
    textSurface = font.render(text,True,black)#render is in-built in pygane
    return textSurface, textSurface.get_rect()


def message_display(text):
    largeText = pygame.font.Font("freesansbold.ttf",116)
    TextSurf,TextRect = text_objects(text, largeText)
    TextRect.center= ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf,TextRect)
    
    
    pygame.display.update()
    time.sleep(2)
    game_loop()
    
    
def crash():

    #pygame.mixer.music.stop()
    #pygame.mixer.Sound.play(crash_sound)
    largeText = pygame.font.SysFont("comicsansms",115)
    TextSurf,TextRect = text_objects("You crashed", largeText)
    TextRect.center= ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf,TextRect)
    while True :
        
        for event in pygame.event.get():
            #print(event)#gets the pos of mouse on the game console
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        #gameDisplay.fill(white)
        

        button("Play again",150,450,100,50,green,bright_green,game_loop)
        button("QUIT",550,450,100,50,red,bright_red,game_quit)

        pygame.display.update()
        clock.tick(30) 


def button(msg,x,y,w,h,ic,ac,action=None):#msg the btn would show, rect shape, inac,ac color
    
    mouse=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    if x+w>mouse[0]>x and y+h> mouse[1]>y:
        
        pygame.draw.rect(gameDisplay, ac ,(x,y,w,h))
        if click[0]==1 and action!=None:
            action()
           #if action=="play":
            #game_loop()
            #elif action=="quit":
             #pygame.quit()
              #quit()
            
    else:
        pygame.draw.rect(gameDisplay, ic ,(x,y,w,h))

    smallText=pygame.font.Font("freesansbold.ttf",20)
    textSurf, textRect = text_objects(msg,smallText)
    textRect.center = ((x+w/2),(y+h/2))
    gameDisplay.blit(textSurf,textRect)



def game_intro(): #creates a intro for the game
    intro = True
    while intro:
        for event in pygame.event.get():
            #print(event)#gets the pos of mouse on the game console
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)
        largeText = pygame.font.Font("freesansbold.ttf",116)
        TextSurf,TextRect = text_objects("A BIT RACEY", largeText)
        TextRect.center= ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf,TextRect)

        button("GO",150,450,100,50,green,bright_green,game_loop)
        button("QUIT",550,450,100,50,red,bright_red,game_quit)

        
        
        pygame.display.update()
        clock.tick(15)
def game_quit():
    pygame.quit()
    quit()
def unpause():
    global pause #global variable
    pause = False

def paused(): #creates a intro for the game
    while pause :
        for event in pygame.event.get():
            #print(event)#gets the pos of mouse on the game console
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        #gameDisplay.fill(white)
        largeText = pygame.font.SysFont("comicsansms",115)
        TextSurf,TextRect = text_objects("Paused", largeText)
        TextRect.center= ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf,TextRect)

        button("Continue",150,450,100,50,green,bright_green,unpause)
        button("QUIT",550,450,100,50,red,bright_red,game_quit)

        
        
        pygame.display.update()
        clock.tick(15)  


def game_loop():
    global pause
    
    x=(display_width *0.45)
    y=(display_height *0.8)

    x_change = 0

    dodged = 0
    
    

    thing_startx= random.randrange(0, display_width)
    thing_starty=-600#we want to start the block off the screen
    thing_speed=7
    thing_width=100
    thing_height=100
    
    gameExit= False

    while not gameExit:
        for event in pygame.event.get():#crates list of event
            if event.type== pygame.QUIT:
                pygame.quit()
                quit()
                gameExit = True
            elif event.type==pygame.KEYDOWN:#keydown and keyup ctrl are used so that the image cannotmove continuously or move whwnever the key is pressed
                if event.key == pygame.K_LEFT:
                    x_change= -5
                elif event.key == pygame.K_RIGHT:
                    x_change= 5
                elif event.key == pygame.K_p:
                    pause = True
                    paused()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT  or  pygame.K_RIGHT:
                    x_change= 0
        x=x+x_change
        
        gameDisplay.fill(white)
        things(thing_startx , thing_starty, thing_width, thing_height,black)
        thing_starty+=thing_speed
        car(x,y)#order is important

        things_dodged(dodged)

        
        if thing_starty > display_height:
            thing_starty= 0- thing_height
            thing_startx= random.randrange(0,display_width)

            dodged+= 1
            thing_speed+=1
            thing_width+=dodged*1.2
            

        if y <thing_starty+thing_height:
            #print("y crossover")

            if x >thing_startx and x< thing_startx+thing_width or x+car_width>thing_startx  and x+car_width < thing_width+thing_startx:
               # print("x crossover")
                crash()
                
            
        if x > display_width - car_width or x< 0:
            crash()

        pygame.display.update()#background processing is easier

        #or pygame.display.flip() but this is always updates the entire frame

        clock.tick(60)#how fast the updating happens


        #but if u want to update things faster but smooth theb frame per sec option
game_intro()#but we need a button to enter into yhe game from the intro
game_loop()
pygame.quit()
quit()
