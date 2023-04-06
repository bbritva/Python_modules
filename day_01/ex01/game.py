class GotCharacter():
    def __init__(self, first_name=None, is_alive=True):
        self.first_name = first_name
        self.is_alive = is_alive


class Martell(GotCharacter):
    """A class representing the Martell family.\nWhen it comes to war I fight for Dorne, when it comes to love... I don't choose sides =)"""

    def __init__(self, first_name=None, is_alive=True):
        super().__init__(first_name=first_name, is_alive=is_alive)
        self.family_name = "Martell"
        self.house_words = "Unbowed, Unbent, Unbroken"

    def print_house_words(self):
        print(self.house_words)

    def die(self):
        self.is_alive = False


class Tyrell(GotCharacter):
    """A class representing the Tyrell family. A golden rose, growing strong? Oh, yes, that strikes fear in the heart!"""

    def __init__(self, first_name=None, is_alive=True):
        super().__init__(first_name=first_name, is_alive=is_alive)
        self.family_name = "Tyrell"
        self.house_words = "Growing Strong"

    def print_house_words(self):
        print(self.house_words)

    def die(self):
        self.is_alive = False


if __name__ == '__main__':
    print("There are two child classes Martell and Tyrell.\n")

    print("Let's create Oberyn")
    oberyn = Martell("Oberyn")
    
    print("Here is object struct:\n", oberyn.__dict__)
    print("Here is Martell's class desc:\n", oberyn.__doc__)
    print("Here is Martell's house words: ", end="")
    oberyn.print_house_words()
    print(f"\nHere is Oberyn's live status: {oberyn.is_alive}")
    oberyn.die()
    print(f"But after the fight with the mountain Oberyn's live status became: {oberyn.is_alive}\n")
    
    
    print("Let's create Olenna")
    olenna = Tyrell("Olenna")
    
    print("Here is object struct:\n", olenna.__dict__)
    print("Here is Tyrell's class desc:\n", olenna.__doc__)
    print("Here is Tyrell's house words", end="")
    olenna.print_house_words()
    print(f"\nHere is Olenna's live status: {olenna.is_alive}")
    olenna.die()
    print(f"But after the date with Jaime Olenna's live status became: {olenna.is_alive}")
