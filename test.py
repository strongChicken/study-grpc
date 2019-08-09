import random
import time

class Minus:
    def minus(self):
        return 1

class Plus:
    def plus(self, i1, i2):
        return Minus()

def get_plus():
    random.seed(time.time_ns())
    r = random.randint(1, 10)
    if r > 5:
        return None
    else:
        return Plus()

if __name__ == '__main__':
    num = get_plus().plus(1, 2).minus()
    if num is None:
        print("NULL")
    else:
        print(num[0])
    print(num)

None[0]
