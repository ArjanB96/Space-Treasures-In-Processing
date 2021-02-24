bg_index = 0
screen = 0
interval = 250

        
def setup():
    loadImages()    
    textFont(createFont('PressStart2P.ttf', 40))
    size(1280, 720)  


def draw():
    global screen

    cycleBackground()
    mouseHoverHandler()
    
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
        text('Voordat het spel gestart\n kan worden moet het\n bordspel opgezet worden.\n\n Hier volgen de stappen om\n dit te doen.', 640, 375)
    
    if screen == 1:
        
        fill(255, 255, 255)
        textSize(45)
        textAlign(CENTER, CENTER)
        text('Voorbereiding', 640, 100)
        
        fill(255, 255, 255)
        textSize(25)
        textAlign(CENTER, CENTER)
        text('Stap 1: Open de speeldoos van\n Space Treasures en leg het\n bordstuk Aarde neer.\n\n Pak vervolgens het brandstof\n fiche en leg die in het midden\n van het bordstuk Aarde.', 640, 375)
        
    if screen == 2:
        
        fill(255, 255, 255)
        textSize(45)
        textAlign(CENTER, CENTER)
        text('Voorbereiding', 640, 100)
        
        fill(255, 255, 255)
        textSize(25)
        textAlign(CENTER, CENTER)
        text('Stap 2: Schud de stapel\n van de overige\n bordstukken en bewaar\n ze voor later in het\n spel.', 640, 375)
        
    if screen == 3:
        
        fill(255, 255, 255)
        textSize(45)
        textAlign(CENTER, CENTER)
        text('Voorbereiding', 640, 100)
        
        fill(255, 255, 255)
        textSize(25)
        textAlign(CENTER, CENTER)
        text('Stap 3: Iedere speler pakt\n een ruimteschip. Vervolgens\n kiest elke speler een van de\n zes buitenste hoeken en\n plaatst daar zijn pionnen.', 640, 375)
    
    if screen == 4:
        
        fill(255, 255, 255)
        textSize(45)
        textAlign(CENTER, CENTER)
        text('Voorbereiding', 640, 100)
        
        fill(255, 255, 255)
        textSize(25)
        textAlign(CENTER, CENTER)
        text('Stap 4: Schud de\n instructiekaarten en leg\n deze naast het bordstuk.', 640, 375)
        
    if screen == 5:
        
        fill(255, 255, 255)
        textSize(45)
        textAlign(CENTER, CENTER)
        text('Voorbereiding', 640, 100)
        
        fill(255, 255, 255)
        textSize(25)
        textAlign(CENTER, CENTER)
        text('Stap 5: Geef elke speler\n fysiek een fiche van elk\n element.\n\n De fiches worden naast\n elkaar neergelegd. Deze\n fiches hebben het doel om\n de artefacten te sorteren\n op basis van elementen.\n\n Bij het verkrijgen van een\n artefact leg je het\n artefact neer bij het\n bijbehorende fiche.', 640, 375)
        
          
    tint(255)     
    imageMode(CENTER)     
    if screen == 0:
        image(pijlTerugIdle, 50, 360, 84, 78)
    else:
        imageShow(pijlTerugPaars, pijlTerug2Paars, 50, 360, 84, 78, True)
    
    if screen == 5:
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
    
def mousePressed():
    global screen
    
    if screen == 0:
        if isMouseOnButton(1230 , 360, 84, 78, True):
            screen += 1
            
    elif screen == 1:
        if isMouseOnButton(1230 , 360, 84, 78, True):
            screen += 1
        elif isMouseOnButton(50 , 360, 84, 78, True):
            screen -= 1
    
    elif screen == 2:
        if isMouseOnButton(1230 , 360, 84, 78, True):
            screen += 1
        elif isMouseOnButton(50 , 360, 84, 78, True):
            screen -= 1
            
    elif screen == 3:
        if isMouseOnButton(1230 , 360, 84, 78, True):
            screen += 1
        elif isMouseOnButton(50 , 360, 84, 78, True):
            screen -= 1
            
    elif screen == 4:
        if isMouseOnButton(1230 , 360, 84, 78, True):
            screen += 1
        elif isMouseOnButton(50 , 360, 84, 78, True):
            screen -= 1
    
    elif screen == 5:
        if isMouseOnButton(50 , 360, 84, 78, True):
            screen -= 1
        
        
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
    
def mouseHoverHandler():
    global screen
    
    if isMouseOnButton(50, 360, 84, 78, True) and screen != 0:
        cursor(HAND)   

    elif isMouseOnButton(1230, 360, 84, 78, True) and screen != 5:
        cursor(HAND)
    else:
        cursor(ARROW)
    


    
  
