# DUH
import pygame;
# we need sys, to halt the program
import sys;
# import our settings from teh settings module
from settings import Settings;
# Get our hero class
from hero import Hero;

# initialize all of the pygame modules
pygame.init();
# screen_size = (1000,800);
# make a background color ... the color grass
# bg_color = (82,111,53)
# Put a message on the status bar so the player knows the name of the game
pygame.display.set_caption("Monster Attack!");
# Create an object out of our Settings class
game_settings = Settings();
screen = pygame.display.set_mode(game_settings.screen_size);
hero = Hero(screen, game_settings);


# This loop will run forever...
while 1:
	for event in pygame.event.get():
		# this means the user clicked on the red x
		if event.type == pygame.QUIT:
			# Stop the game, the user wants off
			sys.exit();
		# check for key press
		elif event.type == pygame.KEYDOWN:
			# print event.key;
			# User pressed a key AND it's the right arrwo
			if event.key == pygame.K_RIGHT:
				print "Pressed right";
				# Set the hero boolean for right to true
				hero.moving_right = True;
			elif event.key == pygame.K_LEFT:
				print "Pressed left";
				hero.moving_left = True;
			elif event.key == pygame.K_UP:
				print "Pressed up";
				hero.moving_up = True;
			elif event.key == pygame.K_DOWN:
				print "Pressed down";
				hero.moving_down = True;
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_RIGHT:
				print "Pressed right";
				# Set the hero boolean for right to true
				hero.moving_right = False;
			elif event.key == pygame.K_LEFT:
				print "Pressed left";
				hero.moving_left = False;
			elif event.key == pygame.K_UP:
				print "Pressed up";
				hero.moving_up = False;
			elif event.key == pygame.K_DOWN:
				print "Pressed down";
				hero.moving_down = False;				

	# put our bg_color as teh fill of our game
	screen.fill(game_settings.bg_color);
	# Update the hero moving booleans
	hero.update_me();
	# Draw the hero
	hero.draw_me();
	# flip the screen = wipe it out
	pygame.display.flip();
