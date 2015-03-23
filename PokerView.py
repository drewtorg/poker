import pygame
import os,sys
import PokerModel

poker = PokerModel.Poker()
poker.test()

HEIGHT = 600
WIDTH = 800

#Global constants here
WHITE = (255,255,255)
BLACK = (0,0,0)
GREY  = (50,50,50)
RED  = (255,50,50)

class Control:
	def __init__(self):
		self.start_up_init()
		self.deck = PokerModel.Deck()
		self.images = {}
		self.scale = .75
		self.resolution = (WIDTH / 7, WIDTH / 5)

		for card in self.deck.deck:
			self.images[str(card.rank) + card.suit] = pygame.image.load(card.image_path).convert_alpha()
			self.images[str(card.rank) + card.suit] = pygame.transform.scale(self.images[str(card.rank) + card.suit], (int(self.scale * self.resolution[0]), int(self.scale * self.resolution[1])))
			print card.image_path + " loaded"

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
		self.font = pygame.font.Font(None,150)
		self.font2 = pygame.font.Font(None, 75)

		self.startText = self.font2.render("Welcome to Poker!", 1, WHITE)
		self.startSize = self.font2.size("Welcome to Poker!")
		self.startLoc = (WIDTH/2 - self.startSize[0]/2, 50)

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
		del self.font2

		del self.startText
		del self.startSize
		del self.startLoc

		del self.startButton
		del self.buttonSize
		del self.buttonLoc

		del self.buttonRect
		del self.buttonRectOutline

		#create the new variables
		self.hand = PokerModel.Hand(self.deck.deal(5))
		self.cardLoc = {}

		#setup the locations for each card in the hand
		x = 2 * int(self.scale * self.resolution[0])
		for card in self.hand:
			print card
			self.cardLoc[str(card.rank)+card.suit] = (x,0)
			x += int(self. scale * self.resolution[0])

	def play(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit();sys.exit()

			#when the user clicks on a card, change its color to signify a selection has occurred
			elif event.type == pygame.MOUSEBUTTONDOWN:
				if event.button == 1:
					#create a rectangle for the mouse click and for each card.  check for intersection
					mouseRect = pygame.Rect(event.pos, (1,1))
					for card in self.hand:										#this minus thirty fixes a minor bug, do not remove
						cardRect = pygame.Rect(self.cardLoc[str(card.rank)+card.suit], (self.resolution[0] - 30, self.resolution[1]))
						if cardRect.colliderect(mouseRect):
							card.selected = not card.selected
						
		SCREEN.fill(GREY)

		#display the player's hand
		for card in self.hand:
			if not card.selected:
				SCREEN.blit(self.images[str(card.rank)+card.suit], self.cardLoc[str(card.rank)+card.suit])
			else:
				SCREEN.blit(self.images[str(card.rank)+card.suit], self.cardLoc[str(card.rank)+card.suit], None, pygame.BLEND_SUB)

		pygame.display.flip()


	def results(self):
		print "results"

	def new_game(self):
		print "new_game"


#############################################################
if __name__ == "__main__":
	os.environ['SDL_VIDEO_CENTERED'] = '1' #center screen
	pygame.init()
	pygame.display.set_caption("Poker")
	SCREEN = pygame.display.set_mode((WIDTH, HEIGHT), 0 ,32)
	
	Runit = Control()
	Myclock = pygame.time.Clock()
	while 1:
		Runit.main()
		Myclock.tick(64)