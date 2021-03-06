from base import Base as BaseTestCase
from roletester.actions.glance import image_create
from roletester.actions.glance import image_wait_for_status
from roletester.actions.nova import server_create
from roletester.actions.nova import server_delete
from roletester.actions.nova import server_wait_for_status
from roletester.actions.neutron import network_create
from roletester.actions.neutron import network_show
from roletester.actions.neutron import network_delete
from roletester.actions.neutron import subnet_create
from roletester.actions.neutron import subnet_show
from roletester.actions.neutron import subnet_delete
from roletester.actions.neutron import subnet_update
from roletester.actions.neutron import router_create
from roletester.actions.neutron import router_show
from roletester.actions.neutron import router_add_interface
from roletester.actions.neutron import router_remove_interface
from roletester.actions.neutron import router_update
from roletester.actions.neutron import router_delete
from roletester.actions.neutron import security_group_create
from roletester.actions.neutron import security_group_show
from roletester.actions.neutron import security_group_add_to_server
from roletester.actions.neutron import security_group_remove_from_server
from roletester.actions.neutron import security_group_rule_create
from roletester.actions.neutron import security_group_delete
from roletester.actions.neutron import security_group_rule_delete
from roletester.actions.neutron import floatingip_associate
from roletester.actions.neutron import floatingip_create
from roletester.actions.neutron import floatingip_delete
from roletester.actions.neutron import floatingip_disassociate
from roletester.actions.neutron import floatingip_show
from roletester.actions.neutron import port_create
from roletester.exc import KeystoneUnauthorized
from roletester.exc import NeutronForbidden
from neutronclient.common.exceptions import NetworkNotFoundClient
from roletester.exc import NeutronNotFound
from roletester.scenario import ScenarioFactory as Factory
from roletester.utils import randomname

from roletester.log import logging

logger = logging.getLogger("roletester.neutron")


class SampleFactory(Factory):

    _ACTIONS = [
        network_create,
        network_show,
        subnet_create,
        subnet_show,
        server_create,
        server_wait_for_status,
        security_group_create,
        security_group_show,
        security_group_rule_create,
        security_group_add_to_server,
        security_group_remove_from_server,
        security_group_rule_delete,
        security_group_delete,
        server_delete,
        router_create,
        router_show,
        router_add_interface,
        router_remove_interface,
        router_delete,
        subnet_delete,
        network_delete
    ]

    NETWORK_CREATE = 0
    NETWORK_SHOW = 1
    SUBNET_CREATE = 2
    SUBNET_SHOW = 3
    SERVER_CREATE = 4
    SERVER_WAIT = 5
    SECURITY_GROUP_CREATE = 6
    SECURITY_GROUP_SHOW = 7
    SECURITY_GROUP_RULE_CREATE = 8
    SECURITY_GROUP_ADD_TO_SERVER = 9
    SECURITY_GROUP_REMOVE_FROM_SERVER = 10
    SECURITY_GROUP_RULE_DELETE = 11
    SECURITY_GROUP_DELETE = 12
    SERVER_DELETE = 13
    ROUTER_CREATE = 14
    ROUTER_SHOW = 15
    ROUTER_ADD_INTERFACE = 16
    ROUTER_REMOVE_INTERFACE = 17
    ROUTER_DELETE = 18
    SUBNET_DELETE = 19
    NETWORK_DELETE = 20


class SecgroupAddFactory(Factory):

    _ACTIONS = [
        network_create,
        network_show,
        subnet_create,
        subnet_show,
        server_create,
        server_wait_for_status,
        security_group_create,
        security_group_show,
        security_group_rule_create,
        security_group_add_to_server,
    ]

    NETWORK_CREATE = 0
    NETWORK_SHOW = 1
    SUBNET_CREATE = 2
    SUBNET_SHOW = 3
    SERVER_CREATE = 4
    SERVER_WAIT = 5
    SECURITY_GROUP_CREATE = 6
    SECURITY_GROUP_SHOW = 7
    SECURITY_GROUP_RULE_CREATE = 8
    SECURITY_GROUP_ADD_TO_SERVER = 9


class AddInterfaceFactory(Factory):

    _ACTIONS = [
        network_create,
        subnet_create,
        server_create,
        server_wait_for_status,
        security_group_create,
        security_group_rule_create,
        security_group_add_to_server,
        security_group_remove_from_server,
        security_group_rule_delete,
        security_group_delete,
        server_delete,
        router_create,
        router_show,
        router_add_interface,

    ]

    NETWORK_CREATE = 0
    SUBNET_CREATE = 1
    SERVER_CREATE = 2
    SERVER_WAIT = 3
    SECURITY_GROUP_CREATE = 4
    SECURITY_GROUP_RULE_CREATE = 5
    SECURITY_GROUP_ADD_TO_SERVER = 6
    SECURITY_GROUP_REMOVE_FROM_SERVER = 7
    SECURITY_GROUP_RULE_DELETE = 8
    SECURITY_GROUP_DELETE = 9
    SERVER_DELETE = 10
    ROUTER_CREATE = 11
    ROUTER_SHOW = 12
    ROUTER_ADD_INTERFACE = 13


class RouterDeleteFactory(Factory):

    _ACTIONS = [
        router_create,
        router_delete
    ]

    ROUTER_CREATE = 0
    ROUTER_DELETE = 1


class RouterUpdateFactory(Factory):

    _ACTIONS = [
        router_create,
        router_update
    ]

    ROUTER_CREATE = 0
    ROUTER_UPDATE = 1


class RouterCreateFactory(Factory):

    _ACTIONS = [
        router_create
    ]

    ROUTER_CREATE = 0


class SubnetDeleteFactory(Factory):

    _ACTIONS = [
        network_create,
        subnet_create,
        subnet_delete
    ]

    NETWORK_CREATE = 0
    SUBNET_CREATE = 1
    SUBNET_DELETE = 2


class SubnetUpdateFactory(Factory):

    _ACTIONS = [
        network_create,
        subnet_create,
        subnet_update
    ]

    NETWORK_CREATE = 0
    SUBNET_CREATE = 1
    SUBNET_UPDATE = 2


class NetworkDeleteFactory(Factory):

    _ACTIONS = [
        network_create,
        network_delete
    ]

    NETWORK_CREATE = 0
    NETWORK_DELETE = 1


class NetworkCreateFactory(Factory):

    _ACTIONS = [
        network_create,
    ]

    NETWORK_CREATE = 0


class SubnetCreateFactory(Factory):

    _ACTIONS = [
        network_create,
        subnet_create
    ]

    NETWORK_CREATE = 0
    SUBNET_CREATE = 1


class FloatingIPFactory(Factory):

    _ACTIONS = [
        network_create,
        subnet_create,
        port_create,
        router_create,
        router_add_interface,
        floatingip_create,
        floatingip_show,
        floatingip_associate,
        floatingip_disassociate,
        floatingip_delete,
    ]

    NETWORK_CREATE = 0
    SUBNET_CREATE = 1
    PORT_CREATE = 2
    ROUTER_CREATE = 3
    ROUTER_ADD_INTERFACE = 4
    FLOATINGIP_CREATE = 5
    FLOATINGIP_SHOW = 6
    FLOATINGIP_ASSOCIATE = 7
    FLOATINGIP_DISASSOCIATE = 8
    FLOATINGIP_DELETE = 9



