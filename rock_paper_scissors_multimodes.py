import random
import time
import json
import logging
import getpass
import re
from datetime import datetime
from typing import Union, Optional, Dict, Tuple, List, Any
import os


# Constants
CHOICES = {
    "rock": "🪨",
    "paper": "📄",
    "scissors": "✂️"
}
WINNING_COMBOS = {"rock": "scissors", "paper": "rock", "scissors": "paper"}
GAME_STATISTICS = "game_stats.json"
MAX_ENTRIES = 3


# Set up logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


# Utilities class
class Utilities:
    @staticmethod
    def get_valid_input(prompt: str, is_numeric: bool = False, min_value: Optional[int] = None, max_value: Optional[int] = None) -> Union[int, str]:
        """
        Generic function to validate user input.
        :param prompt: Input prompt
        :param is_numeric: Whether input should be numeric
        :param min_value: Minimum valid value for the input
        :param max_value: Maximum valid value for the input
        :return : Valid user input
        """
        while True:
            try:
                user_input = input(prompt).strip()
                if is_numeric:
                    user_input = int(user_input)
                    if min_value is not None and user_input < min_value:
                        print(f"Please enter a value greater than or equal to {min_value}.")
                    elif max_value is not None and user_input > max_value:
                        print(f"Please enter a value less than or equal to {max_value}.")
                    else:
                        return user_input
                else:
                    if user_input:
                        return user_input
                    else:
                        print("Input cannot be empty. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
    

    @staticmethod
    def get_valid_choice(player_name: str, is_hidden: Optional[bool] = False, time_limit: Optional[int] = None) -> str:
        """Get a valid choice (with optional timer and hidden input)."""
        options = ", ".join(f"{value} {key.capitalize()}" for key, value in CHOICES.items())
        prompt = f"{player_name}, choose {options}: "
        while True:
            if is_hidden:
                choice = getpass.getpass(prompt).strip().lower()
            else:
                choice = input(prompt).strip().lower()
            
            if choice in CHOICES.keys():
                return choice
            print("Invalid choice. Please try again.")


    @staticmethod
    def get_valid_name(prompt: str) -> str:
        """Validate the player's name."""
        while True:
            name = input(prompt).strip()
            if not name:
                print("Name cannot be empty. Please try again.")
            elif not re.match("^[a-zA-Z ]+$", name):
                print("Name can only contain letters and spaces. Please try again.")
            elif len(name) > 20:
                print("Name cannot be exceed 20 characters. Please try again.")
            else:
                return name


    @staticmethod
    def determine_winner(player_choice: str, opponent_choice: str, player_name="Player") -> str:
        """Determine the winner of a round."""
        if player_choice == opponent_choice:
            print(f"It's a tie! Both chose {player_choice.capitalize()} {CHOICES[player_choice]}")
            return "tie"
        elif WINNING_COMBOS[player_choice] == opponent_choice:
            print(f"{player_name} wins! {player_choice.capitalize()} {CHOICES[player_choice]} beats {opponent_choice.capitalize()} {CHOICES[opponent_choice]}")
            return "win"
        else:
            print(f"{player_name} loses! {opponent_choice.capitalize()} {CHOICES[opponent_choice]} beats {player_choice.capitalize()} {CHOICES[player_choice]}")
            return "lose"
    

    @staticmethod
    def clear_screen():
        """Clears the terminal screen for better UI presentation."""
        os.system('cls' if os.name == 'nt' else 'clear')


class Stats:
    @staticmethod
    def load_statistics() -> List[Dict]:
        """Load statistics from a JSON file."""
        try:
            with open(GAME_STATISTICS, 'r') as file:
                data = json.load(file)
                #Ensure the data is a list
                if isinstance(data, list):
                    return data
                else:
                    logging.warning("Statistics file format is invalid. Resetting to an empty list.")
                    return []
        except FileNotFoundError:
            logging.warning("Statistics file not found. Initializing as an empty list.")
            return []
        except json.JSONDecodeError:
            logging.debug("Error decoding the statistics file. Resetting to an empty list.")
            return []
        except Exception as e:
            logging.critical(f"Unexpected error: {e}")
            raise
    

    @staticmethod
    def save_stats_to_file(stats: Dict[str, Any]) -> None:
        """Save the new game stats to the JSON file with a limit."""
        try:
            all_stats = Stats.load_statistics() # Load existing statistics
        except Exception as e:
            logging.error(f"Failed to load statistics: {e}")
            all_stats = []

        # Append the current game stats
        all_stats.append(stats)

        # Enforce the MAX_ENTRIES limit
        if len(all_stats) > MAX_ENTRIES:
            all_stats = all_stats[-MAX_ENTRIES:] # Keep only the latest MAX_ENTRIES

        try:
            with open(GAME_STATISTICS, "w") as file:
                json.dump(all_stats, file, indent=4)
            print("Statistics successfully saved.")
        except IOError as e:
            logging.error(f"Failed to save statistics: {e}")
            raise


    @staticmethod
    def display_stats(stats: Dict[str, Any]) -> None:
        print("\nGame Summary:")
        print("-" * 40)
        for key, value in stats.items():
            print(f"{key}: {value}")
        print("-" * 40)


class PlayGame:
    def get_players(self, mode: str) -> tuple[str, str]:
        """Get players names based on the mode."""
        if mode == "Single Player":
            return Utilities.get_valid_name("Enter your name: "), "Computer"
        elif mode == "Multiplayer":
            player1 = Utilities.get_valid_name("Enter name of Player 1: ")
            player2 = Utilities.get_valid_name("Enter name of Player 2: ")
            return player1, player2
        elif mode == "Timed Mode":
            return Utilities.get_valid_name("Enter your name: "), "Computer"
        else:
            raise ValueError(f"Unknown mode: {mode}")
    

    def play_round(self, player1: str, player2: str, is_hidden: bool = False, time_limit: Optional[int] = None) -> str:
        """Play a single round and return the result."""
        if player2 == "Computer":
            player1_choice = Utilities.get_valid_choice(player1, is_hidden, time_limit)
            player2_choice = random.choice(list(CHOICES.keys()))
        else:
            player1_choice = Utilities.get_valid_choice(f"(Hidden): {player1}", is_hidden)
            player2_choice = Utilities.get_valid_choice(f"(Hidden): {player2}", is_hidden)
        
        print(f"{player1} chose: {player1_choice.capitalize()} \n{player2} chose: {player2_choice.capitalize()}")

        return Utilities.determine_winner(player1_choice, player2_choice, player1)
    

    def play_game(self, player1: str, player2: str, rounds: Optional[int] = None, time_limit: Optional[int] = None, is_hidden: bool = False) -> Tuple[int, int, int, int]:
        """
        Main game loop for both timed and untimed modes.
        :param player1: Name of player 1 (str)
        :param player2: Name of player 2 (str)
        :param rounds: Total number of rounds to play (int) (None for timed mode).
        :param time_limit: Time limit for the game in seconds (float) (None for untimed mode).
        :return: Tuple containing player 1 wins, player 2 wins, draws, and rounds played.
        """
        p1_wins, p2_wins, draws = 0, 0, 0
        rounds_played = 0
        start_time = time.monotonic() if time_limit else None

        # Loop based on rounds or time limit
        while True:
            # Check if the time limit has been reached
            if time_limit and time.monotonic() - start_time >= time_limit:
                print("Time's up!")
                break

            if time_limit:
                elapsed_time = time.monotonic() - start_time
                remaining_time = max(0, time_limit - elapsed_time)
                print(f"\nTime remaining: {remaining_time: .2f} seconds")
            
            # Check if a specific number of rounds has been completed (only for untimed mode)
            if rounds and rounds_played >= rounds:
                break

            # Play one round
            print(f"\nRound {rounds_played + 1}:")
            result = self.play_round(player1, player2, is_hidden)

            # Update scores based on the result
            if result == "win":
                p1_wins += 1
            elif result == "lose":
                p2_wins += 1
            else:
                draws += 1

            # Increment the rounds played counter
            rounds_played += 1
        
        return p1_wins, p2_wins, draws, rounds_played
    

    def update_statistics(self, stats: Dict[str, int | str], mode: str, player1: str, player2: str, p1_wins: int, p2_wins: int, draws: int, rounds: int, time_limit: Optional[int] = None) -> None:
        """Update the game statistics."""
        stats.update({
            "Mode": mode,
            "Player 1": player1,
            "Player 2": player2,
            "Player 1 Wins": p1_wins,
            "Player 2 Wins": p2_wins,
            "Draws": draws,
            "Total Rounds": rounds,
            "Time Limit": time_limit,
            "Date": datetime.now().strftime("%Y-%m-%d"),
        })
        Stats.display_stats(stats)
        Stats.save_stats_to_file(stats)


class GameMode:
    def __init__(self):
        self.play_game = PlayGame()  # Create an instance of PlayGame
    

    def single_player_mode(self, rounds: int, stats: Dict[str, int | str]) -> None:
        """Handle single player mode."""
        player1, player2 = self.play_game.get_players("Single Player")

        p1_wins, p2_wins, draws, rounds = self.play_game.play_game(player1, player2, rounds)

        overall_winner = self.determine_overall_winner(p1_wins, p2_wins, rounds, player1, player2)
        self.play_game.update_statistics(stats, "Single Player", player1, player2, p1_wins, p2_wins, draws, rounds)
    

    def multiplayer_mode(self, rounds: int, stats: Dict[str, int | str]) -> None:
        """Handle multiplayer mode."""
        player1, player2 = self.play_game.get_players("Multiplayer")

        # Enable hidden input for multiplayer
        is_hidden = True
        print("\nInput will be hidden for multiplayer mode.")
        p1_wins, p2_wins, draws, rounds = self.play_game.play_game(player1, player2, rounds, is_hidden=is_hidden)

        # Determine overall winner
        overall_winner = self.determine_overall_winner(p1_wins, p2_wins, rounds, player1, player2)
        self.play_game.update_statistics(stats, "Multiplayer", player1, player2, p1_wins, p2_wins, draws, rounds)


    def timed_mode(self, stats: Dict[str, int | str]) -> None:
        """Handle the timed mode gameplay."""
        player1, player2 = self.play_game.get_players("Timed Mode")
        time_limit = Utilities.get_valid_input(
            "Enter the time limit in seconds (e.g., 15, 30, 60): ",
            is_numeric=True,
            min_value=0,
            max_value=120,
        )

        # Start the game
        print(f"\n{player1}, your time starts now! You have {time_limit} secons to play.")
        p1_wins, p2_wins, draws, rounds_played = self.play_game.play_game(player1, player2, time_limit=time_limit)

        # Display results
        print(f"\nGame Over! You played {rounds_played} rounds in {time_limit} seconds.")

        # Determine overall winner
        overall_winner = self.determine_overall_winner(p1_wins, p2_wins, rounds_played, player1, player2)

        # Update statistics
        self.play_game.update_statistics(stats, "Timed", player1, player2, p1_wins, p2_wins, draws, rounds_played, time_limit)


    def determine_overall_winner(self, p1_wins: int, p2_wins: int, rounds: int, player1: str, player2: str) -> str:
        """
        Determine and announce the overall winner.
        
        Args:
            p1_wins (int): Number of wins by Player 1.
            p2_wins (int): Number of wins by Player 2.
            rounds (int): Total number of rounds played.
            player1 (str): Name of Player 1.
            player2 (str): name of Player 2.

        Returns:
            str: The overall winner ("Player 1", "Player 2", or "No one").
        """
        if p1_wins > p2_wins:
            overall_winner = player1
            print(f"\n{player1} is the overall winner with {p1_wins} wins out of {rounds} rounds!")
        elif p2_wins > p1_wins:
            overall_winner = player2
            print(f"\n{player2} is the overall winner with {p2_wins} wins out of {rounds} rounds!")
        else:
            overall_winner = "No one"
            print(f"\nIt's a tie! Both {player1} and {player2} have equal wins.")
        return overall_winner


    @staticmethod
    def view_statistics() -> None:
        try:
            # Load statistics from file
            with open(GAME_STATISTICS, 'r') as file:
                stats = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            print("\nNo game statistics available. Play some games to generate statistics!")
            return
        
        # Display statistics if available
        print("\nGame Statistics:")
        print("-" * 40)
        if not stats:
            print("No statistics found.")
        else:
            for stat in stats:
                for key, value in stat.items():
                    print(f"{key}: {value}")
                print("-" * 40)


def main():
    """Main function to run the game."""
    stats = {
        "Mode": None,
        "Player 1": None,
        "Player 2": None,
        "Player 1 Wins": 0,
        "Player 2 Wins": 0,
        "Total Rounds": 0,
        "Draws": 0,
        "Time Limit": None, # For timed mode
        "Date": datetime.now().strftime("%Y-%m-%d"),
    }
    game_mode = GameMode()  # Create an instance of GameMode

    while True:
        print("\nWelcome to Rock 🪨, Paper 📄 and Scissors ✂️!")
        print("1. Single Player Mode")
        print("2. Multiplayer Mode")
        print("3. Timed Mode")
        print("4. View Statistics")
        print("5. Exit")

        user_choice = Utilities.get_valid_input("Choose an option (1-5): ", is_numeric=True, min_value=1, max_value=5)

        if user_choice == 1:
            rounds = Utilities.get_valid_input("Enter number of rounds to play: ", is_numeric=True, min_value=1)
            game_mode.single_player_mode(rounds, stats)  # Call via instance
        elif user_choice == 2:
            rounds = Utilities.get_valid_input("Enter number of rounds to play: ", is_numeric=True, min_value=1)
            game_mode.multiplayer_mode(rounds, stats)  # Call via instance
        elif user_choice == 3:
            game_mode.timed_mode(stats)  # Call via instance
        elif user_choice == 4:
            GameMode.view_statistics()
        elif user_choice == 5:
            Utilities.clear_screen()
            print("Thanks for playing. Goodbye!")
            break


if __name__ == "__main__":
    main() 
