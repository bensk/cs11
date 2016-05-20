todo_list = {}
day = ""

def add():
	user_input=""
	while user_input != "exit":
		user_input = raw_input("What do you need to do?\n")
		day = raw_input("What day?\n").lower()
		todo_list[day] = user_input
	list_app()

# def get(list):
# 	for

def get():
	user_input = raw_input("What day do you need?")
	print todo_list[user_input]

def list_app():
	user_input = raw_input("What would you like to do?\n")
	if user_input == "add":
		add()
	elif user_input =="get":
		get()
	elif user_input == "exit":
		return None
	elif user_input == "print":
		print todo_list

list_app()