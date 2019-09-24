import  pygame
x=pygame.init()
print(x)
#Creating Window
gameWindow=pygame.display.set_mode((1000,600))
pygame.display.set_caption("My First Game")
# Game specific Variable
exit_game=False
game_over=False
