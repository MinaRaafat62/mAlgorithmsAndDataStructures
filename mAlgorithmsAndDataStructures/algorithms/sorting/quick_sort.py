from .sorter import Sorter


class QuickSorter(Sorter):
    def __init__(self, array):
        super(QuickSorter, self).__init__(array)

    def sort(self):
        self.quick_sort(0, len(self.array) - 1)
        return self.array

    def quick_sort(self, low: int, high: int):
        if low < high:
            pivot = self.partition(low, high)
            self.quick_sort(low, pivot - 1)
            self.quick_sort(pivot + 1, high)

    def partition(self, low: int, high: int) -> int:
        pivot = self.array[high]
        idx = low - 1
        for i in range(low, high):
            if self.array[i] <= pivot:
                idx += 1
                self.swap(idx, i)
        idx += 1
        self.swap(idx, high)
        return idx
