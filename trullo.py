"""Trullo

Environment variables:

TRELLO_TOKEN
TRELLO_API_KEY

usage:
    trl l [ <board_id> [ <list_id> [ <card_id> ] ] ]
    trl b
    trl g <api_path>

    -h --help this help message
    -v --version print version and exit

"""

import pprint
from docopt import docopt

from trullo.printer import Printer
from trullo.tclient import TClient

if __name__ == '__main__':
    args = docopt(__doc__, version='Trullo beta')

    tclient = TClient()

    if args['g']:
        api_path = args['<api_path>']
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(tclient.get(api_path))

    if args['b']:
        boards = tclient.get_tree()
        Printer.print_boards(boards)

    if args['l']:
        board_id = args['<board_id>']
        if board_id:
            list_id = args['<list_id>']
            if list_id:
                card_id = args['<card_id>']
                if card_id:
                    card = tclient.get_card(card_id)
                    Printer.print_card(card)
                else:
                    cards = tclient.get_cards(list_id)
                    Printer.print_cards(cards)
            else:
                lists = tclient.get_lists(board_id)
                Printer.print_lists(lists)
        else:
            boards = tclient.get_boards()
            Printer.print_boards(boards)

