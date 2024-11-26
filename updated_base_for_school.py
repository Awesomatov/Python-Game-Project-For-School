#Created by Ethan Nauta
#Bring in pygame module
import pygame, sys

pygame.init()

#define screen size and amount of tiles on screen.
screen_x = 800
screen_y = 400
screen_x2 = screen_x
screen_y2 = screen_y
screen = pygame.display.set_mode((screen_x, screen_y), pygame.RESIZABLE)
pygame.display.set_caption('Resizable')


#create a matrix to position the map tiles!
matrix_columns = int(16)
matrix_rows = int(16)
matrix_column_count = 0
matrix_row_count = 0
matrix = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,1,0,1,1,0,0,0,1,1,1,1,1,1,1,0],
          [0,1,1,1,1,1,1,0,1,1,0,0,1,1,1,0],
          [0,1,0,1,1,1,1,0,1,1,0,1,1,1,1,0],
          [0,1,0,1,1,1,0,0,1,1,1,1,1,1,1,0],
          [0,1,0,1,0,1,1,0,1,1,1,1,1,1,1,0],
          [0,0,0,1,0,0,0,0,1,1,1,0,1,1,1,0],
          [0,0,1,1,0,0,0,0,1,1,0,0,0,1,1,0],
          [0,0,1,1,0,0,1,1,1,1,1,0,1,1,1,0],
          [0,0,1,1,0,0,1,1,1,1,1,1,1,1,1,0],
          [0,0,1,1,0,1,1,0,1,1,1,1,1,1,1,0],
          [0,0,1,1,1,1,1,0,1,1,1,1,1,1,1,0],
          [0,0,1,1,1,1,1,0,1,1,0,0,0,1,1,0],
          [0,0,1,1,0,0,0,0,1,1,1,1,0,1,1,0],
          [0,0,1,1,0,0,0,0,1,1,1,1,1,1,1,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],]


#initialize player object, the object should be divisible to an even number to allow the smooth collision. 
#(ie 50/2 = 25 which is not even so ideally don't use that)
plyr_size = 60
test_surface = pygame.Surface((plyr_size, plyr_size))
test_surface.fill(pygame.Color("gold"))

#size of every tile in the game, their spacing and collision will scale with this. Change it to whatever!
#(just make sure the player doesn't spawn in a block)
tile_size = 100

#these are some methods I was told to use from a video which seem to work. They are elements of pygame.
clock = pygame.time.Clock()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 100)

#x and y position of the top left corner of the screen on the map.
x_pos = 0
y_pos = 0

#the actual x and y positions of the centre of the player character.
r_xpos = 400
r_ypos = 200

#state of players available keyboard inputs.
w_state = 0
a_state = 0
s_state = 0
d_state = 0

#players speed in the game. Each key corresponds to a direction!
w_speed = 10
a_speed = 10
s_speed = 10
d_speed = 10


#core loop of the game, runs at 30FPS, and handles all collision
while True:
    
    screen_x1, screen_y1 = screen.get_size()
    
    if screen_x1 % 2 != 0:
        
        screen_x1 += 1
        screen = pygame.display.set_mode((screen_x1, screen_y1), pygame.RESIZABLE)
        
    if screen_y1 % 2 != 0:
        
        screen_y1 != 1
        screen = pygame.display.set_mode((screen_x1, screen_y1), pygame.RESIZABLE)
        
    if screen_x1 != screen_x2:
        
        x_pos -= 0.5*(screen_x1 - screen_x2)
        screen_x2 = screen_x1
        screen_x = screen_x2
        
    if screen_y1 != screen_y2:
        
        y_pos -= 0.5*(screen_y1 - screen_y2)
        screen_y2 = screen_y1
        screen_y = screen_y2
    
    #at the start of every step of the game, check for all input events.
    for event in pygame.event.get():
        
        #assures game will be completely closed. Also got this from the video linked at the top.
        if event.type == pygame.QUIT:
            
            pygame.quit()
            sys.exit()
       
        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_w:
                
                w_state = -1
            if event.key == pygame.K_a:
                
                a_state = -1
            if event.key == pygame.K_s:
                
                s_state = 1
            if event.key == pygame.K_d:
            
                d_state = 1
                
        if event.type == pygame.KEYUP:
            
            if event.key == pygame.K_w:
                
                w_state = 0
            if event.key == pygame.K_a:
                
                a_state = 0
            if event.key == pygame.K_s:
                
                s_state = 0
            if event.key == pygame.K_d:
            
                d_state = 0
                

            
    #either pass a pygame base color or a RGB tuple, 
    #there is a list of available base colors in the documentation!
    screen.fill(pygame.Color("blue"))
    
    
    #for each row, adjust the position of each tile in each column to the appropriate spacing.
    for rows in range(matrix_rows):
        
        for columns in range(matrix_columns):

            
            #in the map matrix, a zero is defined as a wall, or unwalkable surface!
            if matrix[rows][columns] == 0:
             
                
                #if player is in y range of square, can trigger x collisions, and vice versa
                check_y = (rows*tile_size - r_ypos <= 0.5*plyr_size + 1 and rows*tile_size - r_ypos >= -tile_size - 0.5*plyr_size - 1)
                check_x = (columns*tile_size - r_xpos <= 0.5*plyr_size + 1 and columns*tile_size - r_xpos >= -tile_size - 0.5*plyr_size - 1)
                

                #if the player is inside of a square, push them out in the direction they are closest to
                if check_x and check_y:
                    
                    print('you are touching square ', rows, ' ', columns)
                    
                    if rows*tile_size - r_ypos > 0.5*plyr_size - 1:
                        
                        if matrix[rows-1][columns] != 0:
                            print('hitting top')
                            s_speed = 0
                        
                    elif rows*tile_size - r_ypos < -tile_size - 0.5*plyr_size + 1:
                        
                        if matrix[rows+1][columns] != 0:
                            print('hitting bottom')
                            w_speed = 0
                        
                    if columns*tile_size - r_xpos > 0.5*plyr_size - 1:
                        
                        if matrix[rows][columns-1] != 0:
                            print('hitting left')
                            d_speed = 0
                        
                    elif columns*tile_size - r_xpos < -tile_size - 0.5*plyr_size + 1:
                        
                        if matrix[rows][columns+1] != 0:
                            print('hitting right')
                            a_speed = 0
                    
                    
                    
                        
            if matrix[rows][columns] == 1:
                
                grass = pygame.Surface((tile_size,tile_size))
                grass.fill(pygame.Color("green"))
                
                screen.blit(grass, (columns*tile_size - x_pos, rows*tile_size - y_pos))
                
            if matrix[rows][columns] == 0:
                
                water = pygame.Surface((tile_size,tile_size))
                water.fill(pygame.Color("white"))
                
                screen.blit(water, (columns*tile_size - x_pos, rows*tile_size - y_pos))
                    
                        
                
            columns += 1
        
        rows += 1
        
    
    
        
    #if a and d active, dont move, else move
    x_pos += a_state*a_speed + d_state*d_speed
    y_pos += w_state*w_speed + s_state*s_speed
    
    r_xpos += a_state*a_speed + d_state*d_speed
    r_ypos += w_state*w_speed + s_state*s_speed
    
    w_speed = 10
    a_speed = 10
    s_speed = 10
    d_speed = 10
    
    
    #Positions the test surface on the screen relative to top left of object
    screen.blit(test_surface,(0.5*screen_x - 0.5*plyr_size, 0.5*screen_y - 0.5*plyr_size))
    
    #draw all elems each step
    pygame.display.update()
    
    #sets the fps of the game, game may still run too slow. This runs 30 fps.
    clock.tick(30)