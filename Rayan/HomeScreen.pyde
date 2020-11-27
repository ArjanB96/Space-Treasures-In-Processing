bg_index = 0
width = 1280; height = 720
screen = 0
resizeWidth = 300
resizeHeight = 300
textResize = 70
opacityText = 0
opacityChange = True

def setup():
    global planet, exitButton, exitButton2, homeButton, homeButton2, infoButton, infoButton2, regelButton, regelButton2, gidsButton, gidsButton2, terugKnopButton, terugKnopButton2, verder, verder2, terug, terug2, pijlTerug, pijlTerug2, pijlVerder, pijlVerder2
    textFont(createFont('PressStart2P.ttf', 40))
    size(width, height)
   
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
    pijlVerder = loadImage('images/PijlVerder.png')
    pijlVerder2 = loadImage('images/PijlVerder2.png')
     
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
            
        # Text test
        if opacityText == 0:
            opacityChange = True
        elif opacityText == 255:
            opacityChange = False
        
        if opacityChange:
            opacityText += 5
        else:
            opacityText -= 5   
        textAlign(CENTER, CENTER)   
        fill(opacityText, opacityText, opacityText)
        text('pagina 1', width / 2, height / 2)
        #text('pagina 2', width / 2, height / 2)
        #text('pagina 3', width / 2, height / 2)
        #text('pagina 4', width / 2, height / 2)     
             
         # Terug Button
        if not isMouseOnButton(width / 2 - 400, height / 2, 78, 78, True):
            imageMode(CENTER)
            image(pijlTerug, width / 2 - 400, height / 2, 78, 78)
        else:
            imageMode(CENTER)
            image(pijlTerug2, width / 2 - 400, height / 2, 78, 78)
        
        # Verder Button
        if not isMouseOnButton(width / 2 + 400, height/2, 78, 78, True):
            imageMode(CENTER)
            image(pijlVerder, width / 2 + 400, height / 2, 78, 78)
        else:
            imageMode(CENTER)
            image(pijlVerder2, width / 2 + 400, height / 2, 78, 78)
          

    
    
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
    global screen
    
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
        
        if isMouseOnButton(10, 655, 165, 55):
            screen = 1
        
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
