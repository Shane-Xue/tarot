"""
Tarot Card Class and The Card Deck-- with side
There is also an exception class to indicate a corrupted directory system
"""
import _RandGen

class DirCorError(Exception):
    def __init__(self,str):
        super(str)

class Card():
    """
    A Class for putting in the cards
    """
    def __init__(self,num,side=-1):
        """
        num: The representitive number in the deck of cards
        side: 0--upright 1--reversed -1--undetermined
        """
        self.num=num
        self.side=side

    def _GetDef(self):
        """
        Function to get definition of card
        Client should not be able to access this function
        This function should only be called once during the entire lifetime of the card,
        --that is, when the client wants to print the definition of the card.
        This function will NOT do exeption handling of any kind,
        --so in case the function cannot find the file it will kick an exeption back to the
        --caller.
        The definition is stored in a list so it is easy to read.
        It also deals with concerns of safety, i.e., prevent the user from 'accidentally'
        --changing the contents of the definition.
        """
        file=open(f'def/{self.num}.txt','r')
        self.Definition=[]
        for line in file:
            self.Definition.append(line)
        file.close()

    def Def(self):
        """
        Method to give the user the definition aquired in _GetDef
        """
        try:
            self._GetDef()
        except FileNotFoundError as e:
            raise DirCorError("The definition directory is corrupted!")
        return self.Definition

    def __str__(self):
        """
        In case there is such a majic method!
        """
        return str(self.Definition)

    def __call__(self):
        return str(self)

class _Deck():
    """
    Class to represent a card deck.
    It is designed to be private because I actually want it to be a singleton
    --but don't know how to do the job in Python().
    It also can be indexed so the client will not be able to easily access the
    --list inside the deck. The list inside will be set private.
    """
