"""
Create a 2-player clicking game.
1. Draw an ellipse at a random location on the screen. Be sure to
   store the location info in x/y position variables (or PVector?)
2. Define a mousePressed() function. When the user clicks,
   assign a new location to the ball.
3. Create a score variable. When the user clicks (same function above,
   add +1 to the score.
4. Display the score using the text() function.
5. Now, when the user clicks, use the mouseX and mouseY variables, within the
   previously defined mousePressed() function, compare those values to the 
   location of the ellipse. 
   If the mouse location is within a certain range, then you add to the 
   score and change the ellipse location.
6. Split the board visually in the middle. One side will be for player 1, the
   other for player2. Each will have their own ball to click...
7. Add a second ball, with its own position variable, and its own score, and
   its own click detection in the already defined mousePressed() function.
8. If a player reaches a score of 10, they win. Code this.
"""
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
    
    Ball (Player Two)
    global ballX2
    global ballY2
    
    stroke(43, 20, 3)
    fill(255, 252, 192)
    ellipse(ballX2, ballY2, ballSize, ballSize)
    
    #Score
    global score1
    
    textSize(20)
    fill(201, 248, 247)
    text(score1, 20, 30)
    
def mousePressed():

    global ballX1
    global ballY1
    global ballSize
    global score1
    
    #Click Detection 
    radius = ballSize / 2.0
    
    distanceX1 = abs(mouseX - ballX1)
    distanceY1 = abs(mouseY - ballY1)
    hypotenuse = sqrt(distanceX1 ** 2 + distanceY1 ** 2) 
    if hypotenuse <= radius:
        ballX1 = random(10, 390)
        ballY1 = random(10, 390)
        score1 += 1
    
        
    

    
    
        
        
        
        
        
     
