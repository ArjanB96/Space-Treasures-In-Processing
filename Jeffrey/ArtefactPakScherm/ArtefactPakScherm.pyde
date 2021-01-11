
artefacts = ['Swap','Haste','Eyedrop','Skip','Exchange','Blockade']
spelers = ["player1", "player2", "player3", "player4", "player5"]
elements = ["Amaterasu", 'Aqua', "Kaytsak"] 
cards_player1 = []
cards_player2 = []
cards_player3 = []
cards_player4 = []
cards_player5 = []
artefactIndex = 0
elementIndex = 0
spelerIndex = 0
bg_index = 0
opacityCardAddedMsg = 0
opacityTooManyCardsMsg = 0
cardAddedTo = spelers[0]      #temp voor pop up als kaart is toegevoegd aan een speler
whichCardAdded = artefacts[0] #temp voor pop up als kaart is toegevoegd aan een speler
scherm = 'Jeffrey'
frame = 1
interval = 250
rollFirstTime = True
roll_dice = False
display_dice = 0
dice_roll_time = 60
def setup():
    size(1280, 720)
    frameRate(30)
    textFont(createFont('PressStart2P.ttf', 5))
    loadImages()

def draw():
    global scherm, opacityCardAddedMsg, opacityTooManyCardsMsg, frame, dice_roll_time, roll_dice, display_dice, dices
    cycleBackground()

    if scherm == 'Jeffrey':
        fill(0, 0, 0, 100)
        strokeWeight(0)
        rect(10, 115, 360, 90)
        rect(435, 150, 435, 200)

        #Selecteer knoppen
        #dobbelsteen
        if rollFirstTime == True:
            fill(255)
            textSize(15)
            text("Dobbel in het echt of\nklik op de dobbelsteen\nom te rollen en\nkijk of je de\nartefact mag toevoegen!", 20, 140)
        
        if roll_dice and dice_roll_time > 0 and frame % 2 == 0: 
            display_dice = int(random(1, 7)) - 1  
            dice_roll_time -= 5
            print(display_dice)
     
        if dice_roll_time == 0:
            roll_dice = False
        frame = frame + 1 if frame < 60 else 1
        
        #Spelers
        if spelerIndex == 0:
            image(PijlTerugIdle, 435, 150, 55, 55)
        else: image(PijlTerug, 435, 150, 55, 55)
        
        if spelerIndex == 4:
            image(PijlVerderIdle, 815, 150, 55, 55)
        else: image(PijlVerder, 815, 150, 55, 55)
                #Artefacten
        if artefactIndex == 0:
            image(PijlTerugIdle, 435, 250, 55, 55)
        else: image(PijlTerug, 435, 250, 55, 55)
    
        if artefactIndex == 5:
            image(PijlVerderIdle, 815, 250, 55, 55)
        else: image(PijlVerder, 815, 250, 55, 55)
                #Elementen
        if elementIndex == 0:
            image(PijlTerugIdle, 435, 350, 55, 55)
        else: image(PijlTerug, 435, 350, 55, 55)
    
        if elementIndex == 2:
            image(PijlVerderIdle, 815, 350, 55, 55)
        else: image(PijlVerder, 815, 350, 55, 55)
        
        #Variabelen en text, images
        image(LeegVak, 495, 150, 315, 55)
        image(LeegVak, 495, 250, 315, 55)
        image(LeegVak, 495, 350, 315, 55)
        image(TerugKnop, 10, 655, 165, 55)
        image(ToevoegenKnop, 530, 450, 240, 55)
        image(dices[display_dice], 90, 220, 200, 200)
        
    
    
        #berichtje als iemand geen artefacten meer kan toevoegen
        fill(240, opacityTooManyCardsMsg)
        textSize(17)
        tint(opacityTooManyCardsMsg)
        
        if opacityTooManyCardsMsg > 0:
            opacityTooManyCardsMsg -= 2.5
        if len(cards_player1) == 5 and spelerIndex == 0 and opacityTooManyCardsMsg > 0:
            image(LeegVak, 435, 640, 435, 70)
            text('Kan niet meer toevoegen\nje mag max 5 kaarten!', 450, 655, 500, 55)
        elif len(cards_player2) == 5 and spelerIndex == 1 and opacityTooManyCardsMsg > 0:
            image(LeegVak, 435, 640, 435, 70)
            text('Kan niet meer toevoegen\nje mag max 5 kaarten!', 450, 655, 500, 55)
        elif len(cards_player3) == 5 and spelerIndex == 2 and opacityTooManyCardsMsg > 0:
            image(LeegVak, 435, 640, 435, 70)
            text('Kan niet meer toevoegen\nje mag max 5 kaarten!', 450, 655, 500, 55)
        elif len(cards_player4) == 5 and spelerIndex == 3 and opacityTooManyCardsMsg > 0:
            image(LeegVak, 435, 640, 435, 70)
            text('Kan niet meer toevoegen\nje mag max 5 kaarten!', 450, 655, 500, 55)
        elif len(cards_player5) == 5 and spelerIndex == 4 and opacityTooManyCardsMsg > 0:
            image(LeegVak, 435, 640, 435, 70)
            text('Kan niet meer toevoegen\nje mag max 5 kaarten!', 450, 655, 500, 55)
        
        fill(240, opacityCardAddedMsg)
        tint(opacityCardAddedMsg)
        if opacityCardAddedMsg > 0:
            opacityCardAddedMsg -= 2.5
        #berichtje als iemand een artefact heeft toegevoegd
        if len(cards_player1) != 5 and spelerIndex == 0 and opacityCardAddedMsg > 0:
            image(LeegVak, 435, 640, 435, 70)
            text(whichCardAdded + ' toegevoegd aan \n' + cardAddedTo, 450, 655, 500, 55)
        elif len(cards_player2) != 5 and spelerIndex == 1 and opacityCardAddedMsg > 0:
            image(LeegVak, 435, 640, 435, 70)
            text(whichCardAdded + ' toegevoegd aan \n' + cardAddedTo, 450, 655, 500, 55)
        elif len(cards_player3) != 5 and spelerIndex == 2 and opacityCardAddedMsg > 0:
            image(LeegVak, 435, 640, 435, 70)
            text(whichCardAdded + ' toegevoegd aan \n' + cardAddedTo, 450, 655, 500, 55)
        elif len(cards_player4) != 5 and spelerIndex == 3 and opacityCardAddedMsg > 0:
            image(LeegVak, 435, 640, 435, 70)
            text(whichCardAdded + ' toegevoegd aan \n' + cardAddedTo, 450, 655, 500, 55)
        elif len(cards_player5) != 5 and spelerIndex == 4 and opacityCardAddedMsg > 0:
            image(LeegVak, 435, 640, 435, 70)
            text(whichCardAdded + ' toegevoegd aan \n' + cardAddedTo, 450, 655, 500, 55)
            
        tint(255)
        fill(240)
        textSize(17)
        text('Speler:', 600 , 120, 300, 250)
        text('Kies de artefact:', 505, 220, 500, 500)
        text('Kies het element:', 505, 325, 300, 250)
        textAlign(CENTER)
        text(spelers[spelerIndex], 505, 170, 300, 50)
        text(artefacts[artefactIndex], 505, 270, 300, 150)
        text(elements[elementIndex], 505, 370, 300, 250)
        textAlign(CORNER)
        #muis en image knoppen veranderen wanneer muis op knop
           #terug knop
        if isMouseOnButton(10, 655, 165, 55):
            image(TerugKnop2, 10, 655, 165, 55)
            cursor(HAND)
           #toevoegen knop
        elif isMouseOnButton(530, 450, 240, 55):
            image(ToevoegenKnop2, 530, 450, 240, 55)
            cursor(HAND)
           #player knoppen
        elif isMouseOnButton(435, 150, 55, 55) and spelerIndex > 0:
            image(PijlTerug2, 435, 150, 55, 55)
            cursor(HAND)
        elif isMouseOnButton(815, 150, 55, 55) and spelerIndex < 4:
            image(PijlVerder2, 815, 150, 55, 55)
            cursor(HAND)
           #artefact knoppen
        elif isMouseOnButton(435, 250, 55, 55) and artefactIndex > 0:
            image(PijlTerug2, 435, 250, 55, 55)
            cursor(HAND)
        elif isMouseOnButton(815, 250, 55, 55) and artefactIndex < 5:
            image(PijlVerder2, 815, 250, 55, 55)
            cursor(HAND)
           #element knoppen
        elif isMouseOnButton(435, 350, 55, 55) and elementIndex > 0:
            image(PijlTerug2, 435, 350, 55, 55)
            cursor(HAND)
        elif isMouseOnButton(815, 350, 55, 55) and elementIndex < 2:
            image(PijlVerder2, 815, 350, 55, 55)
            cursor(HAND)
        elif isMouseOnButton(90, 200, 200, 200):
            cursor(HAND)
        else: cursor(ARROW)

