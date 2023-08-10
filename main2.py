import random
import pygame

width = 20
heigth = 15
cell_size = 40

pygame.init()
w = width * cell_size
h = heigth * cell_size
screen = pygame.display.set_mode((w,h))
clock = pygame.time.Clock()

grid = []

for y in range(heigth+1):
    for x in range(width):
        grid.append((x,y))

random.shuffle(grid)

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
        pygame.draw.rect(screen,(0,0,0), (x*cell_size,y*cell_size,cell_size,cell_size),1)

def draw_horizontal_wall(cell):
    print("horizontal wall")
    x,y = cell
    pygame.draw.line(screen,(0,0,0),(x*cell_size,y*cell_size+cell_size),((x+1)*cell_size,y*cell_size+cell_size),6)

def draw_vertical_wall(cell):
    print("draw vertical wall")
    x,y = cell
    pygame.draw.line(screen,(0,0,0),(x*cell_size+cell_size,y*cell_size),(x*cell_size+cell_size,(y+1)*cell_size),6)

running = True

screen.fill((255,255,255))
draw_grid()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    

    edges = []

    for cell in grid:
        x,y = cell
        
        if x < width -1:
            edges.append(((x,y), (x+1,y)))
        if y < heigth:
            edges.append(((x,y), (x,y+1)))

    random.shuffle(edges)

    for edge in edges:
        cell1,cell2 = edge
        # print(f"cell1: {cell1}\ncell2:{cell2}")
        set1 = find_set(cell1)
        set2=find_set(cell2)
        # print(f"set1:{set1}\nset2:{set2}")

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
    clock.tick(30)

pygame.quit()