bg_index = 0
screen = 0
resizeWidth = 300
resizeHeight = 300
textResize = 70
opacityText = 0
opacityImage = 0
opacityChange = True
pagina = 0

def setup():
    global planet, exitButton, exitButton2, homeButton, homeButton2, infoButton, infoButton2, regelButton, regelButton2, gidsButton, gidsButton2, terugKnopButton, terugKnopButton2, verder, verder2, terug, terug2, pijlTerug, pijlTerug2, pijlVerder, pijlVerder2
    global pijlVerderIdle, pijlTerugIdle, Amaterasu, Aqua, Kaytsak, Blockade, Haste, Exchange, EyeDrop, Swap, Skip, Fuel, leegTekstVlak, H1, H2, H3, H4, H5, H6, H7, H8, H9, H10, H11, H12, H12, H13, H1_hover, H2_hover, H3_hover, H4_hover, H5_hover, H6_hover, H7_hover, H8_hover, H9_hover, H10_hover, H11_hover, H12_hover, H12_hover, H13_hover, Hoofdstukken, Hoofdstukken2, blauwVlak, blauwVlak2
    
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
    H9 = loadImage('images/H9.png')
    H10 = loadImage('images/H10.png')
    H11 = loadImage('images/H11.png')
    H12 = loadImage('images/H12.png')
    H13 = loadImage('images/H13.png')
    H1_hover = loadImage('images/H1_hover.png')
    H2_hover = loadImage('images/H2_hover.png')
    H3_hover = loadImage('images/H3_hover.png')
    H4_hover = loadImage('images/H4_hover.png')
    H5_hover = loadImage('images/H5_hover.png')
    H6_hover = loadImage('images/H6_hover.png')
    H7_hover = loadImage('images/H7_hover.png')
    H8_hover = loadImage('images/H8_hover.png')
    H9_hover = loadImage('images/H9_hover.png')
    H10_hover = loadImage('images/H10_hover.png')
    H11_hover = loadImage('images/H11_hover.png')
    H12_hover = loadImage('images/H12_hover.png')
    H13_hover = loadImage('images/H13_hover.png')
    blauwVlak = loadImage('images/BlauwVak.png')
    blauwVlak2 = loadImage('images/BlauwVak2.png')
    
