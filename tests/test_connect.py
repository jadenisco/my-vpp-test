import unittest
import logging

class TestVppConnect(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        # Create data structures needed for the test
        logging.debug("{} setUpClass({})".format(__name__.strip('_'), locals()))
        return super().setUpClass()

    @classmethod
    def tearDownClass(cls) -> None:
        # Delete data structures that were created for the test
        logging.debug("{} tearDownClass({})".format(__name__.strip('_'), locals()))
        return super().tearDownClass()
    
    def setUp(self):
        # Connect to vpp
        logging.debug("\n{} setUp({})".format(__name__.strip('_'), locals()))

    def tearDown(self):
        # Disconnect from vpp
        logging.debug("{} tearDown({})".format(__name__.strip('_'), locals()))

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()

