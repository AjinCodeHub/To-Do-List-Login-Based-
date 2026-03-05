print('###################################')
print('#### To-Do-List ####')
print('###################################')

account = {}

def create_account():
    Username = input('Enter your username: ')
    
    if Username in account:
        print('---- Username already exists! ----')
        return

    Email = input('Enter your email: ')
    Password = input('Enter your password: ')
    Confirm_password = input('Confirm password: ')

    if Password != Confirm_password:
        print('---- Password not matched ----')
        return

    if len(Password) < 8:
        print('---- Password must be at least 8 characters ----')
        return

    account[Username] = {
        'Email': Email,
        'Password': Password,
        'tasks': []
    }

    print("---- Account created successfully! ----")


def login():
    Username = input('Enter your username: ')
    Password = input('Enter your password: ')

    if Username in account and account[Username]['Password'] == Password:
        print("---- Login Successful! ----")
        todo_menu(Username)
    else:
        print('---- Login Failed ----')


def add_task(Username):
    task = input('Enter new task: ')
    account[Username]['tasks'].append(task)
    print('---- Task Added Successfully! ----')


def display_tasks(Username):
    tasks = account[Username]['tasks']

    if len(tasks) == 0:
        print('---- No Tasks ----')
    else:
        print('---- Your Tasks ----')
        for i, task in enumerate(tasks, 1):
            print(i, '-', task)


def remove_task(Username):
    tasks = account[Username]['tasks']

    if len(tasks) == 0:
        print('---- No Tasks ----')
        return

    print('---- Your Tasks ----')
    for i, task in enumerate(tasks, 1):
        print(i, '-', task)

    index = int(input('Enter task number to remove: '))

    if 1 <= index <= len(tasks):
        removed = tasks.pop(index - 1)
        print(removed, "removed successfully!")
    else:
        print("---- Invalid task number ----")


def todo_menu(Username):

    while True:

        print('\n###################################')
        print('---- Welcome To To-Do-List-App ----')
        print('###################################')

        print('1 - Add Task')
        print('2 - Display Tasks')
        print('3 - Remove Task')
        print('4 - Logout')

        option = int(input('Select option: '))

        if option == 1:
            add_task(Username)

        elif option == 2:
            display_tasks(Username)

        elif option == 3:
            remove_task(Username)

        elif option == 4:
            print('---- Logged Out ----')
            break

        else:
            print('---- Invalid Entry ----')


while True:

    print('\n#### Account Menu ####')
    print('1.Create Account')
    print('2.Login Account')
    print('3.Exit')

    choice = int(input('Select option: '))

    if choice == 1:
        create_account()

    elif choice == 2:
        login()

    elif choice == 3:
        print('---- Exit ----')
        break

    else:
        print('---- Invalid Entry ----')