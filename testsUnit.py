import unittest
import sched.app as m


class testDelete(unittest.TestCase):

    def test_error_delete(self):
        self.assertRaises(NotImplementedError, m.appointment_delete, 1)

if __name__ == '__main__':
    unittest.main()
