import sys
words_to_symbols = {
    'add': '+',
    'minus': '-',
    'times': '*',
    'divide': '/'
}

def parse_and_eval():
    # Turn words into the equivalent formula
    operation = ''.join(sys.argv[2] + words_to_symbols[sys.argv[1]] + sys.argv[3])
    print(eval(operation))

parse_and_eval()  