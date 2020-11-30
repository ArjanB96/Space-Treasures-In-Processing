bg_index = 0
screen = 0
resizeWidth = 300
resizeHeight = 300
textResize = 70
opacityText = 0
opacityChange = True
pagina = 0

def setup():
    global planet, exitButton, exitButton2, homeButton, homeButton2, infoButton, infoButton2, regelButton, regelButton2, gidsButton, gidsButton2, terugKnopButton, terugKnopButton2, verder, verder2, terug, terug2, pijlTerug, pijlTerug2, pijlVerder, pijlVerder2
    global pijlVerderIdle, pijlTerugIdle, Amaterasu, Aqua, Kaytsak
    
    textFont(createFont('PressStart2P.ttf', 40))
    size(1280, 720)
   
    # Buttons
    exitButton = loadImage('images/Exit.png')
    exitButton2 = loadImage('images/Exit2.png')
    homeButton = loadImage('images/Home.png')
    homeButton2 = loadImage('images/Home2.png')
    infoButton = loadImage('images/Info.png')
    infoButton2 = loadImage('images/Info2.png')
    regelButton = loadImage('images/Regels.png')
    regelButton2 = loadImage('images/Regels2.png')
    gidsButton = loadImage('images/Gids.png')
    gidsButton2 = loadImage('images/Gids2.png')
    terugKnopButton = loadImage('images/TerugKnop.png')
    terugKnopButton2 = loadImage('images/TerugKnop2.png')
    planet = loadImage('images/planeetAqua.png')
    
    pijlTerug = loadImage('images/PijlTerug.png')
    pijlTerug2 = loadImage('images/PijlTerug2.png')
    pijlTerugIdle = loadImage('images/PijlTerugIdle.png')
    pijlVerder = loadImage('images/PijlVerder.png')
    pijlVerder2 = loadImage('images/PijlVerder2.png')
    pijlVerderIdle = loadImage('images/PijlVerderIdle.png')
    
    Amaterasu = loadImage('images/Amaterasu.png')
    Aqua = loadImage('images/Aqua.png')
    Kaytsak = loadImage('images/Kaytsak.png')
    

