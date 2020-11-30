bg_index = 0
frame = 1

dices = []
roll_dice = False
display_dice = 0
dice_roll_time = 60

def setup():
    cycleBackground()
    
    loadImages()    
    
    size(1280, 720)    
    
def draw():
    global frame, dice_roll_time, roll_dice, display_dice
    
    cycleBackground()
    
    if isMouseOnButton(500, 250, 200, 200):
        cursor(HAND)
    else:
        cursor(ARROW)
    
    if roll_dice and dice_roll_time > 0 and frame % 2 == 0: 
        display_dice = int(random(1, 7)) - 1  
        dice_roll_time -= 1
    
    image(dices[display_dice], 500, 250, 200, 200)
        
    if dice_roll_time == 0:
        roll_dice = False
        
    frame = frame + 1 if frame < 60 else 1
        
def mousePressed():
    global roll_dice, dice_roll_time
    
    if isMouseOnButton(500, 250, 200, 200):
        roll_dice = True
        dice_roll_time = 60

def loadImages():
    global dices
    
    for i in range(1, 7):
        dices.append(loadImage('bot' + str(i) + '.gif'))
    
def isMouseOnButton(posX, posY, buttonWidth, buttonHeight, centered = False):
  if centered:
    return True if posX - buttonWidth / 2 < mouseX < posX + buttonWidth / 2 and posY - buttonHeight / 2 < mouseY < posY + buttonHeight / 2 else False
  return True if posX < mouseX < posX + buttonWidth and posY < mouseY < posY + buttonHeight else False
    
def cycleBackground():
    global bg_index
    background(loadImage('bg' + str(bg_index) + '.jpg'))
    bg_index = bg_index + 1 if bg_index < 32 else 0
