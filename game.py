import pygame
import sys
from bullet import Bullet
from alien import Alien
from time import sleep
def keyDownEvents(event,ship,setting,screen,bullets):
	if event.key == pygame.K_RIGHT:
		ship.moving_right = True
	elif event.key == pygame.K_LEFT:
		ship.moving_left = True
	elif event.key == pygame.K_SPACE:
		newBullet = Bullet(setting,screen,ship)
		bullets.add(newBullet)
def keyUpEvents(event,ship):
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
	if event.key == pygame.K_LEFT:
		ship.moving_left = False
def check_play_button(stats, p_button, mouse_x, mouse_y):
	if p_button.rect.collidepoint(mouse_x, mouse_y):
		stats.reset()
		pygame.mouse.set_visible(False)
		stats.gameActive = True
def check_events(ship,setting,screen,bullets,stats,p_button):
	#respond to key press
	for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				keyDownEvents(event,ship,setting,screen,bullets)
			elif event.type == pygame.KEYUP:
				keyUpEvents(event,ship)
			elif  event.type == pygame.MOUSEBUTTONDOWN:
				mouse_x, mouse_y = pygame.mouse.get_pos()
				check_play_button(stats, p_button, mouse_x, mouse_y)
def createAlienRow(screen,setting,aliens):
	#add a row of aliens
	alien = Alien(screen,setting)
	alienWidth = alien.Alien_rectangle.width
	alienHeight = alien.Alien_rectangle.height
	spaceX = setting.width - 2 * alienWidth #availabe space for alien in a row
	spaceY = setting.height -  alienHeight#availabe space for alien in a column
	numberX = int(spaceX/(alienWidth*2))#number of max alien in a row
	numberY = int(spaceY/(alienHeight*2))#number of max alien
	direction = 1
	for j in range(numberY):
		for i in range(numberX):
			# Create an alien and place it in the row.
			alien = Alien(screen,setting)
			alien.x = alienWidth + 2 * alienWidth * i
			alien.y = alienHeight * j * 1.5 + 50
			alien.Alien_rectangle.x = alien.x
			alien.Alien_rectangle.y = alien.y
			alien.direction = direction
			aliens.add(alien)
		direction *= -1
def checkRowEdges(setting,aliens):
	for alien in aliens.sprites():
		if alien.check_edges():
			for alien in aliens.sprites():
				alien.Alien_rectangle.y += setting.dropSpeed
			setting.rowDirection *= -1
			break
def collitionCheck(bullets,aliens,stats):
	collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
	if collisions:
		stats.score += 10
def shipHit(screen,setting,aliens,ship,bullets,stats):
	if stats.ship_left <= 1:
		aliens.empty()
		bullets.empty()
		createAlienRow(screen,setting,aliens)
		ship.center_ship()
		stats.gameActive = False
		return False
	stats.ship_left -= 1
	aliens.empty()
	bullets.empty()
	createAlienRow(screen,setting,aliens)
	ship.center_ship()
	sleep(1)#pause
def updateScreen(setting,screen,ship,bullets,aliens,stats,p_button,sb):
	screen.fill(setting.bgColor)
	ship.draw()
	aliens.draw(screen)
	sb.show_score()
	#python will draw all alien in alien group
	if stats.gameActive:
		collitionCheck(bullets,aliens,stats)
		checkRowEdges(setting,aliens)
		aliens.update(aliens)
		for alien in aliens.sprites():
			alien.draw()
			if alien.Alien_rectangle.bottom >  screen.get_rect().bottom:
				shipHit(screen,setting,aliens,ship,bullets,stats)
		######
		'''bullet_rectangle = pygame.Rect(0,0,5,5)
		bullet_rectangle.centerx = ship.ship_rectangle.centerx
		bullet_rectangle.bottom = 100
		pygame.draw.rect(screen, (230,230,230), bullet_rectangle,0)'''
		#newBullet = Bullet(setting,screen,ship)
		#newBullet.draw()
		for bullet in bullets.sprites():
			bullet.update()
			bullet.draw()
		#get rid of old bullets
		for bullet in bullets.copy():
			if bullet.Bullet_rectangle.bottom <= 0:
				bullets.remove(bullet)
		######
		centerx = float(ship.ship_rectangle.centerx)
		if ship.moving_right and ship.ship_rectangle.right < ship.screen_rectangle.right:
			centerx = float(ship.ship_rectangle.centerx) + float(ship.shipSpeedFactor)
		if ship.moving_left and ship.ship_rectangle.left > 0:
			centerx = float(ship.ship_rectangle.centerx) - float(ship.shipSpeedFactor)
		ship.ship_rectangle.centerx = float(centerx)
		if len(aliens) == 0:
			bullets.empty()
			createAlienRow(screen,setting,aliens)
			#detect collide
		if pygame.sprite.spritecollideany(ship, aliens):
			shipHit(screen,setting,aliens,ship,bullets,stats)
	else:
		p_button.draw_button()
		pygame.mouse.set_visible(True)
	pygame.display.flip()