import unittest
from mAlgorithmsAndDataStructures.algorithms.sorting.quick_sort import QuickSorter


class QuickSorterTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(QuickSorterTest, self).__init__(*args, **kwargs)

    def test_quick_sort(self):
        array = [5, 3, 69, 420, 4, 1, 8, 7]
        quick_sorter = QuickSorter(array)
        self.assertEqual(quick_sorter.sort(), [1, 3, 4, 5, 7, 8, 69, 420])
