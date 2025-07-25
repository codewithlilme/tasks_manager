import json
def add():
	try:
		with open("task.json","r")as file:
			tasks = json.load(file)
	except (FileNotFoundError , json.JSONDecodeError):
		tasks = {}
	task = input("Enter task: ").lower().strip()
	if not task.isalpha():
		return("Enter a valid task!")
	completion = input("Enter task status(complete/pending): ").lower().strip()
	if completion != "complete" and completion != "pending":
		return("Enter a valid status,'complete' or 'pending'")
	tasks[task] = completion
	with open("task.json","w")as file:
		json.dump(tasks,file)
		return("Task successfully added")		
def view():
	try:
		with open("task.json","r")as file:
			content = json.load(file)
		return(content)	
	except FileNotFoundError:
		return("No task file found")
	except  json.JSONDecodeError:
		return("No tasks present")
def update():
	updated_task = input("Enter task to update: ")
	with open("task.json","r")as file:
		tasks = json.load(file)
		if updated_task in tasks:
			print("Task found!")
			tasks[updated_task]= "completed"
			with open("task.json","w")as file:
				json.dump(tasks,file)
				return("Task updated successfully")
		else:
			return("Task not found")
while True:
	print("\n1.Add task\n2.View all tasks\n3.Update a completed task\n4.Exit\n*Ensure you use numbers only to choose an option\n*This program is case sensitive,avoid using spaces and ensure you use correct spelling of words.")
	choice = input("Enter option: ")
	if choice == "1":
		print(add())
	elif choice == "2":
		print(view())
	elif choice == "3":
		print(update())
	elif choice == "4":
		print("Signing out...")
		break 
	else:
		print("Enter a valid option!")	