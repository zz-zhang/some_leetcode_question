class Bitset:
    
    def __init__(self, size: int):
        self.bits = [False for _ in range(size)]
        self.size = size
        self.count_cache = 0
        self.flipped = False
        # self.all_cache = False
        # self.one_cache = False

    def fix(self, idx: int):
        if not self.flipped:
            if not self.bits[idx]:
                self.count_cache += 1
                self.bits[idx] = True
        else:
            if self.bits[idx]:
                self.count_cache -= 1
                self.bits[idx] = False

    def unfix(self, idx: int):
        if not self.flipped:
            if self.bits[idx]:
                self.count_cache -= 1
                self.bits[idx] = False
        else:
            if not self.bits[idx]:
                self.count_cache += 1
                self.bits[idx] = True

    def flip(self):
        self.flipped = not self.flipped

    def all(self):
        if not self.flipped:
            return self.count_cache == self.size
        else:
            return self.count_cache == 0
        
    def one(self):
        if not self.flipped:
            return self.count_cache != 0
        else:
            return self.count_cache != self.size

    def count(self):
        if not self.flipped:
            return self.count_cache
        else:
            return self.size - self.count_cache

    def toString(self):
        if not self.flipped:
            res = ['1' if b else '0' for b in self.bits]
        else:
            res = ['0' if b else '1' for b in self.bits]
        return ''.join(res)
        


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()

if __name__ == '__main__':
    bs = Bitset(5)
    print(bs.toString())
    bs.fix(3)
    print(bs.toString())
    bs.fix(1)
    print(bs.toString())
    bs.flip()
    print(bs.toString())
    print(bs.all())
    bs.unfix(0)
    print(bs.toString())
    bs.flip()
    print(bs.toString())
    print(bs.one())
    bs.unfix(0)
    print(bs.toString())
    print(bs.count())
