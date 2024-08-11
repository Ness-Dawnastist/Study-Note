import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """测试name_function.py"""
    def test_first_last_name(self):
        # 当运行此文件时，所有test_打头的方法都将自动运行
        """能够正确处理像Janis Joplin这样的姓名吗？"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')
        # 方法.assertEqual将两者进行比较
        # 测试结果会被显示在输出中

    def test_first_last_middle_name(self):
        """能够正确处理像Wolfgang Amadeus Mozart这样的姓名吗？"""
        formatted_name = get_formatted_name(
            'wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')

unittest.main() # 方法.main()用于运行测试