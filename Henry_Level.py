#Created by Ethan Nauta
#Innovated by Henry Lawrence
#Bring in pygame module
import pygame, sys
pygame.init()
#EN: define screen size and amount of tiles on screen
screen_x = 1000
screen_y = 800
screen = pygame.display.set_mode((screen_x, screen_y))
#HL: a bunch of definitions of simple variables. These represent the 'keys' and their associated 'doors' on the map. Capital letter is a door, lowercase is a key.
A = 'A'
a = 'a'
B = 'B'
b = 'b'
C = 'C'
c = 'c'
D = 'D'
d = 'd'
E = 'E'
e = 'e'
F = 'F'
f = 'f'
G = 'G'
g = 'g'
H = 'H'
h = 'h'
I = 'I'
i = 'i'
J = 'J'
j = 'j'
K = 'K'
k = 'k'
L = 'L'
l = 'l'
M = 'M'
m = 'm'
N = 'N'
n = 'n'
O = 'O'
o = 'o'
P = 'P'
p = 'p'
Q = 'Q'
q = 'q'
R = 'R'
r = 'r'
S = 'S'
s = 's'
T = 'T'
t = 't'
U = 'U'
u = 'u'
#HL: defining the list of doors. Eventually every item will be converted to 'used!', and no longer function as doors.
list_of_doors = [A,B,C,D,E,F,G,H,I,J,K,M,N,L,O,P,Q,R,S,T,U]
#HL: defining the list of keys. Eventually every item will be converted to 'used!', and no longer function as keys.
list_of_keys = [a,b,c,d,e,f,g,h,i,j,k,m,n,l,o,p,q,r,s,t,u]
#HL: a list of colors, associated with the list of doors and keys. For example, the first color entry corresponds to the first the key 'a' and the door 'A'.
list_of_colors = ["brown1","deeppink","burlywood4","cadetblue","yellow","chocolate4","coral","coral3","coral4","crimson","darkolivegreen","white","darkolivegreen1","darkorchid","darkred","darksalmon","darkseagreen1","brown1","violetred4","yellowgreen","thistle1","springgreen1","slateblue","red"]
#HL: removed_object_index is a variable that provides a connection between entries in the three lists above. Important when the same index in different lists need to be removed.
removed_object_index = 0
#HL: below is a matrix that represents the map of the game! each entry represents a 100x100 block, and the different entries represent different kind of blocks.
#HL: also defines some variables that will be used later to reference certain entries in the matrix
matrix_columns = int(32)
matrix_rows = int(15)
matrix_column_count = 0
matrix_row_count = 0
matrix = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,1,1,1,T,h,T,F,u,1,1,1,1,0,0,0,1,1,H,h,t,1,0,1,1,1,1,0,0,n,0],
          [0,1,1,0,1,0,0,1,1,0,0,0,0,1,0,0,1,1,1,0,1,1,1,0,0,1,0,1,0,0,S,0],
          [0,1,1,0,1,0,1,G,1,0,f,1,1,1,1,0,1,1,0,0,0,0,1,0,1,1,0,1,1,0,r,0],
          [H,1,1,0,1,0,1,1,0,1,1,1,1,1,1,0,1,1,1,1,1,0,S,0,1,0,0,0,1,0,Q,0],
          [0,0,0,0,1,0,0,1,0,1,1,1,1,1,1,0,1,1,1,0,1,0,1,0,1,1,1,0,1,0,p,0],
          [0,1,1,1,1,1,0,1,1,1,1,1,1,g,1,U,D,1,1,0,1,0,1,1,0,0,M,0,1,0,O,0],
          [0,1,1,0,1,1,U,U,1,1,1,0,0,e,0,0,0,0,0,0,1,1,1,1,0,m,1,0,1,1,1,0],
          [0,1,1,1,0,1,0,1,1,0,1,0,0,0,0,0,1,1,j,0,1,1,0,0,0,0,1,0,0,0,o,0],
          [0,0,1,1,1,1,c,E,1,1,1,C,1,1,1,0,1,0,J,1,1,1,0,1,1,1,1,0,0,0,P,0],
          [0,0,1,1,1,1,0,1,1,1,0,0,0,0,1,0,1,0,0,0,1,1,1,1,0,0,0,0,0,0,q,0],
          [0,0,0,1,0,0,0,0,1,1,1,0,1,1,1,0,1,0,0,1,1,0,0,0,0,0,1,1,1,0,R,0],
          [0,a,B,1,0,0,0,1,1,1,1,0,1,0,0,0,1,1,1,1,1,l,1,0,0,0,1,0,1,0,s,0],
          [0,b,1,1,A,1,1,1,1,1,1,0,1,1,d,0,0,0,1,1,1,0,L,1,1,1,1,0,1,N,1,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],]

