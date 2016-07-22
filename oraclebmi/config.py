from __future__ import absolute_import
import base64
import urllib3


class Config(object):

    def __init__(self):

        self.user = None
        self.tenancy = None
        self.fingerprint = None
        self.key_file = None

        core_endpoint = 'https://core.us-az-phoenix-1.OracleIaaS.com/v1'
        self.endpoint_identity_api = 'https://identity.us-az-phoenix-1.OracleIaaS.com/v1'
        self.endpoint_blockstorage_api = core_endpoint
        self.endpoint_compute_api = core_endpoint
        self.endpoint_vcn_ad_service_api = core_endpoint
        self.endpoint_vcn_service_api = core_endpoint

        self.verify_ssl = True
        self.ssl_ca_cert = None
        self.cert_file = None
        self.debugging = False

