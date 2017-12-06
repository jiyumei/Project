ball_size = 50

non_speed_1 = PVector(3, 6)
non_speed_2 = PVector(6, 4)

non_pos_1 = PVector(random(0, 700))
player_pos = PVector(0,0)

score = 0

def setup():
    size(700, 700)
    
def draw():
    global non_pos_1
    global non_speed_1
    global player_pos
    global score
    
    background(255)
    
    #player sprite
    player_pos.x = mouseX
    player_pos.y = mouseY
    
    noStroke()
    fill(216, 252, 98)
    ellipse(mouseX, mouseY, 50, 50)
    
    #non player sprite 1
    fill(200)
    ellipse(non_pos_1.x, non_pos_1.y, 50, 50)
    
    non_pos.add(non_speed_1)
  
    if non_pos_1.x > width:
        non_pos.x = width
        non_speed_1.x = -non_speed_1.x
    elif non_pos.x < 0:
        non_pos.x = 0
        non_speed_1.x = -non_speed_1.x
    
    if non_pos.y > height:
        non_pos.y = height
        non_speed_1.y = -non_speed_1.y
    elif non_pos.y < 0:
        non_pos.y = 0
        non_speed_1.y = -non_speed_1.y
 
  #score
    textSize(30)
    text("score:", 20, 40)
    text(score, 115, 40)
    fill(0)
