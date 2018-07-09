# Create a class that contains information about employees of a company and define methods to get/set employee name, job title, and start date.
class Employee:
    '''This represents a single employee'''

    def __init__(self, employee_name, employee_title, employee_start_date):
        self.employee_name = employee_name
        self.employee_title = employee_title
        self.employee_start_date = employee_start_date

    def get_employee_name(self):
        '''Returns the employee's name'''
        return self.employee_name

    def set_employee_name(self, new_employee_name):
        '''Changes the employee's name'''
        self.employee_name = new_employee_name
        print(f'Employee name changed to {new_employee_name}')

    def get_employee_title(self):
        '''Returns the employee's job title'''
        return self.employee_title

    def set_employee_title(self, new_title):
        '''Changes the employee's job title'''
        self.employee_title = new_title
        print(f'Employee title changed to {new_title}')

    def get_employee_start_date(self):
        '''Returns the employee's start date'''
        return self.employee_start_date

    def set_employee_start_date(self, new_start_date):
        '''Changes the employee's start date'''
        self.employee_start_date = new_start_date
        print(f'Employee start date changed to {new_start_date}')

    def __str__(self):
        return f'{employee_title}: {employee_name} (since {employee_start_date})'


# Copy the Company class
# Modify the `Company` class so that you assign employees to a company.
class Company:
    """This represents a company in which people work"""

    def __init__(self, company_name, date_founded):
        self.company_name = company_name
        self.date_founded = date_founded
        self.employees = set()

    def get_company_name(self):
        """Returns the name of the company"""

        return self.company_name

    def __str__(self):
        return f'{self.company_name} was founded on {self.date_founded}. Employee list: {self.employees}'

# Create a company, and three employees, and then assign the employees to the company.


# If this module is being executed immediately and not imported
if __name__ == '__main__':
    # Create a company
    MyCo = Company('MyCo', '2018-01-01')

    # Create Employees
    anne = Employee('Anne', 'CEO', '2018-01-01')
    betty = Employee('Betty', 'CFO', '2018-01-01')
    carly = Employee('Carly', 'CIO', '2018-01-01')

    # Add employees to the company
    MyCo.employees.add(anne)
    MyCo.employees.add(betty)
    MyCo.employees.add(carly)

# ? How can I make the employee list print as the __str__ I defined on the class?
    print(MyCo)
