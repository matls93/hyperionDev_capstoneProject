# hyperionDev_capstoneProject

## Task managing application 

This Python-based task managing application allows users to manage tasks through a console interface. Users can **register new accounts**, **add tasks**, **view tasks**, **generate reports**, and **display statistics**. The application stores user data and task information in **text files** (**user.txt** for user credentials and **tasks.txt** for task details).

### Notes:
1. To access admin rights, use the following credentials:
- Username: admin
- Password: password
2. Ensure you open the entire folder containing this application in your code editor, otherwise, the program will look for text files in your root directory.
  
### Features:
**User Management**:
- Registration (r): Allows adding new users to user.txt with unique usernames and passwords.

**Task Management**:
- Add Task (a): Enables users to add new tasks to tasks.txt, specifying details like username, task title, description, and due date.
- View All Tasks (va): Displays all tasks from tasks.txt.
- View My Tasks (vm): Shows tasks assigned to the currently logged-in user.

**Reports and Statistics**:
- Generate Reports (gr): Creates task_overview.txt and user_overview.txt files with detailed summaries of tasks and user assignments.
- Display Statistics (ds): Available for admin users (curr_user == 'admin'), allows viewing statistics on the number of users and tasks.

**File Handling**:
- Data Storage: User credentials and task details are stored in text files (user.txt and tasks.txt respectively).
- File Generation: Automatically creates tasks.txt if it doesn't exist to store task data.

## Usage:
1. Installation:
- Clone the repository to your local machine or download as a ZIP file.

2. Setup:
- Open the entire project folder in Code editor.
- Ensure Python environment is set up correctly with necessary dependencies (os and datetime are used from standard library).

3. Execution:
- Run the application by executing python main.py in the terminal within code editor.

4. Navigation:
- Follow the menu prompts in the console to perform actions like registering users, adding tasks, viewing tasks, generating reports, displaying statistics, and exiting the application (e).

### Security Considerations:
- This application uses a basic form of authentication and authorization for **demonstration purposes only**. It is not suitable for production environments.
- User passwords are stored in plain text within user.txt, which is **insecure for sensitive information**.

### Disclaimer:
This application is **provided as-is** and serves as an educational example of basic Python programming concepts, file handling, and console-based interaction.
