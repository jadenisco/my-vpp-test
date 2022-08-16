'''
my-vpp-test.py
'''

import argparse
import logging
import unittest
import vpplib.vppapi

def vpp_main(args):

    verbosity = 0
    if args.debug:
        logging.basicConfig(level=logging.DEBUG)
        verbosity = 2
    logging.debug("{} vpp_main({})".format(__name__.strip('_'), locals()))

    tests = unittest.TestLoader().discover(start_dir='./tests', pattern='test_*.py')
    rc = unittest.TextTestRunner(verbosity=verbosity, buffer=True).run(tests).wasSuccessful()
    
    if rc == True:
        exit(0)
    else:
        exit(1)

if __name__ == '__main__':
    main_parser = argparse.ArgumentParser(
        prog='my-vpp-test',
        description='A test harness for VPP.',
        epilog='See "%(prog)s help COMMAND" for help on a specific command.')
    main_parser.add_argument('--debug', '-d', action='count', help='Print debug output')
    main_args = main_parser.parse_args()
   
    vpp_main(main_args)
