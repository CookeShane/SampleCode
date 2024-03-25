# Date Created: 07/03/24
# Author: Shane Cooke
# Description: Test file for 'departments.py'
# Last Amended:
# Amendment Author:

from src.departments import Departments
import pytest

def test_add_departments_new_dept():
    departments = Departments()
    departments.add_department('New Department', 5, 15)
    assert 'New Department' in departments.departments

def test_add_departments_neg_min_weight():
    departments = Departments()
    with pytest.raises(ValueError):
        departments.add_department('New Department', -5, 15)

def test_add_departments_neg_max_value():
    departments = Departments()
    with pytest.raises(ValueError):
        departments.add_department('New Department', 5, -15)

def test_add_departments_add_existing_name():
    departments = Departments()
    with pytest.raises(ValueError):
        departments.add_department('Mail', 5, 15)


def test_delete_departments_delete_dept():
    departments = Departments()
    departments.delete_department('Mail')
    assert 'Mail' not in departments.departments

def test_delete_departments_dept_nonexistent():
    departments = Departments()
    with pytest.raises(ValueError):
        departments.delete_department('New Department')


def test_edit_departments_change_weights():
    departments = Departments()
    departments.edit_department('Mail', 5, 15)
    assert departments.departments['Mail'] == (5, 15)

def test_edit_departments_dept_nonexistent():
    departments = Departments()
    with pytest.raises(ValueError):
        departments.edit_department('New Department', 5, 15)