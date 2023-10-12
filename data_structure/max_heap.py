class MaxHeap:
    """
    Max heap
    root node is maximum value in heap
    """

    def __init__(self, array: list = []):
        # heap 的 index 會從 1 開始，所以補一個 None
        self.heap = [None]
        self.length = 0

        for item in array:
            self.insert(item)

    def insert(self, item):
        self.heap.append(item)
        self.length += 1
        self._up_check(self.length)

    def _up_check(self, idx: int):
        """
        insert 的元素會先放在 heap array 的最後一個位置
        開始與 parernt node 比較，如果值大於 parent node
        則交換兩個 node 一直比到 root node 或者值小於 parent node

        Args:
            idx (int): last node index
        """
        while idx > 1 and self.heap[idx] > self.heap[idx // 2]:
            self._exchange(idx // 2, idx)
            idx = idx // 2

    def extract(self):
        self._exchange(1, -1)

        max_ = self.heap.pop()

        self.length -= 1
        self._down_check(1)

        return max_

    def _down_check(self, idx: int):
        """
        在 extract 取出最大值後，最後一個位置的節點會換至根節點
        從根結點開始與自己的子節點做比較，與較大的那個子節點做交換
        一直檢查到無較大的子節點為止

        Args:
            idx (int): root node index = 1
        """
        while 2 * idx <= self.length:
            i = idx * 2

            k = i
            if i < self.length and self.heap[i + 1] > self.heap[i]:
                k = i + 1

            if self.heap[k] > self.heap[idx]:
                self._exchange(idx, k)

            idx = k

    def _exchange(self, i: int, j: int):
        tmp = self.heap[i]
        self.heap[i] = self.heap[j]
        self.heap[j] = tmp


if __name__ == "__main__":
    max_hq = MaxHeap([1, 4, 5, 10, 7, 3, 9])

    print(max_hq.heap)

    while max_hq.length > 0:
        print(max_hq.extract())
        print(max_hq.heap)
