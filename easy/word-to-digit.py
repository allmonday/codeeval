word_book = {
    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
}

str_inputs = ["zero;two;five;seven;eight;four", "three;seven;eight;nine;two"]

for str_input in str_inputs:
    print ' '.join(map(lambda x: str(word_book[x]), str_input.split(';')))
