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

scherm = 'Jeffrey'
def setup():
    size(1280, 720)
    textFont(createFont('PressStart2P.ttf', 5))
    loadImages()

def draw():
    global scherm
    cycleBackground()

    if scherm == 'Jeffrey':
        #Selecteer knoppen
                #Spelers
        image(PijlTerugJeffrey, 435, 150, 55, 55)
        image(PijlVerderJeffrey, 815, 150, 55, 55)
                #Artefacten
        image(PijlTerugJeffrey, 435, 250, 55, 55)
        image(PijlVerderJeffrey, 815, 250, 55, 55)
                #Elementen
        image(PijlTerugJeffrey, 435, 350, 55, 55)
        image(PijlVerderJeffrey, 815, 350, 55, 55)
        #Variabelen en text
        image(LeegVakJeffrey, 495, 150, 315, 55)
        image(LeegVakJeffrey, 495, 250, 315, 55)
        image(LeegVakJeffrey, 495, 350, 315, 55)
        image(TerugKnop, 10, 655, 165, 55)
        image(ToevoegenKnop, 1030, 655, 240, 55)
    
        fill(0)
        textSize(17)
        text('Speler:', 505 , 170, 300, 50)
        text('Artefact:', 505, 270, 300, 150)
        text('Element:', 505, 370, 300, 250)
        text(spelers[spelerIndex], 625, 170, 300, 50)
        text(artefacts[artefactIndex], 660, 270, 300, 150)
        text(elements[elementIndex], 645, 370, 300, 250)
        
        #handje wanneer muis op knop anders arrow en afbeelding image veranderd
           #terug knop
        if isMouseOnButton(10, 655, 165, 55):
            image(TerugKnop2, 10, 655, 165, 55)
            cursor(HAND)
           #toevoegen knop
        elif isMouseOnButton(1030, 655, 240, 55):
            image(ToevoegenKnop2, 1030, 655, 240, 55)
            cursor(HAND)
           #player knoppen
        elif isMouseOnButton(435, 150, 55, 55):
            image(PijlTerugJeffrey2, 435, 150, 55, 55)
            cursor(HAND)
        elif isMouseOnButton(815, 150, 55, 55):
            image(PijlVerderJeffrey2, 815, 150, 55, 55)
            cursor(HAND)
           #artefact knoppen
        elif isMouseOnButton(435, 250, 55, 55):
            image(PijlTerugJeffrey2, 435, 250, 55, 55)
            cursor(HAND)
        elif isMouseOnButton(815, 250, 55, 55):
            image(PijlVerderJeffrey2, 815, 250, 55, 55)
            cursor(HAND)
           #element knoppen
        elif isMouseOnButton(435, 350, 55, 55):
            image(PijlTerugJeffrey2, 435, 350, 55, 55)
            cursor(HAND)
        elif isMouseOnButton(815, 350, 55, 55):
            image(PijlVerderJeffrey2, 815, 350, 55, 55)
            cursor(HAND)
        else: cursor(ARROW)

def mousePressed():
    global artefactIndex, elementIndex, spelerIndex, scherm
    
    if scherm == 'Jeffrey':
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
        #terug knop
        if isMouseOnButton(10, 655, 165, 55):
            print('au')
        #toevoegen knop
        if isMouseOnButton(1030, 655, 240, 55): 
            #artefact tevoegen aan speler
            if spelerIndex == 0 and len(cards_player1) != 5:
                cards_player1.append([artefacts[artefactIndex], elements[elementIndex]])
            elif spelerIndex == 1 and len(cards_player2) != 5:
                cards_player2.append([artefacts[artefactIndex], elements[elementIndex]])
            elif spelerIndex == 2 and len(cards_player3) != 5:
                cards_player3.append([artefacts[artefactIndex], elements[elementIndex]])
            elif spelerIndex == 3 and len(cards_player4) != 5:
                cards_player4.append([artefacts[artefactIndex], elements[elementIndex]])
            elif spelerIndex == 4 and len(cards_player5) != 5:
                cards_player5.append([artefacts[artefactIndex], elements[elementIndex]])
            
            print('artefacten spelers 1')
            print(cards_player1)
            print('artefacten spelers 2')
            print(cards_player2)
            print('artefacten spelers 3')
            print(cards_player3)
            print('artefacten spelers 4')
            print(cards_player4)
            print('artefacten spelers 5')
            print(cards_player5)
    
def isMouseOnButton(posX, posY, buttonWidth, buttonHeight, centered = False):
  if centered:
   return True if posX - buttonWidth / 2 < mouseX < posX + buttonWidth / 2 and posY - buttonHeight / 2 < mouseY < posY + buttonHeight / 2  else False
  return True if posX < mouseX < posX + buttonWidth and posY < mouseY < posY + buttonHeight else False
                
def cycleBackground():
    global bg_index
    background(loadImage('background/bg' + str(bg_index) + '.jpg'))
    bg_index = bg_index + 1 if bg_index < 32 else 0             

def loadImages():
    global PijlTerugJeffrey, PijlTerugJeffrey2, PijlVerderJeffrey, PijlVerderJeffrey2, LeegVakJeffrey, TerugKnop, TerugKnop2, ToevoegenKnop, ToevoegenKnop2
    PijlTerugJeffrey = loadImage('images/PijlTerugJeffrey.png')
    PijlTerugJeffrey2 = loadImage('images/PijlTerugJeffrey2.png')
    PijlVerderJeffrey = loadImage('images/PijlVerderJeffrey.png')
    PijlVerderJeffrey2 = loadImage('images/PijlVerderJeffrey2.png')
    LeegVakJeffrey =  loadImage('images/LeegVakJeffrey.png')
    TerugKnop = loadImage('images/TerugKnop.png')
    TerugKnop2 = loadImage('images/TerugKnop2.png')
    ToevoegenKnop = loadImage('images/Toevoegen.png')
    ToevoegenKnop2 = loadImage('images/Toevoegen2.png')

    
