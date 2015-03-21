import pygame
import os,sys
import PokerModel

poker = PokerModel.Poker()
#poker.test()

HEIGHT = 480
WIDTH = 640

#Global constants here
WHITE = (255,255,255)
BLACK = (0,0,0)
GREY  = (50,50,50)
RED  = (255,50,50)

class Control:
	def __init__(self):
		self.start_up_init()

	def main(self):
		if self.state == 0:
			self.start_up()
		elif self.state == 1:
			self.play()
		elif self.state == 2:
			self.results()
		elif self.state == 3:
			self.new_game()

		return
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit();sys.exit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_a:
					self.keydownA = True
				if event.key == pygame.K_d:
					self.keydownD = True
				if event.key == pygame.K_w:
					self.keydownW = True
				if event.key == pygame.K_s:
					self.keydownS = True


			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RETURN:
					self.state += 1

			elif event.type == pygame.KEYUP:
				if event.key == pygame.K_a:
					self.keydownA = False
				if event.key == pygame.K_d:
					self.keydownD = False
				if event.key == pygame.K_w:
					self.keydownW = False
				if event.key == pygame.K_s:
					self.keydownS = False

			elif event.type == pygame.MOUSEBUTTONDOWN:
				if event.button == 1:
					print "Left click"

	def start_up_init(self):
		#intitialize items for the startup section of the game
		self.font = pygame.font.Font(None,50)

		self.startText = self.font.render("Welcome to Poker!", 1, WHITE)
		self.startSize = self.font.size("Welcome to Poker!")
		self.startLoc = (WIDTH/2 - self.startSize[0]/2, 0)

		self.startButton = self.font.render("Start", 1, BLACK)
		self.buttonSize =self.font.size("Start")
		self.buttonLoc = (WIDTH/2 - self.buttonSize[0]/2, HEIGHT/2 - self.buttonSize[1]/2)

		self.buttonRect = pygame.Rect(self.buttonLoc, self.buttonSize)
		self.buttonRectOutline = pygame.Rect(self.buttonLoc, self.buttonSize)

		self.state = 0

	def start_up(self):

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit();sys.exit()

			#when the user clicks the start button, change to the playing state
			elif event.type == pygame.MOUSEBUTTONDOWN:
				if event.button == 1:
					mouseRect = pygame.Rect(event.pos, (1,1))
					if mouseRect.colliderect(self.buttonRect):
						self.state += 1
						self.play_init()
						return

		#draw images
		SCREEN.fill(GREY)

		#draw welcome text
		SCREEN.blit(self.startText, self.startLoc)

		#draw the start button
		pygame.draw.rect(SCREEN, RED, self.buttonRect)
		pygame.draw.rect(SCREEN, BLACK, self.buttonRectOutline, 2)
		SCREEN.blit(self.startButton, self.buttonLoc)

		pygame.display.flip()

	def play_init(self):
		print "play_init"

		#clean up the variables from the old state
		del self.font

		del self.startText
		del self.startSize
		del self.startLoc

		del self.startButton
		del self.buttonSize
		del self.buttonLoc

		del self.buttonRect
		del self.buttonRectOutline

		#create the new variables

	def play(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit();sys.exit()

			elif event.type == pygame.MOUSEBUTTONDOWN:
				if event.button == 1:
					mouseRect = pygame.Rect(event.pos, (1,1))
					print "Left click"

		SCREEN.fill(GREY)
		pygame.display.flip()


	def results(self):
		print "results"

	def new_game(self):
		print "new_game"


#############################################################
if __name__ == "__main__":
	os.environ['SDL_VIDEO_CENTERED'] = '1' #center screen
	pygame.init()
	pygame.display.set_caption("My Collision Detector")
	SCREEN = pygame.display.set_mode((WIDTH, HEIGHT), 0 ,32)
	
	Runit = Control()
	Myclock = pygame.time.Clock()
	while 1:
		Runit.main()
		Myclock.tick(64)