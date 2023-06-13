# Task managing app
# Notes:
# 1. Use the following username and password to access the admin rights
# username: admin
# password: password
# 2. Ensure you open the whole folder for this task in VS Code otherwise the
# program will look in your root directory for the text files.

# =====importing libraries===========
import os
from datetime import datetime, date
DATETIME_STRING_FORMAT = "%Y-%m-%d"


def write_task_file():
    # creates / writes to task file to store list of tasks
    with open("tasks.txt", "w") as task_file:
        task_list_to_write = []
        for t in task_list:
            str_attrs = [
                t['username'],
                t['title'],
                t['description'],
                t['due_date'].strftime(DATETIME_STRING_FORMAT),
                t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                "Yes" if t['completed'] else "No"
            ]
            task_list_to_write.append(";".join(str_attrs))
        task_file.write("\n".join(task_list_to_write))
    print("Task file successfully updated.")


def reg_user():
    '''Add a new user to the user.txt file'''
    # - Request input of a new username
    new_username = input("New Username: ")
    while new_username in username_password:  # if username in username dictionary prompt user for new input
        new_username = input(
            "This username already exists please try another name: ")
    # - Request input of a new password
    new_password = input("New Password: ")
    # - Request input of password confirmation.
    confirm_password = input("Confirm Password: ")
    # - Check if the new password and confirmed password are the same.
    if new_password == confirm_password:
        # - If they are the same, add them to the user.txt file,
        print("New user added")
        username_password[new_username] = new_password
        with open("user.txt", "w") as out_file:
            user_data = []
            for k in username_password:
                user_data.append(f"{k};{username_password[k]}")
            out_file.write("\n".join(user_data))
    # - if password doesnt match, present a relevant message.
    else:
        print("Passwords do no match")


def add_task():
    '''Allow a user to add a new task to task.txt file
        Prompt a user for the following:
        - A username of the person whom the task is assigned to,
        - A title of a task,
        - A description of the task and
        - the due date of the task.'''

    task_username = input("Name of person assigned to task: ")
    # if user not found in user dictionary then exit
    if task_username not in username_password.keys():
        print("User does not exist. Please enter a valid username")
        return None

    task_title = input("Title of Task: ")
    task_description = input("Description of Task: ")
    while True:
        try:
            task_due_date = input("Due date of task (YYYY-MM-DD): ")
            due_date_time = datetime.strptime(
                task_due_date, DATETIME_STRING_FORMAT)
            break
        except ValueError:
            print("Invalid datetime format. Please use the format specified")

    # Then get the current date.
    curr_date = date.today()
    ''' Add the data to the file task.txt and
            Include 'No' to indicate if the task is complete.'''
    new_task = {
        "username": task_username,
        "title": task_title,
        "description": task_description,
        "due_date": due_date_time,
        "assigned_date": curr_date,
        "completed": False
    }

    task_list.append(new_task)
    write_task_file()