class TestSample(BaseTestCase):

    name = 'scratch'
    flavor = '1'
    # image_file = '/home/chalupaul/cirros-0.3.4-x86_64-disk.img'
    image_file = '/Users/egle/Downloads/cirros-0.3.4-x86_64-disk.img'

    project = randomname()

    def setUp(self):
        super(TestSample, self).setUp()
        try:
            n = self.km.admin_client_manager.get_neutron()
            networks = n.list_networks()['networks']
            public_network = [x['id']
                              for x in networks
                              if x['router:external'] is True][0]
        except IndexError:
            err_str = "No public network found to create floating ips from."
            raise NetworkNotFoundClient(message=err_str)
        self.context["external_network_id"] = public_network

        kwargs = {
            'name': "glance test image",
            'disk_format': 'qcow2',
            'container_format': 'bare',
            'is_public': 'public'
        }
        try:
            image_id = self.context['image_id']
        except Exception:
            logger.info("No image_id found, creating image")

            glance = self.km.admin_client_manager.get_glance()
            images = glance.images.list()
            for img in images:
                if img.name == "glance test image" and img.status == "active" and img.visibility == 'public':
                    logger.info("found image with image id: %s" %img.id)
                    self.context.update(image_id=img.id)
            if 'image_id' in self.context:
                logger.info("image found:")
                logger.info("image_id in context: %s" %self.context['image_id'])
            else:
                logger.info("creating new image.")
                image_create(self.km.admin_client_manager, self.context, self.image_file)
                image_id = self.context['image_id']

    def test_cloud_admin_all(self):
        cloud_admin = self.km.find_user_credentials(
            'Default', self.project, 'cloud-admin'
        )

        SampleFactory(cloud_admin) \
            .produce() \
            .run(context=self.context)

    def test_cloud_admin_floatingip(self):
        cloud_admin = self.km.find_user_credentials(
            'Default', self.project, 'cloud-admin'
        )
        FloatingIPFactory(cloud_admin) \
            .produce() \
            .run(context=self.context)

    def test_cloud_admin_same_domain_different_user(self):
        creator = self.km.find_user_credentials(
            'Default', self.project, 'admin'
        )
        user1 = self.km.find_user_credentials(
            'Default', self.project, 'cloud-admin'
        )
        cloud_admin = self.km.find_user_credentials(
            'Default', self.project, 'cloud-admin'
        )

        SampleFactory(cloud_admin) \
            .set(SampleFactory.NETWORK_CREATE,
                 clients=user1) \
            .set(SampleFactory.SUBNET_CREATE,
                 clients=user1) \
            .set(SampleFactory.SERVER_CREATE,
                 clients=user1) \
            .set(SampleFactory.SERVER_WAIT,
                 clients=user1) \
            .set(SampleFactory.SECURITY_GROUP_CREATE,
                 clients=user1) \
            .set(SampleFactory.SECURITY_GROUP_RULE_CREATE,
                 clients=user1) \
            .set(SampleFactory.SERVER_DELETE,
                 clients=user1) \
            .set(SampleFactory.ROUTER_CREATE,
                 clients=user1) \
            .set(SampleFactory.ROUTER_ADD_INTERFACE,
                 clients=user1) \
            .produce() \
            .run(context=self.context)

    def test_cloud_admin_same_domain_different_user_floatingip(self):
        user1 = self.km.find_user_credentials(
            'Default', self.project, 'cloud-admin'
        )
        cloud_admin = self.km.find_user_credentials(
            'Default', self.project, 'cloud-admin'
        )

        FloatingIPFactory(cloud_admin) \
            .set(FloatingIPFactory.NETWORK_CREATE,
                 clients=user1) \
            .set(FloatingIPFactory.SUBNET_CREATE,
                 clients=user1) \
            .set(FloatingIPFactory.PORT_CREATE,
                 clients=user1) \
            .set(FloatingIPFactory.ROUTER_CREATE,
                 clients=user1) \
            .set(FloatingIPFactory.ROUTER_ADD_INTERFACE,
                 clients=user1) \
            .set(FloatingIPFactory.FLOATINGIP_CREATE,
                 clients=user1) \
            .produce() \
            .run(context=self.context)

    def test_bu_admin_all(self):
        bu_admin = self.km.find_user_credentials(
            'Default', self.project, 'bu-admin'
        )
        cloud_admin = self.km.find_user_credentials(
            'Default', self.project, 'cloud-admin'
        )

        SampleFactory(bu_admin) \
            .set(SampleFactory.NETWORK_CREATE, clients=cloud_admin) \
            .set(SampleFactory.NETWORK_SHOW, clients=cloud_admin) \
            .set(SampleFactory.SUBNET_CREATE, clients=cloud_admin) \
            .set(SampleFactory.SECURITY_GROUP_CREATE, clients=cloud_admin) \
            .set(SampleFactory.SECURITY_GROUP_RULE_CREATE, clients=cloud_admin) \
            .set(SampleFactory.SECURITY_GROUP_RULE_DELETE, clients=cloud_admin) \
            .set(SampleFactory.SECURITY_GROUP_DELETE, clients=cloud_admin) \
            .set(SampleFactory.ROUTER_CREATE, clients=cloud_admin) \
            .set(SampleFactory.ROUTER_ADD_INTERFACE, clients=cloud_admin) \
            .set(SampleFactory.ROUTER_REMOVE_INTERFACE, clients=cloud_admin) \
            .set(SampleFactory.ROUTER_DELETE, clients=cloud_admin) \
            .set(SampleFactory.SUBNET_DELETE, clients=cloud_admin) \
            .set(SampleFactory.NETWORK_DELETE, clients=cloud_admin) \
            .produce() \
            .run(context=self.context)

    def test_bu_admin_floatingip(self):
        cloud_admin = self.km.find_user_credentials(
            'Default', self.project, 'cloud-admin'
        )
        bu_admin = self.km.find_user_credentials(
            'Default', self.project, 'bu-admin'
        )
        FloatingIPFactory(bu_admin) \
            .set(FloatingIPFactory.NETWORK_CREATE, clients=cloud_admin) \
            .set(FloatingIPFactory.SUBNET_CREATE, clients=cloud_admin) \
            .set(FloatingIPFactory.ROUTER_CREATE, clients=cloud_admin) \
            .set(FloatingIPFactory.ROUTER_ADD_INTERFACE, clients=cloud_admin) \
            .set(FloatingIPFactory.FLOATINGIP_DELETE, clients=cloud_admin) \
            .produce() \
            .run(context=self.context)

    def test_bu_admin_same_domain_different_user(self):
        creator = self.km.find_user_credentials(
            'Default', self.project, 'cloud-admin'
        )
        user1 = self.km.find_user_credentials(
            'Default', self.project, 'cloud-admin'
        )
        bu_admin = self.km.find_user_credentials(
            'Default', self.project, 'bu-admin'
        )

        SampleFactory(bu_admin) \
            .set(SampleFactory.NETWORK_CREATE,
                 clients=user1) \
            .set(SampleFactory.SUBNET_CREATE,
                 clients=user1) \
            .set(SampleFactory.SERVER_CREATE,
                 clients=user1) \
            .set(SampleFactory.SERVER_WAIT,
                 clients=user1) \
            .set(SampleFactory.SECURITY_GROUP_CREATE,
                 clients=user1) \
            .set(SampleFactory.SECURITY_GROUP_RULE_CREATE, clients=user1) \
            .set(SampleFactory.SECURITY_GROUP_RULE_DELETE, clients=user1) \
            .set(SampleFactory.SECURITY_GROUP_REMOVE_FROM_SERVER, clients=user1) \
            .set(SampleFactory.SECURITY_GROUP_DELETE, clients=user1) \
            .set(SampleFactory.SERVER_DELETE,
                 clients=user1) \
            .set(SampleFactory.ROUTER_CREATE,
                 clients=user1) \
            .set(SampleFactory.ROUTER_ADD_INTERFACE,
                 clients=user1) \
            .set(SampleFactory.ROUTER_REMOVE_INTERFACE, clients=user1) \
            .set(SampleFactory.ROUTER_DELETE, clients=user1) \
            .set(SampleFactory.SUBNET_DELETE, clients=user1) \
            .set(SampleFactory.NETWORK_DELETE, clients=user1) \
            .produce() \
            .run(context=self.context)

    def test_bu_admin_same_domain_different_user_floatingip(self):
        user1 = self.km.find_user_credentials(
            'Default', self.project, 'cloud-admin'
        )
        bu_admin = self.km.find_user_credentials(
            'Default', self.project, 'bu-admin'
        )

        FloatingIPFactory(bu_admin) \
            .set(FloatingIPFactory.NETWORK_CREATE,
                 clients=user1) \
            .set(FloatingIPFactory.SUBNET_CREATE,
                 clients=user1) \
            .set(FloatingIPFactory.PORT_CREATE,
                 clients=user1) \
            .set(FloatingIPFactory.ROUTER_CREATE,
                 clients=user1) \
            .set(FloatingIPFactory.ROUTER_ADD_INTERFACE,
                 clients=user1) \
            .set(FloatingIPFactory.FLOATINGIP_CREATE,
                 clients=user1) \
            .set(FloatingIPFactory.FLOATINGIP_DELETE, \
                 clients=user1) \
            .produce() \
            .run(context=self.context)

    def test_bu_admin_different_domain_different_user_floatingip(self):
        user1 = self.km.find_user_credentials(
            'Default', self.project, 'cloud-admin'
        )
        bu_admin = self.km.find_user_credentials(
            'Domain2', self.project, 'bu-admin'
        )

        FloatingIPFactory(bu_admin) \
            .set(FloatingIPFactory.NETWORK_CREATE,
                 clients=user1) \
            .set(FloatingIPFactory.SUBNET_CREATE,
                 clients=user1) \
            .set(FloatingIPFactory.PORT_CREATE,
                 clients=user1) \
            .set(FloatingIPFactory.ROUTER_CREATE,
                 clients=user1) \
            .set(FloatingIPFactory.ROUTER_ADD_INTERFACE,
                 clients=user1) \
            .set(FloatingIPFactory.FLOATINGIP_CREATE,
                 clients=user1) \
            .set(FloatingIPFactory.FLOATINGIP_SHOW,
                 expected_exceptions=[KeystoneUnauthorized]) \
            .set(FloatingIPFactory.FLOATINGIP_ASSOCIATE,
                 clients=user1) \
            .set(FloatingIPFactory.FLOATINGIP_DISASSOCIATE,
                 expected_exceptions=[KeystoneUnauthorized]) \
            .set(FloatingIPFactory.FLOATINGIP_DELETE,
                 expected_exceptions=[KeystoneUnauthorized]) \
            .produce() \
            .run(context=self.context)

    def test_bu_admin_different_domain_different_user_secgroup_add_to_server(self):
        creator = self.km.find_user_credentials(
            'Default', self.project, 'cloud-admin'
        )
        user1 = self.km.find_user_credentials(
            'Default', self.project, 'bu-admin'
        )
        bu_admin = self.km.find_user_credentials(
            'Domain2', self.project, 'bu-admin'
        )

        SecgroupAddFactory(bu_admin) \
            .set(SecgroupAddFactory.NETWORK_CREATE,
                 clients=creator) \
            .set(SecgroupAddFactory.NETWORK_SHOW,
                 expected_exceptions = [KeystoneUnauthorized]) \
            .set(SecgroupAddFactory.SUBNET_CREATE,
                 clients=creator) \
            .set(SecgroupAddFactory.SUBNET_SHOW,
                 expected_exceptions = [KeystoneUnauthorized]) \
            .set(SecgroupAddFactory.SERVER_CREATE,
                 clients=user1) \
            .set(SecgroupAddFactory.SERVER_WAIT,
                 clients=user1) \
            .set(SecgroupAddFactory.SECURITY_GROUP_CREATE,
                 clients=creator) \
            .set(SecgroupAddFactory.SECURITY_GROUP_SHOW,
                 expected_exceptions = [KeystoneUnauthorized]) \
            .set(SecgroupAddFactory.SECURITY_GROUP_RULE_CREATE,
                 clients=creator) \
            .set(SecgroupAddFactory.SECURITY_GROUP_ADD_TO_SERVER,
                 expected_exceptions = [KeystoneUnauthorized]) \
            .produce() \
            .run(context=self.context)

    def test_bu_admin_different_domain_different_user_add_interface_to_server(self):
        creator = self.km.find_user_credentials(
            'Default', self.project, 'cloud-admin'
        )
        user1 = self.km.find_user_credentials(
            'Default', self.project, 'cloud-admin'
        )
        bu_admin = self.km.find_user_credentials(
            'Domain2', self.project, 'bu-admin'
        )

        AddInterfaceFactory(bu_admin) \
            .set(AddInterfaceFactory.NETWORK_CREATE,
                 clients=user1) \
            .set(AddInterfaceFactory.SUBNET_CREATE,
                 clients=user1) \
            .set(AddInterfaceFactory.SERVER_CREATE,
                 clients=user1) \
            .set(AddInterfaceFactory.SERVER_WAIT,
                 clients=user1) \
            .set(AddInterfaceFactory.SECURITY_GROUP_CREATE,
                 clients=user1) \
            .set(AddInterfaceFactory.SECURITY_GROUP_RULE_CREATE,
                 clients=user1) \
            .set(AddInterfaceFactory.SECURITY_GROUP_ADD_TO_SERVER,
                 clients=user1) \
            .set(AddInterfaceFactory.SECURITY_GROUP_REMOVE_FROM_SERVER,
                 expected_exceptions=[KeystoneUnauthorized]) \
            .set(AddInterfaceFactory.SECURITY_GROUP_RULE_DELETE,
                 expected_exceptions=[KeystoneUnauthorized]) \
            .set(AddInterfaceFactory.SECURITY_GROUP_DELETE,
                 expected_exceptions=[KeystoneUnauthorized]) \
            .set(AddInterfaceFactory.SERVER_DELETE,
                 clients=user1) \
            .set(AddInterfaceFactory.ROUTER_CREATE,
                 clients=user1) \
            .set(AddInterfaceFactory.ROUTER_SHOW,
                 expected_exceptions=[KeystoneUnauthorized]) \
            .set(AddInterfaceFactory.ROUTER_ADD_INTERFACE,
                 expected_exceptions=[KeystoneUnauthorized]) \
            .produce() \
            .run(context=self.context)

    def test_bu_admin_different_domain_different_user_subnet_delete(self):
        user1 = self.km.find_user_credentials(
            'Default', self.project, 'cloud-admin'
        )
        bu_admin = self.km.find_user_credentials(
            'Domain2', self.project, 'bu-admin'
        )

        SubnetDeleteFactory(user1) \
            .set(SubnetDeleteFactory.SUBNET_DELETE, clients=bu_admin,
                 expected_exceptions=[KeystoneUnauthorized]) \
            .produce() \
            .run(context=self.context)

    def test_bu_admin_different_domain_different_user_network_delete(self):
        user1 = self.km.find_user_credentials(
            'Default', self.project, 'cloud-admin'
        )
        bu_admin = self.km.find_user_credentials(
            'Domain2', self.project, 'bu-admin'
        )

        NetworkDeleteFactory(user1) \
            .set(NetworkDeleteFactory.NETWORK_DELETE, clients=bu_admin,
                 expected_exceptions=[KeystoneUnauthorized]) \
            .produce() \
            .run(context=self.context)

    def test_cloud_admin_subnet_update(self):

        cloud_admin = self.km.find_user_credentials(
            'Default', self.project, 'cloud-admin'
        )
        SubnetUpdateFactory(cloud_admin) \
            .produce() \
            .run(context=self.context)

