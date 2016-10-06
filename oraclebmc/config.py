from __future__ import absolute_import


class Config(object):

    def __init__(self):

        self.user = None
        self.tenancy = None
        self.fingerprint = None
        self.key_file = None

        core_endpoint = 'https://iaas.us-phoenix-1.oraclecloud.com/20160918'
        self.identity_endpoint = 'https://identity.us-phoenix-1.oraclecloud.com/20160918'
        self.blockstorage_endpoint = core_endpoint
        self.compute_endpoint = core_endpoint
        self.virtual_network_endpoint = core_endpoint
        self.object_storage_endpoint = 'https://objectstorage.us-phoenix-1.oraclecloud.com'

        self.verify_ssl = True
        self.log_requests = False
        self.additional_user_agent = None
