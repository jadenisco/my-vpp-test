import unittest
import logging
from vpplib.vppapi import VPPApi

class TestVppConnect(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.logger = logging.getLogger(__name__)
        cls.logger.addHandler(logging.NullHandler())
        cls.logger.debug("{} setUpClass({})".format(__name__.strip('_'), locals()))
        cls.test_name = __name__
        cls.vpp = VPPApi(cls.test_name)
        if not cls.vpp.client:
            cls.logger.critical("The VPP API Client was not created.")
            exit(-1)
        cls.vpp.connect()
        return super().setUpClass()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.logger.debug("{} tearDownClass({})".format(__name__.strip('_'), locals()))
        cls.vpp.disconnect()
        del cls.vpp
        return super().tearDownClass()
    
    def setUp(cls):
        # Setup for individual tests
        cls.logger.debug("\n{} setUp({})".format(__name__.strip('_'), locals()))

    def tearDown(cls):
        cls.logger.debug("{} tearDown({})".format(__name__.strip('_'), locals()))

    def test_show_version(cls):
        cls.logger.debug("{} test_show_version({})".format(__name__.strip('_'), locals()))
        v = cls.vpp.client.api.show_version()
        cls.logger.info("\nVPP Version: {}".format(v.version))

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
