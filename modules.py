class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, number_served):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served
        self.new_customers = 0
    def describe_restaurant(self):
        print(f"Welcome to {self.restaurant_name}, how may we serve you?")
        print(f"We serve {self.cuisine_type} food here.")
        print(f"We have served {self.number_served} people.")
    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")
    def set_number_served(self, new_customers):
        self.number_served = new_customers
    def increment_number_served(self):
        self.number_served += 13

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, number_served, flavors):
        super().__init__(restaurant_name, cuisine_type, number_served)
        self.flavors = flavors
    def display_flavors(self):
        print(f"Our flavors are:")
        for flavor in self.flavors:
            print(flavor.title())

class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0
    def describe_user(self):
        print(f"The user in question is named {self.first_name.title()} {self.last_name.title()}!")
    def greet_user(self, greeting):
        print(f"{greeting}, {self.first_name.title()} {self.last_name.title()}.")
    def increment_login_attempts(self):
        self.login_attempts += 1
    def reset_login_attempts(self):
        self.login_attempts = 0