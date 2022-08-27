import unittest
import logging
from vpplib.vppapi import VPPApi

class TestUDP(unittest.TestCase):
    """ UDP Test Case """

    @classmethod
    def setUpClass(cls):
        cls.logger = logging.getLogger(__name__)
        cls.logger.addHandler(logging.NullHandler())
        cls.logger.debug("{} setUpClass({})".format(__name__.strip('_'), locals()))
        cls.test_name = __name__
        cls.vpp = VPPApi(cls.test_name)
        if not cls.vpp.client:
            cls.logger.critical("The VPP API Client was not created.")
            exit(-1)
        super().setUpClass()

    @classmethod
    def tearDownClass(cls):
        cls.logger.debug("{} tearDownClass({})".format(__name__.strip('_'), locals()))
        del cls.vpp
        super().tearDownClass()

    def setUp(cls):
        cls.logger.debug("\n{} setUp({})".format(__name__.strip('_'), locals()))
        cls.vpp.client.connect(cls.vpp.clientname)
        cls.vpp.client.api.session_enable_disable(is_enable=1)
        cls.loopback_interfaces = []

    def tearDown(cls):
        cls.logger.debug("{} tearDown({})".format(__name__.strip('_'), locals()))
        for i in cls.loopback_interfaces:
            reply = cls.vpp.client.api.delete_loopback(sw_if_index=i)
            cls.assertEquals(reply.retval, 0)

        reply = cls.vpp.client.api.session_enable_disable(is_enable=0)
        cls.assertEquals(reply.retval, 0)
        cls.vpp.client.disconnect()

    def test_aaa_create_loopback(cls):
        cls.logger.debug("{} test_aaa_create_loopback({})".format(__name__.strip('_'), locals()))
        num_loopback_interfaces = 2
        for i in range(0, num_loopback_interfaces):
            create_loopback_reply = cls.vpp.client.api.create_loopback()
            cls.assertEquals(create_loopback_reply.retval, 0)
            cls.logger.info("Loopback Interface: {}".format(create_loopback_reply))
            cls.loopback_interfaces.append(create_loopback_reply.sw_if_index)

####        table_id = 0
####
####        for i in self.lo_interfaces:
####            i.admin_up()
####
####            if table_id != 0:
####                tbl = VppIpTable(self, table_id)
####                tbl.add_vpp_config()
####
####            i.set_table_ip4(table_id)
####            i.config_ip4()
####            table_id += 1
####
####        # Configure namespaces
####        self.vapi.app_namespace_add_del(namespace_id="0",
####                                        sw_if_index=self.loop0.sw_if_index)
####        self.vapi.app_namespace_add_del(namespace_id="1",
####                                        sw_if_index=self.loop1.sw_if_index)
####
####    def tearDown(self):
####        for i in self.lo_interfaces:
####            i.unconfig_ip4()
####            i.set_table_ip4(0)
####            i.admin_down()
####        self.vapi.session_enable_disable(is_enable=0)
####        super(TestUDP, self).tearDown()
####
####    def test_udp_transfer(self):
####        """ UDP echo client/server transfer """
####
####        # Add inter-table routes
####        ip_t01 = VppIpRoute(self, self.loop1.local_ip4, 32,
####                            [VppRoutePath("0.0.0.0",
####                                          0xffffffff,
####                                          nh_table_id=1)])
####        ip_t10 = VppIpRoute(self, self.loop0.local_ip4, 32,
####                            [VppRoutePath("0.0.0.0",
####                                          0xffffffff,
####                                          nh_table_id=0)], table_id=1)
####        ip_t01.add_vpp_config()
####        ip_t10.add_vpp_config()
####
####        # Start builtin server and client
####        uri = "udp://" + self.loop0.local_ip4 + "/1234"
####        error = self.vapi.cli("test echo server appns 0 fifo-size 4 no-echo" +
####                              "uri " + uri)
####        if error:
####            self.logger.critical(error)
####            self.assertNotIn("failed", error)
####
####        error = self.vapi.cli("test echo client mbytes 10 appns 1 " +
####                              "fifo-size 4 no-output test-bytes " +
####                              "syn-timeout 2 no-return uri " + uri)
####        if error:
####            self.logger.critical(error)
####            self.assertNotIn("failed", error)
####
####        self.logger.debug(self.vapi.cli("show session verbose 2"))
####
####        # Delete inter-table routes
####        ip_t01.remove_vpp_config()
####        ip_t10.remove_vpp_config()
####

if __name__ == '__main__':
    unittest.main()