def draw():
    global screen, resizeWidth, resizeHeight, textResize, opacityText, opacityChange, opacityImage
    
    # Background
    cycleBackground()
    mouseHoverHandler()
    
    #############
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
        if isMouseOnButton(width / 2, height / 2, 300, 300, True):
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
        imageShow(exitButton, exitButton2, 10, 655, 135, 55)
        
        # Info button
        imageShow(infoButton, infoButton2, 1235, 50, 68, 69, True)
        

    #############
    # Info scherm
    if screen == 1:
        #global 
        
        tint(255)
        #Home Button
        imageShow(homeButton, homeButton2, 10, 10, 130, 55)
          
        # Regel Button
        imageShow(regelButton, regelButton2, 640, 290, 390, 110, True)

        # Hoofdstukken Button
        imageShow(Hoofdstukken, Hoofdstukken2, 640, 440, 750, 100, True)
     
     
    ############### 
    # Regel Screen       
    if screen == 2:
        
        tint(255)    
        # Hoofdstuk knop
        imageShow(Hoofdstukken, Hoofdstukken2, 640 , 35, 375, 55, True)
        #Home Button
        imageShow(homeButton, homeButton2, 10, 10, 130, 55)
        # TerugKnop Button
        imageShow(terugKnopButton, terugKnopButton2, 10, 655, 165, 55) 
        
        #Hoofdstukken knoppen
        #if pagina == 0:
        #   image(H1, 220, 40, 80, 80) 
        #else:
        #    image(H1, 220, 40, 55, 55)
        #if pagina == 1:
        #    image(H2, 220 + 80, 40, 80, 80)
        #else:
        #    image(H2, 220 + 80, 40, 55, 55)
        #image(H3, 220 + 80 * 2, 40, 55, 55)
        #image(H5, 220 + 80 * 3, 40, 55, 55)
        #image(H6, 220 + 80 * 4, 40, 55, 55)
        #image(H7, 220 + 80 * 5, 40, 55, 55)
        #image(H8, 220 + 80 * 6, 40, 55, 55)
        #image(H9, 220 + 80 * 7, 40, 55, 55)
        #image(H10, 220 + 80 * 8, 40, 55, 55)
        #image(H11, 220 + 80 * 9, 40, 55, 55)
        #image(H12, 220 + 80 * 10, 40, 55, 55)
        #image(H13, 220 + 80 * 11, 40, 55, 55)
        
        hoofdstukShow()
        # Fade in van de tekst
        if opacityText <= 255:
            opacityText += 20
        # Fade van images
        if opacityImage <= 250:
            opacityImage += 15

            
        # Zwart scherm achter de tekst
        tint(255, 100)
        imageMode(CORNER)
        image(leegTekstVlak, 100, 85)
    
        # TEKST  
        textAlign(CORNER, CENTER)   
        fill(opacityText, opacityText, opacityText)
        tint(opacityImage)
        if pagina == 0:
            textSize(20)
            text('INHOUD SPEL:\n- 10 hexagon map stukken,\n- 38 instructiekaarten,\n- 49 fiches,\n- 5 ruimteschepen,\n- 1 dobbelsteen.\n\nDOEL:\nVind twee Elementen van verschillende element \nsoorten en win!\n\nSPELERS:\nSpace Treasures is te spelen met 4 of 5 mensen. ', 125, height / 2)
        if pagina == 1:
            textSize(30)
            text('VOORBEREIDING:', 125, 130)
            textSize(20)
            text('Bord-deel Aarde wordt als eerst neergelegd en wordt \ngebruikt als startplaneet, schud vervolgens de \nresterende bord-delen en leg deze met de goede kant \nomlaag op de tafel. In het midden op Aarde wordt de \nbrandstof fiche neergelegd.\n\nElke speler krijgt zijn eigen ruimteschip. De \nspelers mogen naar eigen keuze zijn/haar \nruimteschip op 1 van de 6 grijze hoeken plaatsen, \nmaximaal 1 speler per hoek. Schud de \ninstructiekaarten en leg deze bij het bord-deel met \nde goede kant omlaag. Elke speler krijgt een \nfiche van elk Element.', 125, height / 2 - 40)
            image(Kaytsak, width / 2 - 300, 500 ,65, 80)
            image(Aqua, width / 2, 500, 65, 80)
            image(Amaterasu, width / 2 + 300, 500, 65, 80)
            textSize(15)
            text('Kaytsak', width / 2 - 325, 600)
            text('Aqua', width / 2 + 5, 600)
            text('Amaterasu', width / 2 + 275, 600)
        if pagina == 2:
            textSize(20)
            text('Om te bepalen wie er begint met het spel, dobbelt \nelke speler 1 keer. De speler die het hoogst aantal \nogen heeft gegooid begint met het spel. Het spel \nkan nu beginnen!', 130, height / 2)
        if pagina == 3:
            textSize(30)
            text('EERSTE BEURT:', 125, 220)
            textSize(20)
            text('De speler die begint trekt 1 van de \ninstructiekaarten en kiest de instructie die hij/zij \nkiest. De speler moet stappen zetten omdat er op \nplaneet "Aarde" geen Artefact te vinden is. Het \nspel gaat met de klok mee.Als eerste willen de \nspelers naar de "brandstof" plek gaan in het midden \nvan de planeet om andere planeten te kunnen \nontdekken. Op de andere planeten zijn de betreffende \nArtefacten, Elementen en meer brandstof te vinden.', 125, height / 2)     
        if pagina == 4:
            textSize(30)
            text('PER BEURT:', 125, 220)
            textSize(20)
            text('Per beurt kan je 3 dingen doen:\n1: Een instructiekaart pakken,\n2: een Artefact gebruiken\n3: of een Element maken.\n\nBij de eerste paar beurten zal je nog geen \nArtefacten hebben, dus kan je het tweede en derde \nnog niet doen. Dan moeten er instructiekaarten \nworden gepakt.', 125, height / 2)
        if pagina == 5:
            textSize(30)
            text('PLANEET ONTDEKKEN:', 125, 245)
            textSize(20)
            text('Zodra een speler een brandstof fiche heeft gekregen \nmoet de speler meteen een planeet ontdekken. Dit doe \nje door een planeet \nte pakken van de stapel, de planeet mag alleen \ngeplaatst worden aangrenzend aan de planeet waar de \nspeler op staat. De speler mag kiezen aan welke kant \nde planeet ontdekt wordt', 130, height/2)
        if pagina == 6:
            textSize(30)
            text('BEWEGING:', 125, 240)
            textSize(20)
            text('Er kan alleen gelopen worden via de lijnen. Je moet \nhet aantal stappen zetten dat aangegeven is, tevens \nlaat je ook je instructiekaart aan je medespelers \nzien. Je mag niet heen en weer blijven lopen. Als je \nvan planeet naar planeet loopt, loop je via de grote \nwitte vakken, daarnaast mag je niet in 1 beurt naar \nmeerdere planeet gaan.', 125, height/2)
        if pagina == 7:
            textSize(30)
            text('ARTEFACT PAKKEN:', 125, 130)
            textSize(20)
            text('Als je een instructiekaart krijgt met een Artefact \nerop, kan je dobbelen voor een Artefact. LET OP! Op \nplaneet Aarde  kan geen Artefact gevonden worden! \nLinksboven staan de minimaal aantal ogen die \ngegooid moeten worden om deze Artefact te mogen \npakken. Als je het minimaal aantal ogen hebt gegooid \nof hoger mag je de kaart bij je houden. De element \nsoort wordt bepaald door op welke planeet je staat. \nAls je op planeet Kaytsak staat, leg je jouw \nArtefact bij het fiche Kaytsak.\n\nPer planeet is er maar 1 artefact te vinden per \npersoon. Als je op planeet x van Amaterasu een \nArtefact hebt gepakt kan je alleen nog Artefacten \nvan Amaterasu vinden op y en z.', 125, height/2)
        if pagina == 8:
            textSize(30)
            text('ARTEFACT GEBRUIKEN:', 125, 230)
            textSize(20)
            text('Als de speler 1 van zijn / haar Artefacten wil \ngebruiken, kost dit een beurt. Je mag dus niet een \ninstructiekaart pakken en daarna een Artefact \ngebruiken. Behalve bij Haste.Als de Artefact een \nafkoeltijd heeft, moet je die na gebruik met de \ngoede kant omlaag neerleggen voor het aantal rondes \ndat aangegeven staat. Per beurt mag er maar 1 \nArtefact gebruikt worden.', 125, height/2)
        if pagina == 9:
            textSize(30)
            text('De Artefacten zijn:', 125, 130)
            textSize(20)
            image(Swap, 145, 155, 60, 96)
            image(Haste, 130, 270, 75, 80)
            image(EyeDrop, 125, 370, 80, 80)
            image(Skip, 130, 490, 60, 78)
            text('Swap: Speler met dit artefact mag 2 spelers \nruilen van plek. Inclusief zichzelf met een \nandere. (Minimaal 4 ogen, afkoeltijd 4 beurten.)\n\n\nHaste: Elke beurt 1 extra stap. \n(Minimaal 4  ogen.)\n\n\nEyeDrop: Een oog minder nodig bij dobbelen om \nArtefact te krijgen. (Minimaal 4 ogen.)\n\n\nSkip: Kies een speler, hij/zij moet een beurt \noverslaan. \n(Minimaal 5 ogen, afkoeltijd 3 beurten.)', 125 + 90, height/2)
        if pagina == 10:
            textSize(20)
            image(Exchange, 130, 200, 72, 78)
            image(Blockade, 115, 380, 96, 96)
            text('Exchange: Ruil 1 Artefact naar keuze met iemand \nop dezelfde planeet. De element-soort verandert \nniet. Eventuele cooldown op geruilde kaart gaat \nweg.(Minimaal 3 ogen, afkoeltijd 4 beurten.)\n\n\nBlockade: Zet een blokkade neer om te voorkomen \ndat andere spelers de planeet betreden. \n(minimaal 3 ogen, afkoeltijd 4 beurten.)\nGebruik: Je legt het "Blockade" fiche aan 1 van \nde kanten op de planeet waar jij op staat. Hij \nkomt tussen de hoekpunten. Blijft 2 rondes \nstaan. Blockade geldt niet voor de gebruiker.', 125 + 90, height/2)
        if pagina == 11:
            textSize(30)
            text('MAXIMAAL ARTEFACTEN:', 125, 130)
            textSize(20)
            text('Elke speler mag maximaal 5 Artefacten hebben. De \nspeler mag niet dobbelen voor een Artefact als hij \ner 5 heeft.', 125, height/2- 170)
            textSize(30)
            text('BRANDSTOF:', 125, 300)
            textSize(20)
            text('Om te reizen tussen eerder ontdekte planeten is geen \nbrandstof nodig. Als de speler de planeet heeft \nneergelegd moet hij/zij ook de brandstof fiche in \nhet midden neerleggen.', 125, height / 2 + 15)
            imageMode(CENTER)
            image(Fuel, width / 2, height / 2 + 150, 150, 150)
            textSize(25)
            text('Brandstof', width / 2 - 105, height / 2 + 250)
        if pagina == 12:
            textSize(30)
            text('KAARTEN:', 125, 130)
            textSize(20)
            text('Na gebruik wordt deze naast de stapel gelegd. Zodra \nde stapel op is wordt die geschud en kan daarna weer \ngebruikt worden.', 125, height/2-165)    
            textSize(30)
            text('ELKE PLANEET ONTDEKT:', 125, 320)
            textSize(20)
            text('Nadat elke planeet ontdekt is, mag je zodra je op \neen brandstof plek komt reizen naar een aangrenzende \nplaneet. Je komt dan op de brandstof plek. Je mag \nniet op dezelfde plek meteen weer naar een andere \nplaneet.', 125, height/2 + 50)
        if pagina == 13:
            textSize(30)
            text('ELEMENTEN:', 130, 130)
            textSize(20)
            text('Als je een instructiekaart hebt gepakt met de optie \nom een Element te maken kan je 3 Artefacten van \nhetzelfde soort element inruilen voor het \ndesbetreffende Element. De Artefacten die ingeruild \nzijn, leg je weg op de stapel van gebruikte kaarten. \nJe pakt dan een fiche van het Element dat je hebt \ngekregen.\n\nVoorbeeld:\nAls je 3 Artefacten hebt van de element Amaterasu. \nDan kan je deze inruilen voor een Element fiche van \nAmaterasu. Mits je de instructiekaart krijgt met de \noptie om een Element te maken.', 130, height/2-40)
            image(Kaytsak, width / 2 - 300, 500 ,80, 95)
            image(Aqua, width / 2, 500, 80, 95)
            image(Amaterasu, width / 2 + 300, 500, 80, 95)
            textSize(15)
            text('Kaytsak', width / 2 - 320, 610)
            text('Aqua', width / 2 + 10, 610)
            text('Amaterasu', width / 2 + 275, 610)
        if pagina == 14:
            textSize(30)
            text('TERMENLIJST:', 152, 130)
            textSize(20)
            text('- Brandstof:\nMet brandstof kan je andere planeten ontdekken.\n\n- Instructiekaarten:\nDit zijn de kaarten waar een keuze gemaakt moet \nworden tussen stappen zetten of een \nArtefact / Element maken.\n\n- Artefacten:\nDe Artefacten heb je nodig om Elementen te maken. \nTevens kunnen deze aan jou voordelen geven of \nandere spelers hinderen.\n\n- Elementen:\nDit is het voorwerp dat nodig is om te winnen. \n2 verschillende Elementen zijn hiervoor nodig.', 152, height / 2)
        if pagina == 15:
            text('- Afkoeltijd:\nDit is het aantal rondes dat je je gebruikte \nArtefact niet meer kunt gebruiken.', 130, height / 2)
        
        
        tint(255)     
        imageMode(CENTER)     
        # Terug Button
        if pagina == 0:
            image(pijlTerugIdle, width / 2 - 590, height / 2, 84, 78)
        else:
            imageShow(pijlTerug, pijlTerug2, width / 2 - 590, height / 2, 84, 78, True)
        
        # Verder Button
        if pagina == 15:
            image(pijlVerderIdle, width / 2 + 590, height / 2, 84, 78)
        else:
            imageShow(pijlVerder, pijlVerder2, width / 2 + 590, height / 2, 84, 78, True)

    
    #####################
    # Hoofdstukken Screen
    elif screen == 3:
  
        #Home Button
        imageShow(homeButton, homeButton2, 10, 10, 130, 55)
        # TerugKnop Button
        imageShow(terugKnopButton, terugKnopButton2, 10, 655, 165, 55)
        fill(0, 0, 0)
        textSize(17)
        textAlign(CENTER, CENTER)
        # H1 : Inhoud
        imageShow(H1, H1_hover, 150, 100, 80, 80, wdthAdd = 250)
        imageShow(blauwVlak, blauwVlak2, 230, 100, 250, 80, wdthMinus = 80, wdthAdd = 80)
        text('INHOUD', 355, 140)
        # H2 : Voorbereiding
        imageShow(H2, H2_hover, 150, 250, 80, 80, wdthAdd = 250) 
        imageShow(blauwVlak, blauwVlak2, 230, 250, 250, 80, wdthMinus = 80, wdthAdd = 80)
        text('VOORBEREIDING', 355, 290)
        # H3 : Beurt
        imageShow(H3, H3_hover, 150, 400, 80, 80, wdthAdd = 250) 
        imageShow(blauwVlak, blauwVlak2, 230, 400, 250, 80, wdthMinus = 80, wdthAdd = 80)
        text('BEURT', 355, 440)
        # H4 : Voortgang
        imageShow(H4, H4_hover, 150, 550, 80, 80, wdthAdd = 250) 
        imageShow(blauwVlak, blauwVlak2, 230, 550, 250, 80, wdthMinus = 80, wdthAdd = 80)
        text('VOORTGANG', 355, 590)
      
                          
