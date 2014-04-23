"""Stopwatch: The Game"""

import simplegui

# define global variables
timer_int = 0 #5899 #test for auto-reset
button_width = 100
attempts = 0
score = 0
game_state = "default"
score_colorset = {"default": "#efefef",
                  "hit": "#a5fbb2",
                  "miss": "#ec3373"}

def format(t):
    """
    returns 't' milliseconds as a string in format M:ss.ms
    currently only handles t in range [0, 5999], or 
    valid return strings are in time range [0:00.0, 9:59.9]
    """
    
    format_string = ""
    
    if t<0:
        print "ERROR: given t = "+str(t)+" is not allowed. Expecting t >= 0"
        return format_string
    
    # extract times
    minutes = t/600
    t %= 600
    seconds = t/10
    milliseconds = t%10
    
    # make format_string
    if minutes <= 9:
        format_string += str(minutes)+":"
    elif minutes < 0:
        print "ERROR: format(t = "+str(t)+") calculated minutes < 0"
    elif minutes > 9:
        print "ERROR: format(t = "+str(t)+") calculated minutes > 9"
    else :
        print "ERROR: format(t = "+str(t)+") calculated unhandled minutes"
    
    if seconds > 9:
        format_string += str(seconds)+"."
    elif seconds >= 0:
        format_string += str(0)+str(seconds)+"."
    elif seconds < 0:
        print "ERROR: format(t = "+str(t)+") calculated seconds < 0"
    else:
        print "ERROR: format(t = "+str(t)+") calculated unhandled seconds"
    
    if milliseconds <= 9:
        format_string += str(milliseconds)
    elif milliseconds < 0:
        print "ERROR: format(t = "+str(t)+") calculated milliseconds < 0"
    elif milliseconds > 9:
        print "ERROR: format(t = "+str(t)+") calculated milliseconds > 9"
    else :
        print "ERROR: format(t = "+str(t)+") calculated unhandled milliseconds"
    
    return format_string
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def button_start_handler():
    if not timer.is_running():
        global game_state
        timer.start()
        game_state = "default"
    else: 
        print "The one and only timer is already running baba"

def button_stop_handler():
    if timer.is_running():
        global attempts, score, game_state
        timer.stop()
        attempts += 1
        if (format(timer_int)[-2:] == ".0") and (timer_int%10 == 0):
            score += 1
            game_state = "hit"
            print "Hit! at :", format(timer_int),
        else: 
            game_state = "miss"
            print "Miss at :", format(timer_int), "-"*(10-timer_int%10), #"("+str((timer_int%10)-10)+")"
        if attempts%100 == 0 :
            print "A rambunctious soul, are we", "("+str(attempts)+" attempts)"
        elif score == 20 :
            print "Both font sizes are equal. There's something wrong with our brains"
        else :
            print
    else:
        print "Hehe, you evil sod"

def button_reset_handler():
    global timer_int, attempts, score, game_state
    print ""
    print "Game manually reset at : ", format(timer_int)
    if timer.is_running():
        timer.stop()
        if timer_int%10 == 0 :
            print "Aahahahhhaaaaha, burned!!!"
            print "You gave in too quickly"
    print ""
    print "Game Summary :", str(score), 
    # Grammar Nazi
    if score == 1 :
        print "Hit",
    else :
        print "Hits",
    print "in", str(attempts),
    if attempts == 1:
        print "Attempt"
    else:
        print "Attempts"
    print "="*42
    timer_int = 0
    attempts, score = 0, 0
    game_state = "default"
    print "Start Timer for a New Game"
    print ""
    # draw_handler(draw_canvas) # Why is this not required???
    
def button_startstop_handler():
    global attempts, score, game_state
    if not timer.is_running():
        timer.start()
        button_startstop.set_text("start/STOP")
        game_state = "default"
    else:
        timer.stop()
        button_startstop.set_text("START/stop")
        attempts += 1
        if (format(timer_int)[-2:] == ".0") and (timer_int%10 == 0):
            score += 1
            game_state = "hit"
            print "Hit! at :", format(timer_int),
        else: 
            game_state = "miss"
            print "Miss at :", format(timer_int), "-"*(10-timer_int%10), #"("+str((timer_int%10)-10)+")"
        if attempts%100 == 0 :
            print "A rambunctious soul, are we", "("+str(attempts)+" attempts)"
        elif score == 20 :
            print "Both font sizes are equal. There's something wrong with our brains"
        else :
            print
            
# define event handler for timer with 0.1 sec interval
def timer_handler():
    global timer_int
    timer_int += 1

