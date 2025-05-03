# crazy8.py

import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Card:
    def __init__(self, suit, value):
        if value < 1 or value > 13:
            raise ValueError("Card value must be between 1 and 13.")
        self.suit = suit
        self.value = value

    def __str__(self):
        if self.value == 1:
            return "Ace of " + self.suit
        elif self.value == 11:
            return "Jack of " + self.suit
        elif self.value == 12:
            return "Queen of " + self.suit
        elif self.value == 13:
            return "King of " + self.suit
        else:
            return f"{self.value} of {self.suit}"

class Deck:
    def __init__(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        self.cards = [Card(suit, value) for suit in suits for value in range(1, 14)]  # Generates cards 1-13
        random.shuffle(self.cards)  # Shuffle the deck

    def draw(self):
        return self.cards.pop() if self.cards else None

class CrazyEightsGame:
    def __init__(self, num_players):
        self.deck = Deck()
        self.players = [[] for _ in range(num_players)]
        self.center_pile = []
        self.turn_count = 0  # Initialize turn count
        self.start_game()

    def start_game(self):
        # Deal 5 cards to each player
        for _ in range(5):
            for player in self.players:
                player.append(self.deck.draw())
        
        # Flip the starter card
        self.flip_starter_card()  # This method will now also print the center card
        
        # Start the game loop
        self.game_loop()

    def flip_starter_card(self):
        starter_card = self.deck.draw()
        if starter_card is None:  # Check if the starter card is None
            print("No more cards in the deck to draw a starter card.")
            return  # Exit the method or handle the situation as needed

        # Check if the starter card is an Ace (1), 2, or 8
        while starter_card.value in [1, 2, 8]:
            print(f"Starter card {starter_card} is not valid. Drawing a new card.")
            self.center_pile.append(starter_card)  # Optionally keep track of the invalid card
            starter_card = self.deck.draw()  # Draw a new starter card
            if starter_card is None:  # Check again after drawing a new card
                print("No more cards in the deck to draw a new starter card.")
                return  # Exit the method or handle the situation as needed

        self.center_pile.append(starter_card)  # Add the valid starter card to the center pile
        print(f"Starter card is: {starter_card}")  # Print the valid starter card

    def calculate_scores(self):
        # Logic for scoring
        scores = {}
        for player_index, player_hand in enumerate(self.players):
            score = 0
            for card in player_hand:
                if card.value in range(2, 10):  # Cards 2 through 9
                    score += card.value
                elif card.value == 14:  # Ace
                    score += 1
                elif card.value in range(10, 13):  # Cards 10 through King
                    score += 10
                elif card.value == 8:  # 8s
                    score += 50
            scores[player_index + 1] = score  # Store the score under the player's number

        # Determine the winner
        winner = min(scores, key=scores.get)
        print(f"Player {winner} wins with a score of {scores[winner]}!")

    def game_loop(self):
        game_over = False  # Initialize game_over variable

        while not game_over:  # Continue looping until game_over is True
            for player_index in range(len(self.players)):
                if not self.players[player_index]:  # Check if the player has no cards
                    print(f"Player {player_index + 1} wins!")
                    self.calculate_scores()
                    game_over = True  # Set game_over to True to end the game
                    break  # Exit the for loop

                self.play_turn(player_index)  # Call the player's turn

    def play_turn(self, player_index):
        player_hand = self.players[player_index]
        print(f"Player {player_index + 1}'s turn.")
        
        # Print the current center card at the start of the turn
        if self.center_pile:  # Check if there are cards in the center pile
            current_center_card = self.center_pile[-1]  # Get the last card played
            print(f"Current center card: {current_center_card}")  # Print only once at the start of the turn
        
        counted_cards = False  # Initialize counted_cards variable

        if player_hand:  
            # Display the player's hand using the __str__ method of Card
            print("Your hand:")
            for card in player_hand:
                print(card)  # Show each card using its string representation

            # Prompt the player to choose a card to play or to draw
            while True:
                card_input = input("Choose a card to play (format: 'value of suit', e.g., '2 of Hearts') or type 'draw' to draw a card: ")
                # Normalize input to lowercase
                card_input = card_input.lower()

                # Split the input to check for a number at the end
                parts = card_input.split()
                if parts and parts[-1].isdigit():  # Check if the last part is a number
                    counted_cards = True  # Set counted_cards to True
                    card_input = ' '.join(parts[:-1])  # Remove the number from the input
                else:
                    counted_cards = False  # Set counted_cards to False

                if card_input == "draw":
                    # Player chooses to draw a card
                    drawn_card = self.deck.draw()  # Draw a card
                    if drawn_card:
                        player_hand.append(drawn_card)
                        print(f"You draw: {drawn_card}")  # Only show the current player what they drew
                    break  # End the turn after drawing a card

                elif self.turn_count > 1 and card_input == "ask":
                    # Check the previous player's card count
                    previous_player_index = (player_index - 1) % len(self.players)
                    if not counted_cards and len(self.players[previous_player_index]) < 4:
                        print(f"Player {previous_player_index + 1} has fewer than 4 cards and must draw 1 card.")
                        drawn_card = self.deck.draw()
                        if drawn_card:
                            self.players[previous_player_index].append(drawn_card)
                            # Do not print what the previous player draws
                    else:
                        print(f"Player {previous_player_index + 1} has 4 or more cards.")
                    continue  # Re-prompt the current player to play a card

                # Check if the input matches any card in the player's hand
                card_found = False  # Flag to check if the card is found
                for card in player_hand:
                    # Create the string representation of the card in the format "value of suit"
                    card_representation = f"{card.value} of {card.suit}".lower()
                    if card_input == card_representation:  # Compare with the string representation
                        print(f"Player {player_index + 1} plays: {card}")
                        self.center_pile.append(card)  # Add the card to the center pile
                        player_hand.remove(card)  # Remove the card from the player's hand
                        card_found = True  # Set flag to True if card is found
                        
                        # Check if the played card is a 2
                        if card.value == 2:
                            next_player_index = (player_index + 1) % len(self.players)  # Determine the next player
                            next_player_hand = self.players[next_player_index]
                            
                            # Check if the next player has an Ace
                            has_ace = any(c.value == 1 for c in next_player_hand)  # Check for an Ace in the next player's hand
                            if has_ace:
                                print(f"Player {next_player_index + 1} has an Ace and can block the effect of the 2.")
                            else:
                                # Next player must draw 2 cards
                                print(f"Player {next_player_index + 1} must draw 2 cards.")
                                for _ in range(2):
                                    drawn_card = self.deck.draw()
                                    if drawn_card:
                                        next_player_hand.append(drawn_card)
                                        # Do not print what the next player draws
                                # End the turn after the next player draws cards
                                return  # Exit the method to end the current player's turn

                        # Allow any 8 to be played regardless of the center card
                        if card.value == 8:
                            new_suit = input("You played an 8! Choose a new suit (Hearts, Diamonds, Clubs, Spades): ").capitalize()
                            while new_suit not in ['Hearts', 'Diamonds', 'Clubs', 'Spades']:
                                new_suit = input("Invalid suit. Please choose a valid suit (Hearts, Diamonds, Clubs, Spades): ").capitalize()
                            # Update the center card's suit
                            current_center_card.suit = new_suit
                            print(f"The suit has been changed to: {new_suit}")
                        break  # Exit the loop after a valid play
                
                if not card_found:
                    print("You do not have that card in your hand. Please choose a valid card or type 'draw'.")
                    continue  # Prompt again if the card is not found

                break  # Exit the while loop after a valid play
        
        else:
            print(f"Player {player_index + 1} has no cards to play.")
        
        # Example logic for drawing a card (if the player cannot play)
        if not player_hand:  # If the player has no cards left
            print(f"Player {player_index + 1} cannot play and draws a card.")
            drawn_card = self.deck.draw()
            if drawn_card:
                player_hand.append(drawn_card)
                print(f"You draw: {drawn_card}")  # Only show the current player what they drew

        # Increment the turn count after the player's turn
        self.turn_count += 1

        # Clear the screen at the end of the turn
        clear_screen()

# Example of starting a game with 4 players
if __name__ == "__main__":
    num_players = int(input("How many players: "))
    if num_players <= 1:
        exit("Not enough Players")
    else:    
        game = CrazyEightsGame(num_players)
        game.start_game()