#todo: retest
    def test_bu_admin_subnet_update(self):
        cloud_admin = self.km.find_user_credentials(
            'Default', self.project, 'cloud-admin'
        )
        bu_admin = self.km.find_user_credentials(
            'Default', self.project, 'bu-admin'
        )
        SubnetUpdateFactory(cloud_admin) \
            .set(SubnetUpdateFactory.SUBNET_UPDATE, clients=bu_admin, expected_exceptions=[NeutronForbidden]) \
            .produce() \
            .run(context=self.context)

    def test_cloud_admin_router_update(self):

        cloud_admin = self.km.find_user_credentials(
            'Default', self.project, 'cloud-admin'
        )
        RouterUpdateFactory(cloud_admin) \
            .produce() \
            .run(context=self.context)

    def test_bu_admin_router_update(self):
        cloud_admin = self.km.find_user_credentials(
            'Default', self.project, 'cloud-admin'
        )
        bu_admin = self.km.find_user_credentials(
            'Default', self.project, 'bu-admin'
        )
        RouterUpdateFactory(cloud_admin) \
            .set(RouterUpdateFactory.ROUTER_UPDATE, clients=bu_admin, expected_exceptions=[NeutronForbidden]) \
            .produce() \
            .run(context=self.context)

# bu-user
#get subnet, get subnet pool
#get network details
    #todo: retest
    def test_bu_user(self):

        user1 = self.km.find_user_credentials(
            'Default', self.project, 'bu-user'
        )
        cloud_admin = self.km.find_user_credentials(
            'Default', self.project, 'cloud-admin'
        )

        SampleFactory(cloud_admin) \
            .set(SampleFactory.NETWORK_SHOW, clients=user1, expected_exceptions=[NeutronNotFound]) \
            .set(SampleFactory.SUBNET_SHOW, clients=user1) \
            .set(SampleFactory.SERVER_WAIT, clients=user1) \
            .set(SampleFactory.SECURITY_GROUP_SHOW, clients=user1) \
            .produce() \
            .run(context=self.context)

    def test_bu_user_network_create(self):

        user1 = self.km.find_user_credentials(
            'Default', self.project, 'bu-user'
        )

        NetworkCreateFactory(user1) \
            .set(NetworkCreateFactory.NETWORK_CREATE, expected_exceptions=[NeutronForbidden]) \
            .produce() \
            .run(context=self.context)

    def test_bu_user_subnet_create(self):

        user1 = self.km.find_user_credentials(
            'Default', self.project, 'bu-user'
        )

        cloud_admin = self.km.find_user_credentials(
            'Default', self.project, 'cloud-admin'
        )
        SubnetCreateFactory(user1) \
            .set(SubnetCreateFactory.NETWORK_CREATE, clients=cloud_admin) \
            .set(SubnetCreateFactory.SUBNET_CREATE, expected_exceptions=[NeutronForbidden]) \
            .produce() \
            .run(context=self.context)

    def test_bu_user_router_create(self):

        user1 = self.km.find_user_credentials(
            'Default', self.project, 'bu-user'
        )
        RouterCreateFactory(user1) \
            .set(RouterCreateFactory.ROUTER_CREATE, expected_exceptions=[NeutronForbidden]) \
            .produce() \
            .run(context=self.context)

    def test_bu_user_network_delete(self):

        user1 = self.km.find_user_credentials(
            'Default', self.project, 'bu-user'
        )
        cloud_admin = self.km.find_user_credentials(
            'Default', self.project, 'cloud-admin'
        )
        NetworkDeleteFactory(cloud_admin) \
            .set(NetworkDeleteFactory.NETWORK_DELETE, clients=user1, expected_exceptions=[NeutronNotFound]) \
            .produce() \
            .run(context=self.context)

    def test_bu_user_subnet_delete(self):

        user1 = self.km.find_user_credentials(
            'Default', self.project, 'bu-user'
        )

        cloud_admin = self.km.find_user_credentials(
            'Default', self.project, 'cloud-admin'
        )
        SubnetDeleteFactory(cloud_admin) \
            .set(SubnetDeleteFactory.SUBNET_DELETE, clients=user1, expected_exceptions=[NeutronNotFound]) \
            .produce() \
            .run(context=self.context)

    def test_bu_user_router_delete(self):

        user1 = self.km.find_user_credentials(
            'Default', self.project, 'bu-user'
        )

        cloud_admin = self.km.find_user_credentials(
            'Default', self.project, 'cloud-admin'
        )
        RouterDeleteFactory(cloud_admin) \
            .set(RouterDeleteFactory.ROUTER_DELETE, clients=user1, expected_exceptions=[NeutronNotFound]) \
            .produce() \
            .run(context=self.context)

    def test_bu_user_subnet_update(self):

        user1 = self.km.find_user_credentials(
            'Default', self.project, 'bu-user'
        )

        cloud_admin = self.km.find_user_credentials(
            'Default', self.project, 'cloud-admin'
        )
        SubnetUpdateFactory(user1) \
            .set(SubnetUpdateFactory.NETWORK_CREATE, clients=cloud_admin) \
            .set(SubnetUpdateFactory.SUBNET_CREATE, clients=cloud_admin) \
            .set(SubnetUpdateFactory.SUBNET_UPDATE, expected_exceptions=[NeutronForbidden]) \
            .produce() \
            .run(context=self.context)

    def test_bu_user_router_update(self):

        user1 = self.km.find_user_credentials(
            'Default', self.project, 'bu-user'
        )

        cloud_admin = self.km.find_user_credentials(
            'Default', self.project, 'cloud-admin'
        )
        RouterUpdateFactory(user1) \
            .set(RouterUpdateFactory.ROUTER_CREATE, clients=cloud_admin) \
            .set(RouterUpdateFactory.ROUTER_UPDATE, expected_exceptions=[NeutronForbidden]) \
            .produce() \
            .run(context=self.context)

    def test_bu_user_get_floatingip(self):
        user1 = self.km.find_user_credentials(
            'Default', self.project, 'bu-user'
        )
        cloud_admin = self.km.find_user_credentials(
            'Default', self.project, 'cloud-admin'
        )

        FloatingIPFactory(cloud_admin) \
            .set(FloatingIPFactory.FLOATINGIP_SHOW,
                 clients=user1) \
            .set(FloatingIPFactory.FLOATINGIP_ASSOCIATE,
                 clients=user1, expected_exceptions=[NeutronForbidden]) \
            .set(FloatingIPFactory.FLOATINGIP_DISASSOCIATE,
                 clients=user1, expected_exceptions=[NeutronForbidden]) \
            .set(FloatingIPFactory.FLOATINGIP_DELETE, clients=user1,
                 expected_exceptions=[NeutronNotFound]) \
            .produce() \
            .run(context=self.context)

    #todo: re-test, seems broken
    def test_bu_user_get_floatingip_diff_domain(self):
        cloud_admin = self.km.find_user_credentials(
            'Default', self.project, 'cloud-admin'
        )

        user1 = self.km.find_user_credentials(
            'Domain2', self.project, 'bu-user'
        )

        FloatingIPFactory(cloud_admin) \
            .set(FloatingIPFactory.FLOATINGIP_SHOW,
                 clients=user1, expected_exceptions=[KeystoneUnauthorized]) \
            .set(FloatingIPFactory.FLOATINGIP_ASSOCIATE,
                 clients=user1, expected_exceptions=[KeystoneUnauthorized]) \
            .set(FloatingIPFactory.FLOATINGIP_DISASSOCIATE,
                 clients=user1, expected_exceptions=[KeystoneUnauthorized]) \
            .set(FloatingIPFactory.FLOATINGIP_DELETE, clients=user1,
                 expected_exceptions=[KeystoneUnauthorized]) \
            .produce() \
            .run(context=self.context)