def view_all():
    '''Reads the task from task.txt file and prints to the console in the
        format of Output 2 presented in the task pdf (i.e. includes spacing
        and labelling)
    '''
    task_number = 1
    for t in task_list:
        disp_str = f"Task: \t\t {t['title']}\n"
        disp_str += f"Assigned to: \t {t['username']}\n"
        disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Task Description: \n {t['description']}\n"
        print(f"Task Number: \t {task_number} \n")
        print(disp_str)
        task_number += 1

    # promt user to exit function or edit specific task
    while True:
        chosen_task = int(input(
            "Please enter a task number to edit a specific task. Otherwise enter -1 to return to the home screen. "))
        if chosen_task == -1:
            return
        else:
            try:
                # save users choice under variable edit_task
                edit_task = task_list[chosen_task-1]
                print({edit_task["title"]})
                break
            except Exception as error:
                print(error)
                print("Task not found please try again")

    option = int(input(
        "To mark the task as complete please enter '1', to edit the task details enter 5: "))
    while option != 1 and option != 5 and option != -1:
        option = int(input(
            "To continue please enter '1' or '5'. Or to quit please enter -1: "))
    if option == -1:
        return
    elif option == 1:
        edit_task["completed"] = True  # update chosen task complete as True
    elif option == 5:
        if edit_task["completed"] == True:
            # if comeplete is True, exit function
            print("\n This task has been completed and can not be edited further")
            return
        else:
            edited_object = input(
                "Would you like to edit the due date or the assigned user? Please enter either 'due' or 'user' ").lower().strip()
            while edited_object != "due" and edited_object != "user":
                edited_object = input(
                    "Would you like to edit the due date or the assigned user? Please enter either 'due' or 'user' ").lower().strip()

            # update task dictionary acording to user input.
            if edited_object == -1:
                return
            elif edited_object == "due":
                while True:
                    try:
                        task_due_date = input(
                            "New due date of task (YYYY-MM-DD): ")
                        due_date_time = datetime.strptime(
                            task_due_date, DATETIME_STRING_FORMAT)
                        # edit due date using datetime formatting
                        edit_task["due_date"] = due_date_time
                        break
                    except ValueError:
                        print(
                            "Invalid datetime format. Please use the format specified")
            elif edited_object == "user":
                task_username = input("Name of person assigned to task: ")
                while task_username not in username_password.keys():
                    task_username = input(
                        "User does not exist. Please enter a valid username: ")  # check for valid user in username_password dictionary
                edit_task['username'] = task_username  # update username

    write_task_file()  # update the task.txt file with user changes


def view_mine():
    '''Reads the task from task.txt file and prints to the console in the
    format of Output 2 presented in the task pdf (i.e. includes spacing
    and labelling)'''

    for t in task_list:
        if t['username'] == curr_user:
            disp_str = f"Task: \t\t {t['title']}\n"
            disp_str += f"Assigned to: \t {t['username']}\n"
            disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Task Description: \n {t['description']}\n"
            print(disp_str)


def generate_task_overview():
    # creates txt file with information on tasks
    # get the total number of tasks, and set variables for completed and late tasks, then calculate by iterating through task_list dictionaries.
    total_tasks = len(task_list)
    completed_tasks = 0
    late_tasks = 0
    for t in task_list:
        if t["completed"] == True:
            completed_tasks += 1
        else:
            if t["due_date"] < datetime.now():
                late_tasks += 1
    # calculate percentages and round.
    incomplete_tasks = total_tasks-completed_tasks
    incomplete_percent = round((incomplete_tasks / total_tasks) * 100)
    overdue_percent = round((late_tasks/total_tasks) * 100)

    # write calculations to txt file, and format
    with open("task_overview.txt", "w") as file:
        file.write(
            f'''TASK OVERVIEW:\n\nTotal Tasks: \t {str(total_tasks)} \n
Completed Tasks: \t {str(completed_tasks)}\n
Uncompleted Tasks: \t {str(len(task_list)-completed_tasks)}\n
Tasks overdue: \t {str(late_tasks)}\n
Percent of tasks incomplete: \t {incomplete_percent}%\n
Percent of task overdue: \t {overdue_percent}%''')


def generate_user_overview():
    # creates txt file with information on each user and their assigned tasks
    # get the total number of users and tasks and create txt file.
    total_users = len(username_password)
    total_tasks = len(task_list)
    with open("user_overview.txt", "w") as file:
        file.write(
            f"USER OVERVIEW\nTotal Users: {total_users}\nTotal Tasks: {total_tasks}\n\n")
    # for each user found in username_password dictionary, create a set of variables to store their data for number of tasks and percentatges.
    for user in username_password.keys():
        username = user
        numof_tasks = 0
        completed_tasks = 0
        uncompleted_tasks = 0
        late_tasks = 0
        # iterate through task list to find task dictionaries associated with user and update variables accordingly.
        for task in task_list:
            if task["username"] == user:
                numof_tasks += 1
                if task["completed"] == True:
                    completed_tasks += 1
                elif task["completed"] == False:
                    uncompleted_tasks += 1
                    if task["due_date"] < datetime.now():
                        late_tasks += 1
        # calculate percentages using updated variables for each user
        user_percent = round((numof_tasks/total_tasks) * 100)
        completed_percent = round((completed_tasks/numof_tasks) *
                                  100) if numof_tasks else 0
        uncompleted_percent = round((
            uncompleted_tasks/numof_tasks) * 100) if numof_tasks else 0
        overdue_percent = round((late_tasks/numof_tasks)
                                * 100) if numof_tasks else 0

        # append to txt file with updated variables and percentages for each user.
        with open("user_overview.txt", "a") as file:
            file.write(f'''User: {username}\n
\t Total Tasks: \t {numof_tasks}\n
\t Percentage of tasks: \t {user_percent}%\n
\t Tasks Completed: \t {completed_percent}%\n
\t Tasks Due: \t {uncompleted_percent}%\n
\t Tasks Overdue: \t {overdue_percent}%\n\n''')


