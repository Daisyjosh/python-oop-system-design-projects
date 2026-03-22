class User:
    def __init__(self,id,name,email,phone):
        self.id = id
        self.name = name
        self.email = email
        self.phone = phone

    def display(self):
        print(self.id,self.name,self.email,self.phone)

    