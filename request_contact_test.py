import unittest
from request_contact import get_contacts_names


class RequestContactTests(unittest.TestCase):
    def test_get_contacts_names_test(self):
        data_request = get_contacts_names()
        response_lenght = len(data_request)
        self.assertEqual(20, response_lenght)


if __name__ == '__main__':
    unittest.main()
