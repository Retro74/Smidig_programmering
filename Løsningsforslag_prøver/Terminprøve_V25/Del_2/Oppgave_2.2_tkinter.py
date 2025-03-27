import tkinter as tk
import tkinter.ttk as ttk
from tkinter import PhotoImage, messagebox
import random
from pathlib import Path
pyFilePath = Path(__file__).resolve().parent

COLS = 5 # Definerer  kolonner
ROWS = 4 # Definerer  rader

class Card:
    def __init__(self,gameBoard, root, front_image: str, back_image: str, row: int, col: int):
        self.gameBoard = gameBoard
        self.front_image = front_image  # Forsidebilde
        self.phIm_front_image = tk.PhotoImage(file=front_image)
        self.back_image = back_image  # Baksidebilde
        self.phIm_back_image = tk.PhotoImage(file=back_image)
        self.is_flipped = False  # Starter med baksiden opp
        self.is_matched = False  # Om kortet er funnet i et par

        # Opprett en knapp som viser kortet
        self.button = ttk.Button(root, image=self.phIm_back_image, command=self.flip, width=10)
        self.button.grid(row=row, column=col, padx=0, pady=0)

    def flip(self):
        #global click_sequence, previous_card
        if self.gameBoard.click_sequence == 0:
            if not self.is_flipped and not self.is_matched:
                self.is_flipped = True
                self.gameBoard.click_sequence+=1
                self.gameBoard.previous_card = self
        elif self.gameBoard.click_sequence ==1:
            if not self.is_flipped and not self.is_matched:
                self.is_flipped = True
                if self.front_image == self.gameBoard.previous_card.front_image:
                    self.is_matched = True
                    self.gameBoard.previous_card.is_matched = True
                    self.gameBoard.click_sequence = 0
                else:
                    self.gameBoard.click_sequence+=1
        elif self.gameBoard.click_sequence ==2:
            if self.is_flipped and not self.is_matched:
                self.is_flipped = False
                self.gameBoard.click_sequence+=1
        elif self.gameBoard.click_sequence ==3:
            if self.is_flipped and not self.is_matched:
                self.is_flipped = False
                self.gameBoard.click_sequence=0
        self.update_image()
    
    def update_image(self):
        if self.is_flipped or self.is_matched:
            self.button.config(image=self.phIm_front_image)
        else:
            self.button.config(image=self.phIm_back_image)

class MemoryGame:
    def __init__(self, root, pyFilePath):
        """Lager objektet MemoyGame

        Args:
            root (tk.Tk): tkinter-vinduet spillet skal plasseres i
            pyFilePath (str): stien til hvor dette spillet ligger
        """
        self.root = root
        self.root.title("Memory-spill")
        self.cards = []
        self.load_cards(pyFilePath)
        self.previous_card = None
        self.click_sequence = 0

    def load_cards(self, pyFilePath):
        """Laster inn kortene i spillet, stokker dem og legger dem på spillbrettet

        Args:
            pyFilePath (str): hvor spillet ligger
        """
        ##Bildene legges inn
        images =[]
        for i in range(1,int(COLS*ROWS/2+1)):
            images.append(f"{pyFilePath.joinpath('images').joinpath(str(i))}.gif")
            images.append(f"{pyFilePath.joinpath('images').joinpath(str(i))}.gif")
        random.shuffle(images)  # Stokk kortene
        back_image =pyFilePath.joinpath('images').joinpath("back.gif")
        # Opprett kortene i et rutenett og legg dem på spillbrettet/vinduet
        for row in range(COLS):
            for col in range(ROWS):
                front_image = images.pop()
                card = Card(self, self.root, front_image, back_image , col, row)
                self.cards.append(card)
root = tk.Tk()
game = MemoryGame(root, pyFilePath)

root.mainloop()
