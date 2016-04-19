import random

# VARIABLES
GAME_OVER = False
PLAYER_HEALTH = 5
PLAYER_FOOD_POUNDS = 500
MILES_TO_GO = 2000
CURRENT_DAY = 1
CURRENT_MONTH = 3
MONTHS_31_DAYS = [3, 5, 7, 8, 10, 12]
HEALTH_DECREASES_THIS_MONTH = 0


def should_decrease_health():
	global HEALTH_DECREASES_THIS_MONTH
	if HEALTH_DECREASES_THIS_MONTH < 2:
		random_day = random.randint(0, 30)
		if random_day < 2:
			return True
	return False

# updates the day
def add_day():
	global PLAYER_FOOD_POUNDS
	global CURRENT_DAY
	global CURRENT_MONTH
	global MONTHS_31_DAYS
	global PLAYER_HEALTH

	if should_decrease_health():
		PLAYER_HEALTH -= 1
	if is_game_over():
		return
	if CURRENT_DAY < 31:
		CURRENT_DAY += 1
	elif CURRENT_DAY == 30 and CURRENT_MONTH in MONTHS_31_DAYS:
		CURRENT_DAY += 1
	else:
		CURRENT_MONTH += 1
		CURRENT_DAY = 1
	PLAYER_FOOD_POUNDS -= 5

# PROVIDE THIS TO STUDENTS
def update_days(low_range, high_range):
	days = random.randint(low_range, high_range)
	for i in range(0, days):
		add_day()

# moves the player 30-60 miles and takes 3-7 days
def travel():
	global MILES_TO_GO
	miles_traveled = random.randint(30, 61)
	MILES_TO_GO -= miles_traveled
	update_days(3, 7)

# increase health 1 level and takes 2-5 days
def rest():
	global PLAYER_HEALTH
	if PLAYER_HEALTH < 5:
		PLAYER_HEALTH += 1
	update_days(2, 5)

# adds 100lbs of food and takes 2-5 days
def hunt():
	global PLAYER_FOOD_POUNDS
	PLAYER_FOOD_POUNDS += 100
	update_days(2, 5)

# displays status
def display_status():
	global PLAYER_HEALTH
	global PLAYER_FOOD_POUNDS
	global MILES_TO_GO
	global CURRENT_DAY
	global CURRENT_MONTH

	print "Current Health: " + str(PLAYER_HEALTH)
	print "Food: " + str(PLAYER_FOOD_POUNDS) + "lbs"
	print "Distance Traveled: " + str(2000-MILES_TO_GO) + "miles"
	print "Day is: " + str(CURRENT_MONTH) + "/" + str(CURRENT_DAY)

# displays commands
def display_help():
	print "Commands are travel, rest, hunt, status, help, and quit"

# ends game before next turn
def quit_game():
	global GAME_OVER
	GAME_OVER = True

# check if the game is over
def is_game_over():
	global GAME_OVER
	global PLAYER_HEALTH
	global PLAYER_FOOD_POUNDS
	global MILES_TO_GO
	global CURRENT_DAY
	global CURRENT_MONTH

	if GAME_OVER:
		return True
	if CURRENT_DAY == 31 and CURRENT_MONTH == 12:
		print "It is Dec. 31st and you are not in Oregon."
		return True
	if PLAYER_HEALTH < 1:
		print "You're health detiorated, and you died :("
		return True
	if PLAYER_FOOD_POUNDS < 1:
		print "You ran out of food and starved"
		return True
	if MILES_TO_GO < 1:
		print "You MADE IT"
		return True
	return False

# parse and act upon input
def process_user_input(user_input):
	if user_input == "travel":
		travel()
	elif user_input == "rest":
		rest()
	elif user_input == "hunt":
		hunt()
	elif user_input == "status":
		display_status()
	elif user_input == "help":
		display_help()
	elif user_input == "quit":
		quit_game()
	else:
		print "Not Correct Input."

def game_loop():
	print 'Welcome to the trail. Would you like to travel, rest, hunt, status, help, or quit?'
	while not is_game_over():
		user_input = raw_input("What is your choice? ")
		process_user_input(user_input)


if __name__ == "__main__":
	game_loop()