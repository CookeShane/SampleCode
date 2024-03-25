# Date Created: 07/03/24
# Author: Shane Cooke
# Description: Class defining departments in the company
# Last Amended:
# Amendment Author:


# Departments Class
# Initilises to default deparments, Mail, Regular & Heavy
# Functions to add new department, delete department or change weight limits
# Can return current dictionary of departments if required
class Departments:
    def __init__(self):
        self.departments = {'Mail': (0, 1), 
                            'Regular': (1, 10),
                            'Heavy': (10, float('inf'))}
    
    def check_weights(self, min_weight, max_weight):
        if min_weight < 0 or max_weight < 0:
            raise ValueError('Error: Weights must be positive')

    def add_department(self, department_name, min_weight, max_weight):
        self.check_weights(min_weight, max_weight)
        if department_name in self.departments:
            raise ValueError('Department already exists. Please choose a unique name.')
        
        self.departments[department_name] = (min_weight, max_weight)
        print('Success: New department added.')   

    def delete_department(self, department_name):
        if department_name not in self.departments:
            raise ValueError('Error: Department does not exist.')
        del self.departments[department_name]

    def edit_department(self, department_name, min_weight, max_weight):
        self.check_weights(min_weight, max_weight)
        if department_name not in self.departments:
            raise ValueError('Error: Department does not exist.')
        self.departments[department_name] = (min_weight, max_weight)
        print('Success: Department weights updated.')

    def get_departments(self):
        return self.departments
    