"""
Create a dodging game.
Ellipses will start at the top of the screen and 
fall downwards. 
The player controls the movement of an ellipse 
at the bottom of the screen using the mouse.
The player must dodge the falling ball
Steps:
    1. Create an ellipse with its own 
    position variables. Draw it in the draw() function
    This will be the falling ball.
    2. Make this ball "fall" by giving it a y-speed.
    Update its location in the draw() function.
    Also give it an x-speed, but keep it at 0
    (unless you want to mess around a bit).
    3. When the ball hits the bottom of the screen,
    reset its position to the top of the window.
    You can assign the x-position to a random value.
    Maybe even assign the y-speed to a random value 
    as well. Also, possibly create a second falling 
    ball.
    4. Create the PLAYER ellipse with its own position
    variables. The position of the PLAYER will update
    every draw loop. In the draw loop, bind the 
    x-location variable to the mouseX variable.
    Keep this ball at the bottom of the screen. 
    Draw this ball in the draw() function.
    This will be the player.
    5. In the draw() function determine if the two
    ellipses are touching:
        a) Use pythagorean theorem to find out the 
        distance (hypotenuse) between the two origins.
        b) check to see if the distance is less than 
        the two ellipse radii. (Radiuses)
"""
# Falling Ball Game! - Fiona Lin

ballX = 30
ballY = 20
ballSize = 30
speedX = 0
speedY = 5
score = 0

def setup():
    size(400, 600)

def draw():
    background(255)
    # background
    beginning = color(5, 5, 99)
    ending = color(5, 201, 187)
    for i in range(701):
        stroke(lerpColor(beginning, ending, i / 750.0))
        line(0, i, width, i)

    # Ball
    global ballX
    global ballY
    global ballSize

    noFill()
    stroke(64, 31, 0)
    strokeWeight(5)
    ellipse(ballX, ballY, ballSize, ballSize)

    # Ball Falling
    global speedY
    global score
    ballY += speedY
    
    if ballY > height:
        ballY = 0
        ballX = random(0, 380)
        score += 1
    
    #The Player
    ballY2 = 570
    ballX2 = mouseX
    
    noStroke()
    fill(252, 230, 112)
    ellipse(ballX2, ballY2, ballSize, ballSize)
    
    #Score
    textSize(30)
    fill(255)
    text(score, 20, 50)
    
    #Detection
    radius = ballSize/2
    
    distanceX = (ballX - ballX2)
    distanceY = (ballY - ballY2)
    hyp = sqrt(distanceX ** 2 + distanceY ** 2) 
    if hyp <= radius:
        score = 0 - 1
        
    #Score Text
    if score >= 10:
        textSize(30)
        fill(255)
        text("Congrats! You won!", 50, 200)
