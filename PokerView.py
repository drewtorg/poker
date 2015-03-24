import pygame
import os,sys
import PokerModel

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
		self.poker = PokerModel.Poker()
		deck = PokerModel.Deck()
		self.images = {}
		self.scale = .75
		self.resolution = (WIDTH / 7, WIDTH / 5)


		font = pygame.font.Font(None, 50)
		loadText = font.render("Loading...", 1, WHITE)
		loadSize = font.size("Loading...")
		loadLoc = (WIDTH/2 - loadSize[0]/2, HEIGHT/2 - loadSize[1]/2)


		SCREEN.fill(GREY)

		SCREEN.blit(loadText, loadLoc)

		pygame.display.flip()

		for card in deck:
			self.images[str(card)] = pygame.image.load(card.image_path).convert_alpha()
			self.images[str(card)] = pygame.transform.scale(self.images[str(card)], (int(self.scale * self.resolution[0]), int(self.scale * self.resolution[1])))
			print str(card) + " loaded"

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
		self.cardLoc = {}
		self.round = 0

		#setup the locations for each card in the hand
		x = 2 * int(self.scale * self.resolution[0])
		self.youLoc = (x - 150,50)

		for index in range(len(self.poker.playerHand)):
			print self.poker.playerHand[index]
			self.cardLoc[index] = (x,0)
			x += int(self. scale * self.resolution[0])
			self.buttonLoc = (x + 30,50)

		#setup the text that will be printed to the screen
		self.font = pygame.font.Font(None, 30)
		self.font2 = pygame.font.Font(None, 60)
		self.youText = self.font.render("Your Hand", 1, WHITE)

		self.replaceButton = self.font2.render("Replace", 1, BLACK)
		self.buttonSize =self.font2.size("Replace")

		self.buttonRect = pygame.Rect(self.buttonLoc, self.buttonSize)
		self.buttonRectOutline = pygame.Rect(self.buttonLoc, self.buttonSize)

	def play(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit();sys.exit()

			#when the user clicks on a card, change its color to signify a selection has occurred
			elif event.type == pygame.MOUSEBUTTONDOWN:
				if event.button == 1:
					#create a rectangle for the mouse click and for each card.  check for intersection
					mouseRect = pygame.Rect(event.pos, (1,1))
					for index in range(len(self.poker.playerHand)):									#this minus thirty fixes a minor bug, do not remove
						cardRect = pygame.Rect(self.cardLoc[index], (self.resolution[0] - 30, self.resolution[1]))
						if cardRect.colliderect(mouseRect):
							self.poker.playerHand[index].selected = not self.poker.playerHand[index].selected
							break

					#check if we clicked the replaceButton
					if mouseRect.colliderect(self.buttonRect):
						self.poker.replace(self.poker.playerHand)
						self.round += 1
						#if self.round == 2:
						#	self.state += 1

						
		SCREEN.fill(GREY)

		#display the player's hand
		for index in range(len(self.poker.playerHand)):
			if not self.poker.playerHand[index].selected:
				SCREEN.blit(self.images[str(self.poker.playerHand[index])], self.cardLoc[index])
			else:
				SCREEN.blit(self.images[str(self.poker.playerHand[index])], self.cardLoc[index], None, pygame.BLEND_SUB)

		#display the text

		SCREEN.blit(self.youText, self.youLoc)
		pygame.draw.rect(SCREEN, RED, self.buttonRect)
		pygame.draw.rect(SCREEN, BLACK, self.buttonRectOutline, 2)
		SCREEN.blit(self.replaceButton, self.buttonLoc)

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