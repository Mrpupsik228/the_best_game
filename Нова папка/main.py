from pygame import *

import sys

init()

dis_x = 8192

dis_y = 8192

FPS = 120

speed = 1

clock= time.Clock()

font = font.SysFont(None, 20)

finish = False

manual = True

game = True

# картинки для анімайії ходьби для перснажа 
hero_an1 = "pictures\hero/run\go1"
hero_an2 = "pictures\hero/run\go2"
hero_an3 = "pictures\hero/run\go3"
hero_an4 = "pictures\hero/run\go4"
hero_an5 = "pictures\hero/run\go5"

# картинки для анімайії стрибка для перснажа 
hero_jamp_an1 = "farmer.png"
hero_jamp_an2 = "pictures\hero\jamp\jamp2"
hero_jamp_an3 = "pictures\hero\jamp\jamp3"
hero_jamp_an4 = "pictures\hero\jamp\jamp4"
hero_jamp_an5 = "pictures\hero\jamp\jamp5"

map = transform.scale(image.load("pictures\map.png"),(8192,8192))# завантаження і створення мапи 

mw = display.set_mode((dis_x,dis_y)) # розміри екрану

mixer.init()# запуск бібліотеки музики

mixer.music.load("music/fon_music.ogg")# завантаження музики фону

mixer.music.play()# запуск музики

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y,size_x,size_y ,player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x,size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        mw.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT]:
            self.rect.x -= self.speed
        if keys[K_RIGHT]:
            self.rect.y += self.speed
        if keys[K_UP]:
            self.rect.y -= self.speed
        if keys[K_DOWN]:
            self.rect.y += self.speed

    def reset(self):
        mw.blit(self.image, (self.rect.x, self.rect.y))

player = Player("farmer.png",0,0,500,500,1)

def menu():
    while manual:
        for e in event.get():
            if e.type == QUIT:
                game = False
                keys = key.get_pressed()
                if keys[K_p]:
                    start_the_game()
                if keys[K_e]:
                    sys.exit()
                

def set_difficulty(value, difficulty):
    pass

def start_the_game():
    game = True
    while game:

        for e in event.get():
            if e.type == QUIT:
                game = False

        if not finish:

            player.update()
            mw.blit(map,(0,0))    

        display.update()
        clock.tick(FPS)
