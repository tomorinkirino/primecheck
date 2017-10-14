# -*- coding: utf-8 -*-
def is_prime(n):
    sq = int(n ** .5)
    for d in range(2, sq+1):
        if n % d == 0:
            return 0
    return n > 1

n = int(input('値を入力してください: '))
print('{0}は素数'.format(n) + ('です' if is_prime(n) else 'ではありません'))
