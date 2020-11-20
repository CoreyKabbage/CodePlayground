from modules import Restaurant
from modules import IceCreamStand
import modules
import othermodule
from random import randint

exercise = int(input("Which exercise?\n"))

#Make a class called restaurant. 9-1



class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")
        
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    def increment_odometer(self, miles):
        self.odometer_reading += miles

class Battery:
    """A simple attempt to model a battery for an electric car."""
    
    def __init__(self, battery_size=75):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
            
        print(f"This car can go about {range} miles on a full charge.")
    
    def upgrade_battery(self):
        if self.battery_size <= 100:
            self.battery_size = 100
        else:
            pass


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    
    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery.battery_size}-kWh battery.")

class Dice():
    def __init__(self, sides):
        self.sides = sides
    def roll_dice(self):
        result = randint(1, self.sides)
        print(result)


if exercise == 1:
    #9-1
    restaurant = Restaurant("Papa's Pizzeria", "Italian")
    restaurant.describe_restaurant()
    restaurant.open_restaurant()

if exercise == 2:
    #9-2 -- Create three different restaurants, and call describe_restaurant() for each of them.
    restaurant1 = Restaurant("Red Robin", "Diner")
    restaurant2 = Restaurant("Olive Garden", "Italian")
    restaurant3 = Restaurant("Wendy's", "fast")

    restaurant1.describe_restaurant()
    restaurant2.describe_restaurant()
    restaurant3.describe_restaurant()

elif exercise == 3:
    #9-3
    #Make a class called User, with two attributes called first_name and last_name. Make amethod caled describe_user() that prints a summary of the user.
    #Another method called greet_user() should print a personalized greeting.
    current_user = User("Lexi", "Games")
    current_user.describe_user()
    current_user.greet_user("You rock")
    current_user = User("Doctor", "Meme")
    current_user.describe_user()
    current_user.greet_user("Meme on me")

elif exercise == 4:
    #9-4 
    #Add number_served to Restaurant, create an instance, and print the number of customers served. Change the value, then print it again.
    #Add a method called set_number_served that changes the number_served value to an input.
    #Add a method called increment_number_served which adds to the number_served per day of business.
    restaurant1 = Restaurant("Cheesecake Factory", "Fatty", 0)
    restaurant1.describe_restaurant()
    restaurant1.set_number_served(10)
    restaurant1.describe_restaurant()
    restaurant1.increment_number_served()
    restaurant1.describe_restaurant()

elif exercise == 5:
    #9-5
    #Add login_attempts to the User class, and write a method to increment_login_attempts(), another method called reset_login_attempts() should do what it says on the tin.
    #Make an instance of User, increment login attempts, then print, reset, and print again.
    user1 = User("Corey", "Kabbage")
    user1.increment_login_attempts()
    print(f"You have tried to log in {user1.login_attempts} times.")
    user1.increment_login_attempts()
    print(f"You have tried to log in {user1.login_attempts} times.")
    user1.reset_login_attempts()
    print(f"Login attempts reset - You have tried to log in {user1.login_attempts} times.")

elif exercise == 6:
    #9-6
    #Write a class called IceCreamStand that inherits from Restaurant, with attributes for ice cream flavors, and display the flavors.
    icecreamparlor = IceCreamStand(restaurant_name="icebaby", cuisine_type="ice cream", number_served=0, flavors=["chocolate", "pistachio", "blue smurf", "peanut butter", "birthday cake"])
    icecreamparlor.describe_restaurant()
    icecreamparlor.display_flavors()

elif exercise == 7:
    #9-7
    #Write a class called Administrator which inherits from User, with an attribute called privileges, which stores a list of strings of admin actions.
    admin = modules.Administrator("Honorable", "Horace", ["ban", "kick", "edit message", "warn", "manage channels"])
    admin.describe_user()
    admin.show_privileges()

elif exercise == 8:
    #9-8
    #Make privileges its own class, and assign the class to an Administrator, then move show_privileges() to the Privilges class, and use the method once it is instanced.
    admin = modules.Administrator("Honorable", "Horace", ["ban", "kick", "edit message", "warn", "manage channels"])
    admin.describe_user()
    admin.privileges.show_privileges()

elif exercise == 9:
    #Using the code from electric_car.py, add a method to the Battery class called upgrade_battery() which sets capacity to 100 if it isn't.
    tesla = ElectricCar("tesla", "cybertruck", 2020)
    tesla.describe_battery()
    tesla.battery.upgrade_battery()
    tesla.describe_battery()
elif exercise == 10:
    restaurant = Restaurant("centaurs' garden", "salad", 3)
    restaurant.describe_restaurant()

elif exercise == 11:
    admin = modules.Administrator("Corey", "Kabbage", ["kick", "ban", "mute", "deafen"])
    admin.privileges.show_privileges()

elif exercise == 12:
    admin = othermodule.Administrator("Corey", "Kabbage", ["kick", "ban", "mute", "deafen"])
    admin.privileges.show_privileges()

elif exercise == 13:
    sixsidedice = Dice(6)
    sixsidedice.roll_dice()
    sixsidedice.roll_dice()
    sixsidedice.roll_dice()
    sixsidedice.roll_dice()
    sixsidedice.roll_dice()
    sixsidedice.roll_dice()
    sixsidedice.roll_dice()
    sixsidedice.roll_dice()
    sixsidedice.roll_dice()
    sixsidedice.roll_dice()
    tensidedice = Dice(10)
    tensidedice.roll_dice()
    tensidedice.roll_dice()
    tensidedice.roll_dice()
    tensidedice.roll_dice()
    tensidedice.roll_dice()
    tensidedice.roll_dice()
    tensidedice.roll_dice()
    tensidedice.roll_dice()
    tensidedice.roll_dice()
    tensidedice.roll_dice()
    twentysidedice = Dice(20)
    twentysidedice.roll_dice()
    twentysidedice.roll_dice()
    twentysidedice.roll_dice()
    twentysidedice.roll_dice()
    twentysidedice.roll_dice()
    twentysidedice.roll_dice()
    twentysidedice.roll_dice()
    twentysidedice.roll_dice()
    twentysidedice.roll_dice()
    twentysidedice.roll_dice()

elif exercise == 14:
    lotterycharacters = ["a", 3, 6 , 9, 2, 5, 8, "x", "n", "u"]
    lotteryrun = True
    lotteryloop = 0
    lotterynumbers = []
    while lotteryrun:
        numberpicked = randint(0, 9)
        lotteryitem = lotterycharacters[numberpicked]
        if lotteryloop <= 10:
            lotterynumbers.append(lotteryitem)
            lotteryloop += 1
        elif lotteryloop >= 10:
            print(f"The lottery ticket with the following is a winner: {lotterynumbers}")
            break

elif exercise == 15:
    #Test later
    lotterycharacters = ["a", 3, 6 , 9, 2, 5, 8, "x", "n", "u"]
    lotteryrun = True
    lotteryloop = 0
    lotterynumbers = []
    my_ticket = [2, 8, "x", "a", 6, "u", 9, 3, "n", 5]
    while lotteryrun:
        numberpicked = randint(0, 9)
        lotteryitem = lotterycharacters[numberpicked]
        if lotteryloop <= 10:
            lotterynumbers.append(lotteryitem)
            lotteryloop += 1
        elif lotteryloop >= 10:
            if lotterynumbers == my_ticket:
                print("You win!")
                break
            else:
                pass

elif exercise == 16:
    #Read about a python module and experiment with it.
    pass
else:
    print("I haven't gotten to that exercise.")