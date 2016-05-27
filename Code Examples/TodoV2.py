todo_list={
    "monday":[],
    "tuesday":[],
    "wednesday":[],
    "thursday":[],
    "friday":[],
    "saturday":[],
    "sunday":[],
}

def add(action,day):
	todo_list[day].append(action)

def get(day):
	print todo_list[day]
	menu()

def menu():
	choice = raw_input("How can I help you?\n")
	if choice == "get":
		when = raw_input("When?\n")
		get(when)
	elif choice == "print":
		for keys in todo_list:
			if todo_list[keys] != []:
				print "On " + keys + " you have to do " +  str(todo_list[keys])
	elif choice == "add":
		todo = ""
		while todo != "exit":
			todo = raw_input("What to do?\n")
			if todo == "exit":
				menu()
			when = raw_input("When?\n")
			add(todo,when)

menu()

# def menu():
# 	choice = raw_input("What would you like to do?")
# 	if choice == "add":
# 		add()
# 	elif choice == "get":
# 		get()
# 	elif choice == "print":
# 		print todo_list


# def list_app():
# 	user_input = raw_input("What would you like to do?\n")
# 	if user_input == "add":
# 		add()
# 	elif user_input =="get":
# 		get()
# 	elif user_input == "exit":
# 		return None
# 	elif user_input == "print":
# 		print todo_list
