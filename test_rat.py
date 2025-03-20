import pygame
import os
pygame.init()
#pls help
class Player:
    def __init__(self, health, stamina, velocity):
        self.health=health
        self.maxStamina=stamina
        self.stamina=stamina
        self.velocity=velocity
        self.momentum=[0, 0]
        self.position=[0, 0]
    def move(direction):
        if sprinting:
            
        if direction="w":
            self.momentum[1]+=self.velocity
            
class Shop:
    def __init__(self):
        pass
class Game:
    def __init__(self, scaling=1, framerate=60):
        if pygame.display.Info().current_w/pygame.display.Info().current_h>750/500:
            self.screenHeight=pygame.display.Info().current_h
            self.screenWidth=self.screenHeight*1.5
            self.scaling=scaling*self.screenHeight/500
        else:
            self.screenWidth=pygame.display.Info().current_w
            self.screenHeight=self.screenWidth*2/3
            self.scaling=scaling*self.screenWidth/750
        self.ratFlipped=False
        self.rat=pygame.image.load("assets/transparentrat.png")
        self.timeForOneFrame=1/framerate
        self.framerate=framerate
        self.font = pygame.font.SysFont('consolas', 20)
        self.enterShopText = self.font.render("Press E to enter or close the shop", 1, (0,0,0))
        self.rat=Player(10, 100, 5)
        pygame.display.set_caption("rat sim dev version")
        print("right-shift to run, and Q to recover stamina\nhope you enjoy!")
    def mainLoop(self):
        while True:
            
#constants and variables
vel = 5
openedshop = False

width = 750
height = 500
window = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()
run = True
sprint = True
stamina = 100

#pygame.mixer.music.load("assets/shop-decode.mp3")
shoprat = pygame.image.load("assets/shoprat.png")
shoprat = pygame.transform.scale(shoprat, (105, 75))
def shopicon():
    window.blit(shoprat, (200, 130))

font = pygame.font.SysFont('consolas', 20)

rat = pygame.image.load("assets/transparentrat.png")
rat = pygame.transform.scale(rat, (125,75))
flipratimg = pygame.transform.flip(rat, True, False)
pygame.display.set_caption("rat sim dev version")
print("right-shift to run, and Q to recover stamina\nhope you enjoy!")
entshoptext = font.render("Press E to enter or close the shop", 1, (0,0,0))

x = (750 * 0.45)
y = (500 * 0.45)
bg = pygame.image.load("assets/background.png")
bg = pygame.transform.scale(bg, (width,height))
def ratty():
    window.blit(bg, (0,0))

def draw(x,y, openedshop):
    ratty()
    keys = pygame.key.get_pressed()
    if openedshop == False:
            shopicon()
            if x >= 140 and x <= 240 and y >= 90 and y <= 145:
                window.blit(entshoptext, (x+100, y+100))
                if keys[pygame.K_e]:
                    openedshop = True
                    os.system("shop-test.py")
                    vel = 0
                    if keys[pygame.K_e]:
                        openedshop = False
    window.blit(rat, (x,y))
    staminatext = font.render("stamina: " + str(int(stamina)), 1, (0,0,0))
    window.blit(staminatext, (25, 460))

    pygame.display.flip()

draw(x,y, openedshop)
pygame.display.flip()

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #simple keybinds and stamina
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RSHIFT] and sprint == True:
        vel = 7.5
        stamina -= 0.2
    else:
        vel = 5
    
    if stamina <= 0:
        vel = 3
        sprint = False
    else:
        sprint = True

    if keys[pygame.K_w] or keys[pygame.K_UP] and openedshop == False:
        y-=vel
        draw(x,y, openedshop)
        if (y <= -60):
            y = 530

    if keys[pygame.K_s] or keys[pygame.K_DOWN] and openedshop == False:
        y+=vel
        draw(x,y, openedshop)
        if (y >= 540):
            y = -40

    if keys[pygame.K_a] or keys[pygame.K_LEFT] and openedshop == False:
        rat = flipratimg
        x-=vel
        draw(x,y, openedshop)
        if (x <= -150):
            x = 730

    if keys[pygame.K_d] or keys[pygame.K_RIGHT] and openedshop == False:
        rat = pygame.image.load("assets/transparentrat.png")
        rat = pygame.transform.scale(rat, (125,75))
        x+=vel
        draw(x,y, openedshop)
        if (x >= 750):
            x = -100
    
    #add stamina
    if keys[pygame.K_q] and stamina < 100:
        stamina += 0.1
        draw(x,y, openedshop)
        
    clock.tick(60)
    pygame.display.flip()
