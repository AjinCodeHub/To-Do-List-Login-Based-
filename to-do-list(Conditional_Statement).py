print('###################################')
print('#### To-Do-List ####')
print('###################################')



account={}
while True:
    print('#### Account Create ####')
    print('1.Create Account')
    print('2.Login Account')
    print('3.Logout')
    
    choice = int(input('Select option: '))
    
    if choice == 1:
        Username = input('Enter your usename:')
        if Username in account:
            print('---- Username is already exit! ----')
        else:
            Email = input('Enter your email:')
            Password = input('Enter your password:')
            Confirm_password = input('Enter your confirm password:')
            if Password == Confirm_password:
                if (len(Password)) >= 8:
                    account[Username] = {
                            'Email':Email,
                            'Password':Password,
                            'tasks':[]
                        }
                    print("---- Account created successfully! ----")
                else:
                    print("---- Password must be at least 8 characters ----")
            else:
                print('---- Password not matched ----')
    elif choice == 2:
        Username = input('Enter your usename:')
        Password = input('Enter your password:')
        if Username in account and account[Username]['Password'] == Password:
            print("---- Account created successfully! ----")
            print("---- Now Login ----")
            while True:
            
                print('###################################')
                print('---- Welcome To To-Do-List-App ----')
                print('###################################')
    
                print('1 - Add To List')
                print('2 - Display List')
                print('3 - Remove From List')
                print('4 - Exit')
                options = int(input('Select your Option: '))
    
                if options == 1:
                    task = input('Enter new task: ')
                    account[Username]['tasks'].append(task)
                    print('---- Task Added Successfully! ----')
        
                elif options == 2:
                    tasks = account[Username]['tasks']
                    if len(tasks) == 0:
                        print('---- No Task ----')
                    else:
                        print('---- Your Tasks ----')
                        for i , task in enumerate(tasks,1):
                            print(i,'-', task)
                
                elif options == 3:
                    tasks = account[Username]['tasks']
        
                    if len(tasks) == 0:
                        print('---- No Task ----')
                    else:
                        print('---- Your Tasks ----')
                        for i , task in enumerate(tasks,1):
                            print(i,'-', task)
                
                        index = int(input('Enter task number to remove: '))
            
                        if 1 <= index <= len(tasks):
                            removed = tasks.pop(index - 1)
                            print(removed, "removed successfully!")
                        else:
                            print("---- Invalid task number! ----")
        
                elif options == 4:
                    print('---- Exit ----')
                    break
                else:
                    print('---- Invalid Entry ----')
        else:
            print('---- Login Failed ----')
    elif choice == 3:
            print('---- Exit ----')
            break
    else:
        print('---- Invalid Entry ----')   