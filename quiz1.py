#class HiLo():
from re import A


def __init__(self):
       pass

# the Hangman game

class Hangman():
    def __init__(self, s="Apple"):
        self.word = s
        self.turns = 5
        self.current = len(s) * "_"
    def self(self):
        self.guess(self.letters) #kept getting error that self wasn't defined, attempted adding definition
    def letter(self):
        self.letters == [A,a,p,l,e] #got error for unresolved references to the letters a,p, l, e, a, so attempting to add the letters as a list
    def guess(self, letter):
        self.word == "Apple"  # putting this here to define what the desired word is.
        self.guess.a == print('A____')  #attempting to tell the system that it should accept either A or a for first letter
        self.guess.A == print('A____')
        self.guess.p == print('_pp__')
        self.guess.l == print('___l_')
        self.guess.e == print('____e')
        self.guess !=[A,a,p,l,e] == print('sorry, that is incorrect') #this intended to provide a statement to the user that the letter they have chosen (anything other than
        pass
    if guess(self.letter) != [A,a,p,l,e]:
        print(self.turns == (-1))
        pass

    # I can't seem to make this pass.  As is my pattern regarding python, I ended spending hours just
    # making a mess of the whole thing.  It appears I'm much better at breaking things then creating them.