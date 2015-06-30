"""
Given a positive integer, find the sum of its constituent digits.
"""

args = [
    "23",
    "496"
]

for arg in args:
    print sum(map(lambda x: int(x), arg))
