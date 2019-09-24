import  pygame
x=pygame.init()
#print(x)
#Creating Window
gameWindow=pygame.display.set_mode((1200,600))
pygame.display.set_caption("My First Game...")
# Game specific Variable
exit_game=False
game_over=False
#Creating Game loop
while not exit_game:
	for event in pygame.event.get():
		print(event)
pygame.quit()
quit()
