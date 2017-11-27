
def setup():
    size(400, 400)
    
def draw():
    background(255)
    
    #sky
    beginning = color(5, 5, 99)
    ending = color(5, 201, 187)
    
    for i in range(401):
        stroke(lerpColor(beginning, ending, i/500.0))
        line(0, i, width, i)
        
    #skyscaper
    noStroke()
    fill(0)
    rect(100, 70, 120, 400)
    
    #checker windows 
    noStroke()
    fill(255, 255, 171)    
    
    for x in range (110, 200, 40):       #(110, +40 makes one column), 40)
        rect(x, 80, 15, 15)
        for y in range(80, 470, 30):     
            #(x-coordinate of top left corner, how many squares added together, space between each square)
            rect(x, y, 15, 15)  
            
    noStroke()
    fill(255, 255, 171)
    
    for x in range (125, x, y):
        rect(x, 
    