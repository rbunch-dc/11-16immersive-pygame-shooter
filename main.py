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
# Get the start button
from button import Start_Button;


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

# Make a group for the hero to belong to so we can use groupcollide
hero_group = Group() 
hero = Hero(screen, game_settings);
# put the hero in the group
hero_group.add(hero)

enemies = Group();
enemies.add(Enemy(screen,game_settings));

# Make a start button
start_button = Start_Button(screen)
print start_button;

# This loop will run forever...
while 1:

	# run our check_events here!
	check_events(hero)

	# put our bg_color as teh fill of our game
	screen.fill(game_settings.bg_color);

	for hero in hero_group.sprites():
		hero.update_me();
		hero.draw_me()

	# Update the hero moving booleans
	# hero.update_me();
	# Draw the hero
	# hero.draw_me();


	for enemy in enemies.sprites():
		enemy.update_me(hero);
		enemy.draw_me();

	hero_died = groupcollide(hero_group, enemies, True, True);
	# print hero_died;
	if hero_died:
		print "You lost!";

	start_button.draw_button();

	# flip the screen = wipe it out
	pygame.display.flip();
