import csv
import sys
import time

# Open CSV file of president info for reading
file = open("presidents.csv", "r")
csv_reader = csv.reader(file)

# Strip Header Line
next(csv_reader)

# List of only president names
potus_names = []

hard_mode = 2

play_again = 2

# Welcome message
hello = ('   ____     ___     ______    __ __     _____      ____  __ __    ___  _____ _____   ___  ____  \n'
         '  |    \   /   \   |      |  |  |  |   / ___/     /    ||  |  |  /  _]/ ___// ___/  /  _]|    \ \n'
         '  |  o  ) |     |  |      |  |  |  |  (   \_     |   __||  |  | /  [_(   \_(   \_  /  [_ |  D  )\n'
         '  |   _/  |  O  |  |_|  |_|  |  |  |   \__  |    |  |  ||  |  ||    _]\__  |\__  ||    _]|    / \n'
         '  |  | __ |     | __ |  | __ |  :  | __/  \ |    |  |_ ||  :  ||   [_ /  \ |/  \ ||   [_ |    \ \n'
         '  |  ||  ||     ||  ||  ||  ||     ||  \    |    |     ||     ||     |\    |\    ||     _|_ .  \ \n'
         '  |__||__| \___/ |__||__||__| \__,_||__|\___|    |___,_| \__,_||_____| \___| \___||____|JDM||\_|\n'
         '^.~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~.^')
                                                                                            

# Read contents into list of lists 
for row in csv_reader:
    potus_names.append(row[1])

for idx, row in enumerate(potus_names):
    potus_names[idx] = row.split()

# Display startup message
print (hello)

# Prompt user for input
print("$$----------------------<| A game to name the U.S. Presidents in order |>-----------------------$$")
print("^.~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~.^\n")
while(play_again != 0):        
    print('Hardcore mode? (Y/N): ', end = " ")
    while hard_mode == 2:
        hard_mode_response = input()
        if hard_mode_response in ['Y'.casefold(), 'yes'.casefold()]:
            hard_mode = 1
            print('\n(Harcore mode active)\n')
        elif hard_mode_response in ['n'.casefold(), 'no'.casefold()]:
            hard_mode = 0
        else:
            print('Please respond w/ \'Yes\' or \'No\'')
    
    print("Type name and hit \'ENTER\':\n")
    if hard_mode == 0:
        # Game loop
        for idx, name in enumerate(potus_names):
            # Print number prompt
            print(f"{idx + 1}. ", end = " ")
            # Get user guess
            guess = input()
            #sys.stdout.write("\033[F")
            # Check guess
            while guess.casefold() not in [name[-1].casefold(), " ".join(name[-2:]).casefold(), " ".join(name).casefold(), 'skip', 's', 'quit']:
                if guess.casefold() == 'hint'.casefold():
                    initials = []
                    for word in name:
                        initials.append(word[0].upper())
                    #sys.stdout.write("\033[F")
                    print(f"Initials are {''.join(initials)}")
                    #time.sleep(0.8)
                    #sys.stdout.write("\033[F")
                # Check if asking for hint
                elif guess.casefold() == 'another hint':
                    #sys.stdout.write("\033[F")
                    print(f"Dude, it's {' '.join(name)}...")
                    break
                    #time.sleep(0.8)
                else:
                    # On wrong guess warn and re-issue prompt
                    sys.stdout.write("\033[F")
                    print('\rThat\'s not right, try again:')
                    time.sleep(0.8)
                    sys.stdout.write("\033[F                                   \r")
                print(f"{idx + 1}. ", end = " ")
        
                # Get next guess
                guess = input()
        print('Well done! You know your presidents')
        
    else:
        # Game loop
        for idx, name in enumerate(potus_names):
            # Print number prompt
            print(f"{idx + 1}. ", end = " ")
            # Get user guess
            guess = input()
            #sys.stdout.write("\033[F")
            # Check guess
            if guess.casefold() not in [name[-1].casefold(), " ".join(name[-2:]).casefold(), " ".join(name).casefold()]:
                print(f"\n\rGAME OVER \n(Correct answer: {' '.join(name)})              \n")
                print('Play again? (Y/N): ', end = " ")
                while play_again == 2:
                    play_again_response = input()
                    if play_again_response in ['Y'.casefold(), 'yes'.casefold()]:
                        play_again = 1
                    elif play_again_response in ['n'.casefold(), 'no'.casefold()]:
                        play_again = 0
                    else:
                        print('Please respond w/ \'Yes\' or \'No\'')
                if play_again == 1:
                    hard_mode = 2
                    print('Restarting...')
                    time.sleep(0.8)
                break
                    #sys.stdout.write("\033[F                                   \r")
    
            