#HL: the two lines below define the size and color of the player.
test_surface = pygame.Surface((90, 90))
test_surface.fill(pygame.Color("gold"))

#HL: initializes the clock, which is used to control the speed of the game (60fps) 
clock = pygame.time.Clock()

#HL: ETHAN WHA
SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 100)

#HL: x_pos and y_pos are used to track the player position, also determining spawn position.
x_pos = -300
y_pos = 0

#HL: these are used later to track and store which keys are pressed.
w_state = 0
a_state = 0
s_state = 0
d_state = 0

#HL: players speed in the game
x_speed = 10
y_speed = 10

#HL: These variables are used to disallow movement for the player. Used to disallow diagonal movement and movement into walls.
disallow_movement_left = False
disallow_movement_right = False
disallow_movement_up = False
disallow_movement_down = False

#EN: core loop
while True:
    
    #EN: at the start of every step of the game, check for all events.
    for event in pygame.event.get():
        
        #EN: assures game will be completely closed.
        if event.type == pygame.QUIT:
            
            pygame.quit()
            sys.exit()
        #HL: Checks each frame if the player pressed any of the wasd keys. Also prevents more than one key from being pressed at the same time. Essential for the game concept. 
        if event.type == pygame.KEYDOWN:
            
            if (event.key == pygame.K_w) and (s_state != 1) and (d_state != 1) and (a_state != -1) :
                               
                w_state = -1
            if (event.key == pygame.K_a) and (s_state != 1) and (d_state != 1) and (w_state != -1):
              
                
                a_state = -1
            if (event.key == pygame.K_s) and (a_state != -1) and (d_state != 1) and (w_state != -1):
               
                
                s_state = 1
            if (event.key == pygame.K_d) and (s_state != 1) and (w_state != -1) and (a_state != -1):
               
                
                d_state = 1  
    #EN: either pass a pygame base color or a RGB tuple
    screen.fill(pygame.Color("white"))
    
    
    #EN: for each row, adjust the position of each tile in each column
    for rows in range(matrix_rows):
        
        for columns in range(matrix_columns):
            #HL: for each tile, defines the following variables in order to create a 'collision box' for the player and a given block.
            x1w = (columns*100) - 0.5*screen_x
            x2w = (columns*100) + 100 -  0.5*screen_x
            y1w = (rows*100) - 0.5*screen_y
            y2w = (rows*100) + 100 - 0.5*screen_y

            x1p = x_pos
            x2p = (x_pos)+90
            y1p = y_pos
            y2p = (y_pos)+90
            #HL: for each wall tile, 0, and each door tile, uppercase letter, checks if the player is up against a given tile. 
            #HL: If so, the given disallow_movement variable is set as true.
            if (matrix[rows][columns] == 0) or (matrix[rows][columns] in list_of_doors):                     
                if (x2w == x1p) and ((y1w < y1p < y2w) or (y1w < y2p < y2w)):
                    disallow_movement_left = True
                    
                if (x2p == x1w) and ((y1w < y1p < y2w) or (y1w < y2p < y2w)):
                    disallow_movement_right = True
            
                if (y2p == y1w) and ((x1w < x1p < x2w) or (x1w < x2p < x2w)):
                    disallow_movement_down = True

                if (y1p == y2w) and ((x1w < x1p < x2w) or (x1w < x2p < x2w)):
                    disallow_movement_up = True
                
            if (matrix[rows][columns] in list_of_keys):
                #HL: if the player is within the hitbox of the key, removes the associated item from the key list and the door list and replaces the entry with 'used!'.
                #HL: Also changes the given entry in the list_of_colors matrix to white
                #HL: for the player, this results in the key being collected, the door being opened, and the tile changing to color white.
                if (y1w <= y1p <= y2w) and (y1w <= y2p <= y2w) and (x1w <= x1p <= x2w) and (x1w <= x2p <= x2w):
                    if (matrix[rows][columns] in list_of_keys) and ((matrix[rows][columns]).upper() in list_of_doors):      
                        removed_object_index = list_of_keys.index(matrix[rows][columns])
                        list_of_keys.pop(removed_object_index)
                        list_of_keys.insert(removed_object_index,'used!')
                        list_of_doors.pop(removed_object_index)
                        list_of_doors.insert(removed_object_index,'used!')
                        list_of_colors.pop(removed_object_index)
                        list_of_colors.insert(removed_object_index, 'white')
    
                    
            
            #HL: if the given tile is a ground tile (1), sets the given 100x100 surface to be white.            
            if matrix[rows][columns] == 1:
                
                grass = pygame.Surface((100,100))
                grass.fill(pygame.Color("white"))
                screen.blit(grass, (columns*100-x_pos, rows*100-y_pos))
            #HL: if the given tile is a wall tile (1), sets the given 100x100 surface to be green.    
            if matrix[rows][columns] == 0:
                
                water = pygame.Surface((100,100))
                water.fill(pygame.Color("green"))
                
                screen.blit(water, (columns*100 - x_pos, rows*100 - y_pos))
            #HL: if the given block is a key tile, creates a circle with a color in the list_of_colors list corresponding to the key in list_of_keys.
            #HL: if the given key has already been collected, this if statement will not pass.
            if (matrix[rows][columns] in list_of_keys):
                key_block_color = pygame.draw.circle(screen,list_of_colors[list_of_keys.index(matrix[rows][columns])] , (columns*100-x_pos+50, rows*100-y_pos+50), 25, 25)
            #HL: if the given block is a door tile, creates a 100x100 area with a color in the list_of_colors list corresponding to the door in list_of_doors.
            #HL: if the given key has already been collected, this if statement will not pass.   
            if (matrix[rows][columns] in list_of_doors):
                key_block_color = pygame.Surface((100,100))
                key_block_color.fill(pygame.Color(list_of_colors[list_of_doors.index(matrix[rows][columns])]))
                screen.blit(key_block_color, (columns*100-x_pos, rows*100-y_pos))                      
                
            columns += 1
        
        rows += 1

    
    #HL: if the player is disallowed to move in a given direction, sets the direction's key value to 0, preventing movement in that direction even if the player is holding a key in that direction.
    if disallow_movement_up:
        w_state = 0
    if disallow_movement_down:
        s_state = 0
    if disallow_movement_left:
        a_state = 0
    if disallow_movement_right:
        d_state = 0
    #HL: If the player chooses to move in an allowed direction, updates that player's position as such.    
    if not disallow_movement_up:
        y_pos += w_state*y_speed
    if not disallow_movement_down:
        y_pos += s_state*y_speed
    if not disallow_movement_right:
        x_pos += d_state*x_speed
    if not disallow_movement_left:
        x_pos += a_state*x_speed
    #HL: resets the disallow_movement variables after each instance of player movement.   
    disallow_movement_left = False
    disallow_movement_right = False
    disallow_movement_up = False
    disallow_movement_down = False

    #EN: Positions the test surface on the screen relative to top left of object
    screen.blit(test_surface,(0.5*screen_x, 0.5*screen_y)) 
    #screen.blit(test_surface,(0,0)) 
    
    #EN: draw all elems each step
    pygame.display.update()
    
    #EN: sets the fps of the game.
    clock.tick(60)