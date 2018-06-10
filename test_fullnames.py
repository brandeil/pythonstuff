import unittest
from fullnames import get_fullname

class NamesTestCase(unittest.TestCase):
    """Tests for names.py"""

    def test_first_last(self):
        """Test names like Janis Joplin"""
        full_name = get_fullname("janis","joplin")
        self.assertEqual(full_name,"Janis Joplin")

unittest.main()