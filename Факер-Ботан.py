# Создание, отрисовка и управление танками
import pygame
from random import randint

pygame.init()

WIDTH, HEIGHT = 800, 600
FPS = 60
TILE = 50 #ширина картинки

window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

fontUI = pygame.font.Font(None, 30) #шрифт по умолчанию

imgBrick = pygame.image.load('images/block_brick.png')

DIRECTS = [[0, -1], [1, 0], [0, 1], [-1, 0]] #смещение в соответствующее направление

class UI:
    def __init__(self):
        pass

    def update(self):
        pass

    def draw(self):
        i = 0
        for obj in objects:
            if obj.type == 'man':
                pygame.draw.rect(window, obj.color, (5 + i * 70, 5, 22, 22))

                text = fontUI.render(str(obj.hp), 1, obj.color) #текстовое поле для отображения жизни соответствующего человека
                rect = text.get_rect(center = (5 + i * 70 + 32, 5 + 11))
                window.blit(text, rect)
                i += 1
class Facker: #класс факеров
    def __init__(self, color, px, py, direct, keyList): #px, py - позиция, direct - направление, куда смотрит человек, keyList - список кнопок
        objects.append(self) #добавляем ссылку на класс Man в список объектов
        self.type = 'man'

        self.color = color
        self.rect = pygame.Rect(px, py, TILE, TILE) #координаты, ширина и высота
        self.direct = direct
        self.moveSpeed = 2
        self.hp = 5

        #параметры пули, учитивыющие урон, скорость и задержку
        self.shotTimer = 0
        self.shotDelay = 60
        self.bulletSpeed = 5
        self.bulletDamage = 1

        #кнопки управления
        self.keyLEFT = keyList[0]
        self.keyRIGHT = keyList[1]
        self.keyUP = keyList[2]
        self.keyDOWN = keyList[3]
        self.keySHOT = keyList[4]

    def update(self): #обновление статусов
        oldX, oldY = self.rect.topleft #сохраняем старую позицию
        if keys[self.keyLEFT]: #движение влево
            self.rect.x -= self.moveSpeed
            self.direct = 3
        elif keys[self.keyRIGHT]: #движение вправо
            self.rect.x += self.moveSpeed
            self.direct = 1
        elif keys[self.keyUP]: #движение вверх
            self.rect.y -= self.moveSpeed
            self.direct = 0
        elif keys[self.keyDOWN]: #движение вниз
            self.rect.y += self.moveSpeed
            self.direct = 2

        for obj in objects: #столкновение человека с блоком
            if obj != self and self.rect.colliderect(obj.rect):
                self.rect.topleft = oldX, oldY

        #механика стрельбы
        if keys[self.keySHOT] and self.shotTimer == 0:
            dx = DIRECTS[self.direct][0] * self.bulletSpeed
            dy = DIRECTS[self.direct][1] * self.bulletSpeed
            Bullet(self, self.rect.centerx, self.rect.centery, dx, dy, self.bulletDamage)
            self.shotTimer = self.shotDelay

        if self.shotTimer > 0: self.shotTimer -= 1

    def draw(self): #рисовка
        pygame.draw.rect(window, self.color, self.rect)

        x = self.rect.centerx + DIRECTS[self.direct][0] * 30
        y = self.rect.centery + DIRECTS[self.direct][1] * 30
        pygame.draw.line(window, 'white', self.rect.center, (x, y), 4)

    #метод насения урона
    def damage(self, value):
        self.hp -= value
        if self.hp <= 0:#смерть
            objects.remove(self)
            print(self.color, 'dead')

