class BitSequence(int):
    def __new__(cls, bits):
        return super().__new__(cls, int(bits, 2))

    def get_bit(self, position):
        return (self >> position) & 1
