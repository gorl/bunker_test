from typing import Dict

from generator import SimpleGenerator
from model import Entity
from reader import load_data
import argparse


def print_card(card:Dict[str, Entity]):
    for k in sorted(card.keys()):
        print('{}: {}'.format(k, card[k]))
    pass


def main():

    parser = argparse.ArgumentParser(description='Generates some cards for bunker')
    parser.add_argument('--xlsx', help='path to excel file')
    args = parser.parse_args()

    fname = args.xlsx

    data = load_data(fname)
    gen = SimpleGenerator(data)

    while True:
        print('Your card is:')
        card = gen.generate()
        print_card(card)
        print('\n\n')
        inp = input("Press Enter to continue...\n")
        if inp == 'Q':
            break


if __name__ == '__main__':
    main()