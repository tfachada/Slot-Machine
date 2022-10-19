from random import choices    # for the slot machine roll

### CLASSES ###
# Slot machine, with symbols and corresponding probabilities and payoff multipliers
# Player, with credits and methods to bet and win them

class Machine:
  symbols = ('A', '★', 'Σ', '∫', '🄯', 'ゴ', 'ඞ')
  probabilities = (50, 40, 30, 20, 10, 5, 1)
  payoffs = {symbols[0]: 5, symbols[1]: 10, symbols[2]: 20, symbols[3]: 70, symbols[4]: 200, symbols[5]: 1000, symbols[6]: 100000}

  def roll(self):
    return choices(self.symbols, weights=self.probabilities, k=3)     # generates list of 3 random symbols with random.choices()

class Player:
  def __init__(self, credits):
    self.credits = credits

  def bet(self, current_bet):
    self.credits -= current_bet
  
  def win(self, machine, symbol, current_bet):
    self.credits += machine.payoffs[symbol] * current_bet


# Game: initial interface. Player sets a positive integer number of credits.

print("\n\t\t\t\tSLOT MACHINE\n")

while True:
  try:
    initial_credits = int(input("How much have you got?\n"))
    if initial_credits <= 0:
      print("Please enter a positive number\n")
    else:
      break
  except ValueError:
    print("Please input an integer\n")

print("\n--------------------\n")


# After the initial credits are defined, the game itself can start

### GLOBAL VARIABLES FOR USE IN THE GAME
# Init machine and player objects
machine = Machine()
player = Player(initial_credits)

# Y/N flag for the main routine of the game
keep_playing = ""


### MAIN ROUTINE
while player.credits > 0 and keep_playing != "N":

  # reset flags for new iteration
  invalid_bet = True
  keep_playing = ""
  
  # bet is only valid if it's a positive integer and the player has the money
  while invalid_bet:
    try:
      current_bet = int(input("Place your bet: "))
      if current_bet <= 0:
        print("Please enter a positive number\n")
      elif current_bet > player.credits:
        print("You don't have that much\n")
      else:
        invalid_bet = False
    except ValueError:
      print("Please input an integer\n")
  
  # place bet and get combination
  player.bet(current_bet)
  combination = machine.roll()

  # then print it
  print("\n")
  print("-------------")
  print("| " + combination[0] + " | " + combination[1] + " | " + combination[2] + " |")
  print("-------------")
  print("\n")

  # and win if there's something to win
  if combination[0] == combination[1] == combination[2]:
    player.win(machine, combination[0], current_bet)
  
  print("Current credits: " + str(player.credits) + "\n")

  # if the player can still play, ask if they want to, and set the keep_playing flag
  if player.credits > 0:
    while(keep_playing != "Y" and keep_playing != "N"):
      keep_playing = input("Keep playing? (Y/N): ").upper()


if player.credits == 0:
  print("You're broke. Bye!\n")
else:
  print("\n")
  print("Started with:\t" + str(initial_credits))
  print("Ended with:\t" + str(player.credits))
  print("\n")
