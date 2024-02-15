# classes and OOP for a website
# class
class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
    
    def follow(self, user):
        user.followers += 1
        self.following += 1
    

# make or initialize object
user_1 = User(user_id="001", username="Bob")

# attributes
user_1.id = "001"
user_1.username = "Bob"

