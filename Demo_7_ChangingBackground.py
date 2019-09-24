import  pygame
x=pygame.init()
#Colors
white=(255,255,255)
red=(255,0,0)
black=(0,0,0)
#print(x)
#Creating Window
screen_width=600
screen_height=300
screen_caption="My First Snake Game"
gameWindow=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption(screen_caption)
pygame.display.update()
#gameWindow.fill(red)
# Game specific Variable
exit_game=False
game_over=False
#Creating Game loop
while not exit_game:
	for event in pygame.event.get():
		print(event)
		if event.type==pygame.QUIT:
			exit_game=True
		gameWindow.fill(white)
		pygame.display.update()
#gameWindow.fill(red)
#pygame.display.update()
pygame.quit()
quit()