#bu-brt
#todo: retest
    def test_bu_brt(self):

        user1 = self.km.find_user_credentials(
            'Default', self.project, 'bu-brt'
        )
        cloud_admin = self.km.find_user_credentials(
            'Default', self.project, 'cloud-admin'
        )

        SampleFactory(cloud_admin) \
            .set(SampleFactory.NETWORK_CREATE) \
            .set(SampleFactory.NETWORK_SHOW, clients=user1) \
            .set(SampleFactory.SUBNET_CREATE) \
            .set(SampleFactory.SUBNET_SHOW, clients=user1) \
            .set(SampleFactory.SERVER_CREATE) \
            .set(SampleFactory.SERVER_WAIT,
                 clients=user1) \
            .set(SampleFactory.SECURITY_GROUP_CREATE) \
            .set(SampleFactory.SECURITY_GROUP_SHOW, clients=user1) \
            .set(SampleFactory.SECURITY_GROUP_RULE_CREATE) \
            .set(SampleFactory.SERVER_DELETE) \
            .set(SampleFactory.ROUTER_CREATE) \
            .set(SampleFactory.ROUTER_SHOW, clients=user1) \
            .set(SampleFactory.ROUTER_ADD_INTERFACE) \
            .produce() \
            .run(context=self.context)

    def test_bu_brt_network_create(self):

        user1 = self.km.find_user_credentials(
            'Default', self.project, 'bu-brt'
        )

        NetworkCreateFactory(user1) \
            .set(NetworkCreateFactory.NETWORK_CREATE, expected_exceptions=[NeutronForbidden]) \
            .produce() \
            .run(context=self.context)

    def test_bu_brt_subnet_create(self):

        user1 = self.km.find_user_credentials(
            'Default', self.project, 'bu-brt'
        )

        cloud_admin = self.km.find_user_credentials(
            'Default', self.project, 'cloud-admin'
        )
        SubnetCreateFactory(user1) \
            .set(SubnetCreateFactory.NETWORK_CREATE, clients=cloud_admin) \
            .set(SubnetCreateFactory.SUBNET_CREATE, expected_exceptions=[NeutronForbidden]) \
            .produce() \
            .run(context=self.context)

    def test_bu_brt_router_create(self):

        user1 = self.km.find_user_credentials(
            'Default', self.project, 'bu-brt'
        )
        RouterCreateFactory(user1) \
            .set(RouterCreateFactory.ROUTER_CREATE, expected_exceptions=[NeutronForbidden]) \
            .produce() \
            .run(context=self.context)

    def test_bu_brt_network_delete(self):

        user1 = self.km.find_user_credentials(
            'Default', self.project, 'bu-brt'
        )
        cloud_admin = self.km.find_user_credentials(
            'Default', self.project, 'cloud-admin'
        )
        NetworkDeleteFactory(cloud_admin) \
            .set(NetworkDeleteFactory.NETWORK_DELETE, clients=user1, expected_exceptions=[NeutronNotFound]) \
            .produce() \
            .run(context=self.context)

    def test_bu_brt_subnet_delete(self):

        user1 = self.km.find_user_credentials(
            'Default', self.project, 'bu-brt'
        )

        cloud_admin = self.km.find_user_credentials(
            'Default', self.project, 'cloud-admin'
        )
        SubnetDeleteFactory(cloud_admin) \
            .set(SubnetDeleteFactory.SUBNET_DELETE, clients=user1, expected_exceptions=[NeutronNotFound]) \
            .produce() \
            .run(context=self.context)

    def test_bu_brt_router_delete(self):

        user1 = self.km.find_user_credentials(
            'Default', self.project, 'bu-brt'
        )

        cloud_admin = self.km.find_user_credentials(
            'Default', self.project, 'cloud-admin'
        )
        RouterDeleteFactory(cloud_admin) \
            .set(RouterDeleteFactory.ROUTER_DELETE, clients=user1, expected_exceptions=[NeutronNotFound]) \
            .produce() \
            .run(context=self.context)

    def test_bu_brt_subnet_update(self):

        user1 = self.km.find_user_credentials(
            'Default', self.project, 'bu-brt'
        )

        cloud_admin = self.km.find_user_credentials(
            'Default', self.project, 'cloud-admin'
        )
        SubnetUpdateFactory(user1) \
            .set(SubnetUpdateFactory.NETWORK_CREATE, clients=cloud_admin) \
            .set(SubnetUpdateFactory.SUBNET_CREATE, clients=cloud_admin) \
            .set(SubnetUpdateFactory.SUBNET_UPDATE, expected_exceptions=[NeutronForbidden]) \
            .produce() \
            .run(context=self.context)

    def test_bu_brt_router_update(self):

        user1 = self.km.find_user_credentials(
            'Default', self.project, 'bu-brt'
        )

        cloud_admin = self.km.find_user_credentials(
            'Default', self.project, 'cloud-admin'
        )
        RouterUpdateFactory(user1) \
            .set(RouterUpdateFactory.ROUTER_CREATE, clients=cloud_admin) \
            .set(RouterUpdateFactory.ROUTER_UPDATE, expected_exceptions=[NeutronForbidden]) \
            .produce() \
            .run(context=self.context)

    def test_bu_brt_get_floatingip(self):
        user1 = self.km.find_user_credentials(
            'Default', self.project, 'bu-brt'
        )
        cloud_admin = self.km.find_user_credentials(
            'Default', self.project, 'cloud-admin'
        )

        FloatingIPFactory(cloud_admin) \
            .set(FloatingIPFactory.FLOATINGIP_SHOW,
                 clients=user1) \
            .set(FloatingIPFactory.FLOATINGIP_ASSOCIATE,
                 clients=user1, expected_exceptions=[NeutronForbidden]) \
            .set(FloatingIPFactory.FLOATINGIP_DISASSOCIATE,
                 clients=user1, expected_exceptions=[NeutronForbidden]) \
            .set(FloatingIPFactory.FLOATINGIP_DELETE, clients=user1,
                 expected_exceptions=[NeutronNotFound]) \
            .produce() \
            .run(context=self.context)

    def test_bu_brt_get_floatingip_diff_domain(self):
        cloud_admin = self.km.find_user_credentials(
            'Default', self.project, 'cloud-admin'
        )

        user1 = self.km.find_user_credentials(
            'Domain2', self.project, 'bu-brt'
        )

        FloatingIPFactory(cloud_admin) \
            .set(FloatingIPFactory.FLOATINGIP_SHOW,
                 clients=user1, expected_exceptions=[KeystoneUnauthorized]) \
            .set(FloatingIPFactory.FLOATINGIP_ASSOCIATE,
                 clients=user1, expected_exceptions=[KeystoneUnauthorized]) \
            .set(FloatingIPFactory.FLOATINGIP_DISASSOCIATE,
                 clients=user1, expected_exceptions=[KeystoneUnauthorized]) \
            .set(FloatingIPFactory.FLOATINGIP_DELETE, clients=user1,
                 expected_exceptions=[KeystoneUnauthorized]) \
            .produce() \
            .run(context=self.context)

