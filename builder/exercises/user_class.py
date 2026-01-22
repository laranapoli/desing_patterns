class User:
    def __init__(self,
                 first_name: str,
                 last_name: str,
                 email_address: str
                 ):
        self.first_name = first_name
        self.last_name = last_name 
        self.age = None
        self.phone_number = None
        self.address = None
        self.email_address = email_address

    def get_name(self):
        full_name = f"{self.first_name} {self.last_name}"
        return full_name
    
    def get_contact(self):
        contact = f"Phone number: {self.phone_number} | e-mail: {self.email_address}"
        return contact
    

class UserBuilder:
    def __init__(self, 
                 first_name: str, 
                 last_name: str, 
                 email_address: str):
        self.user = User(
            first_name,
            last_name,
            email_address
        )

    def add_age(self, age):
        self.user.age = age
        return self.user

    def add_phone_number(self, phone_number):
        self.user.phone_number = phone_number
        return self.user

    def add_address(self, address):
        self.user.address = address
        return self.user
    

user = UserBuilder("Lara", "Nápoli", "Av. Bla").add_age(28)


print(user.get_name())