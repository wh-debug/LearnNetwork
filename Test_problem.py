import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """测试name_function.py"""
    def test_first_last_name(self):
        """主要看文件是否能够正确处理"""
        formatted_name = get_formatted_name('wang', 'tao')
        self.assertEqual(formatted_name, 'Wang Tao')

if __name__ == '__main__':
    unittest.main()