#bu-poweruser
    #todo: test all these

    def test_bu_poweruser_all(self):
        bu_admin = self.km.find_user_credentials(
            'Default', self.project, 'bu-poweruser', False
        )
        cloud_admin = self.km.find_user_credentials(
            'Default', self.project, 'cloud-admin'
        )

        SampleFactory(bu_admin) \
            .set(SampleFactory.NETWORK_CREATE, clients=cloud_admin) \
            .set(SampleFactory.SUBNET_CREATE, clients=cloud_admin) \
            .set(SampleFactory.SECURITY_GROUP_CREATE, clients=cloud_admin) \
            .set(SampleFactory.SECURITY_GROUP_RULE_CREATE, clients=cloud_admin) \
            .set(SampleFactory.SECURITY_GROUP_RULE_DELETE, clients=cloud_admin) \
            .set(SampleFactory.SECURITY_GROUP_DELETE, clients=cloud_admin) \
            .set(SampleFactory.ROUTER_CREATE, clients=cloud_admin) \
            .set(SampleFactory.ROUTER_ADD_INTERFACE, clients=cloud_admin) \
            .set(SampleFactory.ROUTER_REMOVE_INTERFACE, clients=cloud_admin) \
            .set(SampleFactory.ROUTER_DELETE, clients=cloud_admin) \
            .set(SampleFactory.SUBNET_DELETE, clients=cloud_admin) \
            .set(SampleFactory.NETWORK_DELETE, clients=cloud_admin) \
            .produce() \
            .run(context=self.context)

    def test_bu_poweruser_floatingip(self):
        cloud_admin = self.km.find_user_credentials(
            'Default', self.project, 'cloud-admin'
        )
        bu_admin = self.km.find_user_credentials(
            'Default', self.project, 'bu-poweruser', False
        )
        FloatingIPFactory(bu_admin) \
            .set(FloatingIPFactory.NETWORK_CREATE, clients=cloud_admin) \
            .set(FloatingIPFactory.SUBNET_CREATE, clients=cloud_admin) \
            .set(FloatingIPFactory.ROUTER_CREATE, clients=cloud_admin) \
            .set(FloatingIPFactory.ROUTER_ADD_INTERFACE, clients=cloud_admin) \
            .set(FloatingIPFactory.FLOATINGIP_DELETE, clients=cloud_admin) \
            .produce() \
            .run(context=self.context)

    def test_bu_poweruser_same_domain_different_user(self):
        creator = self.km.find_user_credentials(
            'Default', self.project, 'cloud-admin'
        )
        user1 = self.km.find_user_credentials(
            'Default', self.project, 'cloud-admin'
        )
        bu_admin = self.km.find_user_credentials(
            'Default', self.project, 'bu-poweruser', False
        )

        SampleFactory(bu_admin) \
            .set(SampleFactory.NETWORK_CREATE,
                 clients=user1) \
            .set(SampleFactory.SUBNET_CREATE,
                 clients=user1) \
            .set(SampleFactory.SERVER_CREATE,
                 clients=user1) \
            .set(SampleFactory.SERVER_WAIT,
                 clients=user1) \
            .set(SampleFactory.SECURITY_GROUP_CREATE,
                 clients=user1) \
            .set(SampleFactory.SECURITY_GROUP_RULE_CREATE,
                 clients=user1) \
            .set(SampleFactory.SECURITY_GROUP_RULE_DELETE, clients=user1) \
            .set(SampleFactory.SECURITY_GROUP_DELETE, clients=user1) \
            .set(SampleFactory.SERVER_DELETE,
                 clients=user1) \
            .set(SampleFactory.ROUTER_CREATE,
                 clients=user1) \
            .set(SampleFactory.ROUTER_ADD_INTERFACE, clients=user1) \
            .set(SampleFactory.ROUTER_REMOVE_INTERFACE, clients=user1) \
            .set(SampleFactory.ROUTER_DELETE, clients=user1) \
            .set(SampleFactory.SUBNET_DELETE, clients=user1) \
            .set(SampleFactory.NETWORK_DELETE, clients=user1) \
            .produce() \
            .run(context=self.context)

    def test_bu_poweruser_same_domain_different_user_floatingip(self):
        user1 = self.km.find_user_credentials(
            'Default', self.project, 'cloud-admin'
        )
        bu_admin = self.km.find_user_credentials(
            'Default', self.project, 'bu-poweruser', False
        )

        FloatingIPFactory(bu_admin) \
            .set(FloatingIPFactory.NETWORK_CREATE,
                 clients=user1) \
            .set(FloatingIPFactory.SUBNET_CREATE,
                 clients=user1) \
            .set(FloatingIPFactory.PORT_CREATE,
                 clients=user1) \
            .set(FloatingIPFactory.ROUTER_CREATE,
                 clients=user1) \
            .set(FloatingIPFactory.ROUTER_ADD_INTERFACE,
                 clients=user1) \
            .set(FloatingIPFactory.FLOATINGIP_CREATE, clients=user1) \
            .set(FloatingIPFactory.FLOATINGIP_DELETE, clients=user1) \
            .produce() \
            .run(context=self.context)

    def test_bu_poweruser_different_domain_different_user_floatingip(self):
        user1 = self.km.find_user_credentials(
            'Default', self.project, 'cloud-admin'
        )
        bu_admin = self.km.find_user_credentials(
            'Domain2', self.project, 'bu-poweruser', False
        )

        FloatingIPFactory(bu_admin) \
            .set(FloatingIPFactory.NETWORK_CREATE,
                 clients=user1) \
            .set(FloatingIPFactory.SUBNET_CREATE,
                 clients=user1) \
            .set(FloatingIPFactory.PORT_CREATE,
                 clients=user1) \
            .set(FloatingIPFactory.ROUTER_CREATE,
                 clients=user1) \
            .set(FloatingIPFactory.ROUTER_ADD_INTERFACE,
                 clients=user1) \
            .set(FloatingIPFactory.FLOATINGIP_CREATE,
                 clients=user1) \
            .set(FloatingIPFactory.FLOATINGIP_SHOW,
                 expected_exceptions=[KeystoneUnauthorized]) \
            .set(FloatingIPFactory.FLOATINGIP_ASSOCIATE,
                 clients=user1) \
            .set(FloatingIPFactory.FLOATINGIP_DISASSOCIATE,
                 expected_exceptions=[KeystoneUnauthorized]) \
            .set(FloatingIPFactory.FLOATINGIP_DELETE,
                 expected_exceptions=[KeystoneUnauthorized]) \
            .produce() \
            .run(context=self.context)

    def test_bu_poweruser_different_domain_different_user_secgroup_add_to_server(self):
        creator = self.km.find_user_credentials(
            'Default', self.project, 'cloud-admin'
        )
        user1 = self.km.find_user_credentials(
            'Default', self.project, 'bu-poweruser', False
        )
        bu_admin = self.km.find_user_credentials(
            'Domain2', self.project, 'bu-poweruser', False
        )

        SecgroupAddFactory(bu_admin) \
            .set(SecgroupAddFactory.NETWORK_CREATE,
                 clients=creator) \
            .set(SecgroupAddFactory.NETWORK_SHOW,
                 expected_exceptions = [KeystoneUnauthorized]) \
            .set(SecgroupAddFactory.SUBNET_CREATE,
                 clients=creator) \
            .set(SecgroupAddFactory.SUBNET_SHOW,
                 expected_exceptions = [KeystoneUnauthorized]) \
            .set(SecgroupAddFactory.SERVER_CREATE,
                 clients=user1) \
            .set(SecgroupAddFactory.SERVER_WAIT,
                 clients=user1) \
            .set(SecgroupAddFactory.SECURITY_GROUP_CREATE,
                 clients=creator) \
            .set(SecgroupAddFactory.SECURITY_GROUP_SHOW,
                 expected_exceptions = [KeystoneUnauthorized]) \
            .set(SecgroupAddFactory.SECURITY_GROUP_RULE_CREATE,
                 clients=creator) \
            .set(SecgroupAddFactory.SECURITY_GROUP_ADD_TO_SERVER,
                 expected_exceptions = [KeystoneUnauthorized]) \
            .produce() \
            .run(context=self.context)

    def test_bu_poweruser_different_domain_different_user_add_interface_to_server(self):
        creator = self.km.find_user_credentials(
            'Default', self.project, 'cloud-admin'
        )
        user1 = self.km.find_user_credentials(
            'Default', self.project, 'cloud-admin'
        )
        bu_admin = self.km.find_user_credentials(
            'Domain2', self.project, 'bu-poweruser', False
        )

        AddInterfaceFactory(bu_admin) \
            .set(AddInterfaceFactory.NETWORK_CREATE,
                 clients=user1) \
            .set(AddInterfaceFactory.SUBNET_CREATE,
                 clients=user1) \
            .set(AddInterfaceFactory.SERVER_CREATE,
                 clients=user1) \
            .set(AddInterfaceFactory.SERVER_WAIT,
                 clients=user1) \
            .set(AddInterfaceFactory.SECURITY_GROUP_CREATE,
                 clients=user1) \
            .set(AddInterfaceFactory.SECURITY_GROUP_RULE_CREATE,
                 clients=user1) \
            .set(AddInterfaceFactory.SECURITY_GROUP_ADD_TO_SERVER,
                 clients=user1) \
            .set(AddInterfaceFactory.SECURITY_GROUP_REMOVE_FROM_SERVER,
                 expected_exceptions=[KeystoneUnauthorized]) \
            .set(AddInterfaceFactory.SECURITY_GROUP_RULE_DELETE,
                 expected_exceptions=[KeystoneUnauthorized]) \
            .set(AddInterfaceFactory.SECURITY_GROUP_DELETE,
                 expected_exceptions=[KeystoneUnauthorized]) \
            .set(AddInterfaceFactory.SERVER_DELETE,
                 clients=user1) \
            .set(AddInterfaceFactory.ROUTER_CREATE,
                 clients=user1) \
            .set(AddInterfaceFactory.ROUTER_SHOW,
                 expected_exceptions=[KeystoneUnauthorized]) \
            .set(AddInterfaceFactory.ROUTER_ADD_INTERFACE,
                 expected_exceptions=[KeystoneUnauthorized]) \
            .produce() \
            .run(context=self.context)

    def test_bu_poweruser_different_domain_different_user_subnet_delete(self):
        user1 = self.km.find_user_credentials(
            'Default', self.project, 'cloud-admin'
        )
        bu_admin = self.km.find_user_credentials(
            'Domain2', self.project, 'bu-poweruser', False
        )

        SubnetDeleteFactory(user1) \
            .set(SubnetDeleteFactory.SUBNET_DELETE, clients=bu_admin,
                 expected_exceptions=[KeystoneUnauthorized]) \
            .produce() \
            .run(context=self.context)

    def test_bu_poweruser_different_domain_different_user_network_delete(self):
        user1 = self.km.find_user_credentials(
            'Default', self.project, 'cloud-admin'
        )
        bu_admin = self.km.find_user_credentials(
            'Domain2', self.project, 'bu-poweruser', False
        )

        NetworkDeleteFactory(user1) \
            .set(NetworkDeleteFactory.NETWORK_DELETE, clients=bu_admin,
                 expected_exceptions=[KeystoneUnauthorized]) \
            .produce() \
            .run(context=self.context)

    def test_bu_poweruser_subnet_update(self):
        cloud_admin = self.km.find_user_credentials(
            'Default', self.project, 'cloud-admin'
        )
        bu_admin = self.km.find_user_credentials(
            'Default', self.project, 'bu-poweruser', False
        )
        SubnetUpdateFactory(cloud_admin) \
            .set(SubnetUpdateFactory.SUBNET_UPDATE, clients=bu_admin, expected_exceptions=[NeutronForbidden]) \
            .produce() \
            .run(context=self.context)

    def test_bu_poweruser_router_update(self):
        cloud_admin = self.km.find_user_credentials(
            'Default', self.project, 'cloud-admin'
        )
        bu_admin = self.km.find_user_credentials(
            'Default', self.project, 'bu-poweruser', False
        )
        RouterUpdateFactory(cloud_admin) \
            .set(RouterUpdateFactory.ROUTER_UPDATE, clients=bu_admin, expected_exceptions=[NeutronForbidden]) \
            .produce() \
            .run(context=self.context)