# define draw handler
def draw_handler(canvas):
    """draw_handler : expect a lot of hard-coding, not noob level though, #p
    though I can't guarantee for different fonts and stuff"""
    global game_state
    if timer_int > 5999 :
        print "The timer was automatically reset on crossing 9:59:9"
        button_reset_handler() # Reset game after 10 minutes
    # Set Params - Canvas Background
    bg_canvas_points = [[0,0],
                        [frame_width, 0],
                        [frame_width, frame_height],
                        [0, frame_height]]
    bg_canvas_line_width = 1
    bg_canvas_fill_color = "#70cec8"
    bg_canvas_line_color = bg_canvas_fill_color
    
    # Set Params - Background circle
    bg_circle_loc = [frame_width/2, frame_height/2]
    bg_circle_radius = int((min(frame_width, frame_height))/3)
    bg_circle_line_width = 1 + timer_int%10
    bg_circle_fill_color = "#8fdad5"
    bg_circle_line_color = bg_circle_fill_color
    
    # Set Params - Score Circle
    score_circle_radius = int(bg_circle_radius/2)
    score_circle_loc = [frame_width/2 + bg_circle_radius/1.1, 
                        frame_height/2 - bg_circle_radius/1.1]
    score_circle_line_width = 1
    score_circle_fill_color = score_colorset[game_state]
    score_circle_line_color = score_circle_fill_color
    
    # Set Params - Timer Text
    timer_text_string = format(timer_int)
    timer_text_size = 24
    timer_text_color = "#efefef"
    timer_text_loc = [(bg_circle_loc[0]-(10*len(timer_text_string)/2)),
                      (bg_circle_loc[1]+(timer_text_size/3))]
    
    # Set Params - Score Text
    score_text_string = str(score)+"/"+str(attempts)
    score_text_size = 24
    score_text_color = "#545454"
    score_text_loc = [(score_circle_loc[0]-(10*len(score_text_string)/2)),
                      (score_circle_loc[1]+(score_text_size/3))]
    
    # Final Draw
    canvas.draw_polygon(bg_canvas_points,
                        bg_canvas_line_width, bg_canvas_line_color,
                        bg_canvas_fill_color)
    canvas.draw_circle(score_circle_loc, score_circle_radius,
                       score_circle_line_width, score_circle_line_color,
                       score_circle_fill_color)
    canvas.draw_circle(bg_circle_loc, bg_circle_radius,
                       bg_circle_line_width, bg_circle_line_color,
                       bg_circle_fill_color)
    canvas.draw_text(timer_text_string, timer_text_loc, 
                     timer_text_size, timer_text_color)
    canvas.draw_text(score_text_string, score_text_loc, 
                     score_text_size, score_text_color)
    # Cross hairs
    '''
    canvas.draw_line([bg_circle_loc[0]+bg_circle_radius, 0], 
                     [bg_circle_loc[0]+bg_circle_radius, frame_height], 
                     1, "red")
    canvas.draw_line([0, bg_circle_loc[1]-bg_circle_radius], 
                     [frame_width, bg_circle_loc[1]-bg_circle_radius], 
                     1, "red")
    '''
  
# create frame
frame_title = "Stopwatch: The Game"
frame_width = 420
frame_height = 280
frame_control_width = 120
frame = simplegui.create_frame(frame_title, 
                               frame_width, frame_height,
                               frame_control_width)

# register event handlers
# Timer
timer_interval = 100
timer = simplegui.create_timer(timer_interval, timer_handler)

# Draw Handler
draw_canvas = frame.set_draw_handler(draw_handler)

# Start Button
button_start_label = "Start"
button_start_width = button_width
button_start = frame.add_button(button_start_label, 
                                button_start_handler, 
                                button_start_width)

# Stop Button
button_stop_label = "Stop"
button_stop_width = button_width
button_stop = frame.add_button(button_stop_label, 
                               button_stop_handler, 
                               button_stop_width)

# Reset Button
button_reset_label = "Reset"
button_reset_width = button_width
button_reset = frame.add_button(button_reset_label, 
                                button_reset_handler, 
                                button_reset_width)

# Start Stop Button
button_startstop_label = "START/stop"
button_startstop_width = button_width
button_startstop = frame.add_button(button_startstop_label, 
                               button_startstop_handler, 
                               button_startstop_width)


# start frame
print "Welcome to my version of Stopwatch: The Game"
print "Hope the canvas looks pretty"
print "(Some fonts may be wonking the alignments)"
print ""
print "Anyway, you will find an additional button in the controls"
print ""
print "You're welcome"
print ""
print "Get ready for some surprises, even when you miss!!"
frame.start()
# timer.start()
print "="*42
print "Start Timer for a New Game"
print ""
# Please remember to review the grading rubric
