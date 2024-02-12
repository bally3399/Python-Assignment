import unittest
from test import Test


class TestIntegerListGeneration(unittest.TestCase):
    def setUp(self):
        self.test = Test()

    def test_list_length(self):
        integer_list = self.test.generate_integer_list()
        self.assertEqual(len(integer_list), 15)

    def test_list_content(self):
        integer_list = self.test.generate_integer_list()
        expected_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        self.assertEqual(integer_list, expected_list)

    def test_duplicate_element(self):
        duplicated_list = self.test.duplicate_list()
        expected_list = self.test.generate_integer_list()
        self.assertTrue(duplicated_list, expected_list)

    def test_remove_duplicates(self):
        original_list = list(range(1, 16))
        result = self.test.remove_duplicates(self.test.duplicate_list())
        expected_list = original_list
        self.assertEqual(result, expected_list)

    def test_add_every_third(self):
        self.assertEqual(self.test.add_every_third_element(list(range(1, 10))), 18)
        self.assertEqual(self.test.add_every_third_element([10, -5, 3, 8, -2, 4, 7]), 7)

    def test_sum_first_middle_last(self):
        self.assertEqual(self.test.sum_first_middle_last([1, 2, 3, 4, 5, 6, 7, 8, 9]), 15)

    def test_collect_elements(self):
        elements = ['praise', 'praise', 'jane']
        expected = {'praise', 'jane'}
        self.assertEqual(self.test.collect_elements(elements), expected)

    def test_sum_elements(self):
        elements_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        expected_result = sum(elements_list)
        self.assertEqual(self.test.sum_elements(elements_list), expected_result)

    def test_remove_item_present(self):
        input_set = {1, 2, 3, 4, 5}
        number = 3
        expected_removed_element = 3
        expected_updated_set = {1, 2, 4, 5}
        removed_element = self.test.remove_item(input_set, number)
        self.assertEqual(removed_element, expected_removed_element)
        self.assertEqual(input_set, expected_updated_set)

    def test_find_intersection(self):
        set1 = {1, 2, 3, 4, 5}
        set2 = {4, 5, 6, 7, 8}
        self.assertEqual(self.test.find_intersection(set1, set2), {4, 5})


if __name__ == '__main__':
    unittest.main()
