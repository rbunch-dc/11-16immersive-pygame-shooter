# A file for all our game functions to clean up main.py
import pygame;
# we need sys, to halt the program
import sys;

def check_events(hero):
	for event in pygame.event.get():
		# this means the user clicked on the red x
		if event.type == pygame.QUIT:
			# Stop the game, the user wants off
			sys.exit();

		elif event.type == pygame.MOUSEBUTTONDOWN:
			

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
