class chatbook:
    def __init__(self):
        self.username = ''
        self.password = ''
        self.menu()


    def menu(self):
        user_input=input("""
                press 1 for SignUp
                press 2 for Login 
                press 3 for Exit 
                """)
 
        if user_input =='1':
            self.signup()
        elif user_input =='2':
            self.login()
        else:
            print('You are exiting the application')
            exit()
        print('\n')
        self.menu()


    def signup(self):
        email=input('Enter your email id: ')
        password=input('Enter your password: ')
        self.username=email
        self.password=password
        print('You have successfully signed up')
        self.menu()


    def login(self):
        id=input('Enter your email id: ')
        pwd=input('Enter your password: ')
        if self.username==id and self.password==pwd:
            print('You have successfully logged in')
            self.loggedin=True
        else:
            print('Invalid email or password')
        self.menu()

myobject=chatbook()
