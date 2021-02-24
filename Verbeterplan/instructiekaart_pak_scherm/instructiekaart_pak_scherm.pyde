bg_index = 0
interval = 250
stappenzettenPopUp = False
kanElementMaken = False
kanGeenElementMakenPopUp = False
def setup():
    size(1280, 720)
    frameRate(30)
    textFont(createFont('PressStart2P.ttf', 5))
    loadImages()
    
def draw():
    cycleBackground()
    textFont(createFont('data/PressStart2P.ttf', 5))
    
    #images
    image(Regels, 10, 10, 175, 55)
    image(GrootLeegvak, 80, 430, 295, 140)
    image(GrootLeegvak, 480, 430, 295, 140)
    image(GrootLeegvak, 880, 430, 295, 140)
    
    if (stappenzettenPopUp == False and kanGeenElementMakenPopUp == False):
        if isMouseOnButton(10, 10, 175, 55):
            image(Regels2, 10, 10, 175, 55)
            cursor(HAND)
        elif isMouseOnButton(80, 430, 295, 140):
            image(GrootLeegvak2, 80, 430, 295, 140)
            cursor(HAND)
        elif isMouseOnButton(480, 430, 295, 140):
            image(GrootLeegvak2, 480, 430, 295, 140)
            cursor(HAND)
        elif isMouseOnButton(880, 430, 295, 140):
            image(GrootLeegvak2, 880, 430, 295, 140)
            cursor(HAND)
        else: cursor(ARROW)
        
    fill(255)        
    textSize(30)        
    text("Pak een kaart van de stapel", 225, 145)
    text("Wat wil je doen?", 385, 305)
    text("Stappen\nzetten", 125, 500)
    text("Artefact\npakken", 515, 500)
    text("Element\nmaken", 925, 500)
    
    if (stappenzettenPopUp == True):
        image(GrootLeegvak, 250, 50, 800, 500)
        image(PijlVerder, 950, 450, 55, 55)
        if isMouseOnButton(950, 450, 55, 55):
            image(PijlVerder2, 950, 450, 55, 55)
            cursor(HAND)
        else:
            cursor(ARROW)
        
        textSize(29)
        text("Zet nu het aantal stappen\naangegeven op de kaart", 285, 200)
        textSize(15)  
        text("Als je op een brandstof icoontje staat moet\nje een nieuwe planeet neerleggen naast\nde planeet waar je nu op staat\ndit kan 1 keer per planeet", 285, 300)
        
    if (kanGeenElementMakenPopUp == True):
        image(GrootLeegvak, 250, 250, 800, 300)
        image(PijlVerder, 950, 450, 55, 55)
        if isMouseOnButton(950, 450, 55, 55):
            image(PijlVerder2, 950, 450, 55, 55)
            cursor(HAND)
        else:
            cursor(ARROW)
        textSize(22)  
        text("Kan geen element maken\nje hebt minimaal drie artefacten\nnodig met hetzelfde element.", 290, 350)
    
def mousePressed():
    global stappenzettenPopUp, kanGeenElementMakenPopUp
    if (stappenzettenPopUp == False and kanGeenElementMakenPopUp == False):
        #regels knop
        if isMouseOnButton(10, 10, 175, 55):
            print("naar regels toe") #<-- naar regels to
        #stappen zetten knop
        if isMouseOnButton(80, 400, 300, 200):
            stappenzettenPopUp = True 
        #artefact toevoegen knop
        if isMouseOnButton(480, 400, 300, 200):
            print("naar artefact toevoeg scherm")    #<-- naar artefact toevoegen scherm
        #element maken knop    
        if isMouseOnButton(880, 400, 300, 200) and kanElementMaken == True :
            print("element maak scherm") #<--- naar element maken scherm
        elif isMouseOnButton(880, 400, 300, 200) and kanElementMaken == False :
            kanGeenElementMakenPopUp = True
    elif stappenzettenPopUp == True:
        if isMouseOnButton(950, 450, 55, 55):
            stappenzettenPopUp = False
            print("naar ander scherm, door naar volgende beurt ") #<-- naar volgende beurt/huidige speler scherm
    elif kanGeenElementMakenPopUp == True:
        if isMouseOnButton(950, 450, 55, 55):
            kanGeenElementMakenPopUp = False
        
def isMouseOnButton(posX, posY, buttonWidth, buttonHeight, centered = False):
  if centered:
   return True if posX - buttonWidth / 2 < mouseX < posX + buttonWidth / 2 and posY - buttonHeight / 2 < mouseY < posY + buttonHeight / 2  else False
  return True if posX < mouseX < posX + buttonWidth and posY < mouseY < posY + buttonHeight else False
    
def cycleBackground():
    global bg_index, interval
    
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
    
def loadImages():
    global background_img, background_animation_images, Regels, Regels2, GrootLeegvak, GrootLeegvak2, PijlVerder, PijlVerder2
    background_animation_images = [loadImage('background/bg' + str(i) + '.jpg') for i in range(1, 14)]
    background_img = loadImage('background/bg0.jpg')
    Regels = loadImage('images/Regels.png')
    Regels2 = loadImage('images/Regels2.png')
    GrootLeegvak = loadImage('images/GrootLeegvak.png')
    GrootLeegvak2 = loadImage('images/GrootLeegvak2.png')
    PijlVerder = loadImage('images/PijlVerderPaars.png')
    PijlVerder2 = loadImage('images/PijlVerder2Paars.png')
