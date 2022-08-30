import logging
import unittest
import logging
from vpplib.vpp_lo_interface import VppLoInterface


class VppTestCase(unittest.TestCase):
    """This subclass is a base class for VPP test cases that are implemented as
    classes. It provides methods to create and run test case.
    """
    def setUpClass(cls):
        cls.logger = logging.getLogger(__name__)
        cls.logger.addHandler(logging.NullHandler())
        cls.logger.debug("{} setUpClass({})".format(__name__.strip('_'), locals()))

    @classmethod
    def create_loopback_interfaces(cls, count):
        """
        Create loopback interfaces.

        :param count: number of interfaces created.
        :returns: List of created interfaces.
        """
        cls.logger.debug("{} create_loopback_interfaces({})".format(__name__.strip('_'), locals()))
        result = [VppLoInterface(cls) for i in range(count)]
        for intf in result:
            setattr(cls, intf.name, intf)
        cls.lo_interfaces = result
        return result

    @classmethod
    def delete_loopback_interfaces(cls):
        """
        Delete loopback interfaces.

        """
        cls.logger.debug("{} delete_loopback_interface({})".format(__name__.strip('_'), locals()))
        for i in cls.lo_interfaces:
            i.remove_vpp_config()
