import  pygame
import random
x=pygame.init()
#Colors
white=(255,255,255)
red=(255,0,0)
black=(0,0,0)
#print(x)
#Creating Window
speed=5
screen_width=1200
screen_height=600
screen_caption="Snake Game"
gameWindow=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption(screen_caption)
pygame.display.update()
clock=pygame.time.Clock()
font=pygame.font.SysFont(None,55)
def text_screen(text,color,x,y):
	screen_text=font.render(text,True,color)
	gameWindow.blit(screen_text,[x,y])
#Creating Game loop
def plot_snake(gameWindow,black1,snk_list,Snake_size1):
	for x,y in snk_list:
		pygame.draw.rect(gameWindow,black1,[x,y,Snake_size1,Snake_size1])

def gameloop():
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
	food_x=random.randint(0,screen_width/2)
	food_y=random.randint(0,screen_height/2)

	snk_length=1
	snk_list=[]
	with open("highscore.txt","r") as f:
		highscore=f.read()

	while not exit_game:
		if game_over:

			with open("highscore.txt","w") as f:
				f.write(str(highscore))
			gameWindow.fill(white)
			
			text_screen("Game Over! Press Enter To Continue ",red,100,200)
			for event in pygame.event.get():
				#print(event)
				if event.type==pygame.QUIT:
					exit_game=True
				if event.type==pygame.KEYDOWN:
					if event.key==pygame.K_RETURN:
						gameloop()
				
		else:

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
					if event.key==pygame.K_q:
						score +=10
						
			Snake_x +=velocity_x
			Snake_y +=velocity_y	
			if abs(food_x - Snake_x)<10 and abs(food_y - Snake_y)<10:
				score=score+10
				#print("score=",score)
				
				food_x=random.randint(0,screen_width/2)
				food_y=random.randint(0,screen_height/2)
				snk_length +=5
				if score>int(highscore):
					highscore=score
			gameWindow.fill(white)
			text_screen("Score: "+ str(score) +"  High Score:"+ str(highscore),red,5,5)
			pygame.draw.rect(gameWindow,red,[food_x,food_y,Snake_size,Snake_size])
			
			head=[]
			head.append(Snake_x)
			head.append(Snake_y)
			snk_list.append(head)
			#print(snk_list)
			if len(snk_list)>snk_length:
				del snk_list[0]
			
			if head in snk_list[ :-1]:
				game_over=True
			#pygame.draw.rect(gameWindow,black,[Snake_x,Snake_y,Snake_size,Snake_size])
			if (Snake_x<0) or (Snake_y<0) or (Snake_x>screen_width) or (Snake_y>screen_height):
				game_over=True		
			plot_snake(gameWindow,black,snk_list,Snake_size)
		pygame.display.update()
		clock.tick(fps)

	pygame.quit()
	quit()
gameloop()