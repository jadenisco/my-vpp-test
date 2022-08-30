'''
my-vpp-test.py
'''

import argparse
import logging
import unittest
import vpplib.vppapi

logger = logging.getLogger("logger")
logger.addHandler(logging.NullHandler())

def vpp_main(args):

    verbosity = 0
    if args.debug:
        if args.debug == 1:
            logging.basicConfig(level=logging.FATAL)
        elif args.debug == 2:
            logging.basicConfig(level=logging.CRITICAL)
        elif args.debug == 3:
            logging.basicConfig(level=logging.ERROR)
        elif args.debug == 4:
            logging.basicConfig(level=logging.WARNING)
        elif args.debug == 5:
            logging.basicConfig(level=logging.INFO)
        else:
            logging.basicConfig(level=logging.DEBUG)
    logging.debug("{} vpp_main({})".format(__name__.strip('_'), locals()))

    if args.verbosity:
        verbosity = args.verbosity
    else:
        verbosity = 0

    tests = unittest.TestLoader().discover(start_dir='./tests', pattern='test_*.py')
    unittest.TextTestRunner(verbosity=verbosity, buffer=True).run(tests).wasSuccessful()

if __name__ == '__main__':
    main_parser = argparse.ArgumentParser(
        prog='my-vpp-test',
        description='A test harness for VPP.',
        epilog='See "%(prog)s help COMMAND" for help on a specific command.')
    main_parser.add_argument('--debug', '-d', action='count', help='debug level, -ddd for multiple levels')
    main_parser.add_argument('--verbosity', '-v', action='count', help='debug level, -vv for multiple levels')
    main_args = main_parser.parse_args()
   
    vpp_main(main_args)
