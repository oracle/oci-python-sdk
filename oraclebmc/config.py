from __future__ import absolute_import


class Config(object):

    def __init__(self):

        self.user = None
        self.tenancy = None
        self.fingerprint = None
        self.key_file = None

        core_endpoint = 'https://iaas.us-phoenix-1.oraclecloud.com/20160918'
        self.endpoint_identity_api = 'https://identity.us-phoenix-1.oraclecloud.com/20160918'
        self.endpoint_blockstorage_api = core_endpoint
        self.endpoint_compute_api = core_endpoint
        self.endpoint_virtual_network_api = core_endpoint
        self.endpoint_object_storage_api = 'https://objectstorage.us-phoenix-1.oraclecloud.com'

        self.verify_ssl = True
        self.log_requests = False
        self.additional_user_agent = None
