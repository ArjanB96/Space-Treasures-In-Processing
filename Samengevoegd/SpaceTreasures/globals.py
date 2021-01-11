scherm = 'home'
players = []

class Card:
    def __init__(self, name, cooldown, element):
        self.size = (200, 100)
        self.name = name
        self.cooldown = cooldown
        self.element = element
        self.on_cooldown = False
        self.turn = 1
        self.dobbel = 0

class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []
        self.elements = []
        
class Button:
    def __init__(self, name, img, hover_img, pos, size, visible = True):
        self.name = name
        self.img = img
        self.hover_img = hover_img
        self.pos = pos
        self.size = size
        self.visible = visible
