import unittest

import sort

class TestSortLists(unittest.TestCase):

    def setUp(self):
        self.empty_list = []
        self.sorted_short_list = [1, 2, 3]
        self.unsorted_list = [5, 3, 6, 9, 8, 1]
        self.sorted_list = [1, 3, 5, 5, 6, 9]

    #first test
    def test_sort_should_do_nothing_if_an_empty_list_is_passed(self):
        result = sort.sort_list(self.empty_list)

        self.assertEqual([], result)

    
      # second test    
    def test_sort_should_do_nothing_if_the_list_is_already_sorted(self):
        result = sort.sort_list(self.sorted_short_list)

        self.assertEqual([1, 2, 3], result)
    

    # third test: add a test case that verifies that an unsorted list is sorted correctly using the self.unsorted_list and self.sorted_list properties in the test
     
    def test_sort_should_order_the_items_of_the_given_list_in_ascendent_fashion(self):
        result = sort.sort_list(self.unsorted_list)

        self.assertEqual([1,3,5,6,8,9],result)
    


if __name__ == '__main__':
    unittest.main()