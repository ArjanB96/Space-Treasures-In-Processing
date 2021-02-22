import sys
bg_index = 0
frame = 1

go_back = False
roll_dice = False
display_dice = 0
dice_roll_time = 60

def setup():
    loadImages()    
    
    size(1280, 720)    
    
def draw():
    global frame, dice_roll_time, roll_dice, display_dice, back, back2
    
    cycleBackground()
    
    back = loadImage('TerugKnop.png')
    back2 = loadImage('TerugKnop2.png')
    image(back, 100, 600, 150, 50)
    
    fill(255)
    textFont(createFont('PressStart2P.ttf', 30))
    text("Klik op de dobbelsteen om te rollen!", 95, 100)
    
    if isMouseOnButton(500, 250, 200, 200):
        cursor(HAND)
    elif isMouseOnButton(100, 600, 150, 50):
        image(back2, 100, 600, 150, 50)
        cursor(HAND)
    else:
        cursor(ARROW)
    
    if roll_dice and dice_roll_time > 0 and frame % 5 == 0: 
        display_dice = int(random(1, 7)) - 1  
        dice_roll_time -= 5
    
    if go_back:
        sys.exit()
        
    image(dices[display_dice], 500, 250, 200, 200)
        
    if dice_roll_time == 0:
        roll_dice = False
        
    frame = frame + 1 if frame < 60 else 1
    
def mousePressed():
    global roll_dice, dice_roll_time, go_back
    
    if isMouseOnButton(500, 250, 200, 200):
        roll_dice = True
        dice_roll_time = 60
    
    if isMouseOnButton(100, 600, 150, 50):
        go_back = True

def loadImages():
    global dices, background_img, background_animation_images
    dices = []
    
    for i in range(1, 7):
        dices.append(loadImage('bot' + str(i) + '.gif'))
    
    background_img = loadImage('bg0.jpg')
    background_animation_images = [loadImage('bg' + str(i) + '.jpg') for i in range(1, 14)]
    
def isMouseOnButton(posX, posY, buttonWidth, buttonHeight, centered = False):
  if centered:
    return True if posX - buttonWidth / 2 < mouseX < posX + buttonWidth / 2 and posY - buttonHeight / 2 < mouseY < posY + buttonHeight / 2 else False
  return True if posX < mouseX < posX + buttonWidth and posY < mouseY < posY + buttonHeight else False
    
interval = 250

def cycleBackground():
    global bg_index, interval, play_stars_animation
    
    if interval <= 0:
        if bg_index < len(background_animation_images):            
            background(background_animation_images[bg_index])
            bg_index += 1
            if bg_index == 13:
                interval = 250
                bg_index = 0
    else:
        background(background_img)

    interval -= 1