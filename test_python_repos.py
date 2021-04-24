import unittest
from .python_repos import r

class PythonReposTestCase(unittest.TestCase):
    def test_status_code_is_equal_200(self):
        self.assertEqual(r.status_code, 200)

if __name__ == "__main__":
    unittest.main()