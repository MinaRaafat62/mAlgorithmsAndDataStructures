import unittest
from mAlgorithmsAndDataStructures.tree.heap.min_heap import MinHeap

class MinHeapTestCase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(MinHeapTestCase, self).__init__(*args, **kwargs)

        
    def test_full_heap(self):
        min_heap = MinHeap()
        min_heap.insert(5)
        min_heap.insert(3)
        min_heap.insert(69)
        min_heap.insert(420)
        min_heap.insert(4)
        min_heap.insert(1)
        min_heap.insert(8)
        min_heap.insert(7)
        self.assertEqual(min_heap.length,8)
        
    def test_delete_half_heap(self):
        min_heap = MinHeap()
        min_heap.insert(5)
        min_heap.insert(3)
        min_heap.insert(69)
        min_heap.insert(420)
        min_heap.insert(4)
        min_heap.insert(1)
        min_heap.insert(8)
        min_heap.insert(7)
        self.assertEqual(min_heap.delete(),1)
        self.assertEqual(min_heap.delete(),3)
        self.assertEqual(min_heap.delete(),4)
        self.assertEqual(min_heap.delete(),5)
        
    def test_half_heap_length(self):
        min_heap = MinHeap()
        min_heap.insert(5)
        min_heap.insert(3)
        min_heap.insert(69)
        min_heap.insert(420)
        min_heap.insert(4)
        min_heap.insert(1)
        min_heap.insert(8)
        min_heap.insert(7)
        self.assertEqual(min_heap.delete(),1)
        self.assertEqual(min_heap.delete(),3)
        self.assertEqual(min_heap.delete(),4)
        self.assertEqual(min_heap.delete(),5)
        self.assertEqual(min_heap.length,4)
        
    def test_heap_len_after_deletion(self):
        min_heap = MinHeap()
        min_heap.insert(5)
        min_heap.insert(3)
        min_heap.insert(69)
        min_heap.insert(420)
        min_heap.insert(4)
        min_heap.insert(1)
        min_heap.insert(8)
        min_heap.insert(7)
        self.assertEqual(min_heap.delete(),1)
        self.assertEqual(min_heap.delete(),3)
        self.assertEqual(min_heap.delete(),4)
        self.assertEqual(min_heap.delete(),5)
        self.assertEqual(min_heap.delete(),7)
        self.assertEqual(min_heap.delete(),8)
        self.assertEqual(min_heap.delete(),69)
        self.assertEqual(min_heap.delete(),420)
        self.assertEqual(min_heap.length,0)
        
        
        
        
    
        