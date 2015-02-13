class TwoSum:

    def __init__(self):
        self.table = dict()

    def add(self, n):
        self.table[n] = self.table.get(n, 0) + 1

    def find(self, value):
        for i in self.table:
            c = value - i
            if c in self.table or c == i:
                return True
        return False

ts = TwoSum()
ts.add(1)
ts.add(2)
ts.add(4)
print ts.find(7)
