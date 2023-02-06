from matplotlib.pyplot import text
import pygame as py

py.init()                                                                 

screen_res =[640,480]
screen =py.display.set_mode(screen_res)                                     
py.display.set_caption("Bouncing Box")
clock = py.time.Clock()

WHITE =(255,255,255)
BLACK =(0,0,0)

(x_position,y_position) = ([50,screen_res[0]-50,screen_res[0]/2],[50,50,screen_res[1]/2]) 
(rect_x_size,rect_y_size,circle_rad) = (20,100,10)
(vx,vy)=(2,[0,0,2])

font =py.font.SysFont("Calibri",50,False,False)
text = font.render("Game Over", True, BLACK)

class entity:

    def __init__(self, pos_x, pos_y):
        self.pos_x=pos_x
        self.pos_y=pos_y
    
    def render_box(self):
        py.draw.rect(screen, BLACK,(self.pos_x,self.pos_y,rect_x_size,rect_y_size))

    def render_ball(self):
        py.draw.circle(screen,BLACK,(self.pos_x,self.pos_y),circle_rad)

done = False                                        


while not done:

    screen.fill(WHITE)

    for event in py.event.get():
        if event.type == py.QUIT:
            done =True 

        if event.type == py.KEYDOWN:
            if event.key == py.K_w:
                vy[0] = -4 
            if event.key == py.K_s:
                vy[0] = 4
            if event.key == py.K_UP:
                vy[1] = -4 
            if event.key == py.K_DOWN:
                vy[1] = 4

    for i in range(2):
        if y_position[i] <= 0 or y_position[i] >= screen_res[1]-rect_y_size:
            vy[i] = -vy[i]
        y_position[i] += vy[i]
    
    if ((y_position[2] <= circle_rad or y_position[2] >= screen_res[1]-circle_rad) or 
    (((x_position[2]-circle_rad <x_position[0]+rect_x_size and x_position[2]-circle_rad > x_position[0] ) and 
    (y_position[2]> y_position[0] and y_position[2]< y_position[0]+ rect_y_size)) or 
    ((x_position[2]+circle_rad > x_position[1] and x_position[2]+circle_rad < x_position[1]+50) and 
    (y_position[2]> y_position[1] and y_position[2]< y_position[1]+ rect_y_size)))):
        vy[2] = -vy[2]
    y_position[2] += vy[2]

    if (((x_position[2]-circle_rad <x_position[0]+rect_x_size and x_position[2]-circle_rad > x_position[0] ) and 
    (y_position[2]> y_position[0] and y_position[2]< y_position[0]+ rect_y_size)) or 
    ((x_position[2]+circle_rad > x_position[1] and x_position[2]+circle_rad < x_position[1]+50) and 
    (y_position[2]> y_position[1] and y_position[2]< y_position[1]+ rect_y_size))):
        vx = -vx
    x_position[2] += vx

    if x_position[2]< 0 or x_position[2]>screen_res[0]:
        screen.blit(text,[220,180])

    box = [entity(x_position[0],y_position[0]),entity(x_position[1],y_position[1])]
    ball = entity(x_position[2],y_position[2])

    box[0].render_box()
    box[1].render_box()
    ball.render_ball()

    clock.tick(30)

    py.display.flip()
    



        

