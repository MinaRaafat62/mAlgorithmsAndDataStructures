class MinHeap:
    def __init__(self):
        self._data = []
        self.length = 0

    def insert(self, value: int):
        self._data.append(value)
        self._heapify_up(self.length)
        self.length += 1

    def delete(self):
        if self.length == 0:
            raise Exception("you can't delete from an empty min heap")
        
        
        out_value = self._data[0]
        self.length -= 1
        if self.length == 0:
            self._data = []
            return out_value

        self._data[0] = self._data[self.length]
        self._heapify_down(0)
        return out_value

    def _heapify_down(self, idx: int) -> None:
        left_idx = self._left_child(idx)
        right_idx = self._right_child(idx)

        if idx >= self.length or left_idx >= self.length:
            return

        left_value = self._data[left_idx]
        right_value = self._data[right_idx]
        current_value = self._data[idx]

        if left_value > right_value and current_value > right_value:
            self._data[idx] = right_value
            self._data[right_idx] = current_value
            self._heapify_down(right_idx)

        elif right_value > left_value and current_value > left_value:
            self._data[idx] = left_value
            self._data[left_idx] = current_value
            self._heapify_down(left_idx)

    def _heapify_up(self, idx: int) -> None:
        if idx == 0:
            return
        parent_idx = self._parent(idx)
        parent_value = self._data[parent_idx]
        current_value = self._data[idx]
        if parent_value > current_value:
            self._data[idx] = parent_value
            self._data[parent_idx] = current_value
            self._heapify_up(parent_idx)

    def _parent(self, idx: int) -> int:
        return (idx - 1) // 2

    def _left_child(self, idx: int) -> int:
        return 2 * idx + 1

    def _right_child(self, idx: int) -> int:
        return 2 * idx + 2
