import pygame
import random
import pprint

pygame.init()

WIDTH = 300
HEIGHT = 300

DISPLAY_SURFACE = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Labirynth")

FPS = 60

class Square():

    border_size = 3
    color = random_color()

    def __init__(self,x,y,width,surface,state):
        self.x = x
        self.y = y
        self.width = width
        self.surface = surface
        self.state = state
    
    def change_color(self):
        return(255,255,255)
    
    def random_color():
        red = random.randint(0,255)
        green = random.randint(0,255)
        blue = random.randint(0,255)
        return (red,green,blue)
    
    def getPosition(self):
        return (self.x,self.y)
    
    def draw(self):
        pygame.draw.rect(self.surface,random_color(), (self.x,self.y,self.width,self.width),self.border_size)

    def draw_start(self):
        pygame.draw.rect(self.surface,(255,0,0), (self.x,self.y,self.width,self.width),self.border_size)

    def draw_end(self):
        pygame.draw.rect(self.surface,(255,0,0), (self.x,self.y,self.width,self.width),self.border_size)

class Line():

    def __init__(self,start, end, width, surface):
        self.start = start
        self.end = end
        self.width = width
        self.surface = surface

    def draw(self):
        pygame.draw.line(self.surface, (255,255,255),self.start,self.end, self.width)

def solve(all_square, start, target):
    print(f"start at {start.x},{start.y}\nend at {target.x},{target.y}")
    start_line_x = 0
    start_line_y = 0
    end_line_x = 0
    end_line_y = 0

    tmp_x = start.x
    tmp_y = start.y
    start_lines_x = []
    end_lines_x = []

    start_lines_y = []
    end_lines_y = []
    if(start.x > target.x):
        while tmp_x> target.x:
            tmp_x-=30
            start_line_x = start.x
            start_line_y = start.y
            end_line_x = tmp_x
            end_line_y = start.y
            start_lines_x.append((start_line_x,start_line_y))
            end_lines_x.append((end_line_x,end_line_y))
            print(f"Line coordinate(({start_line_x},{start_line_y}),({end_line_x},{end_line_y}))")
            Line((start_line_x,start_line_y),(end_line_x,end_line_y),5,DISPLAY_SURFACE).draw()
    
    # if(start.x<target.x):
    #     tmp_x-=30
    #     start_line_x = start.x
    #     start_line_y = start.y
    #     end_line_x = tmp_x
    #     end_line_y = start.y
    #     start_lines_x.append((start_line_x,start_line_y))
    #     end_lines_x.append((end_line_x,end_line_y))
    #     print(f"Line coordinate(({start_line_x},{start_line_y}),({end_line_x},{end_line_y}))")
    #     Line((start_line_x,start_line_y),(end_line_x,end_line_y),5,DISPLAY_SURFACE).draw()

    if(start.y>target.y):
        while tmp_y > target.y:
                tmp_y-=30
                start
                Line(( end_line_x, end_line_y),( end_line_x, tmp_y ),5,DISPLAY_SURFACE).draw()
            
    if(start.y<target.y):
         while tmp_y > target.y:
                tmp_y+=30
                start
                Line(( end_line_x, end_line_y),( end_line_x, tmp_y ),5,DISPLAY_SURFACE).draw()
    #     for tmp_x in range(start.x%30,target.x%30):
    #         for square in all_square:


def split_screen(surface,width,height):
    square_size = 30
    all_square = [[]]
    points = []
    for square_line in range(width//square_size):
        for square_column in range(height//square_size):
            # all_square[square_line].append(pygame.Rect(square_column,square_line,square_size,square_size))
            # pygame.draw.rect(surface,random_color(),(square_column*square_size,square_line*square_size,square_size,square_size),8)
            state = random.randrange(-1,2)
            square = Square(square_column*square_size,square_line*square_size,square_size,DISPLAY_SURFACE,True if state == 1 else False)
            all_square.append(square)
            square.draw()
            # if(square.state == 1):
            # else:
            #     points.append(square)
            # print(square_line,' ',square_column)
    # start_point = random.choice(points)
    # end_point = random.choice(points) 

    # start_point.draw_start()
    # end_point.draw_end()

    # solve(all_square,start_point, end_point)
    # return all_square


def random_color():
    red = random.randint(0,255)
    green = random.randint(0,255)
    blue = random.randint(0,255)
    return (red,green,blue)

def draw_window():
    DISPLAY_SURFACE.fill((255,255,255))

def draw_square():
    rects = []
    for pixel in range(WIDTH):
        rects.append(pygame.Rect(pixel,0,10,10))#x,y,w,h
    return rects


def main():
    x=0
    y=0
    clock = pygame.time.Clock()
    RUN = True
    all_rectangle = draw_square()
    # print(all_rectangle)
    split_screen(DISPLAY_SURFACE,WIDTH,HEIGHT)
    while RUN:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUN = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x = pygame.mouse.get_pos()[0]
                y = pygame.mouse.get_pos()[1]
                print(pygame.mouse.get_pos())
            
        # draw_square()
    
        # draw_window()
        # draw_square()
        pygame.display.update()
    
    pygame.quit()

if __name__ == "__main__":
    main()