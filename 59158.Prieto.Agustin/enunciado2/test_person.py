import unittest
from employee import Person
from parameterized import parameterized


class TestPerson(unittest.TestCase):
    @parameterized.expand([
        ('Agustin', 'Prieto', 19, '2616804596', {'name': 'Agustin', 'surname': 'Prieto', 'age': 19, 'cellphone': '2616804596'})


    ])
    def test_get_person(self, name, surname, age, cellphone, result):
        persona1 = Person(name, surname, age, cellphone)
        self.assertEqual(persona1.get_person(), result)


if __name__ == '__main__':
    unittest.main()
