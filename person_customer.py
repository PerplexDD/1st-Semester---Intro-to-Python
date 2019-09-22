# Write a class named Person with data attributes for a person's name, address and telephone number.
# Next write a class named Customer that is a subclass of Person class. Customer should have data attribute for
# customer number and a Boolean value indicating whether the customer wishes to be on a mailing list.
# Demonstrate an instance of the Customer class in a simple program.

# Import random module.
import random


class Person:
    """ A class to hold info about a person """

    def __init__(self, name, address, phone):
        """ Initialize """
        self.name = name
        self.address = address
        self.phone = phone

    def show_info(self):
        """ Display info stored """
        print(f'Name: {self.name.title()}')
        print(f'Address: {self.address}')
        print(f'Phone number: {self.phone}')


class Customer(Person):
    """ Type of Person with different attributes """

    def __init__(self, name, address, phone, cust_id):
        """ Constructor with parent inheritance """
        super(Customer, self).__init__(name, address, phone)
        self.cust_id = cust_id
        self.mailing_list = False           # Not subscribed by default

    def update_mailing_list(self, mailing_list):
        if mailing_list.lower() == 'yes':
            self.mailing_list = True
        else:
            self.mailing_list = False

    def show_info(self):
        super(Customer, self).show_info()
        print(f'Customer ID: {self.cust_id}')
        if self.mailing_list:
            print('Mailing list: Subscribed')
        else:
            print('Mailing list: Not Subscribed')


cust_name = input('Enter the customer name: ')
cust_addy = input('Enter the customer address: ')
cust_phone_numb = input('Enter the customer phone number: ')
cust_number = input('Enter the customer ID: ')
cust_mailing = input('Does this customer wish to be on the mailing list(Yes / No): ')


myCustomer = Customer(cust_name, cust_addy,
                      cust_phone_numb, cust_number,
                      )
myCustomer.update_mailing_list(cust_mailing)

myCustomer.show_info()
