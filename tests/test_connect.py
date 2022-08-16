import unittest
import logging
from vpplib.vppapi import VPPApi

class TestVppConnect(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        logging.debug("{} setUpClass({})".format(__name__.strip('_'), locals()))
        cls.test_name = __name__
        cls.vpp = VPPApi(cls.test_name)
        if not cls.vpp.json_files:
            logging.error("The VPP API could not be started, There are no json files.")
            exit(-1)
        return super().setUpClass()

    @classmethod
    def tearDownClass(cls) -> None:
        logging.debug("{} tearDownClass({})".format(__name__.strip('_'), locals()))
        del cls.vpp
        return super().tearDownClass()
    
    def setUp(cls):
        logging.debug("\n{} setUp({})".format(__name__.strip('_'), locals()))
        cls.vpp.connect()

    def tearDown(cls):
        logging.debug("{} tearDown({})".format(__name__.strip('_'), locals()))
        cls.vpp.disconnect()

    def test_upper(cls):
        cls.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(cls):
        cls.assertTrue('FOO'.isupper())
        cls.assertFalse('Foo'.isupper())

    def test_split(cls):
        s = 'hello world'
        cls.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with cls.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()

