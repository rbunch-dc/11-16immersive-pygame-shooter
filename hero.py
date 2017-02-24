# Duh
import pygame;
# this will get the Sprite class from pygame.sprite. Our hero will be a sprite object
from pygame.sprite import Sprite;

class Hero(Sprite):
	# initialize class properties
	def __init__(self, screen, settings):
		super(Hero,self).__init__();
		self.image = pygame.image.load('hero.png');
		# self.image = pygame.transform.scale(self.image,(1000,200))
		# Now that we have the screen, let's give it to our dude
		self.screen = screen;
		# create a rect prop that will be the dimensions and location of the image
		# its available in get_rect because this is a pygame iamge
		self.rect = self.image.get_rect();
		# Now that we have the screen object from main, get the size of the screen
		self.screen_rect = screen.get_rect();
		print self.screen_rect;
		# this will put the middle of the hero at the middle of the screen
		self.rect.centery = self.screen_rect.centery;
		# this will put the left side of our hero at the left side of our screen
		self.rect.left = self.screen_rect.left;
		# Set up the movement booleans. All are false at init
		self.moving_right = False;
		self.moving_left = False;
		self.moving_up = False;
		self.moving_down = False;
		self.speed = settings.hero_speed;

	def update_me(self):
		# if user is pushing left, move my self.rect left
		# and so on...
		if self.moving_right:
			# The hero moving_right boolean is true, so update the hero loc
			self.rect.centerx += 10 * self.speed;
		elif self.moving_left:
			self.rect.centerx -= 10 * self.speed;

		if self.moving_down:
			# The hero moving_right boolean is true, so update the hero loc
			self.rect.centery += 10 * self.speed;
		elif self.moving_up:
			self.rect.centery -= 10 * self.speed;

	def draw_me(self):
		self.screen.blit(source = self.image, dest = self.rect);
