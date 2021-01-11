import home_screen, player_menu, main_game, artefact_screen, globals

def setup():
    frameRate(30)
    size(1280,720)
    background(0)
    
    home_screen.setup()
    player_menu.setup()
    main_game.setup()
    artefact_screen.setup()
    
def draw():
    if globals.scherm == 'home':
        home_screen.draw()
    elif globals.scherm == 'players':
        player_menu.draw()
    elif globals.scherm == 'main':
        main_game.draw()
    elif globals.scherm == 'artifact':
        artefact_screen.draw()
        
def mousePressed():
    if globals.scherm == 'home':
        home_screen.mousePressed()
    elif globals.scherm == 'players':
        player_menu.mousePressed()
    elif globals.scherm == 'main':
        main_game.mousePressed()
    elif globals.scherm == 'artifact':
        artefact_screen.mousePressed()
        
def keyTyped():
    if globals.scherm == 'players':
        player_menu.keyTyped()
