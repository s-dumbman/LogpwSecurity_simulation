import time
import string
from itertools import product
from math import log10

charset = string.ascii_lowercase #abc...xyz
password = 'mathgo'
max_length = len(password)

N = len(charset)**len(password)
log_N = log10(N)    
print(f"가능한 조합 수: {N}, s = {log_N:.2f}")


start = time.time()
for length in range(1, max_length + 1):
    for attempt in product(charset, repeat=length):
        if ''.join(attempt) == password:
            end = time.time()
            print(f"비밀번호 '{password}' - 시도 시간: {end - start:.2f}초")
            break
    else:
        continue
    break
