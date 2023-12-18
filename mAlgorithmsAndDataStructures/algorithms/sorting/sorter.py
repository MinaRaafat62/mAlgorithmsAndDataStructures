class Sorter:
    def __init__(self, array):
        self.array = array

    def sort(self):
        raise NotImplementedError

    def swap(self, i, j):
        self.array[i], self.array[j] = self.array[j], self.array[i]

    def __str__(self):
        return str(self.array)
