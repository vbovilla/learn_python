# employee refers to filename
# Employee refers to classname
from employee import Employee


class Company:
    def __init__(self):
        self.employees = []

    def add_employee(self, new_employee):
        self.employees.append(new_employee)

    def display_employees(self):
        print('print current employees')
        print('-----------------------')
        for i in self.employees:
            print(i.first_name, i.last_name)
        print('-----------------------')

    def pay_employees(self):
        print('paying employees')
        for i in self.employees:
            print('paying for', i.first_name, i.last_name,
                  'amount: ', i.calculate_paycheck())


def main():
    vcarve = Company()
    st001 = Employee('Vishnu', 'Bovilla', 5000)
    vcarve.add_employee(st001)

    st002 = Employee('Harini', 'Vindyala', 10000)
    vcarve.add_employee(st002)

    st003 = Employee('Phani', 'Parepalli', 15000)
    vcarve.add_employee(st003)

    # print(vcarve.employees)
    vcarve.display_employees()
    vcarve.pay_employees()


main()