#cirt
#todo: test all these

    def test_cirt_all(self):
        bu_admin = self.km.find_user_credentials(
            'Default', self.project, 'cirt'
        )
        cloud_admin = self.km.find_user_credentials(
            'Default', self.project, 'cloud-admin'
        )

        SampleFactory(cloud_admin) \
            .set(SampleFactory.SUBNET_SHOW, clients=bu_admin) \
            .set(SampleFactory.ROUTER_SHOW, clients=bu_admin) \
            .set(SampleFactory.SECURITY_GROUP_SHOW, clients=bu_admin) \
            .produce() \
            .run(context=self.context)

    def test_cirt_floatingip(self):
        cloud_admin = self.km.find_user_credentials(
            'Default', self.project, 'cloud-admin'
        )
        bu_admin = self.km.find_user_credentials(
            'Default', self.project, 'cirt'
        )
        FloatingIPFactory(bu_admin) \
            .set(FloatingIPFactory.NETWORK_CREATE, clients=cloud_admin) \
            .set(FloatingIPFactory.SUBNET_CREATE, clients=cloud_admin) \
            .set(FloatingIPFactory.PORT_CREATE, clients=cloud_admin) \
            .set(FloatingIPFactory.FLOATINGIP_CREATE, clients=cloud_admin) \
            .set(FloatingIPFactory.FLOATINGIP_ASSOCIATE, clients=cloud_admin) \
            .set(FloatingIPFactory.FLOATINGIP_DISASSOCIATE, clients=cloud_admin) \
            .set(FloatingIPFactory.FLOATINGIP_DELETE, clients=cloud_admin) \
            .set(FloatingIPFactory.ROUTER_CREATE, clients=cloud_admin) \
            .set(FloatingIPFactory.ROUTER_ADD_INTERFACE, clients=cloud_admin) \
            .produce() \
            .run(context=self.context)

    def test_cirt_same_domain_different_user(self):
        creator = self.km.find_user_credentials(
            'Default', self.project, 'cloud-admin'
        )
        user1 = self.km.find_user_credentials(
            'Default', self.project, 'cloud-admin'
        )
        bu_admin = self.km.find_user_credentials(
            'Default', self.project, 'cirt'
        )

        SampleFactory(bu_admin) \
            .set(SampleFactory.NETWORK_CREATE, clients=user1) \
            .set(SampleFactory.NETWORK_SHOW, clients=user1) \
            .set(SampleFactory.SUBNET_CREATE,
                 clients=user1) \
            .set(SampleFactory.SERVER_CREATE, clients=user1) \
            .set(SampleFactory.SERVER_WAIT, clients=user1) \
            .set(SampleFactory.SECURITY_GROUP_CREATE, clients=user1) \
            .set(SampleFactory.SECURITY_GROUP_RULE_CREATE,
                 clients=user1) \
            .set(SampleFactory.SECURITY_GROUP_ADD_TO_SERVER, clients=user1) \
            .set(SampleFactory.SECURITY_GROUP_REMOVE_FROM_SERVER, clients=user1) \
            .set(SampleFactory.SECURITY_GROUP_RULE_DELETE, clients=user1) \
            .set(SampleFactory.SECURITY_GROUP_DELETE, clients=user1) \
            .set(SampleFactory.SERVER_DELETE,
                 clients=user1) \
            .set(SampleFactory.ROUTER_CREATE,
                 clients=user1) \
            .set(SampleFactory.ROUTER_ADD_INTERFACE, clients=user1) \
            .set(SampleFactory.ROUTER_REMOVE_INTERFACE, clients=user1) \
            .set(SampleFactory.ROUTER_DELETE, clients=user1) \
            .set(SampleFactory.SUBNET_DELETE, clients=user1) \
            .set(SampleFactory.NETWORK_DELETE, clients=user1) \
            .produce() \
            .run(context=self.context)

    def test_cirt_same_domain_different_user_floatingip(self):
        user1 = self.km.find_user_credentials(
            'Default', self.project, 'cloud-admin'
        )
        bu_admin = self.km.find_user_credentials(
            'Default', self.project, 'cirt'
        )

        FloatingIPFactory(bu_admin) \
            .set(FloatingIPFactory.NETWORK_CREATE,
                 clients=user1) \
            .set(FloatingIPFactory.SUBNET_CREATE,
                 clients=user1) \
            .set(FloatingIPFactory.PORT_CREATE, clients=user1) \
            .set(FloatingIPFactory.ROUTER_CREATE,
                 clients=user1) \
            .set(FloatingIPFactory.ROUTER_ADD_INTERFACE,
                 clients=user1) \
            .set(FloatingIPFactory.FLOATINGIP_CREATE,
                 clients=user1) \
            .set(FloatingIPFactory.FLOATINGIP_ASSOCIATE, clients=user1) \
            .set(FloatingIPFactory.FLOATINGIP_DISASSOCIATE, clients=user1) \
            .set(FloatingIPFactory.FLOATINGIP_DELETE, clients=user1) \
            .produce() \
            .run(context=self.context)

    def test_cirt_different_domain_different_user_floatingip(self):
        user1 = self.km.find_user_credentials(
            'Default', self.project, 'cloud-admin'
        )
        bu_admin = self.km.find_user_credentials(
            'Domain2', self.project, 'cirt'
        )

        FloatingIPFactory(bu_admin) \
            .set(FloatingIPFactory.NETWORK_CREATE,
                 clients=user1) \
            .set(FloatingIPFactory.SUBNET_CREATE,
                 clients=user1) \
            .set(FloatingIPFactory.PORT_CREATE,
                 clients=user1) \
            .set(FloatingIPFactory.ROUTER_CREATE,
                 clients=user1) \
            .set(FloatingIPFactory.ROUTER_ADD_INTERFACE,
                 clients=user1) \
            .set(FloatingIPFactory.FLOATINGIP_CREATE,
                 clients=user1) \
            .set(FloatingIPFactory.FLOATINGIP_SHOW,
                 expected_exceptions=[KeystoneUnauthorized]) \
            .set(FloatingIPFactory.FLOATINGIP_ASSOCIATE,
                 clients=user1) \
            .set(FloatingIPFactory.FLOATINGIP_DISASSOCIATE,
                 expected_exceptions=[KeystoneUnauthorized]) \
            .set(FloatingIPFactory.FLOATINGIP_DELETE,
                 expected_exceptions=[KeystoneUnauthorized]) \
            .produce() \
            .run(context=self.context)

    def test_cirt_different_domain_different_user_secgroup_add_to_server(self):
        creator = self.km.find_user_credentials(
            'Default', self.project, 'cloud-admin'
        )
        user1 = self.km.find_user_credentials(
            'Default', self.project, 'cirt'
        )
        bu_admin = self.km.find_user_credentials(
            'Domain2', self.project, 'cirt'
        )

        SecgroupAddFactory(bu_admin) \
            .set(SecgroupAddFactory.NETWORK_CREATE,
                 clients=creator) \
            .set(SecgroupAddFactory.NETWORK_SHOW,
                 expected_exceptions = [KeystoneUnauthorized]) \
            .set(SecgroupAddFactory.SUBNET_CREATE,
                 clients=creator) \
            .set(SecgroupAddFactory.SUBNET_SHOW,
                 expected_exceptions = [KeystoneUnauthorized]) \
            .set(SecgroupAddFactory.SERVER_CREATE,
                 clients=creator) \
            .set(SecgroupAddFactory.SERVER_WAIT,
                 clients=user1) \
            .set(SecgroupAddFactory.SECURITY_GROUP_CREATE,
                 clients=creator) \
            .set(SecgroupAddFactory.SECURITY_GROUP_SHOW,
                 expected_exceptions = [KeystoneUnauthorized]) \
            .set(SecgroupAddFactory.SECURITY_GROUP_RULE_CREATE,
                 clients=creator) \
            .set(SecgroupAddFactory.SECURITY_GROUP_ADD_TO_SERVER,
                 expected_exceptions = [KeystoneUnauthorized]) \
            .produce() \
            .run(context=self.context)

    def test_cirt_different_domain_different_user_add_interface_to_server(self):
        creator = self.km.find_user_credentials(
            'Default', self.project, 'cloud-admin'
        )
        user1 = self.km.find_user_credentials(
            'Default', self.project, 'cloud-admin'
        )
        bu_admin = self.km.find_user_credentials(
            'Domain2', self.project, 'cirt'
        )

        AddInterfaceFactory(bu_admin) \
            .set(AddInterfaceFactory.NETWORK_CREATE,
                 clients=user1) \
            .set(AddInterfaceFactory.SUBNET_CREATE,
                 clients=user1) \
            .set(AddInterfaceFactory.SERVER_CREATE,
                 clients=user1) \
            .set(AddInterfaceFactory.SERVER_WAIT,
                 clients=user1) \
            .set(AddInterfaceFactory.SECURITY_GROUP_CREATE,
                 clients=user1) \
            .set(AddInterfaceFactory.SECURITY_GROUP_RULE_CREATE,
                 clients=user1) \
            .set(AddInterfaceFactory.SECURITY_GROUP_ADD_TO_SERVER,
                 clients=user1) \
            .set(AddInterfaceFactory.SECURITY_GROUP_REMOVE_FROM_SERVER,
                 expected_exceptions=[KeystoneUnauthorized]) \
            .set(AddInterfaceFactory.SECURITY_GROUP_RULE_DELETE,
                 expected_exceptions=[KeystoneUnauthorized]) \
            .set(AddInterfaceFactory.SECURITY_GROUP_DELETE,
                 expected_exceptions=[KeystoneUnauthorized]) \
            .set(AddInterfaceFactory.SERVER_DELETE,
                 clients=user1) \
            .set(AddInterfaceFactory.ROUTER_CREATE,
                 clients=user1) \
            .set(AddInterfaceFactory.ROUTER_SHOW,
                 expected_exceptions=[KeystoneUnauthorized]) \
            .set(AddInterfaceFactory.ROUTER_ADD_INTERFACE,
                 expected_exceptions=[KeystoneUnauthorized]) \
            .produce() \
            .run(context=self.context)

    def test_cirt_different_domain_different_user_subnet_delete(self):
        user1 = self.km.find_user_credentials(
            'Default', self.project, 'cloud-admin'
        )
        bu_admin = self.km.find_user_credentials(
            'Domain2', self.project, 'cirt'
        )

        SubnetDeleteFactory(user1) \
            .set(SubnetDeleteFactory.SUBNET_DELETE, clients=bu_admin,
                 expected_exceptions=[KeystoneUnauthorized]) \
            .produce() \
            .run(context=self.context)

    def test_cirt_different_domain_different_user_network_delete(self):
        user1 = self.km.find_user_credentials(
            'Default', self.project, 'cloud-admin'
        )
        bu_admin = self.km.find_user_credentials(
            'Domain2', self.project, 'cirt'
        )

        NetworkDeleteFactory(user1) \
            .set(NetworkDeleteFactory.NETWORK_DELETE, clients=bu_admin,
                 expected_exceptions=[KeystoneUnauthorized]) \
            .produce() \
            .run(context=self.context)

    def test_cirt_subnet_update(self):
        cloud_admin = self.km.find_user_credentials(
            'Default', self.project, 'cloud-admin'
        )
        bu_admin = self.km.find_user_credentials(
            'Default', self.project, 'cirt'
        )
        SubnetUpdateFactory(cloud_admin) \
            .set(SubnetUpdateFactory.SUBNET_UPDATE, clients=bu_admin, expected_exceptions=[NeutronForbidden]) \
            .produce() \
            .run(context=self.context)

    def test_cirt_router_update(self):
        cloud_admin = self.km.find_user_credentials(
            'Default', self.project, 'cloud-admin'
        )
        bu_admin = self.km.find_user_credentials(
            'Default', self.project, 'cirt'
        )
        RouterUpdateFactory(cloud_admin) \
            .set(RouterUpdateFactory.ROUTER_UPDATE, clients=bu_admin, expected_exceptions=[NeutronForbidden]) \
            .produce() \
            .run(context=self.context)

