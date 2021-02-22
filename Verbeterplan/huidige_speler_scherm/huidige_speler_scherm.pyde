bg_index = 0
interval = 250
kaart_pakken_popup = False
artefact_gebruiken_popup = False
no_pop_up = False
playername = "Spelersnaam"          # <-- hier kan je fixen dat de spelersnaam per beurt naar een andere speler gaat

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
    image(GrootLeegvak, 290, 430, 295, 140)
    image(GrootLeegvak, 710, 430, 295, 140)
    image(GrootLeegvak, 360, 60, 595, 120)        # leeg vlak voor welke speler aan de beurt is
    
    
    if (kaart_pakken_popup == False and artefact_gebruiken_popup == False):
        if isMouseOnButton(10, 10, 175, 55):
            image(Regels2, 10, 10, 175, 55)
            cursor(HAND)
        elif isMouseOnButton(290, 430, 295, 140):
            image(GrootLeegvak2, 290, 430, 295, 140)
            cursor(HAND)
            cursor(HAND)
        elif isMouseOnButton(710, 430, 295, 140):
            image(GrootLeegvak2, 710, 430, 295, 140)
            cursor(HAND)
        else: cursor(ARROW)
        
    fill(255)        
    textSize(30)        
    text("Kies wat wil je doen", 385, 305)
    text("Kaart\npakken", 345, 500)
    textSize(27)
    text("Artefact\ngebruiken", 735, 500)
    text(playername, 490, 140)                    # line met de variable , check line 4!!!
    
    if (kaart_pakken_popup == True):                ## line 45 tm 57 is de popup voor kaarten pakken 
        image(GrootLeegvak, 250, 50, 800, 500)
        image(PijlVerder, 950, 450, 55, 55)
        if isMouseOnButton(950, 450, 55, 55):
            image(PijlVerder2, 950, 450, 55, 55)
            cursor(HAND)
        else:
            cursor(ARROW)
        
        textSize(30)
        text("Pak een kaart", 475, 200)
        textSize(15)  
        text("Pak een kaart, moet hier nog extra tekst bij?\n IDK maar de optie is er in ieder geval ", 285, 300)

    if artefact_gebruiken_popup == True:    ##line 59 tm 71 is voor artefact gebruiken popup
        image(GrootLeegvak, 250, 50, 800, 500)
        image(PijlVerder, 950, 450, 55, 55)
        if isMouseOnButton(950, 450, 55, 55):
            image(PijlVerder2, 950, 450, 55, 55)
            cursor(HAND)
        else:
            cursor(ARROW)
        
        textSize(30)
        text("Gebruik je artefact", 375, 200)
        textSize(15)  
        text("Pak een kaart, moet hier nog extra tekst bij?\n IDK maar de optie is er in ieder geval ", 285, 300)
        
        
def mousePressed():
    global kaart_pakken_popup, artefact_gebruiken_popup
    if (kaart_pakken_popup == False):
        #regels knop
        if isMouseOnButton(10, 10, 175, 55):
            print("Regels") # <-------------------- Ga naar regelscherm
            
        if isMouseOnButton(290, 430, 295, 140): #Kaarten pak knop
            kaart_pakken_popup = True
            
        if isMouseOnButton(710, 430, 295, 140): #Artefact gebruiken knop
            artefact_gebruiken_popup = True
            
    elif kaart_pakken_popup == True:
        if isMouseOnButton(950, 450, 55, 55):
            print("Scherm Jeffrey")   
            kaarten_pakken_popup = False              # !!!Ga naar het scherm van Jeffrey met Stappen zetten / artefact toevoegen / element maken!!!
            
    elif artefact_gebruiken_popup == True:
        if isMouseOnButton(950, 450, 55, 55):
            print("Scherm Hayk")                           # !!!Ga naar het scherm van Hayk!!!
            artefact_gebruiken_popup = False
            
        
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
