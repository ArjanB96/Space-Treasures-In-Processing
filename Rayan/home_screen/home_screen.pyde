bg_index = 0
screen = 0
resizeWidth = 300
resizeHeight = 300
textResize = 70
opacityText = 0
opacityImage = 0
opacityChange = True
pagina = 0
screenList = []

def setup():
    global planet, exitButton, exitButton2, homeButton, homeButton2, infoButton, infoButton2, regelButton, regelButton2, gidsButton, gidsButton2, terugKnopButton, terugKnopButton2, verder, verder2, terug, terug2, pijlTerug, pijlTerug2, pijlVerder, pijlVerder2, pijlVerderIdle, pijlTerugIdle, Amaterasu, Aqua, Kaytsak, Blockade, Haste, Exchange, EyeDrop, Swap, Skip, Fuel, leegTekstVlak, H1, H2, H3, H4, H5, H6, H7, H8, H1_hover, H2_hover, H3_hover, H4_hover, H5_hover, H6_hover, H7_hover, H8_hover, Hoofdstukken, Hoofdstukken2, blauwVlak, blauwVlak2, H1_idle, H2_idle, H3_idle, H4_idle, H5_idle, H6_idle, H7_idle, H8_idle, hoofdstukVlak, pijlTerugPaars, pijlTerug2Paars, pijlVerderPaars, pijlVerder2Paars
    textFont(createFont('PressStart2P.ttf', 40))
    size(1280, 720)
    
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
    pijlTerugPaars = loadImage('images/PijlTerugPaars.png')
    pijlTerug2Paars = loadImage('images/PijlTerug2Paars.png')
    pijlTerugIdle = loadImage('images/PijlTerugIdle.png')
    pijlVerder = loadImage('images/PijlVerder.png')
    pijlVerder2 = loadImage('images/PijlVerder2.png')
    pijlVerderPaars = loadImage('images/PijlVerderPaars.png')
    pijlVerder2Paars = loadImage('images/PijlVerder2Paars.png')
    pijlVerderIdle = loadImage('images/PijlVerderIdle.png')
    leegTekstVlak = loadImage('images/LeegTekstVlak.png')
    
    Amaterasu = loadImage('images/Amaterasu.png')
    Aqua = loadImage('images/Aqua.png')
    Kaytsak = loadImage('images/Kaytsak.png')
    Blockade = loadImage('images/Blockade.png')
    Exchange = loadImage('images/Exchange.png')
    EyeDrop = loadImage('images/EyeDrop.png')
    Haste = loadImage('images/Haste.png')
    Skip = loadImage('images/Skip.png')
    Swap = loadImage('images/Swap.png')
    Fuel = loadImage('images/Fuel.png')
    
    Hoofdstukken = loadImage('images/Hoofdstukken.png')
    Hoofdstukken2 = loadImage('images/Hoofdstukken2.png')
    H1 = loadImage('images/H1.png')
    H2 = loadImage('images/H2.png')
    H3 = loadImage('images/H3.png')
    H4 = loadImage('images/H4.png')
    H5 = loadImage('images/H5.png')
    H6 = loadImage('images/H6.png')
    H7 = loadImage('images/H7.png')
    H8 = loadImage('images/H8.png')
    H1_hover = loadImage('images/H1_hover.png')
    H2_hover = loadImage('images/H2_hover.png')
    H3_hover = loadImage('images/H3_hover.png')
    H4_hover = loadImage('images/H4_hover.png')
    H5_hover = loadImage('images/H5_hover.png')
    H6_hover = loadImage('images/H6_hover.png')
    H7_hover = loadImage('images/H7_hover.png')
    H8_hover = loadImage('images/H8_hover.png')
    H1_idle = loadImage('images/H1_idle.png')
    H2_idle = loadImage('images/H2_idle.png')
    H3_idle = loadImage('images/H3_idle.png')
    H4_idle = loadImage('images/H4_idle.png')
    H5_idle = loadImage('images/H5_idle.png')
    H6_idle = loadImage('images/H6_idle.png')
    H7_idle = loadImage('images/H7_idle.png')
    H8_idle = loadImage('images/H8_idle.png')
    hoofdstukVlak = loadImage('images/HoofdstukVak.png')
    blauwVlak = loadImage('images/BlauwVak.png')
    blauwVlak2 = loadImage('images/BlauwVak2.png')
    
