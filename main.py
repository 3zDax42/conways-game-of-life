import pygame
import random

pygame.init()
Game_Screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Game of Life")
Clock = pygame.time.Clock()
Game_On = True


Map = []
for i in range(100):
    Map.append([i%2 for i in range(100)])

def Update_Grid(Matrix):
    OutMatrix = Matrix[::]
    for i in range(100):
        for j in range(100):
            Counter = 0
            if i < 99 and Matrix[i+1][j]:
                Counter += 1
            if i > 0 and Matrix[i-1][j]:
                Counter += 1
            if j < 99 and Matrix[i][j+1]:
                Counter += 1
            if j > 0 and Matrix[i][j-1]:
                Counter += 1
            if i < 99 and j < 99 and Matrix[i+1][j+1]:
                Counter += 1
            if i > 0 and j < 99 and Matrix[i-1][j+1]:
                Counter += 1
            if i < 99 and j > 0 and Matrix[i+1][j-1]:
                Counter += 1
            if i > 0 and j > 0 and Matrix[i-1][j-1]:
                Counter += 1
            if Matrix[i][j] == 1 and Counter <= 1:
                OutMatrix[i][j] = 0
            if Matrix[i][j] == 1 and Counter >= 4:
                OutMatrix[i][j] = 0
            if Matrix[i][j] == 0 and Counter == 3:
                OutMatrix[i][j] = 1
    return OutMatrix

while Game_On:
    Clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Game_On = False
    
    Map = Update_Grid(Map)

    Game_Screen.fill((0, 0, 0))
    for i in range(100):
        for j in range(100):
            if Map[i][j]==0:
                pygame.draw.rect(Game_Screen, (50, 50, 50), (j*5, i*5, 5, 5))
            if Map[i][j]==1:
                pygame.draw.rect(Game_Screen, (200, 20, 200), (j*5, i*5, 5, 5))


    pygame.display.flip()
pygame.quit()
