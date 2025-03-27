import pygame
import random

from pathlib import Path
pyFilePath = Path(__file__).resolve().parent

# Konstanter til bruk i spillet 
COLS = 5 # Definerer  bredde
ROWS = 4 # Definerer  bredde
CELL_SIZE = 160
WIDTH, HEIGHT = COLS*CELL_SIZE, ROWS*CELL_SIZE 

CARDS = COLS * ROWS

# Initialiser Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Memory")

# lager liste med bilder og stokker dem
IMAGES = []
for i in range(1, int(CARDS/2)+1):
    MyIMG = pyFilePath.joinpath("images").joinpath(str(i)+".png")
    IMAGES.append(MyIMG)
    IMAGES.append(MyIMG)
random.shuffle(IMAGES)

# Baksidebildet
BackIMG = pyFilePath.joinpath("images").joinpath("back.png")

class Card:
    def __init__(self,front_image: str, back_image: str, row:int, col:int):
        """Card er klassen for et memory-spill-kort. Kortet brukes som en del av klassen MemmoryGame

        Args:
            front_image (str): Sti til bildet for kortets for-/bildeside
            back_image (str): Sti til bildet for kortets bakside
            row (int): Kortets rad-plassering på spillbrettet
            col (int): Kortets kolonne-plassering på spillbrettet
        """
        self._row = row
        self._col = col
        self._front_image = front_image
        self._back_image = back_image
        self.is_matched = False
        self.is_flipped = False
    
    def get_front_image(self):
        """Henter den private verdien self._front_image 

        Returns:
            str: self._front_image
        """
        return self._front_image
    
    def draw(self, surface):
        """Bliter inn kortet (med forside eller bakside) inn på spillbrettet, på sin plass

        Args:
            surface (pygame.display): pyGame's spill-vindu
        """
        if self.is_matched or self.is_flipped:
            show_image = self._front_image
        else:
            show_image = self._back_image
        show_image = pygame.image.load(show_image)
        show_image = pygame.transform.scale(show_image, (CELL_SIZE, CELL_SIZE))
        surface.blit(show_image, (self._col * CELL_SIZE, self._row * CELL_SIZE))

class MemoryGameTable:
    def __init__(self, surface):
        self._surface = surface
        self._flips = 0
        self._cards=[] #Først en tom liste
        for i in range(ROWS):
            row =[]
            for j in range(COLS):
                # Legger til en rad kort i rad 
                row.append(Card(IMAGES[i * COLS + j],BackIMG,i,j))
            self._cards.append(row)
        self._previousCard = None
        self.turnCounter=0

    def draw(self):
        # Tegner kortene ved å traversere listen med lister over kort og kjører draw() på hvert kort
        for row in self._cards:
            for card in row:
                card.draw(self._surface)        

    def handle_click(self, pos):
        col = pos[0] // CELL_SIZE
        row = pos[1] // CELL_SIZE

        if self._flips == 0:
            # Det første av to kort skal snus
            # Snu kortet om det er mulig, med fremsiden opp og ta vare på kortet
            if not self._cards[row][col].is_flipped and not self._cards[row][col].is_matched:  
                self._cards[row][col].is_flipped = True #Slik at det det tegnes med siden opp 
                self._previousCard = self._cards[row][col]
                self._flips += 1

        elif self._flips == 1:
            # Det andre av to kort skal snus
            # Snu kortet om det er mulig med fremsiden opp og sammenlign om det er lik det forige
            if not self._cards[row][col].is_flipped and not self._cards[row][col].is_matched:
                ##Snur kortet og ser om det er likt
                self._cards[row][col].is_flipped = True
                if self._previousCard.get_front_image() == self._cards[row][col].get_front_image():
                    #Det er en match, så sett is_matched = True på begge og start på to nye
                    self._previousCard.is_matched = True
                    self._cards[row][col].is_matched = True
                    self._flips = 0
                else:
                    self._flips +=1

        elif self._flips == 2:
        # Den tredje snu
            if self._cards[row][col].is_flipped and not self._cards[row][col].is_matched:
                self._cards[row][col].is_flipped=False
                self._flips +=1

        elif self._flips == 3:
        # Den fjerde snu
            if self._cards[row][col].is_flipped and not self._cards[row][col].is_matched:
                self._cards[row][col].is_flipped=False
                self._flips =0
                self.turnCounter+=1

##Oppretter MemoryGameTable som igjen oppretter celler på brettet
memoryGame = MemoryGameTable(screen)
# Spill-løkke
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            memoryGame.handle_click(event.pos)

    #Tegner brettet, som igjen håndterer tegning av celler
    memoryGame.draw()

    #Oppdaterer vinduet
    pygame.display.flip()
print(memoryGame.turnCounter)
pygame.quit()