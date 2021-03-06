import unittest
from employee import Employee
from administration import Administration
from parameterized import parameterized


class TestAdministration(unittest.TestCase):
    @parameterized.expand([
        ("Alicia", "Carrizo", 25, 1567352, 50000, 0),
        ("Pedro", "Jones", 31, 1524168, 45000, 1),
        ("María", "Vila", 35, 1523521, 25000, 2)
    ])
    def test_add_employee(self, name, surname, age, phone, salary, legajo):
        employee = Employee(name, surname, age, phone, salary)
        adm = Administration()
        adm.add_employee(employee.get_employee())
        key = len(adm.listEmployee) - 1
        self.assertEqual(key, legajo)


if __name__ == '__main__':
    unittest.main()
