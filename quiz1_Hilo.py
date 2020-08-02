class HiLo:
    def __init__(self):
        self.game = (1) #put a 1 in so that a passing answer is defined as 1

    def game(self):
        pass

    def Hilo(self):
        self.game(1)  # kept getting error that HiLo didn't exist, so added a definition = no more error.
        pass

    def guess(self,n):
        pass

    def guesses(self):
        self.game.guess(0) == -1  ##here I am attempting to return correct positions if a number is selected
        self.game.guess(1) == 0
        self.game.guess(2) == 1

    def number(self, n, hence=None):  ##I am putting this in so the program knows that a number should be entered
        if (1) != int:
            print("nope")  #I put this in as an attempt to give a "nope" if a number is not entered

##at this point, when I attempt to run, it doesn't return any errors, just Process finished with exit code 0

    # the Hangman game

#class Hangman():
#    def __init__(self, s="testing"):
#        self.word = s
#        self.turns = 0
#        self.current = len(s) * "_"

#    def guess(self, letter):
#    pass