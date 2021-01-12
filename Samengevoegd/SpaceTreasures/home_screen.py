import globals

bg_index = 0
screen = 0
resizeWidth = 440
resizeHeight = 300
opacityText = 0
opacityImage = 0
opacityChange = True
pagina = 0
screenList = []
game_in_progress = False
interval = 250

def setup():
    global planet_start, planet_hervat, exitButton, exitButton2, homeButton, homeButton2, infoButton, infoButton2, regelButton, regelButton2, terugKnopButton, terugKnopButton2, verder, verder2, terug, terug2, pijlVerderIdle, pijlTerugIdle, Amaterasu, Aqua, Kaytsak, Blockade, Haste, Exchange, EyeDrop, Swap, Skip, Fuel, leegTekstVlak, H1, H2, H3, H4, H5, H6, H7, H8, H1_hover, H2_hover, H3_hover, H4_hover, H5_hover, H6_hover, H7_hover, H8_hover, Hoofdstukken, Hoofdstukken2, blauwVlak, blauwVlak2, H1_idle, H2_idle, H3_idle, H4_idle, H5_idle, H6_idle, H7_idle, H8_idle, pijlTerugPaars, pijlTerug2Paars, pijlVerderPaars, pijlVerder2Paars, GrijsVlak, background_img, background_animation_images, hervatButton, hervatButton2
    size(1280, 720)
    frameRate(30)
    
    exitButton = loadImage('assets/images/Exit.png')
    exitButton2 = loadImage('assets/images/Exit2.png')
    hervatButton = loadImage('assets/images/Hervat.png')
    hervatButton2 = loadImage('assets/images/Hervat2.png')
    homeButton = loadImage('assets/images/Home.png')
    homeButton2 = loadImage('assets/images/Home2.png')
    infoButton = loadImage('assets/images/Info.png')
    infoButton2 = loadImage('assets/images/Info2.png')
    regelButton = loadImage('assets/images/Regels.png')
    regelButton2 = loadImage('assets/images/Regels2.png')
    terugKnopButton = loadImage('assets/images/TerugKnop.png')
    terugKnopButton2 = loadImage('assets/images/TerugKnop2.png')
    
    planet_start = loadImage('assets/images/planeet_start.png')
    planet_hervat = loadImage('assets/images/planeet_hervat.png')
    
    pijlTerugPaars = loadImage('assets/images/PijlTerugPaars.png')
    pijlTerug2Paars = loadImage('assets/images/PijlTerug2Paars.png')
    pijlTerugIdle = loadImage('assets/images/PijlTerugIdle.png')
    pijlVerderPaars = loadImage('assets/images/PijlVerderPaars.png')
    pijlVerder2Paars = loadImage('assets/images/PijlVerder2Paars.png')
    pijlVerderIdle = loadImage('assets/images/PijlVerderIdle.png')
    leegTekstVlak = loadImage('assets/images/LeegTekstVlak.png')
    Amaterasu = loadImage('assets/images/Amaterasu.png')
    Aqua = loadImage('assets/images/Aqua.png')
    Kaytsak = loadImage('assets/images/Kaytsak.png')
    Blockade = loadImage('assets/images/Blockade.png')
    Exchange = loadImage('assets/images/Exchange.png')
    EyeDrop = loadImage('assets/images/EyeDrop.png')
    Haste = loadImage('assets/images/Haste.png')
    Skip = loadImage('assets/images/Skip.png')
    Swap = loadImage('assets/images/Swap.png')
    Fuel = loadImage('assets/images/Fuel.png')
    
    Hoofdstukken = loadImage('assets/images/Hoofdstukken.png')
    Hoofdstukken2 = loadImage('assets/images/Hoofdstukken2.png')
    H1 = loadImage('assets/images/H1.png')
    H2 = loadImage('assets/images/H2.png')
    H3 = loadImage('assets/images/H3.png')
    H4 = loadImage('assets/images/H4.png')
    H5 = loadImage('assets/images/H5.png')
    H6 = loadImage('assets/images/H6.png')
    H7 = loadImage('assets/images/H7.png')
    H8 = loadImage('assets/images/H8.png')
    H1_hover = loadImage('assets/images/H1_hover.png')
    H2_hover = loadImage('assets/images/H2_hover.png')
    H3_hover = loadImage('assets/images/H3_hover.png')
    H4_hover = loadImage('assets/images/H4_hover.png')
    H5_hover = loadImage('assets/images/H5_hover.png')
    H6_hover = loadImage('assets/images/H6_hover.png')
    H7_hover = loadImage('assets/images/H7_hover.png')
    H8_hover = loadImage('assets/images/H8_hover.png')
    H1_idle = loadImage('assets/images/H1_idle.png')
    H2_idle = loadImage('assets/images/H2_idle.png')
    H3_idle = loadImage('assets/images/H3_idle.png')
    H4_idle = loadImage('assets/images/H4_idle.png')
    H5_idle = loadImage('assets/images/H5_idle.png')
    H6_idle = loadImage('assets/images/H6_idle.png')
    H7_idle = loadImage('assets/images/H7_idle.png')
    H8_idle = loadImage('assets/images/H8_idle.png')
    blauwVlak = loadImage('assets/images/BlauwVak.png')
    blauwVlak2 = loadImage('assets/images/BlauwVak2.png')
    GrijsVlak = loadImage('assets/images/GrijsVlak.png')
    
    background_img = loadImage('background/bg0.jpg')
    background_animation_images = [loadImage('background/bg' + str(i) + '.jpg') for i in range(1, 14)]

    
