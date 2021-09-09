class Phrase:
    def __init__(self, phrase):
        self.pass_phrase: str = phrase
        self.pass_phrase_list = list(self.pass_phrase)
        self.display = ["_" if char.isalpha() else " " for char in self.pass_phrase]
