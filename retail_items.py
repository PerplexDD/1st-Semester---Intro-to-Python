# Creates a class for RetailItems.
class RetailItems:
    """ A class to hold info on retail items """

    def __init__(self, description, units, price):
        """ Initiates the constructor """
        self.description = description
        self.units = int(units)
        self.price = float(price)

    # Method to display the retail item info in a multi-line string.
    def display_item(self):
        """ Displays the info about a retail item """
        print(f'''Item:   {self.description.title()}
Units:  {self.units}
Price: ${self.price}
            ''')


# Creates objects from given infomration.
myItem_one = RetailItems('Jacket', 12, 59.95)
myItem_two = RetailItems('Designer Jeans', 40, 34.95)
myItem_three = RetailItems('Shirt', 20, 24.95)

# Uses the display method to output the information.
myItem_one.display_item()
myItem_two.display_item()
myItem_three.display_item()
