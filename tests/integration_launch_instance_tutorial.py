from tests.service_test_base import ServiceTestBase
import tests.util
import oraclebmi
import os.path
import time

class TestLaunchInstanceTutorial(ServiceTestBase):
    """This test is based on the Launching Your First Instance tutorial in the help docs."""

    def setUp(self):
        self.context = self.create_context(profile_name='DEBUG')

        self.test_id = tests.util.random_number_string()

        # TODO DEX-17: Currently this test only runs against R2 and
        # if you have the private and public key files. We should be
        # getting these dynamically based on a specified environment.
        self.availability_domain = 'kIdk:PHX-AD-2'
        self.compartment = self.context.config.tenancy
        self.public_key_file = '~/.ssh/id_rsa.pub'

    def test_tutorial(self):
        print('Running Launching Your First Instance tutorial')
        print('Objects will have ID ' + self.test_id)

        try:
            self.create_cloud_network()
            self.create_subnet()
            self.create_internet_gateway()
            self.update_route_table()

            # There's a bug where the instance will immediately terminate if we don't add some extra
            # wait time before launching. (COM-79)
            time.sleep(15)

            self.launch_instance()
            self.get_public_ip_address()
            self.create_volume()
            self.attach_volume()
        except Exception as e:
            print('Exception during creation phase: ' + e)
            raise
        finally:
            self.detach_volume()
            self.delete_volume()
            self.terminate_instance()
            self.delete_subnet()
            self.delete_cloud_network()


    def create_cloud_network(self):
        print('Creating cloud network')
        request = oraclebmi.models.CreateVcnRequest()
        request.cidr_block = '10.0.0.0/16'
        request.display_name = 'pythonsdk_test_vcn_' + self.test_id
        request.compartment_id = self.compartment

        response = self.context.vcn_service_api.create_vcn(request)

        self.vcn = response.data
        self.assertEqual(200, response.status)
        assert (type(response.data) is oraclebmi.models.Vcn)

        response = self.context.vcn_service_api.get_vcn(self.vcn.id)
        response = self.context.wait_until(response, 'state', 'AVAILABLE')

        self.assertEquals('AVAILABLE', response.data.state)

    def delete_cloud_network(self):
        if hasattr(self, 'vcn'):
            print('Deleting vcn')
            response = self.context.vcn_service_api.delete_vcn(self.vcn.id)
            self.assertEqual(204, response.status)

            with self.assertRaises(oraclebmi.exceptions.ServiceError) as errorContext:
                response = self.context.vcn_service_api.get_vcn(self.vcn.id)
                self.context.wait_until(response, 'state', 'TERMINATED', max_wait_seconds=180)

            self.assertEqual(404, errorContext.exception.status)

    def create_subnet(self):
        print('Creating subnet')
        request = oraclebmi.models.CreateSubnetRequest()
        request.cidr_block = '10.0.0.0/16'
        request.availability_domain = self.availability_domain
        request.display_name = 'pythonsdk_test_subnet_' + self.test_id
        request.compartment_id = self.compartment
        request.route_table_id = self.vcn.default_route_table_id
        request.vcn_id = self.vcn.id
        response = self.context.vcn_service_api.create_subnet(request)

        self.subnet = response.data
        self.assertEqual(200, response.status)
        assert (type(self.subnet) is oraclebmi.models.Subnet)

        response = self.context.vcn_service_api.get_subnet(self.subnet.id)
        self.context.wait_until(response, 'state', 'AVAILABLE')

    def delete_subnet(self):
        if hasattr(self, 'subnet'):
            print('Deleting subnet')
            response = self.context.vcn_service_api.delete_subnet(self.subnet.id)
            self.assertEqual(204, response.status)

            with self.assertRaises(oraclebmi.exceptions.ServiceError) as errorContext:
                response = self.context.vcn_service_api.get_subnet(self.subnet.id)
                self.context.wait_until(response, 'state', 'TERMINATED')

            self.assertEqual(404, errorContext.exception.status)

    def create_internet_gateway(self):
        print('Creating internet gateway')
        request = oraclebmi.models.CreateInternetGatewayRequest()
        request.display_name = 'pythonsdk_test_ig_' + self.test_id
        request.compartment_id = self.compartment
        request.is_enabled = True
        request.vcn_id = self.vcn.id
        response = self.context.vcn_service_api.create_internet_gateway(request)

        self.internet_gateway = response.data
        self.assertEqual(200, response.status)
        assert (type(self.internet_gateway) is oraclebmi.models.InternetGateway)

        response = self.context.vcn_service_api.get_internet_gateway(self.internet_gateway.id)
        self.context.wait_until(response, 'state', 'AVAILABLE')

    def update_route_table(self):
        print('Updating route table')
        route_rule = oraclebmi.models.RouteRule()
        route_rule.cidr_block = '0.0.0.0/0'
        route_rule.display_name = 'pythonsdk_route_rule_' + self.test_id
        route_rule.network_entity_id = self.internet_gateway.id
        route_rule.network_entity_type = 'INTERNET_GATEWAY'

        request = oraclebmi.models.UpdateRouteTableRequest()
        request.route_rules = [route_rule]
        response = self.context.vcn_service_api.update_route_table(self.vcn.default_route_table_id, request)

        self.route_table = response.data
        self.assertEqual(200, response.status)
        assert (type(self.route_table) is oraclebmi.models.RouteTable)

        response = self.context.vcn_service_api.get_route_table(self.vcn.default_route_table_id)
        self.context.wait_until(response, 'state', 'AVAILABLE')

    def get_public_key(self, file):
        file = os.path.expanduser(file)
        with open(file) as f:
            return f.read().strip()

    def launch_instance(self):
        print('Launching instance')

        ssh_public_key = self.get_public_key(self.public_key_file)

        request = oraclebmi.models.LaunchInstanceRequest()
        request.availability_domain = self.availability_domain
        request.compartment_id = self.compartment
        request.display_name = 'pythonsdk_tutorial_instance_' + self.test_id
        request.image = 'ol7.1-base-0.0.1'
        request.shape = 'x5-2.36.512'
        request.subnet_id = self.subnet.id
        request.metadata = {'ssh_authorized_keys': ssh_public_key}
        response = self.context.compute_api.launch_instance(request)

        self.instance = response.data
        self.assertEqual(200, response.status)
        self.assertEqual('PROVISIONING', self.instance.state)

        response = self.context.compute_api.get_instance(self.instance.id)
        self.instance = self.context.wait_until(response, 'state', 'RUNNING', max_wait_seconds=300).data

        self.assertEqual('RUNNING', self.instance.state)

    def terminate_instance(self):
        if hasattr(self, 'instance'):
            print('Terminating instance')
            response = self.context.compute_api.terminate_instance(self.instance.id)
            self.assertEqual(204, response.status)

            response = self.context.compute_api.get_instance(self.instance.id)
            self.context.wait_until(response, 'state', 'TERMINATED')

    def create_volume(self):
        print('Creating volume')
        request = oraclebmi.models.CreateVolumeRequest()
        request.display_name = 'pythonsdk_volume_' + self.test_id
        request.compartment_id = self.compartment
        request.availability_domain = self.availability_domain
        response = self.context.blockstorage_api.create_volume(request, opc_idempotency_token='testtoken' + self.test_id)

        self.volume = response.data
        self.assertEqual(202, response.status)
        assert (type(self.volume) is oraclebmi.models.Volume)

        response = self.context.blockstorage_api.get_volume(self.volume.id)
        self.context.wait_until(response, 'state', 'AVAILABLE', max_wait_seconds=180)

    def delete_volume(self):
        if hasattr(self, 'volume'):
            print('Deleting volume')
            response = self.context.blockstorage_api.delete_volume(self.volume.id)
            self.assertEqual(202, response.status)

            response = self.context.blockstorage_api.get_volume(self.volume.id)
            self.context.wait_until(response, 'state', 'TERMINATED', max_wait_seconds=180)

    def get_public_ip_address(self):
        print('Getting public IP address')
        response = self.context.compute_api.list_vnic_attachments(self.compartment, instance_id = self.instance.id)
        self.assertEqual(200, response.status)
        assert (len(response.data) > 0)

        self.vnic_attachment = next((va for va in response.data if va.instance_id == self.instance.id), None)

        assert(self.vnic_attachment != None)

        # Just get the address for the first vnic attachment.
        response = self.context.vcn_ad_service_api.get_vnic(self.vnic_attachment.vnic_id)
        self.vnic_attachment = self.context.wait_until(response, 'state', 'AVAILABLE').data

        self.vnic = response.data
        self.assertEqual(200, response.status)
        assert(self.vnic.public_ip != None)

        print('Public IP Address: ' + self.vnic.public_ip)


    def attach_volume(self):
        print('Attaching volume')
        request = oraclebmi.models.AttachIScsiVolumeRequest()
        request.compartment_id = self.compartment
        request.instance_id = self.instance.id
        request.volume_id = self.volume.id
        response = self.context.compute_api.attach_volume(request)

        self.volume_attachment = response.data
        self.assertEqual(200, response.status)
        assert (type(self.volume_attachment) is oraclebmi.models.IScsiVolumeAttachment)

        response = self.context.compute_api.get_volume_attachment(self.volume_attachment.id)
        self.context.wait_until(response, 'state', 'ATTACHED')


    def detach_volume(self):
        if hasattr(self, 'volume'):
            print('Detaching volume')
            response = self.context.compute_api.detach_volume(self.volume_attachment.id)
            self.assertEqual(204, response.status)

            response = self.context.compute_api.get_volume_attachment(self.volume_attachment.id)
            self.context.wait_until(response, 'state', 'DETACHED')

if __name__ == '__main__':
    unittest.main()