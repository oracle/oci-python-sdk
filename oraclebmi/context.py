from .config import Config
from .config_file_loader import ConfigFileLoader
from .signer import Signer
from .api_client import ApiClient
import apis

class Context(object):

    def __init__(self, config_file_location=ConfigFileLoader.DEFAULT_CONFIG_FILE, profile_name=ConfigFileLoader.DEFAULT_PROFILE):
        self.config = ConfigFileLoader.load_config(config_file_location, profile_name)

        self.signer = Signer(self.config.tenancy, self.config.user, self.config.fingerprint, self.config.key_file)
        self.api_client = ApiClient(self.config, self.signer)

        self.blockstorage_api = apis.BlockstorageApi(self.api_client)
        self.compute_api = apis.ComputeApi(self.api_client)
        self.identity_api = apis.IdentityApi(self.api_client)
        self.vcn_ad_service_api = apis.VcnADServiceApi(self.api_client)
        self.vcn_service_api = apis.VcnServiceApi(self.api_client)
