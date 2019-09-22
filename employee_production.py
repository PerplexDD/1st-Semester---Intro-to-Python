# Write an Employee class that has fields for the following pieces of information:
#
# • Employee name
# • Employee number
#
# Next, write a class named ProductionWorker that extends the Employee class. The
# ProductionWorker class should have fields to hold the following information:
#
# • Shift number (an integer, such as 1, 2, or 3)
# • Hourly pay rate
#
# The workday is divided into two shifts, day and night. The shift attribute will hold an integer value representing
# the shift that the employee works. The day shift is shift 1 and the night shift is shift 2. Write the appropriate
# accessor and mutator methods for each class.
#
# Once you have designed the classes, write a program that creates an object of
# ProductionWorker class and prompts the user to enter data for each of the object’s data attributes. Store the data
# in the object and then use the object’s accessor methods to retrieve it and display it on the screen.


class Employee:
    """ Class to hold info on an Employee """

    def __init__(self, name, numb):
        self.emp_name = name
        self.emp_numb = numb

    def set_emp_info(self, name, number):
        self.emp_name = name
        self.emp_numb = number

    def get_name(self):
        return self.emp_name

    def get_number(self):
        return self.emp_numb


class ProductionWorker(Employee):
    """ Specific class of Employee """

    def __init__(self, name, numb, shift, pay_rate):
        super(ProductionWorker, self).__init__(name, numb)
        self.shift = shift
        self.pay_rate = pay_rate

    def set_values(self, name, number, shift, pay):
        self.emp_name = name
        self.emp_numb = number
        self.shift = shift
        self.pay_rate = pay

    def get_name(self):
        return self.emp_name

    def get_number(self):
        return self.emp_numb

    def get_shift(self):
        return self.shift

    def get_pay(self):
        return self.pay_rate


myWorker = ProductionWorker("", "", 0, 0.00)

emp_name = input("Enter the Production worker's name: ")
emp_number = input("Enter the Production worker's ID number: ")
emp_shift = input("Enter the Production worker's shift identifier(1 for 1st, 2 for 2nd): ")
emp_pay = float(input("Enter the production worker's hourly pay rate: "))

myWorker.set_values(emp_name, emp_number, emp_shift, emp_pay)

print('Production Worker Info: ')
print(f'Name: {myWorker.get_name().title()}')
print(f'Worker ID: {myWorker.get_number().upper()}')
if emp_shift == '1':
    print(f'Shift: {myWorker.get_shift()}st')
else:
    print(f'Shift: {myWorker.get_shift()}nd')
print(f'Pay Rate: ${format(myWorker.get_pay(), ".2f")}')

