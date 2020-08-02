class HiLo():

    def __init__(self):
        pass


class HiLo:
    def __init__(self):
        self.game = (1)  # put a 1 in so that a passing answer is defined as 1

    def game(self):
        pass

    def Hilo(self):
        self.game  # kept getting error that HiLo didn't exist, so added a definition = no more error.
        pass

    def guess(self, n):
        pass

    def guesses(self):
        self.game.guess(0) == -1  ##here I am attempting to return correct positions if a number is selected
        self.game.guess(1) == 0
        self.game.guess(2) == 1

    def number(self, n, hence=None):  ##I am putting this in so the program knows that a number should be entered
        if (1) != int:
            print("nope")  # I put this in as an attempt to give a "nope" if a number is not entered


##at this point, when I attempt to run, it doesn't return any errors, just Process finished with exit code 0
# the Hangman game

class Hangman():
    def __init__(self, s="Apple"):
        self.word = s
        self.turns = 5
        self.current = len(s) * "_"
    pass
    def Hangman(self):
        self.Hangman()
        pass
    def self(self):
        self.guess(self.letters)  # kept getting error that self wasn't defined, attempted adding definition

    def letter(self):
        self.guess() == [A, a, p, l,e]  # got error for unresolved references to the letters a,p, l, e, a, so attempting to add the letters as a list
        x = letter
        pass
    def guess(self, letter):
        self.word == "Apple"  # putting this here to define what the desired word is.
        self.guess.a == print(
            'A____')  # attempting to tell the system that it should accept either A or a for first letter
        self.guess.A == print('A____')
        self.guess.p == print('_pp__')
        self.guess.l == print('___l_')
        self.guess.e == print('____e')
        self.guess != [A, a, p, l, e] == print(
            'sorry, that is incorrect')  # this intended to provide a statement to the user that the letter they have chosen (anything other than
        pass

    if guess(letter != ([A, l, a, p, e])):
        print(self.turns == (-1))
        pass

    # I can't seem to make this pass.  As is my pattern regarding python, I ended spending hours just
    # making a mess of the whole thing.  It appears I'm much better at breaking things then creating them.
