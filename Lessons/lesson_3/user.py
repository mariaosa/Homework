class User:
    def __init__(self, first_name, last_name):
        print("я создался")
        self.userfirst_name = first_name
        self.userlast_name = last_name

    def sayFirstname(self):
        print("Moe имя:", self.userfirst_name)

    def sayLastname(self):
        print("Моя фамилия:", self.userlast_name)

    def sayFirstnameLastname(self):
        print("Мои имя и фамилия:", self.userfirst_name, self.userlast_name)