def draw():
    global screen, resizeWidth, resizeHeight, opacityText, opacityChange, opacityImage

    cycleBackground()
    mouseHoverHandler()
    
    textFont(createFont('PressStart2P.ttf', 40))
    
    # Home screen
    if screen == 0:
        # 'Space Treasures' text        
        fill(255, 255, 255)
        textSize(75)
        textAlign(CENTER, CENTER)
        text('Space Treasures', 640, 140)
        
        tint(255)
        # Start Button
        imageMode(CENTER)
        if isMouseOnButton(640, 360, 300, 300, True):
            image(planet_hervat if game_in_progress else planet_start, 640, 360, resizeWidth, resizeHeight)
            if resizeHeight <= 320:
                resizeHeight += 10
            if resizeWidth <= 470:
                resizeWidth += 15
        else:
            image(planet_hervat if game_in_progress else planet_start, 640, 360, resizeWidth, resizeHeight)
            if resizeHeight >= 300:
                resizeHeight -= 10
            if resizeWidth >= 440:
                resizeWidth -= 15
            
        # EXIT button
        imageShow(exitButton, exitButton2, 10, 655, 135, 55)
        # Info button
        imageShow(infoButton, infoButton2, 1235, 50, 68, 69, True)
        
    # Info scherm
    elif screen == 1:
        
        tint(255)
        #Home Button
        imageShow(homeButton, homeButton2, 10, 10, 130, 55)
        # Regel Button
        imageShow(regelButton, regelButton2, 640, 80, 350, 90, True)
        
        fill(0, 0, 0)
        textSize(18)
        textAlign(CENTER, CENTER)
        # H1 : Inhoud
        imageShow(H1, H1_hover, 220, 180, 80, 80, wdthAdd = 250)
        imageShow(blauwVlak, blauwVlak2, 300, 180, 250, 80, wdthMinus = 80, wdthAdd = 80)
        text('INHOUD', 420, 220)
        # H2 : Voorbereiding
        imageShow(H2, H2_hover, 220, 315, 80, 80, wdthAdd = 250) 
        imageShow(blauwVlak, blauwVlak2, 300, 315, 250, 80, wdthMinus = 80, wdthAdd = 80)
        text('VOORBEREIDING', 420, 355)
        # H3 : Beurt
        imageShow(H3, H3_hover, 220, 440, 80, 80, wdthAdd = 250) 
        imageShow(blauwVlak, blauwVlak2, 300, 440, 250, 80, wdthMinus = 80, wdthAdd = 80)
        text('BEURT', 420, 480)
        # H4 : Voortgang
        imageShow(H4, H4_hover, 220, 565, 80, 80, wdthAdd = 250) 
        imageShow(blauwVlak, blauwVlak2, 300, 565, 250, 80, wdthMinus = 80, wdthAdd = 80)
        text('VOORTGANG', 420, 605)
        # H5 : Artefacten
        imageShow(H5, H5_hover, 770, 180, 80, 80, wdthAdd = 250)
        imageShow(blauwVlak, blauwVlak2, 850, 180, 250, 80, wdthMinus = 80, wdthAdd = 80)
        text('ARTEFACTEN', 970, 220)
        # H6 : Overig
        imageShow(H6, H6_hover, 770, 315, 80, 80, wdthAdd = 250)
        imageShow(blauwVlak, blauwVlak2, 850, 315, 250, 80, wdthMinus = 80, wdthAdd = 80)
        text('OVERIG', 970, 355)
        # H7 : Elementen
        imageShow(H7, H7_hover, 770, 440, 80, 80, wdthAdd = 250)
        imageShow(blauwVlak, blauwVlak2, 850, 440, 250, 80, wdthMinus = 80, wdthAdd = 80)
        text('ELEMENTEN', 970, 480)
        # H8 : Termenlijst
        imageShow(H8, H8_hover, 770, 565, 80, 80, wdthAdd = 250)
        imageShow(blauwVlak, blauwVlak2, 850, 565, 250, 80, wdthMinus = 80, wdthAdd = 80)
        text('TERMENLIJST', 970, 605)
        
        
    # Regel Screen       
    elif screen == 2:
        
        tint(255)    
        # Home Button
        imageShow(homeButton, homeButton2, 10, 10, 130, 55)
        # TerugKnop Button
        imageShow(terugKnopButton, terugKnopButton2, 10, 655, 165, 55) 
        
        hoofdstukShow()
        # Fade in of the text
        if opacityText <= 255:
            opacityText += 20
        # Fade of images
        if opacityImage <= 250:
            opacityImage += 15

        # Black picture behind text
        tint(255, 100)
        imageMode(CORNER)
        image(leegTekstVlak, 100, 85)
    
        # TEKST  
        textAlign(CORNER, CENTER)   
        fill(opacityText, opacityText, opacityText)
        tint(opacityImage)
        if pagina == 0:
            textSize(20)
            text('INHOUD SPEL:\n- 10 hexagon map stukken,\n- 38 instructiekaarten,\n- 49 fiches,\n- 5 ruimteschepen,\n- 1 dobbelsteen.\n\nDOEL:\nVind twee Elementen van verschillende element \nsoorten en win!\n\nSPELERS:\nSpace Treasures is te spelen met 4 of 5 mensen. ', 125, 360)
        elif pagina == 1:
            textSize(30)
            text('VOORBEREIDING:', 125, 130)
            textSize(20)
            text('Bord-deel Aarde wordt als eerst neergelegd en wordt \ngebruikt als startplaneet, schud vervolgens de \nresterende bord-delen en leg deze met de goede kant \nomlaag op de tafel. In het midden op Aarde wordt de \nbrandstof fiche neergelegd.\n\nElke speler krijgt zijn eigen ruimteschip. De \nspelers mogen naar eigen keuze zijn/haar \nruimteschip op 1 van de 6 grijze hoeken plaatsen, \nmaximaal 1 speler per hoek. Schud de \ninstructiekaarten en leg deze bij het bord-deel met \nde goede kant omlaag. Elke speler krijgt een \nfiche van elk Element.', 125, 320)
            image(Kaytsak, 340, 500 ,65, 80)
            image(Aqua, 640, 500, 65, 80)
            image(Amaterasu, 940, 500, 65, 80)
            textSize(15)
            text('Kaytsak', 315, 600)
            text('Aqua', 645, 600)
            text('Amaterasu', 915, 600)
        elif pagina == 2:
            textSize(20)
            text('Om te bepalen wie er begint met het spel, dobbelt \nelke speler 1 keer. De speler die het hoogst aantal \nogen heeft gegooid begint met het spel. Het spel \nkan nu beginnen!', 130, 360)
        elif pagina == 3:
            textSize(30)
            text('EERSTE BEURT:', 125, 220)
            textSize(20)
            text('De speler die begint trekt 1 van de \ninstructiekaarten en kiest de instructie die hij/zij \nkiest. De speler moet stappen zetten omdat er op \nplaneet "Aarde" geen Artefact te vinden is. Het \nspel gaat met de klok mee.Als eerste willen de \nspelers naar de "brandstof" plek gaan in het midden \nvan de planeet om andere planeten te kunnen \nontdekken. Op de andere planeten zijn de betreffende \nArtefacten, Elementen en meer brandstof te vinden.', 125, 360)     
        elif pagina == 4:
            textSize(30)
            text('PER BEURT:', 125, 220)
            textSize(20)
            text('Per beurt kan je 3 dingen doen:\n1: Een instructiekaart pakken,\n2: een Artefact gebruiken\n3: of een Element maken.\n\nBij de eerste paar beurten zal je nog geen \nArtefacten hebben, dus kan je het tweede en derde \nnog niet doen. Dan moeten er instructiekaarten \nworden gepakt.', 125, 360)
        elif pagina == 5:
            textSize(30)
            text('PLANEET ONTDEKKEN:', 125, 245)
            textSize(20)
            text('Zodra een speler een brandstof fiche heeft gekregen \nmoet de speler meteen een planeet ontdekken. Dit doe \nje door een planeet \nte pakken van de stapel, de planeet mag alleen \ngeplaatst worden aangrenzend aan de planeet waar de \nspeler op staat. De speler mag kiezen aan welke kant \nde planeet ontdekt wordt', 130, 360)
        elif pagina == 6:
            textSize(30)
            text('BEWEGING:', 125, 240)
            textSize(20)
            text('Er kan alleen gelopen worden via de lijnen. Je moet \nhet aantal stappen zetten dat aangegeven is, tevens \nlaat je ook je instructiekaart aan je medespelers \nzien. Je mag niet heen en weer blijven lopen. Als je \nvan planeet naar planeet loopt, loop je via de grote \nwitte vakken, daarnaast mag je niet in 1 beurt naar \nmeerdere planeet gaan.', 125, 360)
        elif pagina == 7:
            textSize(30)
            text('ARTEFACT PAKKEN:', 125, 130)
            textSize(20)
            text('Als je een instructiekaart krijgt met een Artefact \nerop, kan je dobbelen voor een Artefact. LET OP! Op \nplaneet Aarde  kan geen Artefact gevonden worden! \nLinksboven staan de minimaal aantal ogen die \ngegooid moeten worden om deze Artefact te mogen \npakken. Als je het minimaal aantal ogen hebt gegooid \nof hoger mag je de kaart bij je houden. De element \nsoort wordt bepaald door op welke planeet je staat. \nAls je op planeet Kaytsak staat, leg je jouw \nArtefact bij het fiche Kaytsak.\n\nPer planeet is er maar 1 artefact te vinden per \npersoon. Als je op planeet x van Amaterasu een \nArtefact hebt gepakt kan je alleen nog Artefacten \nvan Amaterasu vinden op y en z.', 125, 360)
        elif pagina == 8:
            textSize(30)
            text('ARTEFACT GEBRUIKEN:', 125, 230)
            textSize(20)
            text('Als de speler 1 van zijn / haar Artefacten wil \ngebruiken, kost dit een beurt. Je mag dus niet een \ninstructiekaart pakken en daarna een Artefact \ngebruiken. Behalve bij Haste.Als de Artefact een \nafkoeltijd heeft, moet je die na gebruik met de \ngoede kant omlaag neerleggen voor het aantal rondes \ndat aangegeven staat. Per beurt mag er maar 1 \nArtefact gebruikt worden.', 125, 360)
        elif pagina == 9:
            textSize(30)
            text('De Artefacten zijn:', 125, 130)
            textSize(20)
            image(Swap, 145, 155, 60, 96)
            image(Haste, 130, 270, 75, 80)
            image(EyeDrop, 125, 370, 80, 80)
            image(Skip, 130, 490, 60, 78)
            text('Swap: Speler met dit artefact mag 2 spelers \nruilen van plek. Inclusief zichzelf met een \nandere. (Minimaal 4 ogen, afkoeltijd 4 beurten.)\n\n\nHaste: Elke beurt 1 extra stap. \n(Minimaal 4  ogen.)\n\n\nEyeDrop: Een oog minder nodig bij dobbelen om \nArtefact te krijgen. (Minimaal 4 ogen.)\n\n\nSkip: Kies een speler, hij/zij moet een beurt \noverslaan. \n(Minimaal 5 ogen, afkoeltijd 3 beurten.)', 125 + 90, 360)
        elif pagina == 10:
            textSize(20)
            image(Exchange, 130, 200, 72, 78)
            image(Blockade, 115, 380, 96, 96)
            text('Exchange: Ruil 1 Artefact naar keuze met iemand \nop dezelfde planeet. De element-soort verandert \nniet. Eventuele cooldown op geruilde kaart gaat \nweg.(Minimaal 3 ogen, afkoeltijd 4 beurten.)\n\n\nBlockade: Zet een blokkade neer om te voorkomen \ndat andere spelers de planeet betreden. \n(minimaal 3 ogen, afkoeltijd 4 beurten.)\nGebruik: Je legt het "Blockade" fiche aan 1 van \nde kanten op de planeet waar jij op staat. Hij \nkomt tussen de hoekpunten. Blijft 2 rondes \nstaan. Blockade geldt niet voor de gebruiker.', 125 + 90, 360)
        elif pagina == 11:
            textSize(30)
            text('MAXIMAAL ARTEFACTEN:', 125, 130)
            textSize(20)
            text('Elke speler mag maximaal 5 Artefacten hebben. De \nspeler mag niet dobbelen voor een Artefact als hij \ner 5 heeft.', 125, 190)
            textSize(30)
            text('BRANDSTOF:', 125, 300)
            textSize(20)
            text('Om te reizen tussen eerder ontdekte planeten is geen \nbrandstof nodig. Als de speler de planeet heeft \nneergelegd moet hij/zij ook de brandstof fiche in \nhet midden neerleggen.', 125, 375)
            imageMode(CENTER)
            image(Fuel, 640, 510, 150, 150)
            textSize(25)
            text('Brandstof', 535, 610)
        elif pagina == 12:
            textSize(30)
            text('KAARTEN:', 125, 130)
            textSize(20)
            text('Na gebruik wordt deze naast de stapel gelegd. Zodra \nde stapel op is wordt die geschud en kan daarna weer \ngebruikt worden.', 125, 195)    
            textSize(30)
            text('ELKE PLANEET ONTDEKT:', 125, 320)
            textSize(20)
            text('Nadat elke planeet ontdekt is, mag je zodra je op \neen brandstof plek komt reizen naar een aangrenzende \nplaneet. Je komt dan op de brandstof plek. Je mag \nniet op dezelfde plek meteen weer naar een andere \nplaneet.', 125, 410)
        elif pagina == 13:
            textSize(30)
            text('ELEMENTEN:', 130, 130)
            textSize(20)
            text('Als je een instructiekaart hebt gepakt met de optie \nom een Element te maken kan je 3 Artefacten van \nhetzelfde soort element inruilen voor het \ndesbetreffende Element. De Artefacten die ingeruild \nzijn, leg je weg op de stapel van gebruikte kaarten. \nJe pakt dan een fiche van het Element dat je hebt \ngekregen.\n\nVoorbeeld:\nAls je 3 Artefacten hebt van de element Amaterasu. \nDan kan je deze inruilen voor een Element fiche van \nAmaterasu. Mits je de instructiekaart krijgt met de \noptie om een Element te maken.', 130, 320)
            image(Kaytsak, 340, 500 ,80, 95)
            image(Aqua, 640, 500, 80, 95)
            image(Amaterasu, 940, 500, 80, 95)
            textSize(15)
            text('Kaytsak', 320, 610)
            text('Aqua', 650, 610)
            text('Amaterasu', 915, 610)
        elif pagina == 14:
            textSize(30)
            text('TERMENLIJST:', 152, 130)
            textSize(20)
            text('- Brandstof:\nMet brandstof kan je andere planeten ontdekken.\n\n- Instructiekaarten:\nDit zijn de kaarten waar een keuze gemaakt moet \nworden tussen stappen zetten of een \nArtefact / Element maken.\n\n- Artefacten:\nDe Artefacten heb je nodig om Elementen te maken. \nTevens kunnen deze aan jou voordelen geven of \nandere spelers hinderen.\n\n- Elementen:\nDit is het voorwerp dat nodig is om te winnen. \n2 verschillende Elementen zijn hiervoor nodig.', 152, 360)
        elif pagina == 15:
            text('- Afkoeltijd:\nDit is het aantal rondes dat je je gebruikte \nArtefact niet meer kunt gebruiken.', 130, 360)
        
        tint(255)     
        imageMode(CENTER)     
        # Terug Button
        if pagina == 0:
            image(pijlTerugIdle, 50, 360, 84, 78)
        else:
            imageShow(pijlTerugPaars, pijlTerug2Paars, 50, 360, 84, 78, True)
        # Verder Button
        if pagina == 15:
            image(pijlVerderIdle, 1230, 360, 84, 78)
        else:
            imageShow(pijlVerderPaars, pijlVerder2Paars, 1230, 360, 84, 78, True)
            
        
