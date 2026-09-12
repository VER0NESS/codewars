a + b      # 20
a - b      # 6
a * b      # 91
a / b      # 1.8571428571428572  (true division, returns float)
a // b     # 1                   (floor division)
a % b      # 6                   (remainder)
a ** b     # 62748517            (13 to the power 7)
+a         # 13                  (unary plus)
-a         # -13                 (unary minus)

a & b      # 5    (13 & 7)
a | b      # 15   (13 | 7)
a ^ b      # 10   (13 ^ 7)
~a         # -14  (bitwise NOT: ~x == -x - 1)
a << 1     # 26   (left shift by 1)
a >> 1     # 6    (right shift by 1)


Binary view:
13 = 1101
 7 = 0111

13 & 7 = 0101 = 5
13 | 7 = 1111 = 15
13 ^ 7 = 1010 = 10

Bool
a == b     # False
a != b     # True
a < b      # False
a <= b     # False
a > b      # True
a >= b     # True

x = 13; x += 7     # x = 20
x = 13; x -= 7     # x = 6
x = 13; x *= 7     # x = 91
x = 13; x /= 7     # x = 1.8571428571428572
x = 13; x //= 7    # x = 1
x = 13; x %= 7     # x = 6
x = 13; x **= 7    # x = 62748517
x = 13; x &= 7     # x = 5
x = 13; x |= 7     # x = 15
x = 13; x ^= 7     # x = 10
x = 13; x <<= 1    # x = 26
x = 13; x >>= 1    # x = 6

import math

math.sqrt(25)        # 5.0
math.sin(0)          # 0.0
math.cos(0)          # 1.0
math.floor(3.9)      # 3
math.ceil(3.1)       # 4
math.pow(2, 5)       # 32.0
math.log(math.e)     # 1.0
math.log(100, 10)    # 2.0

math.tan(math.pi / 4)   # 0.9999999999999999
math.exp(1)             # 2.718281828459045
math.factorial(5)       # 120
math.gcd(12, 18)        # 6