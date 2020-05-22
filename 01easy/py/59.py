'''
请定义一个队列并实现函数 max_value 得到队列里的最大值，要求函数max_value、push_back 和 pop_front 的均摊时间复杂度都是O(1)。

若队列为空，pop_front 和 max_value 需要返回 -1

'''

class MaxQueue:

    def __init__(self):
        self._queue = []

    def max_value(self) -> int:
        if self._queue:
            return max(self._queue)
        else:
            return -1

    def push_back(self, value: int) -> None:
        self._queue.append(value)

    def pop_front(self) -> int:
        if self._queue:
            return self._queue.pop(0)
        else:
            return -1