def mousePressed():
    global screen, pagina, opacityText, opacityImage, screenList, resizeWidth, resizeHeight
    # Home screen
    if screen == 0:
        if isMouseOnButton(640, 360, 300, 300, True):
            globals.scherm = 'players'
            resizeWidth = 430
            resizeHeight = 299
            return
        elif isMouseOnButton(10 , 655, 135, 55): # EXIT button
            exit()
        elif isMouseOnButton(1235, 50, 68, 69, True): # Info Button
            screen = 1   
    # Info Screen
    elif screen == 1:
        if isMouseOnButton(10, 10, 130, 55): # Home Button
            screen = 0
            pagina = 0
        elif isMouseOnButton(640, 100, 390, 110, True): # Regel button
            screen = 2
        elif isMouseOnButton(220, 180, 330, 80): # H1
            screen = 2 
            pagina = 0
        elif isMouseOnButton(220, 315, 330, 80): # H2
            screen = 2
            pagina = 1
        elif isMouseOnButton(220, 440, 330, 80): # H3
            screen = 2
            pagina = 3
        elif isMouseOnButton(220, 565, 330, 80): # H4
            screen = 2
            pagina = 5
        elif isMouseOnButton(770, 180, 330, 80): # H5
            screen = 2
            pagina = 7
        elif isMouseOnButton(770, 315, 330, 80): # H6
            screen = 2
            pagina = 11
        elif isMouseOnButton(770, 440, 330, 80): # H7
            screen = 2
            pagina = 13
        elif isMouseOnButton(770, 565, 330, 80): # H8
            screen = 2
            pagina = 14
    # Regel Screen
    elif screen == 2:
        if isMouseOnButton(10, 10, 130, 55): # Home Button
            screen = 0
            pagina = 0 
            opacityText = 0 
            opacityImage = 0
        elif isMouseOnButton(10, 655, 165, 55): # Terug button
            screen = 1
            opacityText = 0 
            opacityImage = 0 
        elif isMouseOnButton(50, 360, 84, 78, True) and pagina != 0: # Terug Button
            pagina -= 1
            opacityText = 0 
            opacityImage = 0 
        elif isMouseOnButton(1230, 360, 84, 78, True) and pagina != 15: # Verder Button
            pagina += 1
            opacityText = 0
            opacityImage = 0
    
