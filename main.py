# DUH
import pygame;
# we need sys, to halt the program
# import sys;
# import our settings from teh settings module
from settings import Settings;
# Get our hero class
from hero import Hero;
# Get the check_events function from game_functions module
from game_functions import check_events
# From pygame, get the sprite stuff and groupcollide to handle collision
from pygame.sprite import Group, groupcollide
# get our enemy class
from enemy import Enemy;


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

enemies = Group();
enemies.add(Enemy(screen,game_settings));

# This loop will run forever...
while 1:

	# run our check_events here!
	check_events(hero)

	# put our bg_color as teh fill of our game
	screen.fill(game_settings.bg_color);
	# Update the hero moving booleans
	hero.update_me();
	# Draw the hero
	hero.draw_me();

	for enemy in enemies.sprites():
		enemy.update_me(hero);
		enemy.draw_me();


	# flip the screen = wipe it out
	pygame.display.flip();
