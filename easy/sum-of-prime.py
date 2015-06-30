# coding: utf-8
# 前1000个素数之和

import math

def get_prime_sum(count):

    cnt = 1
    sum = 2 # for sake of 2
    i = 1 # for sake of 2

    while(cnt < count):
        i += 1
        sqrt = int(math.ceil(math.sqrt(i)))
        if (all([i % j != 0 for j in range(2, sqrt + 1)])):
            cnt += 1
            sum += i
    return sum

print(get_prime_sum(1000));