def generate_reports():
    # runs both report functions
    generate_task_overview()
    generate_user_overview()
    print("Please find generated reports in file directory")


def display_statistics():
    '''If the user is an admin they can display statistics about number of users
            and tasks.'''
    choice = input(
        "To view user statistics please enter 'u', to view task statistics please enter 't'").lower()
    while choice != "u" and choice != "t":
        choice = input(
            "To view user statistics please enter 'u', to view task statistics please enter 't'").lower()
    # if file does not exist, run generate txt function to create report and then read to console.
    if choice == "t":
        if not os.path.exists("task_overview.txt"):
            generate_task_overview()
        print()
        with open("task_overview.txt", "r") as file:
            for line in file:
                if line.strip():
                    print(line)
    # if file does not exist, run generate txt function to create report and then read to console.
    elif choice == "u":
        if not os.path.exists("user_overview.txt"):
            generate_user_overview()
        print()
        with open("user_overview.txt", "r") as file:
            for line in file:
                if line.strip():
                    print(line + "\n")


# Create tasks.txt if it doesn't exist
if not os.path.exists("tasks.txt"):
    with open("tasks.txt", "w") as default_file:
        pass

# variable 'task data is a list of all lines of info within the tasks.txt file.
with open("tasks.txt", 'r') as task_file:
    task_data = task_file.read().split("\n")
    task_data = [t for t in task_data if t != ""]


task_list = []
for t_str in task_data:
    curr_t = {}
    # Split by semicolon and manually add each component to two curr_t dictionaries and add both dictionaries to the task_list list.
    task_components = t_str.split(";")
    curr_t['username'] = task_components[0]
    curr_t['title'] = task_components[1]
    curr_t['description'] = task_components[2]
    curr_t['due_date'] = datetime.strptime(
        task_components[3], DATETIME_STRING_FORMAT)
    curr_t['assigned_date'] = datetime.strptime(
        task_components[4], DATETIME_STRING_FORMAT)
    curr_t['completed'] = True if task_components[5] == "Yes" else False
    task_list.append(curr_t)


# ====Login Section====
'''This code reads usernames and password from the user.txt file to 
    allow a user to login.
'''
# If no user.txt file, write one with a default account
if not os.path.exists("user.txt"):
    with open("user.txt", "w") as default_file:
        default_file.write("admin;password")

# Read in user_data
with open("user.txt", 'r') as user_file:
    user_data = user_file.read().split("\n")

# Convert to a dictionary
username_password = {}
for user in user_data:
    username, password = user.split(';')
    username_password[username] = password

logged_in = False
while not logged_in:

    print("LOGIN")
    curr_user = input("Username: ")
    curr_pass = input("Password: ")
    if curr_user not in username_password.keys():
        print("User does not exist")
        continue
    elif username_password[curr_user] != curr_pass:
        print("Wrong password")
        continue
    else:
        print("Login Successful!")
        logged_in = True


while True:
    # presenting the menu to the user and
    # making sure that the user input is converted to lower case.
    print()
    menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - View my task
gr - Generate reports
ds - Display statistics
e - Exit
: ''').lower()

    if menu == 'r':
        reg_user()

    elif menu == 'a':
        add_task()

    elif menu == 'va':
        view_all()

    elif menu == 'vm':
        view_mine()

    elif menu == 'gr':
        generate_reports()

    elif menu == 'ds' and curr_user == 'admin':
        display_statistics()

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")
