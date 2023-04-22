class User:
    def __init__(self, id, username) -> None:
        self.id = id
        self.username = username
    def follow (self, followers, following):

        

user_1 = User("001", "Avni")

print(user_1.id)