def mousePressed():
    global rollFirstTime, roll_dice, dice_roll_time, artefactIndex, elementIndex, spelerIndex, scherm, opacityCardAddedMsg, opacityTooManyCardsMsg, cardAddedTo, whichCardAdded
    if scherm == 'Jeffrey':
        if isMouseOnButton(90, 200, 200, 200):
            roll_dice = True
            dice_roll_time = 60
            rollFirstTime = False
        
        #terug knop
        if isMouseOnButton(10, 655, 165, 55):
            print('au')
        
        #Speler selecteer knoppen
        if isMouseOnButton(435, 150, 55, 55):
            if spelerIndex == 0:
                spelerIndex = spelerIndex
            else: spelerIndex -= 1
        if isMouseOnButton(815, 150, 55, 55):
            if spelerIndex == 4:
                spelerIndex = spelerIndex
            else: spelerIndex += 1        
        #Artefact selecteer knoppen
        if isMouseOnButton(435, 250, 55, 55):
            if artefactIndex == 0:
                artefactIndex = artefactIndex
            else: artefactIndex -= 1                
        if isMouseOnButton(815, 250, 55, 55):
            if artefactIndex == 5:
                artefactIndex = artefactIndex
            else: artefactIndex += 1        
        #Element selecteer knoppen
        if isMouseOnButton(435, 350, 55, 55):
            if elementIndex == 0:
                elementIndex = elementIndex
            else: elementIndex -= 1        
        if isMouseOnButton(815, 350, 55, 55):
            if elementIndex == 2:
                elementIndex = elementIndex
            else: elementIndex += 1                
    
        #toevoegen knop
        if isMouseOnButton(530, 450, 240, 55): 
            #artefact tevoegen aan speler
            if spelerIndex == 0:
                if len(cards_player1) != 5:
                    cards_player1.append([artefacts[artefactIndex], elements[elementIndex]])
                    opacityCardAddedMsg = 255
                    cardAddedTo = spelers[spelerIndex]
                    whichCardAdded = artefacts[artefactIndex]
                    opacityTooManyCardsMsg = 255
                elif len(cards_player1) == 5:
                    opacityTooManyCardsMsg = 255
            elif spelerIndex == 1:
                if len(cards_player2) != 5:
                    cards_player2.append([artefacts[artefactIndex], elements[elementIndex]])
                    opacityCardAddedMsg = 255
                    cardAddedTo = spelers[spelerIndex]
                    whichCardAdded = artefacts[artefactIndex]
                    opacityTooManyCardsMsg = 255
                elif len(cards_player2) == 5:
                    opacityTooManyCardsMsg = 255
            elif spelerIndex == 2:
                if len(cards_player3) != 5:
                    cards_player3.append([artefacts[artefactIndex], elements[elementIndex]])
                    opacityCardAddedMsg = 255
                    cardAddedTo = spelers[spelerIndex]
                    whichCardAdded = artefacts[artefactIndex]
                    opacityTooManyCardsMsg = 255
                elif len(cards_player3) == 5:
                    opacityTooManyCardsMsg = 255
            elif spelerIndex == 3:
                if len(cards_player4) != 5:
                    cards_player4.append([artefacts[artefactIndex], elements[elementIndex]])
                    opacityCardAddedMsg = 255
                    cardAddedTo = spelers[spelerIndex]
                    whichCardAdded = artefacts[artefactIndex]
                    opacityTooManyCardsMsg = 255
                elif len(cards_player4) == 5:
                    opacityTooManyCardsMsg = 255
            elif spelerIndex == 4:
                if len(cards_player5) != 5:
                    cards_player5.append([artefacts[artefactIndex], elements[elementIndex]])
                    opacityCardAddedMsg = 255
                    cardAddedTo = spelers[spelerIndex]
                    whichCardAdded = artefacts[artefactIndex]
                    opacityTooManyCardsMsg = 255
                elif len(cards_player5) == 5:
                    opacityTooManyCardsMsg = 255
            
        
            
    
