import pygame
import sys
from settings import Settings
from ship import Ship
from alien import Alien
import game
from pygame.sprite import Group
from stats import Stats
from button import Button
from scoreboard import Scoreboard
bullets = Group()
aliens = Group()
def runGame():
	# Initialize game and create a screen object.
	pygame.init()
	setting = Settings()
	stats = Stats(setting)
	screen = pygame.display.set_mode((setting.width,setting.height))
	sb = Scoreboard(setting,screen,stats)
	p_button = Button(setting,screen,"Play")
	ship = Ship(screen)
	pygame.display.set_caption("Alien")
	game.createAlienRow(screen,setting,aliens)
	while True:
		game.check_events(ship,setting,screen,bullets,stats,p_button)
		game.updateScreen(setting,screen,ship,bullets,aliens,stats,p_button,sb)
		bullets.update()
		#pygame.time.wait(5)
runGame()