def draw():
    global screen, resizeWidth, resizeHeight, textResize, opacityText, opacityChange
    
    # Background
    cycleBackground()
    
    #############
    # Home screen
    if screen == 0:
        
        # To show if hand should be shown or not
        if isMouseOnButton(640, 360, 300, 300, True):    # START button
            cursor(HAND)
        elif isMouseOnButton(10 , 655, 135, 55):    # EXIT button
            cursor(HAND)
        elif isMouseOnButton(1235, 50, 68, 69, True):    # Info button
            cursor(HAND)
        else:
            cursor(ARROW)    
        
        # 'Space Treasures' text
        fill(250, 250, 250)
        textSize(75)
        textAlign(CENTER, CENTER)
        text('Space Treasures', 640, 140)
        
        # Start Button
        if isMouseOnButton(width / 2, height / 2, 300, 300, True):
            imageMode(CENTER)
            image(planet, width / 2, height / 2, resizeWidth, resizeHeight)

            # Movement of Planet
            if resizeWidth <= 320:
                resizeWidth += 10; resizeHeight += 10

            # Movement of text : 'START'
            if textResize <= 75:
                textResize += 1.1
            textSize(textResize)
            text('START', width / 2, height / 2)
        else:
            imageMode(CENTER)
            image(planet, width / 2, height / 2, resizeWidth, resizeHeight)
            #image(loadImage('images/planeetAqua.png'), width / 2, height / 2, resizeWidth, resizeHeight)
            
            # Movement of Planet
            if resizeWidth >= 305:
                resizeWidth -= 10; resizeHeight -= 10
                
            # Movement of text : 'START'
            if textResize >= 70:
                textResize -= 1.1
            textSize(textResize)
            text('START', width / 2, height / 2)
            
        # EXIT button
        if not isMouseOnButton(10, 655, 135, 55):
            imageMode(CORNER)
            image(exitButton, 10, 655, 135, 55)   
        else:
            imageMode(CORNER)
            image(exitButton2, 10, 655, 135, 55)
        
        

        
        # Info button
        if not isMouseOnButton(1235, 50, 68, 69, True):
            imageMode(CENTER)
            image(infoButton, 1235, 50, 68, 69)
        else:
            imageMode(CENTER)
            image(infoButton2, 1235, 50, 68, 69)

    #############
    # Info scherm
    if screen == 1:
        #global 
        

        # To show if hand should be shown or not
        if isMouseOnButton(10, 10, 130, 55):
            cursor(HAND)
        elif isMouseOnButton(640, 290, 390, 110, True):
            cursor(HAND)
        elif isMouseOnButton(640, 440, 390, 110, True):
            cursor(HAND)
        else:
            cursor(ARROW)
        
        #Home Button
        if not isMouseOnButton(10, 10, 130, 55):
            imageMode(CORNER)
            image(homeButton, 10, 10, 130, 55)
        else:
            imageMode(CORNER)
            image(homeButton2, 10, 10, 130, 55)
            
        # Regel Button
        if not isMouseOnButton(640, 290, 390, 110, True):
            imageMode(CENTER)
            image(regelButton, 640, 290, 390, 110)
        else:
            imageMode(CENTER)
            image(regelButton2, 640, 290, 390, 110)
        
        # Gids Button
        if not isMouseOnButton(640, 440, 390, 110, True):
            imageMode(CENTER)
            image(gidsButton, 640, 440, 390, 110)
        else:
            imageMode(CENTER)
            image(gidsButton2, 640, 440, 390, 110)
     
     
    ############### 
    # Regel Screen       
    if screen == 2:
        
         # To show if hand should be shown or not
        if isMouseOnButton(10, 10, 130, 55): # Home Button
            cursor(HAND)
        elif isMouseOnButton(10, 655, 165, 55): # TerugKnop Button
            cursor(HAND)
        elif isMouseOnButton(width / 2 - 590, height / 2, 84, 78, True) and pagina != 0: # Terug Button
            cursor(HAND)
        elif isMouseOnButton(width / 2 + 590, height / 2, 84, 78, True): # Verder Button
            cursor(HAND)
        else: 
            cursor(ARROW)
            
        #Home Button
        if not isMouseOnButton(10, 10, 130, 55):
            imageMode(CORNER)
            image(homeButton, 10, 10, 130, 55)
        else:
            imageMode(CORNER)
            image(homeButton2, 10, 10, 130, 55)
        
        # TerugKnop Button
        if not isMouseOnButton(10, 655, 165, 55):
            imageMode(CORNER)
            image(terugKnopButton, 10, 655, 165, 55)
        else:
            imageMode(CORNER)
            image(terugKnopButton2, 10, 655, 165, 55)
            
        # Fade in van de tekst
        if opacityText != 255:
            opacityText += 10

             
        # TEKST  
        textAlign(CORNER, CENTER)   
        fill(opacityText, opacityText, opacityText)
        if pagina == 0:
            textSize(20)
            text('INHOUD:\n- 10 hexagon map stukken,\n- 38 instructiekaarten,\n- 49 fiches,\n- 5 ruimteschepen,\n- 1 dobbelsteen.\n\nDOEL:\nVind twee Elementen van verschillende element \nsoorten en win!\n\nSPELERS:\nSpace Treasures is te spelen met 4 of 5 mensen. ', 130, height / 2)
        if pagina == 1:
            textSize(30)
            text('VOORBEREIDING:', 130, 130)
            textSize(20)
            text('Bord-deel Aarde wordt als eerst neergelegd en wordt \ngebruikt als startplaneet, schud vervolgens de \nresterende bord-delen en leg deze met de goede kant \nomlaag op de tafel. In het midden op Aarde wordt de \nbrandstof fiche neergelegd.\n\nElke speler krijgt zijn eigen ruimteschip. De \nspelers mogen naar eigen keuze zijn/haar \nruimteschip op 1 van de 6 grijze hoeken plaatsen, \nmaximaal 1 speler per hoek. Schud de \ninstructiekaarten en leg deze bij het bord-deel met \nde goede kant omlaag. Elke speler krijgt een \nfiche van elk Element.', 130, height / 2 - 40)
            image(Kaytsak, width / 2 - 300, 500 ,65, 80)
            image(Aqua, width / 2, 500, 65, 80)
            image(Amaterasu, width / 2 + 300, 500, 65, 80)
            textSize(15)
            text('Kaytsak', width / 2 - 325, 600)
            text('Aqua', width / 2 + 5, 600)
            text('Amaterasu', width / 2 + 275, 600)
        if pagina == 2:
            textSize(20)
            text('Om te bepalen wie er begint met het spel, dobbelt \nelke speler 1 keer. De speler die het hoogst aantal \nogen heeft gegooid begint met het spel. Het spel \nkan nu beginnen!', 135, height / 2)
        if pagina == 3:
            textSize(30)
            text('EERSTE BEURT:', 130, 220)
            textSize(20)
            text('De speler die begint trekt 1 van de \ninstructiekaarten en kiest de instructie die hij/zij \nkiest. De speler moet stappen zetten omdat er op \nplaneet "Aarde" geen Artefact te vinden is. Het \nspel gaat met de klok mee.Als eerste willen de \nspelers naar de "brandstof" plek gaan in het midden \nvan de planeet om andere planeten te kunnen \nontdekken. Op de andere planeten zijn de betreffende \nArtefacten, Elementen en meer brandstof te vinden.', 130, height / 2)     
        if pagina == 4:
            textSize(30)
            text('PER BEURT:', 130, 220)
            textSize(20)
            text('Per beurt kan je 3 dingen doen:\n1: Een instructiekaart pakken,\n2: een Artefact gebruiken\n3: of een Element maken.\n\nBij de eerste paar beurten zal je nog geen \nArtefacten hebben, dus kan je het tweede en derde \nnog niet doen. Dan moeten er instructiekaarten \nworden gepakt.', 130, height / 2)
        if pagina == 5:
            textSize(30)
            text('PLANEET ONTDEKKEN:', 130, 245)
            textSize(20)
            text('Zodra een speler een brandstof fiche heeft gekregen \nmoet de speler meteen een planeet ontdekken. Dit doe \nje door een planeet \nte pakken van de stapel, de planeet mag alleen \ngeplaatst worden aangrenzend aan de planeet waar de \nspeler op staat. De speler mag kiezen aan welke kant \nde planeet ontdekt wordt', 130, height/2)
        if pagina == 6:
            textSize(30)
            text('BEWEGING:', 130, 240)
            textSize(20)
            text('Er kan alleen gelopen worden via de lijnen. Je moet \nhet aantal stappen zetten dat aangegeven is, tevens \nlaat je ook je instructiekaart aan je medespelers \nzien. Je mag niet heen en weer blijven lopen. Als je \nvan planeet naar planeet loopt, loop je via de grote \nwitte vakken, daarnaast mag je niet in 1 beurt naar \nmeerdere planeet gaan.', 130, height/2)
        if pagina == 7:
            textSize(30)
            text('ARTEFACT PAKKEN:', 130, 130)
            textSize(20)
            text('Als je een instructiekaart krijgt met een Artefact \nerop, kan je dobbelen voor een Artefact. LET OP! Op \nplaneet Aarde  kan geen Artefact gevonden worden! \nLinksboven staan de minimaal aantal ogen die \ngegooid moeten worden om deze Artefact te mogen \npakken. Als je het minimaal aantal ogen hebt gegooid \nof hoger mag je de kaart bij je houden. De element \nsoort wordt bepaald door op welke planeet je staat. \nAls je op planeet Kaytsak staat, leg je jouw \nArtefact bij het fiche Kaytsak.\n\nPer planeet is er maar 1 artefact te vinden per \npersoon. Als je op planeet x van Amaterasu een \nArtefact hebt gepakt kan je alleen nog Artefacten \nvan Amaterasu vinden op y en z.', 130, height/2)
        if pagina == 8:
            text('', 130, height/2)
        if pagina == 9:
            text('', 130, height/2)
        if pagina == 10:
            text('', 130, height/2)
        if pagina == 11:
            text('', 130, height/2)
        if pagina == 12:
            text('', 130, height/2)    
        #if pagina == laatste pagina:
        #    textSize(30)
        #    text('TERMENLIJST:', 152, 130)
        #    textSize(20)
        #    text('-Brandstof:\nMet brandstof kan je andere planeten ontdekken.\n\n-Instructiekaarten:\nDit zijn de kaarten waar een keuze gemaakt moet \nworden tussen stappen zetten of een \nArtefact / Element maken.\n\n-Artefacten:\nDe Artefacten heb je nodig om Elementen te maken. \nTevens kunnen deze aan jou voordelen geven of \nandere spelers hinderen.\n\n-Elementen:\nDit is het voorwerp dat nodig is om te winnen. \n2 verschillende Elementen zijn hiervoor nodig.', 152, height / 2)

        
                  
         # Terug Button
        if pagina == 0:
            imageMode(CENTER)
            image(pijlTerugIdle, width / 2 - 590, height / 2, 84, 78)
        elif not isMouseOnButton(width / 2 - 590, height / 2, 84, 78, True):
            imageMode(CENTER)
            image(pijlTerug, width / 2 - 590, height / 2, 84, 78)
        else:
            imageMode(CENTER)
            image(pijlTerug2, width / 2 - 590, height / 2, 84, 78)
    
        # Verder Button
        if not isMouseOnButton(width / 2 + 590, height / 2, 84, 78, True):
            imageMode(CENTER)
            image(pijlVerder, width / 2 + 590, height / 2, 84, 78)
        else:
            imageMode(CENTER)
            image(pijlVerder2, width / 2 + 590, height / 2, 84, 78)
          

    
    
    #############
    # Gids Screen
    if screen == 3:
        
        # To show if hand should be shown or not
        if isMouseOnButton(10, 10, 130, 55):
            cursor(HAND)
        elif isMouseOnButton(10, 655, 165, 55):
            cursor(HAND)
        else: 
            cursor(ARROW)
        
        #Home Button
        if not isMouseOnButton(10, 10, 130, 55):
            imageMode(CORNER)
            image(homeButton, 10, 10, 130, 55)
        else:
            imageMode(CORNER)
            image(homeButton2, 10, 10, 130, 55)
        
        # TerugKnop Button
        if not isMouseOnButton(10, 655, 165, 55):
            imageMode(CORNER)
            image(terugKnopButton, 10, 655, 165, 55)
        else:
            imageMode(CORNER)
            image(terugKnopButton2, 10, 655, 165, 55)
        
                