def isMouseOnButton(posX, posY, buttonWidth, buttonHeight, centered = False):
    if centered:
        return True if posX - buttonWidth / 2 < mouseX < posX + buttonWidth / 2 and posY - buttonHeight / 2 < mouseY < posY + buttonHeight / 2 else False
    else:
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

def imageShow(img, img2, x, y, wdth, hght, centered = False, wdthAdd = 0, wdthMinus = 0):
    imageMode(CENTER if centered else CORNER)
    if isMouseOnButton(x - wdthMinus, y, wdth + wdthAdd, hght, centered):
        image(img2, x, y, wdth, hght)
    else:
        image(img, x, y, wdth, hght)
            
def mouseHoverHandler():
    if screen == 0:
        if isMouseOnButton(640, 360, 300, 300, True):    # START button
            cursor(HAND)
        elif isMouseOnButton(10 , 655, 135, 55):    # EXIT button
            cursor(HAND)
        elif isMouseOnButton(1235, 50, 68, 69, True):    # Info button
            cursor(HAND)
        else:
            cursor(ARROW)
    elif screen == 1:
        if isMouseOnButton(10, 10, 130, 55):
            cursor(HAND)
        elif isMouseOnButton(640, 80, 350, 90, True):
            cursor(HAND)
        elif isMouseOnButton(220, 180, 330, 80): # H1
            cursor(HAND)
        elif isMouseOnButton(220, 315, 330, 80): # H2
            cursor(HAND)
        elif isMouseOnButton(220, 440, 330, 80): # H3
            cursor(HAND)
        elif isMouseOnButton(220, 565, 330, 80): # H4
            cursor(HAND)
        elif isMouseOnButton(770, 180, 330, 80): # H5
            cursor(HAND)
        elif isMouseOnButton(770, 315, 330, 80): # H6
            cursor(HAND)
        elif isMouseOnButton(770, 440, 330, 80): # H7
            cursor(HAND)
        elif isMouseOnButton(770, 565, 330, 80): # H8
            cursor(HAND)
        else:
            cursor(ARROW)
    elif screen == 2:
        if isMouseOnButton(10, 10, 130, 55): # Home Button
            cursor(HAND)
        elif isMouseOnButton(10, 655, 165, 55): # TerugKnop Button
            cursor(HAND)
        elif isMouseOnButton(50, 360, 84, 78, True) and pagina != 0: # Terug Button
            cursor(HAND)
        elif isMouseOnButton(1230, 360, 84, 78, True) and pagina != 15: # Verder Button
            cursor(HAND)
        else:
            cursor(ARROW)

