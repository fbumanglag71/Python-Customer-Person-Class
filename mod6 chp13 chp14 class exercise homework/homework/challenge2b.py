## Author: Francisco Bumanglag
## Project: Customer and Person Class
## Assignment: Module 6 Project 1
## Course: Python Santa Ana College
## Class: CMPR114 Jason Sim
## Date: July 17, 2023


class Person:
    def __init__(self, name, address, telephone):
        self.name = name
        self.address = address
        self.telephone = telephone

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_address(self):
        return self.address

    def set_address(self, address):
        self.address = address

    def get_telephone(self):
        return self.telephone

    def set_telephone(self, telephone):
        self.telephone = telephone

#Next, write a class named Customer that is a subclass of the Person class. 
#The Customer class should have a data attribute for a customer number, and a Boolean 
#data attribute indicating whether the customer wishes to be on a mailing list. Demonstrate 
#an instance of the Customer class in a simple program.

class Customer(Person):
    def __init__(self, name, address, telephone, customer_number, mailing_list):
        super().__init__(name, address, telephone)
        self.customer_number = customer_number
        self.mailing_list = mailing_list

    def get_customer_number(self):
        return self.customer_number

    def set_customer_number(self, customer_number):
        self.customer_number = customer_number

    def gets_mailing_list(self):
        return self.mailing_list

    def set_mailing_list(self, mailing_list):
        self.mailing_list = mailing_list


def main():

    info = Customer("Francisco Bumanglag", "123 Street", "111-222-3333", "98765-4", "Y")

    print("Customers Name: ", info.get_name())
    print("Customers Address: ", info.get_address())
    print("Customers Telephone Number: ", info.get_telephone())
    print("Customers ID Number: ", info.get_customer_number())
    print("Mailing List: ", info.gets_mailing_list())
    print()


   if __name__ == "__main__":
    main()


