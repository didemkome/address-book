import os
import sys
import address_book

from argparse import ArgumentParser

SELF_SCRIPT = sys.argv[0].split("/")[-1]

HELPS = {
    'command': '{} add | list | remove'.format(SELF_SCRIPT),
    'add': "{} add 'My new task' 'Other task' 'more' or single item".format(SELF_SCRIPT),
    'params': 'can be a task (string) or index (int)',
}

def main(argv=None):

    if argv is None:
        argv = sys.argv

    command_choices = ['list', 'add', 'remove']

    parser = ArgumentParser(prog=SELF_SCRIPT)
    parser.add_argument('command', choices=command_choices, type=str, nargs='?', help=HELPS['command'])
    parser.add_argument('params', type=str, nargs='*', help=HELPS['params'])
    parser.add_argument('-v', '--version', action='version', version=address_book.VERSION)
    args = parser.parse_args()

    if args.command is None:
        parser.print_help()
        return 2
    
    if args.command.lower() == 'add':
        app = address_book.AddressBookDatabase()
        app.add_person()

    if args.command.lower() == 'list':
            app = address_book.AddressBookDatabase()
            app.list_person()

    if args.command.lower() == 'remove':
            app = address_book.AddressBookDatabase()
            app.remove_person()

if __name__ == "__main__":
    sys.exit(main())
