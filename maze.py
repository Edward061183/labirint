from pygame import * #подключение библиотек


"""Необходимые классы"""
class GameSprite(sprite.Sprite): #создание класса гейм спрайт
    def __init__(self, image_sprite, img_x, img_y, speed): #создание дефа с конструктором внутри класса
        super().__init__()
        self.image = transform.scale(image.load(image_sprite),(65,65)) #обозначение детали конструктора
        self.speed = speed #обозначение детали конструктора
        self.rect = self.image.get_rect() #обозначение детали конструктора
        self.rect.x = img_x #обозначение детали конструктора
        self.rect.y = img_y #обозначение детали конструктора

    def show_s(self): # дэф для создания картинки
        window.blit(self.image,(self.rect.x, self.rect.y)) #параметры картинки


class Player(GameSprite): #создание класса игрока
    def update(self):  #дэф для движения игрока
        keys = key.get_pressed() #нажатие кнопки
        if keys[K_a] and self.rect.x > 5: #команда ходбы
            self.rect.x -= self.speed #команда ходбы
        if keys[K_d] and self.rect.x < win_width -80: #команда ходбы
            self.rect.x += self.speed #команда ходбы
        if keys[K_w] and self.rect.y > 5: #команда ходбы
            self.rect.y -= self.speed #команда ходбы
        if keys[K_s] and self.rect.y < win_hight - 80: #команда ходбы
            self.rect.y += self.speed #команда ходбы

class Enemy(GameSprite):
    naprav = "left"
    def update(self):
        if self.rect.x <= 470:
            self.naprav = "right"
        if self.rect.x >= win_width - 85:
            self.naprav = "left"

        if self.naprav == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

class Wall(sprite.Sprite):
    def __init__(self, color1, color2, color3, wall_x, wall_y, wall_width, wall_hight):
        super().__init__()
        self.color1 = color1
        self.color2 = color2
        self.color3 = color3
        self.wall_width = wall_width
        self.wall_hight = wall_hight

        self.image = Surface ((self.wall_width, self.wall_hight))
        self.image.fill((self.color1,self.color2,self.color3))

        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y

    def show_s(self): # дэф для создания картинки
        window.blit(self.image,(self.rect.x, self.rect.y)) #параметры картинки
 

win_width = 700 #параметры экрана
win_hight = 500 #параметры экрана

window = display.set_mode((700,500)) #создание окна игры
display.set_caption("igra") #название игры
bg = transform.scale(image.load("background.jpg"), (win_width,win_hight)) #фон

player = Player("hero.png",5, win_hight-70, 4) #игрок 
monster = Enemy("cyborg.png", win_width - 80, 280, 2) #киборг (монстр)
finish_s = GameSprite("treasure.png",win_width - 120, win_hight - 80, 0) #золото (цель)
w1 = Wall(122,34,1 ,225,205,20,400)
w2 = Wall(122,34,1 ,225,200,240,20)
w3 = Wall(122,34,1 ,445,205,20,400)
game = True #переводится как "правильно" используется для запуска игры
finish = False #переводится как "не правильно" используется для остановки игры

clock = time.Clock() #не помню если честно

mixer.init() #миксер используется для связывания действий
mixer.music.load("jungles.ogg") #музыка на фоне 
mixer.music.play() #миксер музыку запустил


font.init()
font = font.Font(None, 70)
win = font.render('поздравляю, ты победил!', True, (255, 215, 0))
lose = font.render('ты загнал занозу', True, (135, 0, 0))
smer = font.render('тебя съели', True, (180, 0, 0))

while game: #игровой цикл
    for i in event.get(): #просто цикл 
        if i.type == QUIT: #тут если нажимаешь  игра остонавливается
           game = False #для самой остановки

    if finish != True: #то что будут остонавливать
        window.blit(bg, (0,0)) #на окне показывают обьект
        player.show_s() #биндят персонажей если можно так сказать
        monster.show_s() #биндят персонажей если можно так сказать
        finish_s.show_s() #биндят персонажей если можно так сказать

        w1.show_s()
        w2.show_s()
        w3.show_s()

        if sprite.collide_rect(player, w1) or sprite.collide_rect(player, w2) or sprite.collide_rect(player, w3):
            finish = True
            window.blit(lose, (165,90))

        if sprite.collide_rect(player, finish_s):
            finish = True
            window.blit(win, (25,145))

        if sprite.collide_rect(player, monster):
            finish = True
            window.blit(smer, (210,145))

        player.update() #не знаю игрока обновляет
        monster.update()

    display.update() #FPS
    clock.tick(60) #количество FPS