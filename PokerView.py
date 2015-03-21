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
		self.font = pygame.font.Font(None,50)
		self.startText = self.font.render("Welcome to Poker!", 1, WHITE)
		self.startButton = self.font.render("Start", 1, BLACK)
		self.buttonSize =self.font.size("Start")

		self.buttonRect = pygame.Rect((WIDTH/2, HEIGHT/2), self.buttonSize)
		self.buttonRectOutline = pygame.Rect((WIDTH / 2, HEIGHT/2 ), self.buttonSize)

		self.state = 0

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

	def start_up(self):

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit();sys.exit()
			elif event.type == pygame.MOUSEBUTTONDOWN:
				if event.button == 1:
					mouseRect = pygame.Rect(event.pos, (1,1))
					if mouseRect.colliderect(self.buttonRect):
						self.state += 1

		#draw images
		SCREEN.fill(GREY)

		SCREEN.blit(self.startText, (WIDTH/2, 0))
		pygame.draw.rect(SCREEN, RED, self.buttonRect)
		pygame.draw.rect(SCREEN, BLACK, self.buttonRectOutline, 2)
		SCREEN.blit(self.startButton, (WIDTH / 2, HEIGHT / 2))

		pygame.display.flip()

	def play(self):
		print "play"

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