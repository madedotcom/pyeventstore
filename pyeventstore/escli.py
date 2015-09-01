import argparse
import sys

from cli import writeevents


def main(prog, args):
    opts = get_options(prog, args)
    instance = opts.cls(opts)
    instance.run()

def get_options(prog, args):
    parser = argparse.ArgumentParser(prog=prog)
    parser.add_argument(
        '--host', dest='host', default='localhost',
        help='eventstore host (default: localhost)')
    parser.add_argument(
        '--debug', dest='debug', action='store_true',
        help='Show debug messages')
    subparsers = parser.add_subparsers()

    add_subcommand(subparsers, writeevents.WriteEvents)

    return parser.parse_args(args)


def add_subcommand(subparsers, cls):
    parser = subparsers.add_parser(cls._command, help=cls._help)
    parser.set_defaults(cls=cls)
    cls.extend_arguments(parser)


def climain():
    main(sys.argv[0], sys.argv[1:])


if __name__ == '__main__':
    climain()