def isMouseOnButton(posX, posY, buttonWidth, buttonHeight, centered = False):
  if centered:
   return True if posX - buttonWidth / 2 < mouseX < posX + buttonWidth / 2 and posY - buttonHeight / 2 < mouseY < posY + buttonHeight / 2  else False
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

def loadImages():
    global background_img, background_animation_images, PijlVerderIdle, dices, PijlTerugIdle, PijlTerug, PijlTerug2, PijlVerder, PijlVerder2, LeegVak, TerugKnop, TerugKnop2, ToevoegenKnop, ToevoegenKnop2
    dices = []
    for i in range(1, 7):
        dices.append(loadImage('images/bot' + str(i) + '.gif'))
    PijlTerugIdle = loadImage('images/PijlTerugIdle.png')
    PijlVerderIdle = loadImage('images/PijlVerderIdle.png')
    PijlTerug = loadImage('images/PijlTerugPaars.png')
    PijlTerug2 = loadImage('images/PijlTerug2Paars.png')
    PijlVerder = loadImage('images/PijlVerderPaars.png')
    PijlVerder2 = loadImage('images/PijlVerder2Paars.png')
    LeegVak =  loadImage('images/LeegVak.png')
    TerugKnop = loadImage('images/TerugKnop.png')
    TerugKnop2 = loadImage('images/TerugKnop2.png')
    ToevoegenKnop = loadImage('images/Toevoegen.png')
    ToevoegenKnop2 = loadImage('images/Toevoegen2.png')
    background_img = loadImage('background/bg0.jpg')
    background_animation_images = [loadImage('background/bg' + str(i) + '.jpg') for i in range(1, 14)]

    
