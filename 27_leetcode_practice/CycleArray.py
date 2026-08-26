class CycleArray:
    def __init__(self, size=1):
        #[)
        #end
        #start          
        #[1,    2,3,4,5]
        if size <= 0:
            raise ValueError("size must be greater than 0")
        self.size = size
        self.array = [None] * size
        self.start = 0
        self.end = 0
        self.count = 0

    def resize(self, newSize):
        if newSize < self.count or newSize <= 0:
            raise ValueError("newSize must be positive and no less than count")
        new_arr = [None] * newSize
        #将旧的arr copy到新的arr
        for i in range(self.count):
            new_arr[i] = self.array[(self.start + i) % self.size]
        self.array = new_arr
        self.start = 0
        # end 始终指向队尾的下一个空位置
        self.end = self.count % newSize
        self.size = newSize

    def add_first(self, val):
        #[1,2,3,4,5,_] add[6]
        #[1,2,3,4,5,6]
        if self.is_full():
            self.resize(self.size * 2)
        #左移start然后赋值
        self.start = (self.start - 1) % self.size
        self.array[self.start] = val
        self.count += 1

    def remove_first(self):
        if self.is_empty():
            return None
        #清空然后start右移一位
        val = self.array[self.start]
        self.array[self.start] = None
        self.start = (self.start + 1) % self.size
        self.count -= 1
        return val

    def add_last(self, val):
        if self.is_full():
            self.resize(self.size * 2)
        self.array[self.end] = val
        self.end = (self.end + 1) % self.size
        self.count += 1

    def remove_last(self):
        if self.is_empty():
            return None
        self.end = (self.end - 1 + self.size) % self.size
        val = self.array[self.end]
        self.array[self.end] = None
        self.count -= 1
        return val

    def get_first(self):
        if self.is_empty():
            return None
        return self.array[self.start]

    def get_last(self):
        if self.is_empty():
            return None
        return self.array[(self.end - 1 + self.size) % self.size]

    def is_full(self):
        return self.count == self.size

    def is_empty(self):
        return self.count == 0