def draw():
    global screen, resizeWidth, resizeHeight, textResize, opacityText, opacityChange, opacityImage

    cycleBackground()
    mouseHoverHandler()
    
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
            image(planet, 640, 360, resizeWidth, resizeHeight)
            if resizeWidth <= 320:
                resizeWidth += 10; resizeHeight += 10
            if textResize <= 75:
                textResize += 1.2
            textSize(textResize)
            text('START', 640, 360)
        else:
            image(planet, 640, 360, resizeWidth, resizeHeight)
            if resizeWidth >= 305:
                resizeWidth -= 10; resizeHeight -= 10
            if textResize >= 70:
                textResize -= 1.1
            textSize(textResize)
            text('START', 640, 360)
            
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
        imageShow(regelButton, regelButton2, 640, 290, 390, 110, True)
        # Hoofdstukken Button
        imageShow(Hoofdstukken, Hoofdstukken2, 640, 440, 750, 100, True)
     
    # Regel Screen       
    elif screen == 2:
        
        tint(255)    
        # Hoofdstuk knop
        imageShow(Hoofdstukken, Hoofdstukken2, 640, 50, 400, 65, True)
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
            
    # Hoofdstukken Screen
    elif screen == 3:
  
        #Home Button
        imageShow(homeButton, homeButton2, 10, 10, 130, 55)
        # TerugKnop Button
        imageShow(terugKnopButton, terugKnopButton2, 10, 655, 165, 55)
        
        fill(0, 0, 0)
        textSize(18)
        textAlign(CENTER, CENTER)
        # H1 : Inhoud
        imageShow(H1, H1_hover, 220, 100, 80, 80, wdthAdd = 250)
        imageShow(blauwVlak, blauwVlak2, 300, 100, 250, 80, wdthMinus = 80, wdthAdd = 80)
        text('INHOUD', 420, 140)
        # H2 : Voorbereiding
        imageShow(H2, H2_hover, 220, 250, 80, 80, wdthAdd = 250) 
        imageShow(blauwVlak, blauwVlak2, 300, 250, 250, 80, wdthMinus = 80, wdthAdd = 80)
        text('VOORBEREIDING', 420, 290)
        # H3 : Beurt
        imageShow(H3, H3_hover, 220, 400, 80, 80, wdthAdd = 250) 
        imageShow(blauwVlak, blauwVlak2, 300, 400, 250, 80, wdthMinus = 80, wdthAdd = 80)
        text('BEURT', 420, 440)
        # H4 : Voortgang
        imageShow(H4, H4_hover, 220, 550, 80, 80, wdthAdd = 250) 
        imageShow(blauwVlak, blauwVlak2, 300, 550, 250, 80, wdthMinus = 80, wdthAdd = 80)
        text('VOORTGANG', 420, 590)
        # H5 : Artefacten
        imageShow(H5, H5_hover, 770, 100, 80, 80, wdthAdd = 250)
        imageShow(blauwVlak, blauwVlak2, 850, 100, 250, 80, wdthMinus = 80, wdthAdd = 80)
        text('ARTEFACTEN', 970, 140)
        # H6 : Overig
        imageShow(H6, H6_hover, 770, 250, 80, 80, wdthAdd = 250)
        imageShow(blauwVlak, blauwVlak2, 850, 250, 250, 80, wdthMinus = 80, wdthAdd = 80)
        text('OVERIG', 970, 290)
        # H7 : Elementen
        imageShow(H7, H7_hover, 770, 400, 80, 80, wdthAdd = 250)
        imageShow(blauwVlak, blauwVlak2, 850, 400, 250, 80, wdthMinus = 80, wdthAdd = 80)
        text('ELEMENTEN', 970, 440)
        # H8 : Termenlijst
        imageShow(H8, H8_hover, 770, 550, 80, 80, wdthAdd = 250)
        imageShow(blauwVlak, blauwVlak2, 850, 550, 250, 80, wdthMinus = 80, wdthAdd = 80)
        text('TERMENLIJST', 970, 590)
        