def hoofdstukShow():
    imageMode(CORNER)
    image(GrijsVlak, 515, 650, 300, 55)
    textAlign(CENTER, CENTER)
    fill(0, 0, 0)
    textSize(20)
    if pagina == 0:
        text('INHOUD', 665, 677.5)
        image(H1_idle, 460, 650, 60, 55)
    elif pagina == 1 or pagina == 2:
        text('VOORBEREIDING', 665, 677.5)
        image(H2_idle, 460, 650, 60, 55)
    elif pagina == 3 or pagina == 4:
        text('BEURT', 665, 677.5)
        image(H3_idle, 460, 650, 60, 55)
    elif pagina == 5 or pagina == 6:
        text('VOORTGANG', 665, 677.5)
        image(H4_idle, 460, 650, 60, 55)
    elif pagina == 7 or pagina == 8 or pagina == 9 or pagina == 10:
        text('ARTEFACTEN', 665, 677.5)
        image(H5_idle, 460, 650, 60, 55)
    elif pagina == 11 or pagina == 12:
        text('OVERIG', 665, 677.5)
        image(H6_idle, 460, 650, 60, 55)
    elif pagina == 13:
        text('ELEMENTEN', 665, 677.5)
        image(H7_idle, 460, 650, 60, 55)
    elif pagina == 14 or pagina == 15:
        text('TERMENLIJST', 665, 677.5)
        image(H8_idle, 460, 650, 60, 55)
