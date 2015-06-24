IN = 'Hello World'

def reverse(string):
    reverse = string.strip().split(' ')
    return ' '.join(reverse[::-1])

print reverse(IN)