def mousePressed():
    global screen, pagina, opacityText
    
    # All buttons for Home screen
    if screen == 0:
        
        # EXIT button
        if isMouseOnButton(10 , 655, 135, 55):
            exit()
            
        # Info Button
        if isMouseOnButton(1235, 50, 68, 69, True):
            screen = 1
            
    # All buttons for Info Screen
    if screen == 1:
        
        # Home Button
        if isMouseOnButton(10, 10, 130, 55):
            screen = 0
        
        # Regel button
        if isMouseOnButton(640, 290, 390, 110, True):
            screen = 2
        
        # Gids button
        if isMouseOnButton(640, 440, 390, 110, True):
            screen = 3
            
    # All buttons for Regel Screen
    if screen == 2:
        
        # Home Button
        if isMouseOnButton(10, 10, 130, 55):
            screen = 0
            pagina = 0 # Om pagina te resetten
            opacityText = 0 # Om te Fade In te resetten
        # Terug button
        if isMouseOnButton(10, 655, 165, 55):
            screen = 1
            pagina = 0 # Om pagina te resetten
            opacityText = 0 # Om te Fade In te resetten
        # Terug Button
        if isMouseOnButton(width / 2 - 590, height / 2, 78, 78, True) and pagina != 0:
            pagina -= 1
            opacityText = 0 # Om te Fade In te resetten
        # Verder Button
        if isMouseOnButton(width / 2 + 590, height / 2, 78, 78, True): #and pagina != ?:
            pagina += 1
            opacityText = 0 # Om te Fade In te resetten
        
    # All buttons for Gids Screen
    if screen == 3:
        
        # Home Button
        if isMouseOnButton(10, 10, 130, 55):
            screen = 0
        
        if isMouseOnButton(10, 655, 165, 55):
            screen = 1
   
         
# Function to check if mouse is on the button
def isMouseOnButton(posX, posY, buttonWidth, buttonHeight, centered = False):
    if centered:
        return True if posX - buttonWidth / 2 < mouseX < posX + buttonWidth / 2 and posY - buttonHeight / 2 < mouseY < posY + buttonHeight / 2 else False
    else:
        return True if posX < mouseX < posX + buttonWidth and posY < mouseY < posY + buttonHeight else False
  
      
# Background
def cycleBackground():
    global bg_index
    background(loadImage('background/bg' + str(bg_index) + '.jpg'))
    bg_index = bg_index + 1 if bg_index < 32 else 0
