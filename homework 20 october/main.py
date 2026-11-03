import pygame #start code to run

#start features in code
pygame.init()

#setting measurements of screen
HEIGHT = 600
WIDTH = 1000
#constants
FPS = 60 #refresh rate is the same
PLAYER_SPEED = 5
BULLET_SPEED = 7
MAX_BULLET = 10

rocket_x = 450
rocket_y = 450

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("spaceshooter game")

#creating class for the bullet
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, direction): #setting parameters
        super().__init__() #initialises parent class
        self.image = pygame.Surface((10,10))
        self.image.fill('Black')
        self.rect = self.image.get_rect(center = (x,y))
        self.direction = direction
    


#creating player class blueprint of rocket
class Player(pygame.sprite.Sprite): #inherit from sprite class
    def __init__(self, x, y, image_path, control):#paameters
        super().__init__() #initialises parent sprite class
        self.image = pygame.image.load(image_path)
        self.control = control
        self.bullets = pygame.sprite.Group()
        self.rect = self.image.get_rect(topleft = (x,y)) #creating the hitbox around the image

    def move(self, pressed_keys):
        if pressed_keys[self.control['left']]:
            self.rect.x -= PLAYER_SPEED
        if pressed_keys[self.control['right']]:
            self.rect.x += PLAYER_SPEED
        self.rect.left = max(0, self.rect.left)  
        self.rect.right = min(self.rect.right, WIDTH)

rocket = Player(rocket_x, rocket_y, 'rocket.png', {'left':pygame.K_LEFT, 'right':pygame.K_RIGHT})        
player_group = pygame.sprite.Group()
player_group.add(rocket)


def draw():
    screen.fill('pink')

    player_group.draw(screen)

    pygame.display.update()

while True:
    draw() #calls function 

    keys = pygame.key.get_pressed()
    rocket.move(keys)
    
    for event in pygame.event.get(): #code for exiting the gamr
        if event.type == pygame.QUIT:
            exit()



pygame.quit()

