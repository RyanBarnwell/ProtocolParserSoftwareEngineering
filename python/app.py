# DO NOT CHANGE THIS FILE
import sys

import parser


def process_args():

    if len(sys.argv) == 1:
        print('Please specify one of the following:')
        print('  * Space separated list of input values')
        print('  * The argument -f followed by the full path to an input file')
        sys.exit(1)

    elif sys.argv[1] == '-f':
        print('Reading file: %s' % sys.argv[2])
        with open(sys.argv[2], 'r') as f:
            input_values = f.readline().split()
            input_values = ' '.join(input_values)
    else:
        input_values = ' '.join(sys.argv[1:])

    return input_values


class ParserOutput(object):

    def __init__(self):
        self.output = []

    def print(self, text):
        self.output.append(text)


if __name__ == '__main__':
    values = process_args()
    print('Processing input: %s' % values)
    print('')

    parser_output = ParserOutput()

    try:
        parser.parse(values, parser_output)
    except Exception as e:
        print("Error parsing protocol: " + type(e).__name__)

    for line in parser_output.output:
        print(line)
