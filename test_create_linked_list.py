import unittest
from test_merge_sorted_lists import createLinkedList, ListNode, printLinkedList

class TestCreateLinkedList(unittest.TestCase):
    def test_create_empty_list(self):
        result = createLinkedList([])
        self.assertIsNone(result)

    def test_create_single_element_list(self):
        result = createLinkedList([5])
        self.assertEqual(result.val, 5)
        self.assertIsNone(result.next)

    def test_create_multiple_element_list(self):
        result = createLinkedList([1, 2, 3])
        self.assertEqual(printLinkedList(result), [1, 2, 3])

    def test_create_list_with_negative_numbers(self):
        result = createLinkedList([-1, -2, -3])
        self.assertEqual(printLinkedList(result), [-1, -2, -3])

    def test_create_list_with_mixed_numbers(self):
        result = createLinkedList([-1, 0, 1])
        self.assertEqual(printLinkedList(result), [-1, 0, 1])

    def test_create_list_with_duplicates(self):
        result = createLinkedList([1, 1, 1])
        self.assertEqual(printLinkedList(result), [1, 1, 1])

if __name__ == '__main__':
    unittest.main()
