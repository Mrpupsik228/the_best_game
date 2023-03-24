from pygame import *
import sys

init()

font.init()

text1 = font.SysFont ("Arial",75)

text_col = (255,255,255)

play_img = image.load("play.png")
settings_img = image.load("settings.png")
exit_img = image.load("exit.png")
volume_img = image.load("volume.png")
back_img = image.load("back.png")
ogorod_image = image.load("ogorod.png")

menu_state = "main"

game_paused = False

dis_x = 1280

dis_y = 720

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

# картинки для анімації стрибка для перснажа 
hero_jamp_an1 = "jamp1.png"
hero_jamp_an2 = "pictures\hero\jamp\jamp2"
hero_jamp_an3 = "pictures\hero\jamp\jamp3"
hero_jamp_an4 = "pictures\hero\jamp\jamp4"
hero_jamp_an5 = "pictures\hero\jamp\jamp5"

map = transform.scale(image.load("map.png"),(1280,720))# завантаження і створення мапи 

mw = display.set_mode((dis_x,dis_y)) # розміри екрану

mixer.init()# запуск бібліотеки музики

mixer.music.load("music/fon_music.ogg")# завантаження музики фону

mixer.music.play()# запуск музики

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y,size_x,size_y ,player_speed,):
        super().__init__()
        self.image = transform.scale(image.load("farmer.png"), (size_x,size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        mw.blit(self.image, (self.rect.x, self.rect.y))

class Ogorod(sprite.Sprite):
    def __init__(self, ogorod_image, ogorod_x, ogorod_y,og_size_x,og_size_y):
#
#       super().init()
        self.image = transform.scale(image.load("ogorod.png"), (og_size_x,og_size_y))
        self.rect = self.image.get_rect()
        self.rect.x = ogorod_x
        self.rect.y = ogorod_y
    def a(self):
        keys = key.get_pressed()
#        ogorod_x = self.rect.x 
        if keys[K_1]:
            pass
#            print("огород робочий")
#           plant_menu()
    def reset(self):
        mw.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()

        if keys[K_a] and not keys[K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed

        if keys[K_d] and not keys[K_RIGHT] and self.rect.x < 1180:
            self.rect.x += self.speed

        if keys[K_w] and not keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed

        if keys[K_s] and not keys[K_DOWN] and self.rect.y < 620:
            self.rect.y += self.speed

        if keys[K_LEFT] and not keys[K_a] and self.rect.x > 0:
            self.rect.x -= self.speed

        if keys[K_RIGHT] and not keys[K_d] and self.rect.x < 1180:
            self.rect.x += self.speed

        if keys[K_UP] and not keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed

        if keys[K_DOWN] and not keys[K_s] and self.rect.y < 620:
            self.rect.y += self.speed

class Button():
    def __init__(self,x,y,image,scale):
        width = image.get_width()
        height = image.get_height()
        self.image = transform.scale(image,(int(width * scale),int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = x,y
        self.clicked = False

    def draw(self,mw):
        action = False
        pos = mouse.get_pos()

        if self.rect.collidepoint(pos):
            if mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if mouse.get_pressed()[0] == 0:
            self.clicked = False
        mw.blit(self.image, (self.rect.x,self.rect.y))
        return action


ogorod1 = Ogorod(ogorod_image, 1000, 500,  100, 100)

play_button = Button(575,150,play_img,1)
settings_button = Button(575,300,settings_img,1)
exit_button = Button(575,450,exit_img,1)
back_button = Button(725,300,back_img,1)
volume_button = Button(425,300,volume_img,1)
volume1_button = Button(575,100,volume_img,1)
volume2_button = Button(575,250,volume_img,1)
volume3_button = Button(575,400,volume_img,1)
volume4_button = Button(575,550,volume_img,1)
player = Player("hero_jamp_an1",100,100,100,100,5)

def draw_text (text, font, text_col, x, y,):
    img = font.render(text,True,text_col)
    mw.blit(img,(x,y))

def menu():
    global game_paused,menu_state
    while True:
        mw.blit(map,(0,0))
        if game_paused:
            if menu_state == "main":
                
                if play_button.draw(mw):
                    start_the_game()

                if settings_button.draw(mw):
                    menu_state = "options"
                    time.delay(300)

                if exit_button.draw(mw):
                    sys.exit()

            if menu_state == "options":
                if volume_button.draw(mw):
                    menu_state = "volume"

                if back_button.draw(mw):
                    menu_state = "main"

            if menu_state == "volume":
                if volume1_button.draw(mw):
                    mixer.music.set_volume(0)

                if volume2_button.draw(mw):
                    mixer.music.set_volume(0.25)

                if volume3_button.draw(mw):
                    mixer.music.set_volume(0.5)

                if volume4_button.draw(mw):
                    mixer.music.set_volume(1)

                if back_button.draw(mw):
                    menu_state = "options"

        else:
            draw_text("Press spase to go the menu",text1,text_col,160,250)
            keys = key.get_pressed()
            if keys[K_SPACE]:
                game_paused = True
        
        for e in event.get():
            if e.type == QUIT:
                sys.exit()

        display.update()
        clock.tick(FPS)

def start_the_game():
    game = True
    while game:
        for e in event.get():
            if e.type == QUIT:
                game = False

        if not finish:

            mw.blit(map,(0,0))    
            ogorod1.a()
            player.update()
            player.reset()
            ogorod1.reset()

        display.update()
        clock.tick(FPS)

menu()