#cloud-support
#todo: test all these

    def test_cloud_support_all(self):
        bu_admin = self.km.find_user_credentials(
            'Default', self.project, 'cloud-support'
        )
        cloud_admin = self.km.find_user_credentials(
            'Default', self.project, 'cloud-admin'
        )

        SampleFactory(cloud_admin) \
            .set(SampleFactory.NETWORK_SHOW, clients=bu_admin) \
            .set(SampleFactory.SUBNET_SHOW, clients=bu_admin) \
            .set(SampleFactory.ROUTER_SHOW, clients=bu_admin) \
            .set(SampleFactory.SECURITY_GROUP_SHOW, clients=bu_admin) \
            .produce() \
            .run(context=self.context)

    def test_cloud_support_floatingip(self):
        cloud_admin = self.km.find_user_credentials(
            'Default', self.project, 'cloud-admin'
        )
        bu_admin = self.km.find_user_credentials(
            'Default', self.project, 'cloud-support'
        )
        FloatingIPFactory(bu_admin) \
            .set(FloatingIPFactory.NETWORK_CREATE, clients=cloud_admin) \
            .set(FloatingIPFactory.SUBNET_CREATE, clients=cloud_admin) \
            .set(FloatingIPFactory.ROUTER_CREATE, clients=cloud_admin) \
            .set(FloatingIPFactory.ROUTER_ADD_INTERFACE, clients=cloud_admin) \
            .set(FloatingIPFactory.FLOATINGIP_DELETE, clients=cloud_admin) \
            .produce() \
            .run(context=self.context)

    def test_cloud_support_same_domain_different_user(self):
        creator = self.km.find_user_credentials(
            'Default', self.project, 'cloud-admin'
        )
        user1 = self.km.find_user_credentials(
            'Default', self.project, 'cloud-admin'
        )
        bu_admin = self.km.find_user_credentials(
            'Default', self.project, 'cloud-support'
        )

        SampleFactory(bu_admin) \
            .set(SampleFactory.NETWORK_CREATE,
                 clients=user1) \
            .set(SampleFactory.SUBNET_CREATE,
                 clients=user1) \
            .set(SampleFactory.SERVER_CREATE,
                 clients=user1) \
            .set(SampleFactory.SERVER_WAIT,
                 clients=user1) \
            .set(SampleFactory.SECURITY_GROUP_CREATE,
                 clients=user1) \
            .set(SampleFactory.SECURITY_GROUP_RULE_CREATE, clients=user1) \
            .set(SampleFactory.SECURITY_GROUP_ADD_TO_SERVER, clients=user1) \
            .set(SampleFactory.SECURITY_GROUP_REMOVE_FROM_SERVER, clients=user1) \
            .set(SampleFactory.SECURITY_GROUP_RULE_DELETE, clients=user1) \
            .set(SampleFactory.SECURITY_GROUP_DELETE, clients=user1) \
            .set(SampleFactory.SERVER_DELETE,
                 clients=user1) \
            .set(SampleFactory.ROUTER_CREATE,
                 clients=user1) \
            .set(SampleFactory.ROUTER_ADD_INTERFACE, clients=user1) \
            .set(SampleFactory.ROUTER_REMOVE_INTERFACE, clients=user1) \
            .set(SampleFactory.ROUTER_DELETE, clients=user1) \
            .set(SampleFactory.SUBNET_DELETE, clients=user1) \
            .set(SampleFactory.NETWORK_DELETE, clients=user1) \
            .produce() \
            .run(context=self.context)

    def test_cloud_support_same_domain_different_user_floatingip(self):
        user1 = self.km.find_user_credentials(
            'Default', self.project, 'cloud-admin'
        )
        bu_admin = self.km.find_user_credentials(
            'Default', self.project, 'cloud-support'
        )

        FloatingIPFactory(bu_admin) \
            .set(FloatingIPFactory.NETWORK_CREATE,
                 clients=user1) \
            .set(FloatingIPFactory.SUBNET_CREATE,
                 clients=user1) \
            .set(FloatingIPFactory.PORT_CREATE,
                 clients=user1) \
            .set(FloatingIPFactory.ROUTER_CREATE,
                 clients=user1) \
            .set(FloatingIPFactory.ROUTER_ADD_INTERFACE,
                 clients=user1) \
            .set(FloatingIPFactory.FLOATINGIP_CREATE,
                 clients=user1) \
            .set(FloatingIPFactory.FLOATINGIP_DELETE, clients=user1) \
            .produce() \
            .run(context=self.context)

    def test_cloud_support_different_domain_different_user_floatingip(self):
        user1 = self.km.find_user_credentials(
            'Default', self.project, 'cloud-admin'
        )
        bu_admin = self.km.find_user_credentials(
            'Domain2', self.project, 'cloud-support'
        )

        FloatingIPFactory(bu_admin) \
            .set(FloatingIPFactory.NETWORK_CREATE,
                 clients=user1) \
            .set(FloatingIPFactory.SUBNET_CREATE,
                 clients=user1) \
            .set(FloatingIPFactory.PORT_CREATE,
                 clients=user1) \
            .set(FloatingIPFactory.ROUTER_CREATE,
                 clients=user1) \
            .set(FloatingIPFactory.ROUTER_ADD_INTERFACE,
                 clients=user1) \
            .set(FloatingIPFactory.FLOATINGIP_CREATE,
                 clients=user1) \
            .set(FloatingIPFactory.FLOATINGIP_SHOW,
                 expected_exceptions=[KeystoneUnauthorized]) \
            .set(FloatingIPFactory.FLOATINGIP_ASSOCIATE,
                 clients=user1) \
            .set(FloatingIPFactory.FLOATINGIP_DISASSOCIATE,
                 expected_exceptions=[KeystoneUnauthorized]) \
            .set(FloatingIPFactory.FLOATINGIP_DELETE,
                 expected_exceptions=[KeystoneUnauthorized]) \
            .produce() \
            .run(context=self.context)

    def test_cloud_support_different_domain_different_user_add_interface_to_server(self):
        creator = self.km.find_user_credentials(
            'Default', self.project, 'cloud-admin'
        )
        user1 = self.km.find_user_credentials(
            'Default', self.project, 'cloud-admin'
        )
        bu_admin = self.km.find_user_credentials(
            'Domain2', self.project, 'cloud-support'
        )

        AddInterfaceFactory(bu_admin) \
            .set(AddInterfaceFactory.NETWORK_CREATE,
                 clients=user1) \
            .set(AddInterfaceFactory.SUBNET_CREATE,
                 clients=user1) \
            .set(AddInterfaceFactory.SERVER_CREATE,
                 clients=user1) \
            .set(AddInterfaceFactory.SERVER_WAIT,
                 clients=user1) \
            .set(AddInterfaceFactory.SECURITY_GROUP_CREATE,
                 clients=user1) \
            .set(AddInterfaceFactory.SECURITY_GROUP_RULE_CREATE,
                 clients=user1) \
            .set(AddInterfaceFactory.SECURITY_GROUP_ADD_TO_SERVER,
                 clients=user1) \
            .set(AddInterfaceFactory.SECURITY_GROUP_REMOVE_FROM_SERVER,
                 expected_exceptions=[KeystoneUnauthorized]) \
            .set(AddInterfaceFactory.SECURITY_GROUP_RULE_DELETE,
                 expected_exceptions=[KeystoneUnauthorized]) \
            .set(AddInterfaceFactory.SECURITY_GROUP_DELETE,
                 expected_exceptions=[KeystoneUnauthorized]) \
            .set(AddInterfaceFactory.SERVER_DELETE,
                 clients=user1) \
            .set(AddInterfaceFactory.ROUTER_CREATE,
                 clients=user1) \
            .set(AddInterfaceFactory.ROUTER_SHOW,
                 expected_exceptions=[KeystoneUnauthorized]) \
            .set(AddInterfaceFactory.ROUTER_ADD_INTERFACE,
                 expected_exceptions=[KeystoneUnauthorized]) \
            .produce() \
            .run(context=self.context)

    def test_cloud_support_different_domain_different_user_subnet_delete(self):
        user1 = self.km.find_user_credentials(
            'Default', self.project, 'cloud-admin'
        )
        bu_admin = self.km.find_user_credentials(
            'Domain2', self.project, 'cloud-support'
        )

        SubnetDeleteFactory(user1) \
            .set(SubnetDeleteFactory.SUBNET_DELETE, clients=bu_admin,
                 expected_exceptions=[KeystoneUnauthorized]) \
            .produce() \
            .run(context=self.context)

    def test_cloud_support_different_domain_different_user_network_delete(self):
        user1 = self.km.find_user_credentials(
            'Default', self.project, 'cloud-admin'
        )
        bu_admin = self.km.find_user_credentials(
            'Domain2', self.project, 'cloud-support'
        )

        NetworkDeleteFactory(user1) \
            .set(NetworkDeleteFactory.NETWORK_DELETE, clients=bu_admin,
                 expected_exceptions=[KeystoneUnauthorized]) \
            .produce() \
            .run(context=self.context)

#todo: retest
    def test_cloud_support_subnet_update(self):
        cloud_admin = self.km.find_user_credentials(
            'Default', self.project, 'cloud-admin'
        )
        bu_admin = self.km.find_user_credentials(
            'Default', self.project, 'cloud-support'
        )
        SubnetUpdateFactory(cloud_admin) \
            .set(SubnetUpdateFactory.SUBNET_UPDATE, clients=bu_admin, expected_exceptions=[NeutronForbidden]) \
            .produce() \
            .run(context=self.context)

    def test_cloud_support_router_update(self):
        cloud_admin = self.km.find_user_credentials(
            'Default', self.project, 'cloud-admin'
        )
        bu_admin = self.km.find_user_credentials(
            'Default', self.project, 'cloud-support'
        )
        RouterUpdateFactory(cloud_admin) \
            .set(RouterUpdateFactory.ROUTER_UPDATE, clients=bu_admin, expected_exceptions=[NeutronForbidden]) \
            .produce() \
            .run(context=self.context)