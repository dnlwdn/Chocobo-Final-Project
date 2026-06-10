 ## Assignment: Final Project
 ## Student: Daniel Wooden
 ## Pasadena City College, Spring 2026
 ## Course Name: DMA60 Creative Coding
 ## Prof. George McKinney
 ## Project Description: This project is a simple interactive mini game based by the Final Fantasy series where you control the CHOCOBO to collect 10 eggs that randomly appear around the environment with your mouse. CHOCOBO is a famous iconic species from the Final Fantasy series.
 ## Last Modified: 6/9/26

img_x, img_y = 100, 100
img_w, img_h = 50, 50
cursor_img = None
score = 0

def setup():
    size(500, 500)
    background(245)
    frameRate(15)
    global img
    global cursor_img
    ## adding image of eggs
    img = loadImage("snake_egg copy.png")
    ## chocobo character 
    cursor_img = loadImage("chocobo_2.png")
    
def draw_grass():
    tile_size = 25
    for x in range(0, width, tile_size):
        for y in range(0, height, tile_size):
            if (x // tile_size + y // tile_size) % 2 == 0:
                fill(155, 188, 15)
            else:
                fill(140, 170, 10)
            noStroke()
            rect(x, y, tile_size, tile_size)

def draw():
    global img_x, img_y, score
    draw_grass()

    if score < 10: ## game is still in progress if less than 10 eggs is caught
        ## when mouse moves over egg
        if (img_x <= mouseX <= img_x + img_w and
            img_y <= mouseY <= img_y + img_h):
            ## moving egg to random area
            img_x = random(width - img_w)
            img_y = random(height - img_h)

            score += 1
            
        tint(255, 240, 200) ## adding tint to egg
        image(img, img_x, img_y, img_w, img_h)
        noTint()
   
    else: ## score reached 10! GAME WON!
        if (frameCount % 60 < 30):
            textSize(28)
            textAlign(CENTER)
            fill(255, 255, 0)
            text("YAY! YOU CAUGHT THEM ALL!!!", 250, 250) ## blinking text

        textSize(16)
        fill(0)
    
    ## score box
    textSize(24)
    textAlign(CENTER)
    fill(0, 0, 0, 150)  ## transparent box
    noStroke()
    rect(100, 8, 300, 35, 10)  ## rounded corners
    fill(255, 255, 0)
    text("EGGS CAUGHT: " + str(score), 250, 32)
    textAlign(LEFT) ## keeping score
    
    image(cursor_img, mouseX, mouseY)  ## chocobo character
    
    
def mousePressed():
    print("Yoco WARKS!") ## its like a bark noise as an example, wish I can add audio here
    
name = "Yoco"
class Companion():
    species = "Chocobo" ## class variable belonging to the class
    def __init__(self, name="Yoco"):
        self.name = "Yoco"
    def companionMethod(self): ## method functions
        print (self.name + " says: Class! We made it, congrats everyone! ^_^ <3") 
        
c = Companion() ## instances of class
c.companionMethod() ## methods functions of class
