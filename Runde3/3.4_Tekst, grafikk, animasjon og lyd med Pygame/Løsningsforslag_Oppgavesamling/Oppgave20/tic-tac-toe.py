import pygame
from pathlib import Path
pyFilePath = Path(__file__).resolve().parent


# Konstanter til bruk i spillet 
WIDTH, HEIGHT = 300, 300 # Bør være like
GRID_SIZE = 3 # Definerer høyde og bredde

CELL_SIZE = WIDTH // GRID_SIZE 
BGCOLOR = (255, 255, 255)
LINE_COLOR = (0, 0, 0)

# Initialiser Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe")

# Laster inn bilder og skalerer dem til celle-størrelse
X_IMG = pygame.image.load(pyFilePath.joinpath("images").joinpath("x.png"))
O_IMG = pygame.image.load(pyFilePath.joinpath("images").joinpath("o.png"))
X_IMG = pygame.transform.scale(X_IMG, (CELL_SIZE, CELL_SIZE))
O_IMG = pygame.transform.scale(O_IMG, (CELL_SIZE, CELL_SIZE))

class Cell:
    def __init__(self, row:int, col:int):
        """ Celle på spillbrettet
            Er avhengig av de globale variablene CELL_SIZE:int, X_IMG:pygame.image og O_IMG:pygame.image

        Args:
            row (int): cellens rad-plassering
            col (int): cellens kolonne-plassering
        """
        self.row = row
        self.col = col
        self.mark = None  # 'X' eller 'O'

    def draw(self, surface):
        """Tegner cellen på vinduet/surface, tegner et x-bilde ved self.mark = "x" og o-bilde ved "o" 

        Args:
            surface (pyagme-display): Vinduet til pygame
        """
        if self.mark == 'x':
            surface.blit(X_IMG, (self.col * CELL_SIZE, self.row * CELL_SIZE))
        elif self.mark == 'o':
            surface.blit(O_IMG, (self.col * CELL_SIZE, self.row * CELL_SIZE))

    def sett_mark(self, turn):
        """Setter markeringen hvis cellen er tom. Setter mark til "x" eller "o" om det er tomt

        Args:
            turn (str): Merket som skal settes "x" eller "o"

        Returns:
            bool: Om merket er satt eller ikke
        """
        if self.mark is None:
            self.mark = turn
            return True
        return False

class Board:
    def __init__(self):
        """ Board som er spillbrettet
            Klassen er avhengig av de globale variablene CELL_SIZE:int, GRID_SIZE:int, BGCOLOR:tuple, LINE_COLOR:tuple, WIDTH:int og HEIGHT:int
        """
        #Oppretter listen med 3 lister (rader) av 3 Celler i hver kolonne
        self.cells=[] #Først en tom liste
        for i in range(GRID_SIZE):
            row =[]
            for j in range(GRID_SIZE):
                # Legger til en celle i rad med index-er til cellen selv 
                # om hvilken rad og kolonne den tilhører
                row.append(Cell(i,j))
            self.cells.append(row)
        # x starter
        self.turn = 'x'

    def draw(self, surface):
        """Tegner Board på vinuduet med alle celler og rutenett

        Args:
            surface (pygame.display): vinduet for pygame
        """
        # Setter bakgrunnen BGCOLOR
        surface.fill(BGCOLOR)
        # Tegner cellene ved å traversere listen med lister og 
        # kjører draw() på hver celle
        for row in self.cells:
            for cell in row:
                cell.draw(surface)
        
        # Tegner rutenettet over
        for i in range(1, GRID_SIZE):
            pygame.draw.line(surface, LINE_COLOR, (0, i * CELL_SIZE), (WIDTH, i * CELL_SIZE), 3)
            pygame.draw.line(surface, LINE_COLOR, (i * CELL_SIZE, 0), (i * CELL_SIZE, HEIGHT), 3)

    def handle_click(self, pos):
        """Håndeterer at det trykkes på Board

        Args:
            pos (tuple): posisjonen hvor det trykkes på vinduet med musepekeren
        """
        col = pos[0] // CELL_SIZE
        row = pos[1] // CELL_SIZE

        # Bytter spiller, 
        # "x" -> "o" eller omvendt 
        # dersom et merke blir satt
        if self.cells[row][col].sett_mark(self.turn):
            self.turn = 'o' if self.turn == 'x' else 'x'  



##Oppretter Board som igjen oppretter celler på brettet
board = Board()

# Spill-løkke
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            board.handle_click(event.pos)

    #Tegner brettet, som igjen håndterer tegning av celler
    board.draw(screen)

    #Oppdaterer vinduet
    pygame.display.flip()

pygame.quit()
