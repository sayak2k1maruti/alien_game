import pygame
from settings import Settings
settings = Settings()
class Ship():
	def __init__(self,screen):
		self.screen = screen
		self.image =  pygame.image.load('ship.png')
		self.ship_rectangle = self.image.get_rect()
		self.screen_rectangle = screen.get_rect()
		#centersixe along x axix
		self.ship_rectangle.centerx = self.screen_rectangle.centerx
		#place to the bottom
		self.ship_rectangle.bottom = self.screen_rectangle.bottom
		#move flag
		self.moving_right = False
		self.moving_left = False
		self.shipSpeedFactor = settings.shipSpeedFactor
		self.rect = self.ship_rectangle
	def draw(self):
		self.screen.blit(self.image, self.ship_rectangle)
	def center_ship(self):
		self.ship_rectangle.centerx = self.screen_rectangle.centerx