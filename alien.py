import pygame
from pygame.sprite import Sprite
from settings import Settings
# Adding constructive comments for better understanding setting = Settings()
class Alien(Sprite):
	def __init__(self,screen,setting):
		super().__init__()
		self.direction = 1
		self.setting = setting
		self.screen = screen
		self.image = pygame.image.load('spaceship.png')
		self.screen_rectangle = screen.get_rect()
		self.Alien_rectangle = self.image.get_rect()
		self.Alien_rectangle.x = self.Alien_rectangle.width
		self.Alien_rectangle.y = 0
		self.x = float(self.Alien_rectangle.x)
		self.y = float(self.Alien_rectangle.y)
		#only for sprite
		self.rect = self.Alien_rectangle
	def draw(self):
		self.screen.blit(self.image, self.Alien_rectangle)
	def update(self,aliens):
		self.x += self.setting.alien_speed_factor * self.direction * self.setting.rowDirection
		self.Alien_rectangle.x = self.x
	def check_edges(self):
		"""Return True if alien is at edge of screen."""
		if self.Alien_rectangle.right >= self.screen_rectangle.right:
			return True
		elif self.Alien_rectangle.left <= 0:
                        return True
		else:
			return False