def mousePressed():
    global screen, pagina, opacityText, opacityImage, screenList
    # Home screen
    if screen == 0:
        if isMouseOnButton(10 , 655, 135, 55): # EXIT button
            exit()
        elif isMouseOnButton(1235, 50, 68, 69, True): # Info Button
            screen = 1   
            screenList.append(screen)
    # Info Screen
    elif screen == 1:
        if isMouseOnButton(10, 10, 130, 55): # Home Button
            screen = 0
            del screenList[:]
        elif isMouseOnButton(640, 290, 390, 110, True): # Regel button
            screen = 2
            screenList.append(screen)
        elif isMouseOnButton(640, 440, 750, 110, True): # Hoofdstukken button
            screen = 3
            screenList.append(screen)
    # Regel Screen
    elif screen == 2:
        if isMouseOnButton(10, 10, 130, 55): # Home Button
            screen = 0
            pagina = 0 
            opacityText = 0 
            opacityImage = 0
            del screenList[:]
        elif isMouseOnButton(10, 655, 165, 55): # Terug button
            screen = screenList[-2]
            del screenList[-1]
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
        elif isMouseOnButton(640, 50, 400, 65, True): # Hoofdstukken Button
            screen = 3
            screenList.append(screen)
            opacityText = 0 
            opacityImage = 0
    # Hoofdstukken 
    elif screen == 3:
        if isMouseOnButton(10, 10, 130, 55): # Home Button
            screen = 0
            del screenList[:]
            pagina = 0
            opacityText = 0 
            opacityImage = 0 
        elif isMouseOnButton(10, 655, 165, 55): # Terug button
            del screenList[-1]
            screen = screenList[-1]
            opacityText = 0
            opacityImage = 0 
        elif isMouseOnButton(220, 100, 330, 80): # H1
            screen = 2 
            pagina = 0
            screenList.append(screen)
        elif isMouseOnButton(220, 250, 330, 80): # H2
            screen = 2
            pagina = 1
            screenList.append(screen)
        elif isMouseOnButton(220, 400, 330, 80): # H3
            screen = 2
            pagina = 3
            screenList.append(screen)
        elif isMouseOnButton(220, 550, 330, 80): # H4
            screen = 2
            pagina = 5
            screenList.append(screen)
        elif isMouseOnButton(770, 100, 330, 80): # H5
            screen = 2
            pagina = 7
            screenList.append(screen)
        elif isMouseOnButton(770, 250, 330, 80): # H6
            screen = 2
            pagina = 11
            screenList.append(screen)
        elif isMouseOnButton(770, 400, 330, 80): # H7
            screen = 2
            pagina = 13
            screenList.append(screen)
        elif isMouseOnButton(770, 550, 330, 80): # H8
            screen = 2
            pagina = 14
            screenList.append(screen)
    
def isMouseOnButton(posX, posY, buttonWidth, buttonHeight, centered = False):
    if centered:
        return True if posX - buttonWidth / 2 < mouseX < posX + buttonWidth / 2 and posY - buttonHeight / 2 < mouseY < posY + buttonHeight / 2 else False
    else:
        return True if posX < mouseX < posX + buttonWidth and posY < mouseY < posY + buttonHeight else False
  
def cycleBackground():
    global bg_index
    background(loadImage('background/bg' + str(bg_index) + '.jpg'))
    bg_index = bg_index + 1 if bg_index < 32 else 0

def imageShow(img, img2, x, y, wdth, hght, centered = False, wdthAdd = 0, wdthMinus = 0):
    if centered:
        imageMode(CENTER)
    else:
        imageMode(CORNER)
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
        elif isMouseOnButton(640, 290, 390, 110, True):
            cursor(HAND)
        elif isMouseOnButton(640, 440, 390, 110, True):
            cursor(HAND)
        elif isMouseOnButton(640, 440, 750, 110, True):
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
        elif isMouseOnButton(640, 50, 400, 65, True): # Hoofstukken Button
            cursor(HAND)
        else:
            cursor(ARROW)
    elif screen == 3:
        if isMouseOnButton(10, 10, 130, 55):
            cursor(HAND)
        elif isMouseOnButton(10, 655, 165, 55):
            cursor(HAND)
        elif isMouseOnButton(220, 100, 330, 80):
            cursor(HAND)
        elif isMouseOnButton(220, 250, 330, 80):
            cursor(HAND)
        elif isMouseOnButton(220, 400, 330, 80):
            cursor(HAND)
        elif isMouseOnButton(220, 550, 330, 80):
            cursor(HAND)
        elif isMouseOnButton(770, 100, 330, 80):
            cursor(HAND)
        elif isMouseOnButton(770, 250, 330, 80):
            cursor(HAND)
        elif isMouseOnButton(770, 400, 330, 80):
            cursor(HAND)
        elif isMouseOnButton(770, 550, 330, 80):
            cursor(HAND)
        else:
            cursor(ARROW)

def hoofdstukShow():
    imageMode(CORNER)
    image(hoofdstukVlak, 460, 650, 300, 55)
    if pagina == 0:
        image(H1_idle, 760, 650, 60, 55)
    elif pagina == 1 or pagina == 2:
        image(H2_idle, 760, 650, 60, 55)
    elif pagina == 3 or pagina == 4:
        image(H3_idle, 760, 650, 60, 55)
    elif pagina == 5 or pagina == 6:
        image(H4_idle, 760, 650, 60, 55)
    elif pagina == 7 or pagina == 8 or pagina == 9 or pagina == 10:
        image(H5_idle, 760, 650, 60, 55)
    elif pagina == 11 or pagina == 12:
        image(H6_idle, 760, 650, 60, 55)
    elif pagina == 13:
        image(H7_idle, 760, 650, 60, 55)
    elif pagina == 14 or pagina == 15:
        image(H8_idle, 760, 650, 60, 55)
