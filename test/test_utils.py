import unittest
from core.utils import GetAPIMessage

class TestGetAPIMessage(unittest.TestCase):
    def test_get_api_message(self):
        self.assertEqual(GetAPIMessage(1), "Success")
