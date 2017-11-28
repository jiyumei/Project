# 1. Create variables for a ball that moves 
# You need a x-position, x-position
# also a x-speed and y-speed variable
#2. Convert the variables to PVector objects. 
#    Objects have:
#      attributes - info for specific object (i.e., location)
#      behaviours - things they can DO (methods like .add())


position = PVector(50, 50)     
speed = PVector(3, 6)

def setup():
    frameRate(60)
    size(300, 300)
    background(255)
    
def draw():
    global position
    global speed
    
    position.add(speed)      #equal to speed.x += and speed.y += 
    
    background(255)
    ellipse(position.x, position.y, 30, 30)
    
    # 3. Get the ball to bounce along the border.
    if position.x > width:
        position.x = width
        speed.x = -speed.x
    elif position.x < 0:
        position.x = 0
        speed.x = -speed.x
    
    if position.y > height:
        position.y = height
        speed.y = -speed.y
    elif position.y < 0:
        position.y = 0
        speed.y = -speed.y
        
    # 4. Get the mouse to attract the ball.
    #      - create a new vector using the mouse 
    #        location variables mouseX and mouseY.
    #      - Use the PVector sub() method
    #        https://processing.org/reference/PVector_sub_.html
    #      - Print out the angle using the heading()
    #        function. This prints out the angle in radians
    #      - Use the degrees() function to convert radians to degrees.
    #change speed to 0, 0
    #set speed to diff between two vector points

