# %%
import random

# scorekeeping
evan_wins = 0
player_wins = 0
ties = 0

# game roles (for randomization of Evan's roles)
roles = ['Phoenix', 'Mage', 'Warrior']

# flag whether game has started
game_started = False

# FUNCTIONS ===========================================================================================================>

def open_game_menu():
    """ 
    Presents the player with the game menu. Player may either start the game,
    display the game rules, or quit by entering 'g', 'r', or 'q', respectively.
    """
    
    print("=== MENU ===")
    menu_selection = ""
    valid_selections = ['g', 'r', 'q']

    while menu_selection not in valid_selections: # keep showing menu if player gives invalid input
        menu_selection = input("Select an option: \n"
                               "- Start game (g) \n"
                               "- Show rules (r) \n"
                               "- Quit (q) \n")
        print()

    # selection logic
    if menu_selection == 'r':
        print_rules()
        open_game_menu()
    elif menu_selection == 'g':
        start_game()
    elif menu_selection == 'q':
        pass
# =========================================================================================

def print_rules():
    """ Prints the rules of the game for the player to read. """
    print("=== RULES === \n"
         "You are faced with a computer opponent: EVAN. Through a series of \n"
          "rounds, you and Evan must try to beat each other by selecting from \n"
          "one of the following roles: Phoenix, Mage, Warrior \n"
          "(hence the name of the game) \n\n"
          
          "Role Dynamics:\n"
          "- Phoenix beats Warrior \n"
          "- Warrior beats Mage \n"
          "- Mage beats Phoenix \n\n"
          
          "Should you and Evan select the same role, the round ends in a tie. \n"
          "Good luck, player! \n\n"
         )
    
# =========================================================================================

def start_game():
    """ Starts the game by prompting the user for how many rounds they would like to play. """
    
    # set game_started flag to True
    global game_started 
    game_started = True

    print("---> GAME START")

    # prompt player
    rounds = input("How many rounds would you like to play?")

    # input validation
    # (if user doesn't enter an integer or enters an integer less than 1)
    while rounds.isdigit() == False or int(rounds) < 1:
        rounds = input("Enter a number greater than 0:")

    rounds = int(rounds) # convert to int
    print()
    
    play_game(rounds)

# =========================================================================================

def play_game(rounds):
    """ 
    Iterates the player through the game based on the number of rounds they elected to play.
    In each round, the player may select a role (Phoenix, Mage, or Warrior) or opt to quit.
    After each round, the current score is displayed.
    """
    global evan_wins, player_wins, ties # access global variables
    
    for i in range(1, rounds+1):
        print('== Round', i, '==')
        player_choice = input("Select your role (Phoenix, Mage, Warrior) \nor enter 'quit' to end the game:\n").lower()

        # input validation
        valid_choices = ['phoenix', 'mage', 'warrior', 'quit']
        while (player_choice not in valid_choices):
            player_choice = input('Enter a valid role: ')

        # quit Game
        if player_choice == 'quit':
            print("GAME END")
            break  # exit for loop

        # continue game
        evan_choice = random.choice(roles)
        print(f'\nEvan chose {evan_choice}!')
    
        # determine round winner
        if player_choice == evan_choice.lower(): # tie
            print('Nothing happened. You both live another day!')
            ties += 1
        elif player_choice == 'phoenix':
            if evan_choice == 'Warrior':
                print('You blew Evan to smithereens with your fiery breath!')
                player_wins += 1
            elif evan_choice == 'Mage':
                print('Evan cast a spell on you!')
                evan_wins += 1
        elif player_choice == 'mage':
            if evan_choice == 'Phoenix':
                print('You cast a spell on Evan!')
                player_wins += 1
            elif evan_choice == 'Warrior':
                print('Evan slayed you with his sword!')
                evan_wins += 1
        elif player_choice == 'warrior':
            if evan_choice == 'Mage':
                print('You slayed Evan with your sword!')
                player_wins += 1
            elif evan_choice == 'Phoenix':
                print('Evan blew you to ashes!')
                evan_wins += 1
    
        # print score
        print(f'Evan: {evan_wins} | You: {player_wins} | Tie: {ties}\n\n')

    # signal end of game after last round
    print("GAME END")
        
# =========================================================================================

def declare_winner():
    """ States whether the player or Evan won the game. If neither, a tie is declared. """
    if evan_wins > player_wins:
        print("Evan wins. Better luck next time!")
    elif player_wins > evan_wins:
        print("You win!")
    else:
        print("It's a tie!")
        
# END OF FUNCTIONS ================================================================================================>

# game execution
print("========================== \n"
      "|      AETHER-TRIAD      | \n" # replace
      "========================== \n"
     )

open_game_menu()

if game_started: # if player quits before even starting the game, no winner is declared
    declare_winner()