class Botan: #класс ботанов
    def __init__(self, color, px, py, direct, keyList): #px, py - позиция, direct - направление, куда смотрит человек, keyList - список кнопок
        objects.append(self) #добавляем ссылку на класс Man в список объектов
        self.type = 'man'

        self.color = color
        self.rect = pygame.Rect(px, py, TILE, TILE) #координаты, ширина и высота
        self.direct = direct
        self.moveSpeed = 2
        self.hp = 5

        #параметры пули, учитивыющие урон, скорость и задержку
        self.shotTimer = 0
        self.shotDelay = 60
        self.bulletSpeed = 5
        self.bulletDamage = 1

        #кнопки управления
        self.keyLEFT = keyList[0]
        self.keyRIGHT = keyList[1]
        self.keyUP = keyList[2]
        self.keyDOWN = keyList[3]
        self.keySHOT = keyList[4]

    def update(self): #обновление статусов
        oldX, oldY = self.rect.topleft #сохраняем старую позицию
        if keys[self.keyLEFT]: #движение влево
            self.rect.x -= self.moveSpeed
            self.direct = 3
        elif keys[self.keyRIGHT]: #движение вправо
            self.rect.x += self.moveSpeed
            self.direct = 1
        elif keys[self.keyUP]: #движение вверх
            self.rect.y -= self.moveSpeed
            self.direct = 0
        elif keys[self.keyDOWN]: #движение вниз
            self.rect.y += self.moveSpeed
            self.direct = 2

        for obj in objects: #столкновение человека с блоком
            if obj != self and self.rect.colliderect(obj.rect):
                self.rect.topleft = oldX, oldY

        #механика стрельбы
        if keys[self.keySHOT] and self.shotTimer == 0:
            dx = DIRECTS[self.direct][0] * self.bulletSpeed
            dy = DIRECTS[self.direct][1] * self.bulletSpeed
            Bullet(self, self.rect.centerx, self.rect.centery, dx, dy, self.bulletDamage)
            self.shotTimer = self.shotDelay

        if self.shotTimer > 0: self.shotTimer -= 1

    def draw(self): #рисовка
        pygame.draw.rect(window, self.color, self.rect)

        x = self.rect.centerx + DIRECTS[self.direct][0] * 30
        y = self.rect.centery + DIRECTS[self.direct][1] * 30
        pygame.draw.line(window, 'white', self.rect.center, (x, y), 4)

    #метод насения урона
    def damage(self, value):
        self.hp -= value
        if self.hp <= 0:#смерть
            objects.remove(self)
            print(self.color, 'dead')

class Bullet:#класс пули
    def __init__(self, parent, px, py, dx, dy, damage):#parent- от кого идет пуля, р_х, р_у-координаты начала пули, d_x,d_y- куда летит пуля, damage- урон
        bullets.append(self)
        self.parent = parent
        self.px, self.py = px, py
        self.dx, self.dy = dx, dy
        self.damage = damage

    def update(self):#изменение параметров
        self.px += self.dx
        self.py += self.dy

        #механизм удаления пули, если она вылетела за пределы игрового поля и при попадании в объект
        if self.px < 0 or self.px > WIDTH or self.py < 0 or self.py > HEIGHT:
            bullets.remove(self)
        else:
            for obj in objects:
                if obj != self.parent and obj.rect.collidepoint(self.px, self.py):
                    obj.damage(self.damage)
                    bullets.remove(self)
                    break

    def draw(self): #параметры пули
        pygame.draw.circle(window, 'yellow', (self.px, self.py), 3)

class Block: #создаем класс блоков-преград (учебники по ангему)
    def __init__(self, px, py, size):
        objects.append(self)
        self.type = 'block'

        self.rect = pygame.Rect(px, py, size, size)
        self.hp = 1

    def update(self):
        pass

    def draw(self):
        pygame.draw.rect(window, 'green', self.rect)
        pygame.draw.rect(window, 'gray20', self.rect, 2)

    def damage(self, value):
        self.hp -= value
        if self.hp <= 0: objects.remove(self)

bullets = []


objects = [] #тут храним все объекты, которые используем в игре
Facker('blue', 100, 275, 0, (pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s, pygame.K_SPACE))
Botan('red', 650, 275, 0, (pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN, pygame.K_RSHIFT))
ui = UI()

for _ in range(50): #расставляем блоки на поле рандомным образом
    while True:
        #расстановка блоков без пересечений ровно по сетке
        x = randint(0, WIDTH // TILE - 1) * TILE
        y = randint(1, HEIGHT // TILE - 1) * TILE
        rect = pygame.Rect(x, y, TILE, TILE)
        fined = False
        for obj in objects: #отсутствие наслаивания
            if rect.colliderect(obj.rect): fined = True

        if not fined: break

    Block(x, y, TILE)

play = True
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False

    keys = pygame.key.get_pressed()
    for bullet in bullets: bullet.update()
    for obj in objects: obj.update()
    ui.update()

    window.fill('black') #закрашиваем фон в черный
    for obj in objects: obj.draw()
    for bullet in bullets: bullet.draw()
    ui.draw()

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()