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
screen_caption="Snake Game"
gameWindow=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption(screen_caption)
pygame.display.update()
# Game specific Variable
exit_game=False
game_over=False
Snake_x=45
Snake_y=55
Snake_size=10
fps=30 #means frame per secound
clock=pygame.time.Clock()
#Creating Game loop
while not exit_game:
	for event in pygame.event.get():
		print(event)
		if event.type==pygame.QUIT:
			exit_game=True
		if event.type==pygame.KEYDOWN:
			if event.key==pygame.K_RIGHT:
				Snake_x=Snake_x+10
			if event.key==pygame.K_LEFT:
				Snake_x=Snake_x-10
			if event.key==pygame.K_UP:
				Snake_y=Snake_y-10
			if event.key==pygame.K_DOWN:
				Snake_y=Snake_y+10
			
		gameWindow.fill(white)
		pygame.draw.rect(gameWindow,black,[Snake_x,Snake_y,Snake_size,Snake_size])
		pygame.display.update()
		clock.tick(fps)

pygame.quit()
quit()