def mousePressed():
    global screen, pagina, opacityText, opacityImage
    
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
        # Hoofdstukken button
        if isMouseOnButton(640, 440, 750, 110, True):
            screen = 3
            
    # All buttons for Regel Screen
    if screen == 2:
        # Home Button
        if isMouseOnButton(10, 10, 130, 55):
            screen = 0
            pagina = 0 # To reset 'pagina'
            opacityText = 0 # To reset Fade
            opacityImage = 0 # To reset Fade
        # Terug button
        if isMouseOnButton(10, 655, 165, 55):
            screen = 1
            pagina = 0 # To reset 'pagina'
            opacityText = 0 # To reset Fade
            opacityImage = 0 # To reset Fade
        # Terug Button
        if isMouseOnButton(width / 2 - 590, height / 2, 78, 78, True) and pagina != 0:
            pagina -= 1
            opacityText = 0 # To reset Fade
            opacityImage = 0 # To reset Fade
        # Verder Button
        if isMouseOnButton(width / 2 + 590, height / 2, 78, 78, True) and pagina != 15:
            pagina += 1
            opacityText = 0 # To reset Fade
            opacityImage = 0 # To reset Fade
        # Hoofdstukken Button
        if isMouseOnButton(640 , 35, 375, 55, True):
            screen = 3
            pagina = 0
            opacityText = 0 # To reset Fade
            opacityImage = 0 # To reset Fade
    
    # All buttons for Hoofdstukken 
    if screen == 3:
        # Home Button
        if isMouseOnButton(10, 10, 130, 55):
            screen = 0
            pagina = 0 # To reset 'pagina'
            opacityText = 0 # To reset Fade
            opacityImage = 0 # To reset Fade
        # Terug button
        if isMouseOnButton(10, 655, 165, 55):
            screen = 1
            pagina = 0 # To reset 'pagina'
            opacityText = 0 # To reset Fade
            opacityImage = 0 # To reset Fade
        # H1
        if isMouseOnButton(150, 100, 80 + 250, 80):
            screen = 2 
            pagina = 0
        # H2
        if isMouseOnButton(150, 250, 80 + 250, 80):
            screen = 2
            pagina = 1
        # H3
        if isMouseOnButton(105, 400, 80 + 250, 80):
            screen = 2
            pagina = 3
        # H4
        if isMouseOnButton(105, 550, 80 + 250, 80):
            screen = 2
            pagina = 5
        
               
