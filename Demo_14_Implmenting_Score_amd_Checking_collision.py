import  pygame
import random
x=pygame.init()
pygame.font.init()
#Colors
white=(255,255,255)
red=(255,0,0)
black=(0,0,0)
#print(x)
#Creating Window
speed=5
screen_width=600
screen_height=300
screen_caption="Snake Game"
food_x=random.randint(0,screen_width/2)
food_y=random.randint(0,screen_height/2)
gameWindow=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption(screen_caption)
pygame.display.update()
# Game specific Variable
exit_game=False
game_over=False
score=0
Snake_x=45
Snake_y=55
Snake_size=20
velocity_x=0
velocity_y=0
fps=30 #means frame per secound
clock=pygame.time.Clock()
#rendering font from pygame
font=pygame.font.SysFont(None,55)
def text_screen(text,color,x,y):
	screen_text=font.render(text,True,color)
	gameWindow.blit(screen_text,[x,y])
	pass
#Creating Game loop

while not exit_game:
	for event in pygame.event.get():
		#print(event)
		if event.type==pygame.QUIT:
			exit_game=True
		if event.type==pygame.KEYDOWN:
			if event.key==pygame.K_RIGHT:
				velocity_x=speed
				velocity_y=0
			if event.key==pygame.K_LEFT:
				velocity_x=-speed
				velocity_y=0
			if event.key==pygame.K_UP:
				velocity_y=-speed
				velocity_x=0
			if event.key==pygame.K_DOWN:
				velocity_y=speed
				velocity_x=0
	Snake_x +=velocity_x
	Snake_y +=velocity_y	
	if abs(food_x - Snake_x)<10 and abs(food_y - Snake_y)<10:
		score=score+10
		print("score=",score)
		
		food_x=random.randint(0,screen_width/2)
		food_y=random.randint(0,screen_height/2)
	gameWindow.fill(white)
	text_screen("Score: "+ str(score),red,5,5)
	pygame.draw.rect(gameWindow,black,[Snake_x,Snake_y,Snake_size,Snake_size])
	pygame.draw.rect(gameWindow,red,[food_x,food_y,Snake_size,Snake_size])
	
	pygame.display.update()
	clock.tick(fps)

pygame.quit()
quit()
