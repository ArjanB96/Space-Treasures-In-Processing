bg_index = 0
screen = 0
opacityText = 0
interval = 250

        
def setup():
    loadImages()    
    textFont(createFont('PressStart2P.ttf', 40))
    size(1280, 720)  


def draw():

    cycleBackground()
    
    pijlTerugPaars = loadImage('data/PijlTerugPaars.png')
    pijlTerug2Paars = loadImage('data/PijlTerug2Paars.png')
    pijlTerugIdle = loadImage('data/PijlTerugIdle.png')
    pijlVerderPaars = loadImage('data/PijlVerderPaars.png')
    pijlVerder2Paars = loadImage('data/PijlVerder2Paars.png')
    pijlVerderIdle = loadImage('data/PijlVerderIdle.png')
    
    if screen == 0:
        
        fill(255, 255, 255)
        textSize(45)
        textAlign(CENTER, CENTER)
        text('Voorbereiding', 640, 100)
        
        fill(255, 255, 255)
        textSize(25)
        textAlign(CENTER, CENTER)
        text('Voordat het spel gestart\n kan worden moet het\n bordspel opgezet worden.\n\n hier volgen de stappen om\n dit te doen. Om een stap\n verder te gaan druk je op\n het pijltje rechts.\n\n Mocht je een stap terug\n willen kan je op het pijltje\n naar links drukken.', 640, 375)
        
    tint(255)     
    imageMode(CENTER)     
    if screen == 0:
        image(pijlTerugIdle, 50, 360, 84, 78)
    else:
        imageShow(pijlTerugPaars, pijlTerug2Paars, 50, 360, 84, 78, True)
    
    if screen == 15:
        image(pijlVerderIdle, 1230, 360, 84, 78)
    else:
        imageShow(pijlVerderPaars, pijlVerder2Paars, 1230, 360, 84, 78, True)


        
def loadImages():
    global background_img, background_animation_images
    
    background_img = loadImage('bg0.jpg')
    background_animation_images = [loadImage('bg' + str(i) + '.jpg') for i in range(1, 14)]
    
def imageShow(img, img2, x, y, wdth, hght, centered = False, wdthAdd = 0, wdthMinus = 0):
    imageMode(CENTER if centered else CORNER)
    if isMouseOnButton(x - wdthMinus, y, wdth + wdthAdd, hght, centered):
        image(img2, x, y, wdth, hght)
    else:
        image(img, x, y, wdth, hght)
    
def isMouseOnButton(posX, posY, buttonWidth, buttonHeight, centered = False):
  if centered:
    return True if posX - buttonWidth / 2 < mouseX < posX + buttonWidth / 2 and posY - buttonHeight / 2 < mouseY < posY + buttonHeight / 2 else False
  return True if posX < mouseX < posX + buttonWidth and posY < mouseY < posY + buttonHeight else False
    

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
