from employee import SalaryEmployee, HourlyEmployee, CommissionEmployee


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
    st001 = SalaryEmployee('Vishnu', 'Bovilla', 50000)
    vcarve.add_employee(st001)

    st002 = HourlyEmployee('Harini', 'Vindyala', 25, 50)
    vcarve.add_employee(st002)

    st003 = CommissionEmployee('Phani', 'Parepalli', 50000, 10, 10)
    vcarve.add_employee(st003)

    # print(vcarve.employees)
    vcarve.display_employees()
    vcarve.pay_employees()


main()
