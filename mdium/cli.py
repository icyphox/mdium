import argparse
import sys
from mdium import mdium
from mdium import __version__


def main():
    desc = 'Publish your markdown to Medium, from the CLI'
    usage = 'mdium ' + '(init <token> | publish <path>)'
    parser = argparse.ArgumentParser(description=desc, usage=usage)
    parser.add_argument('-v', '--version', action='version', version='{}'.format(__version__))
    sp = parser.add_subparsers(dest='cmd')
    p_init = sp.add_parser('init')
    p_init.add_argument('token')
    p_pub = sp.add_parser('publish')
    p_pub.add_argument('path')

    args = parser.parse_args()

    if len(sys.argv) <= 1:
        parser.print_help()
        sys.exit(1)
    elif args.cmd == 'init':
        if args.token:
            mdium.init(args.token)
        else:
            parser.print_help()
    elif args.cmd == 'publish':
        if args.path:
            mdium.publish(args.path)
        else:
            parser.print_help()
    else:
        parser.print_help()
