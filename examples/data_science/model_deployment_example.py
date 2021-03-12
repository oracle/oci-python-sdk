"""
This is a model deployment example using the Python-SDK
This script requires to have a configuration file and information for setting up the deployment:
    - The config file should include (more details: https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/configuration.html)
        user = <your user_ocid>
        fingerprint = <your fingerprint>
        tenancy = <your tenancy_ocid>
        region = <region>
        key_file = <the path to the private key>
    - User need to provide information to set up the script
        + config_file = <your config file>
        + compartment_id = <compartment_ocid>
        + project_id = <project_ocid>
        + model_id = <model_ocid>
        + input_body = <json file for prediction>
        + new_display_name = <new name for the model deployment if you want to update model deployment>
        + instance_configuration.instance_shape_name = <new instance shape name if you want to update model deployment>
        + new_model_id = <new model id if you want to update the deployment with new model>
This script shows: creating a model deployment
                    getting a model deployment info
                    making prediction using a model deployment url
                    updating a model deployment with display name, instance shape name and model id when a deployment is active
                    activating a model deployment
                    deactivating a model deployment
                    deleting a model deployment
For other use cases: see details in the documentation https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/api/data_science.html
"""
import oci
import oci.data_science as data_science
from oci.signer import Signer
from oci.data_science.models import CreateModelDeploymentDetails, ModelConfigurationDetails
from oci.data_science.models import InstanceConfiguration, FixedSizeScalingPolicy
from oci.data_science.models import UpdateModelDeploymentDetails, UpdateModelConfigurationDetails, UpdateSingleModelDeploymentConfigurationDetails
import json
import requests

# --- Set up
# TODO: Change the below variables to prepare for model deployment activities
config_file = <oci configuration file> #'~/.oci/config' 

# TODO: Change the compartment id and project id
compartment_id = <compartment ocid>
project_id = <project ocid>

# TODO: Change configuration details for deploying a model
deployment_name = "my_deployment"
model_id = <model_ocid>
instance_shape_name = "VM.Standard2.1"
instance_count = 1
bandwidth_mbps = 10

# TODO: Set the input to make a prediction using the newly created model deployment
input_body = <input json format>

# TODO: Change the variables for updating model deployment
new_deployment_name = "my_new_model_deployment" # new name of the model deployment
new_instance_shape_name = "VM.Standard2.2" # instance shape name
new_model_id = <new model_ocid>

