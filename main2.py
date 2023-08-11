import random
import pygame

BLOCK_WIDTH = 30
BLOCK_HEIGTH = 15
CELL_SIZE = 30
SCREEN_WIDTH = BLOCK_WIDTH * CELL_SIZE
SCREEN_HEIGTH = BLOCK_HEIGTH * CELL_SIZE
SCREEN = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGTH))
RUNNING = True
FPS = 30

pygame.init()

clock = pygame.time.Clock()
grid = []

for y in range(BLOCK_HEIGTH+1):
    for x in range(BLOCK_WIDTH):
        grid.append((x,y))

# random.shuffle(grid)
sets = [{cell} for cell in grid]

def find_set(cell):
    for s in sets:
        if cell in s:
            return s

def merge_sets(set1,set2):
    sets.remove(set1)
    sets.remove(set2)
    merged_set = set1.union(set2)
    sets.append(merged_set)

def draw_grid():
    for cell in grid:
        x,y = cell
        pygame.draw.rect(SCREEN,(0,0,0), (x*CELL_SIZE,y*CELL_SIZE,CELL_SIZE,CELL_SIZE),1)

def draw_horizontal_wall(cell):
    x,y = cell
    pygame.draw.line(SCREEN,random_color(),(x*CELL_SIZE,y*CELL_SIZE+CELL_SIZE),((x+1)*CELL_SIZE,y*CELL_SIZE+CELL_SIZE),6)

def draw_vertical_wall(cell):
    x,y = cell
    pygame.draw.line(SCREEN, random_color(),(x*CELL_SIZE+CELL_SIZE,y*CELL_SIZE),(x*CELL_SIZE+CELL_SIZE,(y+1)*CELL_SIZE),6)

def random_color():
    red = random.randint(0,255)
    green = random.randint(0,255)
    blue = random.randint(0,255)
    return (red,green,blue)

SCREEN.fill((0,0,0))
draw_grid()
while RUNNING:
    edges = []
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False

    for cell in grid:
        x,y = cell
        if x < BLOCK_WIDTH -1:
            edges.append(((x,y), (x+1,y)))
        if y < BLOCK_HEIGTH:
            edges.append(((x,y), (x,y+1)))

    random.shuffle(edges)

    for edge in edges:
        cell1,cell2 = edge
        # print(f"cell1: {cell1}\ncell2:{cell2}")
        set1 = find_set(cell1)
        set2=find_set(cell2)
        # if set1 != set2 and set1 is not None and set2 is not None:
        if set1 != set2:
            merge_sets(set1,set2)
            x1,y1 = cell1
            x2,y2 = cell2
            if x1 == x2:
                draw_horizontal_wall(cell1)
            elif y1 == y2:
                draw_vertical_wall(cell1)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()