# Function to check if mouse is on the button
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
        elif isMouseOnButton(width / 2 - 590, height / 2, 84, 78, True) and pagina != 0: # Terug Button
            cursor(HAND)
        elif isMouseOnButton(width / 2 + 590, height / 2, 84, 78, True) and pagina != 15: # Verder Button
            cursor(HAND)
        elif isMouseOnButton(640 , 35, 375, 55, True): # Hoofstukken Button
            cursor(HAND)
        else:
            cursor(ARROW)
    elif screen == 3:
        if isMouseOnButton(10, 10, 130, 55):
            cursor(HAND)
        elif isMouseOnButton(10, 655, 165, 55):
            cursor(HAND)
        elif isMouseOnButton(150, 100, 80 + 250, 80):
            cursor(HAND)
        elif isMouseOnButton(150, 250, 80 + 250, 80):
            cursor(HAND)
        elif isMouseOnButton(150, 400, 80 + 250, 80):
            cursor(HAND)
        elif isMouseOnButton(150, 550, 80 + 250, 80):
            cursor(HAND)
        else:
            cursor(ARROW)

def hoofdstukShow():
    imageMode(CENTER)
    textAlign(CENTER, CENTER)
    textSize(20)
    fill(255, 255, 255)
    text('Hoofdstuk: ', 500, 674)  
    if pagina == 0:
        image(H1, 640, 675, 75, 75)
    if pagina == 1 or pagina == 2:
        image(H2, 640, 675, 75, 75)
    if pagina == 3 or pagina == 4:
        image(H3, 640, 675, 75, 75)
    if pagina == 5 or pagina == 6:
        image(H4, 640, 675, 75, 75)
    if pagina == 7 or pagina == 8 or pagina == 9 or pagina == 10:
        image(H5, 640, 675, 75, 75)
    if pagina == 11 or pagina == 12:
        image(H6, 640, 675, 75, 75)
    if pagina == 13:
        image(H7, 640, 675, 75, 75)
    if pagina == 14 or pagina == 15:
        image(H8, 640, 675, 75, 75)