class ModelDeployment:
    def __init__(self, config_file, compartment_id, project_id):
        self.model_deployment_id = None
        self.config_file = config_file
        self.compartment_id = compartment_id
        self.project_id = project_id
        self.active = False
        # -- Create data science client and data science composite client with oci config to organize your work
        try:
            print("*** Setting up data science client....")
            # read oci_config file
            self.oci_config = oci.config.from_file(self.config_file, "DEFAULT")
            self.data_science_client = data_science.DataScienceClient(config=self.oci_config)
            print("Setting up a data science client succeeded!")
            self.data_science_composite_client = data_science.DataScienceClientCompositeOperations(self.data_science_client)
            print("Setting up a data science composite client succeeded!")
            self.auth = Signer(tenancy=self.oci_config['tenancy'], user=self.oci_config['user'], fingerprint=self.oci_config['fingerprint'],
                          private_key_file_location=self.oci_config['key_file'], pass_phrase=self.oci_config['pass_phrase'])
        except Exception as e:
            print("Setting up a data science client failed!!!")
            raise e

    def create_model_deployment(self, deployment_name, instance_shape_name, instance_count, bandwidth_mbps, model_id):
        # -- Create a model deployment
        print ("------------------------------------")
        print ("*** Creating a model deployment ...")
        try:
            self.deployment_name = deployment_name
            self.instance_configuration = InstanceConfiguration() # model deployment instance configuration
            self.instance_configuration.instance_shape_name = instance_shape_name

            self.scaling_policy = FixedSizeScalingPolicy() # the fixed size scaling policy for model deployment
            self.scaling_policy.instance_count = instance_count
            self.model_id = model_id
            self.bandwidth_mbps = bandwidth_mbps
            # create a model confifguration details object
            model_config_details = ModelConfigurationDetails(model_id=self.model_id, bandwidth_mbps=self.bandwidth_mbps, instance_configuration=self.instance_configuration, scaling_policy=self.scaling_policy)

            # create a model type deployment
            single_model_deployment_config_details = data_science.models.SingleModelDeploymentConfigurationDetails(deployment_type="SINGLE_MODEL", model_configuration_details=model_config_details)

            # set up parameters required to create a new model deployment.
            create_model_deployment_details = CreateModelDeploymentDetails(display_name=deployment_name, model_deployment_configuration_details=single_model_deployment_config_details, compartment_id=self.compartment_id, project_id=self.project_id)

            # create a model deployment with data science composite client
            create_model_deployment_response = self.data_science_composite_client.create_model_deployment_and_wait_for_state(create_model_deployment_details=create_model_deployment_details, wait_for_states=["SUCCEEDED", "FAILED"])
            work_request_resources = create_model_deployment_response.data.resources
            self.model_deployment_id = work_request_resources[0].identifier
            if create_model_deployment_response.data.status == "SUCCEEDED":
                print("Creating a model deployment succeeded!")
                self.active = True
            else:
                print("Creating a model deployment failed!!!")
        except Exception as e:
            print("Creating a model deployment failed!!!")
            raise e

    def get_model_deployment_info (self):
        #-- Get the model deployment info
        print("------------------------------------")
        print("*** Getting the model deployment details ... ")
        try:
            model_deployment = self.data_science_client.get_model_deployment(model_deployment_id=self.model_deployment_id)
            print (model_deployment.data)
            self.model_deployment_url = model_deployment.data.model_deployment_url
        except Exception as e:
            print("The model deployment has not created. Should run create_model_deployment method first!")
            raise e

    def make_prediction(self, input_body):
        #-- Make predictions
        print("------------------------------------")
        print("*** Making prediction ...")
        try:
            if self.model_deployment_url is None:
                self.get_model_deployment_info()
            prediction = requests.post(self.model_deployment_url+"/predict", data=json.dumps(input_body), auth=self.auth) # make a prediction request
            if prediction.status_code == 200:
                print (prediction.json())
            else:
                print ("Making predictions failed!!!")
        except Exception as e:
            print ("Making predictions failed!!!")
            raise e

    def deactivate_model_deployment(self):
        #-- Deactivate a model deployment
        print("------------------------------------")
        print("*** Deactivating the model deployment ...")
        try:
            deactivate_model_deployment_response = self.data_science_composite_client.deactivate_model_deployment_and_wait_for_state(model_deployment_id=self.model_deployment_id, wait_for_states=["SUCCEEDED", "FAILED"])
            if deactivate_model_deployment_response.data.status == "SUCCEEDED":
                print ("Deactivating the model deployment succeeded, model_deployment_id = ", self.model_deployment_id)
                self.active = False
            else:
                print ("Deactivating the model deployment failed!!!")
        except Exception as e:
            print ("Deactivating the model deployment failed!!!")
            raise e

    def activate_model_deployment(self):
        #-- Activate a model deployment
        print("------------------------------------")
        print("*** Activating the model deployment ...")
        try:
            if self.active == False:
                activate_model_deployment_response = self.data_science_composite_client.activate_model_deployment_and_wait_for_state(
                    model_deployment_id=self.model_deployment_id,
                    wait_for_states=["SUCCEEDED", "FAILED"])
                if activate_model_deployment_response.data.status == "SUCCEEDED":
                    print("Activating the model deployment succeeded, model_deployment_id = ", self.model_deployment_id)
                    self.active = True
                else:
                    print("Activating the model deployment failed!!!")
        except Exception as e:
            print("Activating the model deployment failed!!!")
            raise e

    def update_model_deployment (self, new_deployment_name, new_instance_shape_name, new_model_id):
        #-- Update a model deployment with changing display name, instance shape name, and model_id when the model deployment is active
        print("------------------------------------")
        print("*** Updating the model deployment ... ")
        self.model_deployment_name = new_deployment_name
        self.instance_configuration.instance_shape_name = new_instance_shape_name
        self.model_id = new_model_id
        try:
            update_model_config_details = UpdateModelConfigurationDetails(bandwidth_mbps=self.bandwidth_mbps, instance_configuration=self.instance_configuration, model_id=self.model_id, scaling_policy=self.scaling_policy)
            update_model_deployment_config_details = UpdateSingleModelDeploymentConfigurationDetails(deployment_type="SINGLE_MODEL", model_configuration_details=update_model_config_details)
            update_model_deployment_details = UpdateModelDeploymentDetails(display_name=self.model_deployment_name, model_deployment_configuration_details=update_model_deployment_config_details)
            update_model_deployment_response = self.data_science_composite_client.update_model_deployment_and_wait_for_state(model_deployment_id=self.model_deployment_id, update_model_deployment_details=update_model_deployment_details, wait_for_states=["SUCCEEDED", "FAILED"])
            if update_model_deployment_response.data.status == "SUCCEEDED":
                print("Updating the model deployment succeeded, model_deployment_id = ", self.model_deployment_id)
            else:
                print("Updating the model deployment failed!!!")
        except Exception as e:
            print("Updating the model deployment failed!!!")
            raise e

    def delete_model_deployoment(self):
        #-- Delete the model deployment
        print("------------------------------------")
        print("*** Deleting the model deployment ... ")
        try:
            delete_model_deployment_response = self.data_science_composite_client.delete_model_deployment_and_wait_for_state(model_deployment_id=self.model_deployment_id, wait_for_states=["SUCCEEDED", "FAILED"])
            if delete_model_deployment_response.data.status == "SUCCEEDED":
                print ("Deleting the model deployment succeeded, model_deployment_id = ", self.model_deployment_id)
                self.model_deployment_id = None
                self.model_deployment_name = None
                self.model_deployment_url = None
            else:
                print ("Deleting the model deployment failed!!! ")
        except Exception as e:
            print ("Deleting the model deployment failed!!!")
            raise e
if __name__ == "__main__":
    """
    All variables can be specified above by user.
    A user can select the methods to run.
    """
    try:
        md = ModelDeployment(config_file, compartment_id, project_id) # initialize a model deployment
        md.create_model_deployment(deployment_name, instance_shape_name, instance_count, bandwidth_mbps, model_id) # create a model deployment
        md.get_model_deployment_info() # get a model deployment
        md.make_prediction(input_body) # make a prediction using a newly created model deployment
        md.deactivate_model_deployment() # deactivate a model deployment
        md.activate_model_deployment() # activate a model deployment
        md.update_model_deployment(new_deployment_name, new_instance_shape_name, new_model_id) # update a model deployment configurations
        md.delete_model_deployoment() # delete a model deployment
    except Exception as e:
        print("ERROR: ", e)
        if md.model_deployment_id is not None:
            print ("*** Starting clean up ... ")
            md.delete_model_deployoment()





