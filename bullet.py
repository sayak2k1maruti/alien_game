import pygame
from pygame.sprite import Sprite
#class Bullet(Sprite):
class Bullet(Sprite):
	def __init__(self,setting,screen,ship):
		super().__init__()
		self.screen = screen
		self.setting = setting
		self.ship = ship
		self.Bullet_rectangle = pygame.Rect(0,0,setting.bulletWidth,setting.bulletHeight)
		self.Bullet_rectangle.top = ship.ship_rectangle.top
		#self.Bullet_rectangle.centerx = ship.ship_rectangle.centerx
		self.Bullet_rectangle.centerx = ship.ship_rectangle.centerx
		#self.Bullet_rectangle.y = 0
		self.y = float(self.Bullet_rectangle.y)
		self.color = setting.bulletColor
		self.BulletSpeedFactor = setting.bulletSpeedFactor
		#only for sprite
		self.rect = self.Bullet_rectangle
	def update(self):
		#self.y -= self.BulletSpeedFactor
		self.Bullet_rectangle.y -= 1
	def draw(self):
		pygame.draw.rect(self.screen,self.color,self.Bullet_rectangle)