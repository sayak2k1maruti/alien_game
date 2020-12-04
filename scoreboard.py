import pygame.font
class Scoreboard():
	def __init__(self,setting,screen,stats):
		self.screen = screen
		self.setting = setting
		self.stats = stats
		self.fontColor = (30,30,30)
		self.font = pygame.font.SysFont(None, 48)
		self.score = str(self.stats.score)
	def prep_score(self):
		self.score_image = self.font.render(self.score, True, self.fontColor,self.setting.bgColor)
		self.rect = self.score_image.get_rect()
		self.rect.right = self.screen.get_rect().right - 10
		self.rect.top = 10
	def show_score(self):
		self.score = str( "{:,}".format(self.stats.score))
		self.prep_score()
		self.screen.blit(self.score_image, self.rect)
