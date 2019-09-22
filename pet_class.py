# Create the pet class and attributes.
class Pet:
    """ A class to describe a pet """

    def __init__(self, name, animal_type, age):
        """ Initialize """
        self.name = name
        self.animal_type = animal_type
        self.age = age

    # Set the method for assigning the name.
    def get_name(self, name):
        """ Sets the name of pet """
        self.name = name

    # Set the method for assigning the type.
    def get_animal_type(self, animal_type):
        """ Sets the animal type """
        self.animal_type = animal_type

    # Set the method for assigning the age.
    def get_age(self, age):
        """ Sets age of pet """
        self.age = age

    # Set the method for returning the name.
    def set_name(self):
        """ Collects pet name """
        return self.name

    # Set the method for returning the type.
    def set_animal_type(self):
        """ Collects animal type """
        return self.animal_type

    # Set the method for returning the age.
    def set_age(self):
        """ Collects animal age """
        return self.age


# Creates a new Pet.
myPet = Pet('', '', 0)

# Gathers user input and assigns the attributes through calling the methods.
myPet.get_name(input("What is your pet's name?"))
myPet.get_animal_type(input("What type of animal is your pet?"))
myPet.get_age(float(input("How many years old is your pet?")))

# User the get methods to return the value into variables.
pets_name = myPet.set_name()
pets_type = myPet.set_animal_type()
pets_age = myPet.set_age()

# Prints out a statement of name, age and type.
print(f"Your pet's name is {pets_name.title()}, who is {pets_age} years old and a {pets_type}.")
