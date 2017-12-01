"""
#Ball Game! - Fiona Lin

ballSize = 50

ballX1 = 50
ballY1 = 50
score1 = 0

ballX2 = 750
ballY2 = 50
score2 = 0

def setup():
    size(800, 400)
    
def draw():
    #Background (Player One)
    background(255, 175, 136)
    #Background (Player Two)
    fill(84, 3, 4)
    noStroke()
    rect(400, 0, 400, 400)
    
    #Ball (Player One)
    global ballX1 
    global ballY1
    global ballSize
    
    fill(0)
    stroke(255, 252, 192)
    ellipse(ballX1, ballY1, ballSize, ballSize)
    
    #Ball (Player Two)
    global ballX2
    global ballY2
    
    stroke(43, 20, 3)
    fill(255, 252, 192)
    ellipse(ballX2, ballY2, ballSize, ballSize)
    
    #Score
    global score1
    global score2
    
    textSize(20)
    fill(201, 248, 247)
    text(score1, 20, 30)
    text(score2, 420, 30)
    
    #Winner
    if score1 == 10:
        textSize(40)
        fill(255)
        text("Winner!!!", 200, 200)
    elif score2 == 10:
        textSize(40)
        fill(255)
        text("Winner!!!", 600, 200)
        
def mousePressed():

    global ballX1
    global ballY1
    global ballSize
    global score1
    
    global ballX2
    global ballY2
    global score2
    
    #Click Detection (Player One) 
    radius = ballSize / 2.0
    
    distanceX1 = abs(mouseX - ballX1)
    distanceY1 = abs(mouseY - ballY1)
    hypotenuse = sqrt(distanceX1 ** 2 + distanceY1 ** 2) 
    if hypotenuse <= radius:
        ballX1 = random(10, 390)
        ballY1 = random(10, 390)
        score1 += 1
    #Click Detection (Player Two)
    
    distanceX2 = abs(mouseX - ballX2)
    distanceY2 = abs(mouseY - ballY2)
    hypotenuse2 = sqrt(distanceX2 ** 2 + distanceY2 ** 2) 
    if hypotenuse2 <= radius:
        ballX2 = random(400, 800)
        ballY2 = random(200, 400)
        score2 += 1
