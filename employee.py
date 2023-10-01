
"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""
class Employee:

    def __init__(self, name, contract, bonus):

        self.name = name

        self.contract = contract

        self.bonus = bonus

        self.pay = self.contract.get_salary() + self.bonus.get_bonus()

        

        

    def get_pay(self):

        return self.pay



    def __str__(self):

        text = self.name + self.contract.get_str() + self.bonus.get_str() + "Their total pay is " + str(self.pay) + "."

        return text



class Contract:

    def __init_(self):

        self.salary = 0

        

    def get_salary(self):

        return self.salary

    

    def get_str(self):

        return ""



class MonthlyContract(Contract):

    def __init__ (self, salary):

        self.salary = salary;

        

    def get_salary(self):

        return self.salary

    

    def get_str(self):

        return " works on a monthly salary of " + str(self.salary) 

    

class HourlyContract(Contract):

    def __init__(self, pay, hours):

        self.pay = pay

        self.hours = hours

        

    def get_salary(self):

        return self.pay * self.hours

    

    def get_str(self):

        return " works on a contract of " + str(self.hours) + " hours at " + str(self.pay) + "/hour"

    

class Commission:

    def __init__(self):

        self.bonus = 0

        

    def get_bonus(self):

        return self.bonus

    

    def get_str(self):

        return ". "



class BonusCom(Commission):

    def __init__(self, bonus):

        self.bonus = bonus

    

    def get_bonus(self):

        return self.bonus

    

    def get_str(self):

        return " and receives a bonus commission of " + str(self.bonus) +". "

    

class ContractCom(Commission):

    def __init__(self, contracts, commission):

        self.contracts = contracts

        self.commission = commission

    

    def get_bonus(self):

        return self.contracts * self.commission

    

    def get_str(self):

        return " and receives a commission for " + str(self.contracts) +" contract(s) at " + str(self.commission) +"/contract. "

    

class NoCom(Commission):

    def __init__(self):

        super().__init__()

    

# Billie works on a monthly salary of 4000.  Their total pay is 4000.

billieContract = MonthlyContract(4000)

billieBonus = NoCom()

billie = Employee('Billie', billieContract, billieBonus)







# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.

charlieContract = HourlyContract(25, 100)

charlieBonus = NoCom()

charlie = Employee('Charlie', charlieContract, charlieBonus)





# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.

reneeContract = MonthlyContract(3000)

reneeBonus = ContractCom(4, 200)

renee = Employee('Renee', reneeContract, reneeBonus)





# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.

janContract = HourlyContract(25, 150)

janBonus = ContractCom(3,220)

jan = Employee('Jan', janContract, janBonus)

print(jan.__str__())



# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.

robbieContract = MonthlyContract(2000)

robbieBonus = BonusCom(1500)

robbie = Employee('Robbie', robbieContract, robbieBonus)

print(robbie.__str__())



# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.

arielContract = HourlyContract(30,120)

arielBonus = BonusCom(600)

ariel = Employee('Ariel', arielContract, arielBonus)

print(ariel.__str__())


