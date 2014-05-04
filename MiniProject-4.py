"""Pong"""
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

ball_pos = []
ball_vel = []
paddle1_pos = []
paddle1_vel = 0
paddle2_pos = []
paddle2_vel = 0
paddle1_acc = 5 #
paddle2_acc = 5 #
score1, score2 = 0, 0

def spawn_ball(direction):
    global ball_pos, ball_vel
    ball_pos = [WIDTH//2, HEIGHT//2]
    ball_vel = [random.randrange(120,240)//60, random.randrange(60,180)//60] # draw is called every 1/60 of second
    if direction is RIGHT :
        ball_vel[1] *= -1 # up-ing, default right for +ive vel
    elif direction is LEFT :
        ball_vel[0] *= -1 # left-ing
        ball_vel[1] *= -1 # up-ing
    elif (LEFT and RIGHT) or not (LEFT and RIGHT) :
        print "LEFT RIGHT are not acting mutually exclusive"
    else :
        print "Unhandled case : spawn_ball has wonky LEFT RIGHT"


# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    score1, score2 = 0, 0
    paddle1_pos = [[0, (HEIGHT//2 - HALF_PAD_HEIGHT)],  # top-left
                   [0, (HEIGHT//2 + HALF_PAD_HEIGHT)],  # bottom-left
                   [PAD_WIDTH, (HEIGHT//2 + HALF_PAD_HEIGHT)],  # bottom-right
                   [PAD_WIDTH, (HEIGHT//2 - HALF_PAD_HEIGHT)]]  # top-right
    paddle2_pos = [[WIDTH - 0, (HEIGHT//2 - HALF_PAD_HEIGHT)],
                   [WIDTH - 0, (HEIGHT//2 + HALF_PAD_HEIGHT)],
                   [WIDTH - PAD_WIDTH, (HEIGHT//2 + HALF_PAD_HEIGHT)],
                   [WIDTH - PAD_WIDTH, (HEIGHT//2 - HALF_PAD_HEIGHT)]]
    spawn_ball(RIGHT)
    

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    global paddle1_acc, paddle2_acc
    
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    if (ball_pos[1] <= BALL_RADIUS or
        ball_pos[1] >= HEIGHT - BALL_RADIUS):
        ball_vel[1] *= -1
    
    if ball_pos[0] <= BALL_RADIUS + PAD_WIDTH:
        if (ball_pos[1] >= paddle1_pos[3][1] and
            ball_pos[1] <= paddle1_pos[2][1]):
            ball_vel[0] *= -1.1 # increase ball_vel by 10%
        else:
            score2 += 1
            spawn_ball(RIGHT)
    elif ball_pos[0] >= WIDTH - PAD_WIDTH - BALL_RADIUS:
        if (ball_pos[1] >= paddle2_pos[0][1] and
            ball_pos[1] <= paddle2_pos[1][1]):
            ball_vel[0] *= -1.1
        else:
            score1 += 1
            spawn_ball(LEFT)
         
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 1, "White", "White")
    # update paddle's vertical position, keep paddle on the screen
    if not (paddle1_pos[0][1]+paddle1_vel <= 0 or
            paddle1_pos[2][1]+paddle1_vel >= HEIGHT):
        for i in range(len(paddle1_pos)):
            paddle1_pos[i][1] += paddle1_vel
    '''    if paddle1_vel > 0:
            paddle1_acc *= 1.1'''
    if not (paddle2_pos[3][1]+paddle2_vel <= 0 or
            paddle2_pos[2][1]+paddle2_vel >= HEIGHT):
        for i in range(len(paddle1_pos)):
            paddle2_pos[i][1] += paddle2_vel
    '''    if paddle2_acc > 0:
            paddle2_acc *= 1.1'''
    # draw paddles
    canvas.draw_polygon(paddle1_pos, 1, "White", "White")
    canvas.draw_polygon(paddle2_pos, 1, "White", "White")
    # draw scores
    canvas.draw_text(str(score1), [WIDTH//2 - 40, 40], 24, "White")
    canvas.draw_text(str(score2), [WIDTH//2 + 24, 40], 24, "White")
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP['w']:
        paddle1_vel -= paddle1_acc
    elif key == simplegui.KEY_MAP['s']:
        paddle1_vel += paddle1_acc
    elif key == simplegui.KEY_MAP['up']:
        paddle2_vel -= paddle2_acc
    elif key == simplegui.KEY_MAP['down']:
        paddle2_vel += paddle2_acc
    else: 
        print "This game responds only to keys 'w', 's', 'up', and 'down'"
   
def keyup(key):
    global paddle1_vel, paddle2_vel, paddle1_acc, paddle2_acc
    if (key == simplegui.KEY_MAP['w'] or 
        key == simplegui.KEY_MAP['s']): # left paddle
        paddle1_vel = 0
        # paddle1_acc = 1
    elif (key == simplegui.KEY_MAP['up'] or 
          key == simplegui.KEY_MAP['down']): # right paddle
        paddle2_vel = 0
        # paddle2_acc = 1


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", new_game)


# start frame
new_game()
frame.start()
