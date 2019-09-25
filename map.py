import random

class Map:

    def __init__(self, filename):
        self.filename = filename
        self.structure = []

    def load_maze(self):
        # loading a maze structure from the txt file
        with open(self.filename, "r") as f:
            for ligne in f:
                line_level = list(ligne)
                line_level = line_level[:-1] # remove last character from line_level list
                self.structure.append(line_level)

    def load_hero(self):
        # define the initial position of MacGyver
        for n_ligne, ligne in enumerate(self.structure):
            for n_col, col in enumerate(ligne):
                if col == "d":
                    self.start = (n_ligne, n_col)
                    print(self.start)

    def load_guardian(self):
        # define the initial position of guardian
        for n_ligne, ligne in enumerate(self.structure):
            for n_col, col in enumerate(ligne):
                if col == "a":
                    self.finish = (n_ligne, n_col)
                    print(self.finish)

    def load_items(self):
        self.items_poss = []
        for n_ligne, ligne in enumerate(self.structure):
            for n_col, col in enumerate(ligne):
                if col == "0":
                    position = (n_ligne, n_col)
                    self.items_poss.append(position)
        self.items = random.sample(self.items_poss, 3)
        print(self.items)

    


def main():
    map = Map("level.txt")
    map.load_maze()
    print(map.structure)
    map.load_hero()
    map.load_guardian()
    map.load_items()
    

if __name__ == "__main__":
    main()