"""Main Controller class"""


class Main_Model:
    """Main Model class"""

    def __init__(self):
        self.model = None

    def user_sign_in(self, username, password):
        """User sign in method"""
        print(f"User {username} and {password} signed in")
