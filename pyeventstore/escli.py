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
        help='Eventstore host (default: localhost)')
    subparsers = parser.add_subparsers()

    add_subcommand(subparsers, writeevents.WriteEvents)

    return parser.parse_args(args)


def add_subcommand(subparsers, cls):
    parser = subparsers.add_parser(cls._command, help=cls._help)
    parser.set_defaults(cls=cls)
    cls.extend_arguments(parser)


if __name__ == '__main__':
    main(sys.argv[0], sys.argv[1:])
