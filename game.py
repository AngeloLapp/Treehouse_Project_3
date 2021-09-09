import random
from phrase import Phrase


class Game:
    def __init__(self):
        self.missed = 0
        self.phrases = [Phrase(a) for a in ['Mario Bros', 'Ice Climbers', 'Kid Icarus', 'Legend of Zelda', 'Ducktales']]
        self.active_phrase = random.choice(self.phrases)
        self.guesses = list()

    def start(self) -> None:
        while True:
            print('- - - - - Welcome to Phrase Hunter! - - - - -',
                  '- - - - - Guess the phrase to win! - - - - -',
                  '- - - - - - - You get 5 lives! - - - - - - -', sep="\n")
            self.play_game()
            print('\n', self.game_over(win=self.play_game()), '\n')
            print('The phrase was:', self.active_phrase.pass_phrase)
            if not self.ask_to_play_again():
                break

    def play_game(self) -> bool:
        while self.active_phrase.display != self.active_phrase.pass_phrase_list:
            if self.missed == 5:
                return False
            print(" ".join(self.active_phrase.display))
            print(f"You have {5 - self.missed} turns remaining.")
            guess = None
            while guess is None:
                guess = input("Guess any individual letter in the phrase: ")
                if not (guess.isalpha() and len(guess) == 1):
                    guess = None
            # I'm sure there is a cleaner way to check upper and lower but this is the best I can do.
            if guess.lower() in self.active_phrase.pass_phrase_list \
                    or guess.upper() in self.active_phrase.pass_phrase_list:
                # I struggled a little with handling repetetive guesses. This worked but it took a bunch of tries.
                if guess in self.active_phrase.display:
                    print('You have already guessed that letter...')
                    self.missed += 1
                else:
                    self.active_phrase.display = [self.active_phrase.pass_phrase_list[a]
                                                  if self.active_phrase.pass_phrase_list[a].lower() == guess.lower()
                                                  else self.active_phrase.display[a]
                                                  for a in range(0, len(self.active_phrase.pass_phrase_list))]
            else:
                self.missed += 1
        return True

    def game_over(self, win: bool) -> str:
        return {False: 'Game over! You lose!', True: 'You won! Game over!'}[win]

    def ask_to_play_again(self) -> bool:
        answer = input('\nPress "Y" to play again or any other key to quit: ')
        if answer.lower() == 'y':
            self.missed = 0
            self.phrases = [Phrase(a) for a in
                            ['Mario Bros', 'Ice Climbers', 'Kid Icarus', 'Legend of Zelda', 'Ducktales']]
            self.active_phrase = random.choice(self.phrases)
            self.guesses = list()
            return True
        else:
            return False

