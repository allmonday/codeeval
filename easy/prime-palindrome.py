# coding: utf-8
# 小于1000 的 素数回文数
import math

def is_palindrome(number):
    number_str = str(number)
    strlen = len(number_str)
    return all([number_str[j] == number_str[strlen-j-1] for j in range(strlen)])

def get_prime(upper):
    for i in xrange(upper, 2, -1):
        sqrt = int(math.ceil(math.sqrt(i)))
        if (all([i % j != 0 for j in range(2, sqrt)])) and is_palindrome(i):
            return i

print get_prime(1000);
