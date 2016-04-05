# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True

ball_pos = [WIDTH/2, HEIGHT/2]
ball_vel = [0, 0]

paddle1_pos = [[0, HEIGHT/2-HALF_PAD_HEIGHT],[PAD_WIDTH, HEIGHT/2-HALF_PAD_HEIGHT],[PAD_WIDTH, HEIGHT/2+HALF_PAD_HEIGHT],[0, HEIGHT/2+HALF_PAD_HEIGHT]]
paddle2_pos = [[WIDTH-PAD_WIDTH, HEIGHT/2-HALF_PAD_HEIGHT],[WIDTH, HEIGHT/2-HALF_PAD_HEIGHT],[WIDTH, HEIGHT/2+HALF_PAD_HEIGHT],[WIDTH-PAD_WIDTH, HEIGHT/2+HALF_PAD_HEIGHT]]

paddle1_vel = 0
paddle2_vel = 0

score1 = 0
score2 = 0

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH/2, HEIGHT/2]
    if direction :
        ball_vel[0] = random.randrange(120/60, 240/60)
        ball_vel[1] = -random.randrange(60/60, 180/60)
    else:
        ball_vel[0] = -random.randrange(120/60, 240/60)
        ball_vel[1] = -random.randrange(60/60, 180/60)
    


# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    score1 = score2 = 0
    paddle1_pos = [[0, HEIGHT/2-HALF_PAD_HEIGHT],[PAD_WIDTH, HEIGHT/2-HALF_PAD_HEIGHT],[PAD_WIDTH, HEIGHT/2+HALF_PAD_HEIGHT],[0, HEIGHT/2+HALF_PAD_HEIGHT]]
    paddle2_pos = [[WIDTH-PAD_WIDTH, HEIGHT/2-HALF_PAD_HEIGHT],[WIDTH, HEIGHT/2-HALF_PAD_HEIGHT],[WIDTH, HEIGHT/2+HALF_PAD_HEIGHT],[WIDTH-PAD_WIDTH, HEIGHT/2+HALF_PAD_HEIGHT]]

    paddle1_vel = 0
    paddle2_vel = 0
    spawn_ball(LEFT)

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel, paddle1_vel, paddle2_vel
 
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    if ball_pos[0] <= PAD_WIDTH + BALL_RADIUS :
        #ball_vel[0] = -ball_vel[0]
        
        if ball_pos[1] >= paddle1_pos[2][1] or ball_pos[1] <= paddle1_pos[1][1] :
            score2 += 1
            spawn_ball(RIGHT)
        else:
            ball_vel[0] += ball_vel[0]/10
            ball_vel[0] = -ball_vel[0]
            ball_vel[1] += ball_vel[1]/10
        
    if ball_pos[0] >= WIDTH - (PAD_WIDTH + BALL_RADIUS) :
        #ball_vel[0] = -ball_vel[0]
        
        if ball_pos[1] >= paddle2_pos[2][1] or ball_pos[1] <= paddle2_pos[1][1] :
            score1 += 1
            spawn_ball(LEFT)
        else:
            ball_vel[0] += ball_vel[0]/10
            ball_vel[0] = -ball_vel[0]
            ball_vel[1] += ball_vel[1]/10
    
    if ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]
        
    if ball_pos[1] >= HEIGHT - BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]
    
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")
    # update paddle's vertical position, keep paddle on the screen
    if (paddle1_pos[0][1] <= 1 and paddle1_vel < 0) :
        paddle1_pos = paddle1_pos
    elif (paddle1_pos[2][1] >= HEIGHT-1 and paddle1_vel > 0) :
        paddle1_pos = paddle1_pos
    else:
        paddle1_pos[0] = [paddle1_pos[0][0], paddle1_pos[0][1]+paddle1_vel] 
        paddle1_pos[1] = [paddle1_pos[1][0], paddle1_pos[1][1]+paddle1_vel]
        paddle1_pos[2] = [paddle1_pos[2][0], paddle1_pos[2][1]+paddle1_vel] 
        paddle1_pos[3] = [paddle1_pos[3][0], paddle1_pos[3][1]+paddle1_vel] 
    
    if (paddle2_pos[0][1] <= 1 and paddle2_vel < 0):
        paddle2_pos = paddle2_pos
    elif (paddle2_pos[2][1] >= HEIGHT-1 and paddle2_vel > 0):
        paddle2_pos = paddle2_pos
    else:
        paddle2_pos[0] = [paddle2_pos[0][0], paddle2_pos[0][1]+paddle2_vel] 
        paddle2_pos[1] = [paddle2_pos[1][0], paddle2_pos[1][1]+paddle2_vel] 
        paddle2_pos[2] = [paddle2_pos[2][0], paddle2_pos[2][1]+paddle2_vel] 
        paddle2_pos[3] = [paddle2_pos[3][0], paddle2_pos[3][1]+paddle2_vel] 
    
    # draw paddles
    canvas.draw_polygon(paddle1_pos, 1, "Red", "Red")
    canvas.draw_polygon(paddle2_pos, 1, "Red", "Red")
    
    # determine whether paddle and ball collide    
    
    # draw scores
    canvas.draw_text(str(score1), [200, 50], 30, "White")
    canvas.draw_text(str(score2), [400, 50], 30, "White")
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel = -1
    if key == simplegui.KEY_MAP["s"]:
        paddle1_vel = 1
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel = -1
    if key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 1
        
   
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel = 0
    if key == simplegui.KEY_MAP["s"]:
        paddle1_vel = 0
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel = 0
    if key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 0

def button_handler():
    new_game()
    
# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
button1 = frame.add_button('Restart', button_handler)


# start frame
new_game()
frame.start()
