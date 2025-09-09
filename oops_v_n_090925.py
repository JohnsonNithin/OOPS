class Chatbook:
    """
    A simple Chatbook application that allows users to sign up and log in.
    Stores one user's credentials (email and password).
    """

    def __init__(self):
        """Initialize Chatbook with empty username and password."""
        self.username = ""
        self.password = ""
        self.logged_in = False
        self.menu()

    def menu(self):
        """
        Display the main menu and handle user input.
        Keeps running until the user chooses to exit.
        """
        while True:
            user_input = input(
                """
                ====== Chatbook Menu ======
                1. Sign Up
                2. Login
                3. Exit
                ===========================
                Enter your choice: """
            )

            if user_input == "1":
                self.signup()
            elif user_input == "2":
                self.login()
            elif user_input == "3":
                print("Exiting the application. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

    def signup(self):
        """
        Sign up a new user by asking for email and password.
        Stores the credentials in memory.
        """
        email = input("Enter your email id: ")
        password = input("Enter your password: ")

        # store the new user credentials
        self.username = email
        self.password = password

        print("✅ You have successfully signed up!")

    def login(self):
        """
        Log in an existing user by validating email and password.
        """
        email = input("Enter your email id: ")
        pwd = input("Enter your password: ")

        if self.username == email and self.password == pwd:
            self.logged_in = True
            print("🎉 You have successfully logged in!")
        else:
            print("❌ Invalid email or password")


# Run the app
if __name__ == "__main__":
    Chatbook()
