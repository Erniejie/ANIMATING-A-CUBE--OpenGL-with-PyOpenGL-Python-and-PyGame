##SENTDEX-OpenGL with PyOpenGL tutorial Python and PyGame - 
#Part 9: Infinite Cubes 2 - Example -Nov 23th 2014
# WHOLE CODE

import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

import random

# 8 vertices(nodes)
vertices = (
    (1,-1,-1),
    (1,1,-1),
    (-1,1,-1),
    (-1,-1,-1),
    (1,-1,1),
    (1,1,1),
    (-1,-1,1),
    (-1,1,1)
    )

# 12 egdes:
edges = (
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7)
    )

surfaces=(
    (0,1,2,3),
    (3,2,7,6),
    (6,7,5,4),
    (4,5,1,0),
    (1,5,7,2),
    (4,0,3,6)
    
    )

colors = (
    (1,0,0),
    (0,1,0),
    (0,0,1),
    (0,0,0),
    (1,1,1),
    (0,1,1),
    (1,0,0),
    (0,1,0),
    (0,0,1),
    (1,0,0),
    (1,1,1),
    (0,1,1)
    )

ground_vertices = (
    (-10,-1.1,20),
    (10,-1.1,20),
    (-10,-1.1,-300),
    (10,-1.1,-300),
    )

def ground():
    glBegin(GL_QUADS)
    for vertex in ground_vertices:
        glColor3fv((0,0.5,0.5))
        glVertex3fv(vertex)

    glEnd()




def set_vertices(max_distance,min_distance =-20,camera_x =0,camera_y =0):
    camera_x =-1*int(camera_x)
    camera_y =-1*int(camera_y)

    
    x_value_change = random.randrange(camera_x-75,camera_x+75)
    y_value_change = random.randrange(camera_y-75,camera_y+75)
    z_value_change = random.randrange(-1*max_distance,min_distance)

    new_vertices = []

    for vert in vertices:
        new_vert = []

        new_x = vert[0] + x_value_change
        new_y = vert[1] + y_value_change
        new_z = vert[2] + z_value_change


        new_vert.append(new_x)
        new_vert.append(new_y)
        new_vert.append(new_z)

        new_vertices.append(new_vert)

    return new_vertices
        
        
        


def Cube(vertices):

    glBegin(GL_QUADS)
    
    for surface in surfaces:
        x =0

        for vertex in surface:
            x += 1
            glColor3fv(colors[x])   ##glColor3fv((0,1,0))  #  0:minimum ; 1:maximum
            glVertex3fv(vertices[vertex])





    glEnd()











    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])

    glEnd()


def main():
    pygame.init()
    display =(800,600)
    pygame.display.set_mode(display,DOUBLEBUF|OPENGL)

#-------------------------CLIPPING PLANES: CP:  IN /OUT------------------------------


    max_distance = 100    # smoother navegation  for 100 and less laggy than 300
    
    """ EXPLANATION :gluPerspective(45,(display[0]/display[1]) ,Closest CP_In, Farthest CP_Out)"""

    gluPerspective(45,(display[0]/display[1]) ,0.1, max_distance)  # CP_In = 0.1  ' CP_Out = 50
    #gluPerspective(45,(display[0]/display[1]) ,6, 20)
    #gluPerspective(45,(display[0]/display[1]) ,7, 10)
    

#------------------------------------------------------------------------------------
    """Notation:glTranslate(x,y,z)"""
    #glTranslate(0,0,-40)

              #     x variable              y variable
    ##glTranslate(random.randrange(-5,5),random.randrange(-5,5),-40)   # "random function" into action
    glTranslate(0,0,-40)

    ##object_passed = False

    x_move = 0
    y_move = 0

    cur_x = 0
    cur_y = 0

    game_speed = 2
    direction_speed = 20

    #max_distance = 300
    

    cube_dict = {}

    # drawing 75 cubes

    #for x in range (75):
    for x in range (77):    # 20 cubes less laggy than 75 cubes
        
        cube_dict[x] = set_vertices(max_distance)
        


    
   
#----------------------- we disable this  function for this tutorial Part 4:
    """ EXPLANATION:glRotate(degree,move in x,?,?)"""
    #glRotate(26,3,1,0)   #  this "rotation function is at STATIC POINT"  but will makes the ANIMATION IN 3D later on
#----------------------------------------------------------------------------

    ##while not object_passed :
    while True:
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
#------------MOVING THE CUBE WITH THE KEYBOARD:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_move = direction_speed 
                    
                if event.key == pygame.K_RIGHT:
                    x_move = -1*direction_speed 
                    
                if event.key == pygame.K_UP:
                    y_move = -1*direction_speed 

                if event.key == pygame.K_DOWN:
                    y_move = direction_speed 
                    
#-------------------Applyin Restrictions: Press, hold and release the MOUSE
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_move = 0
                    
                    
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_move =0
                
                 

#---------DISABLED FOR THIS PART 4 --MOUSE WHEEL ROLLING FOWARD AND BACKWARD:
##
##            if event.type == pygame.MOUSEBUTTONDOWN:
##                if event.button == 4:
##                    glTranslate(0,0,1)     #  "+Z" : ZOOM IN
##
##                if event.button == 5:
##                    glTranslate(0,0,-1)    #  "-Z" : ZOOM OUT
                
#-------------------------------------------------------------               
                
                


        """Notation:glRotate(x,y,z)"""
        #glRotate(1,3,2,1)
        #glRotate(1,1,-1,1)


        #glRotate(1,4,1,1)         #--- This " rotation Function" IGNITES The rotation in FULL motion""

        x = glGetDoublev(GL_MODELVIEW_MATRIX)
        #print(x)

        camera_x = x[3][0]
        camera_y = x[3][1]
        camera_z = x[3][2]


        cur_x += x_move    # modifies current location in x
        cur_y += y_move    # modifies current location in y
        
        
        
        

        

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

        #glTranslate(0,0,0.10)
        #glTranslate(0,0,0.50)   #NOTE:say,by increasing from 0.10 to 0. 50. it will speed up the animation!

        #glTranslate(x_move,y_move,0.5)
        glTranslate(x_move,y_move,game_speed)   # value of game_speed ="2" will make move faster

        #ground()

        for each_cube in cube_dict:
            Cube(cube_dict[each_cube])

        #delete_list =[]

        for each_cube in cube_dict:
            if camera_z <= cube_dict[each_cube][0][2]:
                
                new_max = int(-1*(camera_z- (max_distance*2)))

                cube_dict[each_cube] = set_vertices(new_max,int(camera_z-max_distance),cur_x,cur_y)
                










        


        pygame.display.flip()
        #pygame.time.wait(10)  # this code line may be redundant

#  many cubes happen at the same time:

main()
pygame.quit()
quit()
