import pygame
class Button():
	def __init__(self,setting,screen,msg):
		self.screen = screen
		self.width = 100
		self.height = 50
		self.msg = msg
		self.button_color = (0, 255, 0)
		self.text_color = (0,0,255)
		self.font = pygame.font.SysFont(None, 48)
		self.rect = pygame.Rect(0, 0, self.width, self.height)
		self.rect.center = screen.get_rect().center
		self.prep_msg(msg)
	def prep_msg(self,msg):
		self.msg_image = self.font.render(msg, True, self.text_color,self.button_color)
		self.msg_image_rect = self.msg_image.get_rect()
		self.msg_image_rect.center = self.rect.center
	def draw_button(self):
	# Draw blank button and then draw message.
		self.screen.fill(self.button_color, self.rect)
		self.screen.blit(self.msg_image, self.msg_image_rect)