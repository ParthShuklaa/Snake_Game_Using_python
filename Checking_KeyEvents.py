import  pygame
x=pygame.init()
#print(x)
#Creating Window
gameWindow=pygame.display.set_mode((600,600))
pygame.display.set_caption("My First Game")
# Game specific Variable
exit_game=False
game_over=False
#Creating Game loop
while not exit_game:
	for event in pygame.event.get():
		#print(event)
		if event.type==pygame.QUIT:
			exit_game=True
		if event.type==pygame.KEYDOWN:
			if event.key==pygame.K_RIGHT:
				print("You Have Pressed Right Arrow Key")

			if event.key==pygame.K_LEFT:
				print("You Have Pressed Left Arrow Key")

			
pygame.quit()
quit()
