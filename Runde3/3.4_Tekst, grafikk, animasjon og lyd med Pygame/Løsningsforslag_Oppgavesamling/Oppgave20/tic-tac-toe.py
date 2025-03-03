import pygame
from pathlib import Path
pyFilePath = Path(__file__).resolve().parent


# Konstanter
WIDTH, HEIGHT = 300, 300
GRID_SIZE = 3
CELL_SIZE = WIDTH // GRID_SIZE
WHITE = (255, 255, 255)
LINE_COLOR = (0, 0, 0)

# Initialiser Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe")

# Last bilder
X_IMG = pygame.image.load(pyFilePath.joinpath("images").joinpath("x.png"))
O_IMG = pygame.image.load(pyFilePath.joinpath("images").joinpath("o.png"))
X_IMG = pygame.transform.scale(X_IMG, (CELL_SIZE, CELL_SIZE))
O_IMG = pygame.transform.scale(O_IMG, (CELL_SIZE, CELL_SIZE))

class Cell:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.mark = None  # 'X' eller 'O'

    def draw(self, surface):
        if self.mark == 'X':
            surface.blit(X_IMG, (self.col * CELL_SIZE, self.row * CELL_SIZE))
        elif self.mark == 'O':
            surface.blit(O_IMG, (self.col * CELL_SIZE, self.row * CELL_SIZE))

    def sett_mark(self, turn):
        """Setter markeringen hvis cellen er tom"""
        if self.mark is None:
            self.mark = turn
            return True
        return False

class Board:
    def __init__(self):
        self.cells = [[Cell(r, c) for c in range(GRID_SIZE)] for r in range(GRID_SIZE)]
        self.turn = 'X'

    def draw(self, surface):
        surface.fill(WHITE)
        for row in self.cells:
            for cell in row:
                cell.draw(surface)
        
        # Tegn rutenett
        for i in range(1, GRID_SIZE):
            pygame.draw.line(surface, LINE_COLOR, (0, i * CELL_SIZE), (WIDTH, i * CELL_SIZE), 3)
            pygame.draw.line(surface, LINE_COLOR, (i * CELL_SIZE, 0), (i * CELL_SIZE, HEIGHT), 3)

    def handle_click(self, pos):
        col = pos[0] // CELL_SIZE
        row = pos[1] // CELL_SIZE
        if self.cells[row][col].sett_mark(self.turn):
            self.turn = 'O' if self.turn == 'X' else 'X'  # Bytt spiller

# Spill-løkke
board = Board()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            board.handle_click(event.pos)

    board.draw(screen)
    pygame.display.flip()

pygame.quit()
