# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

"""
This is a model deployment example using the Python-SDK
This script requires to do authentication, see details: https://docs.oracle.com/en-us/iaas/data-science/using/use-notebook-sessions.htm#signing-oci-apis
    + Using OCI configuration file:
        user = <your user_ocid>
        fingerprint = <your fingerprint>
        tenancy = <your tenancy_ocid>
        region = <region>
        key_file = <the path to the private key>
    + Or using the resource principal:
        Sample code:# import oci
                    # from oci.data_science import DataScienceClient
                    # rps = oci.auth.signers.get_resource_principals_signer()
                    # dsc = DataScienceClient(config={}, signer=rps)
A user needs to provide information below to set up and run the script (check #TODO)
    + config_file = <OCI configuration file>
    + compartment_id = <compartment ocid>
    + project_id = <project ocid>
    + model_id = <model ocid>
    + instance_shape_name = <instance shape name>
    + instance_count = <number of instances>
    + bandwidth_mbps = <load balancer bandwidth>
    + access_log_id = <access log ocid> -- optional
    + predict_log_id = <predict log ocid> -- optional
    + log_group_id = <log group ocid> -- optional
    + input_body = <input in json format for making prediction>
    + new_deployment_name = <new name for the model deployment to update a model deployment>
    + new_instance_shape_name = <new instance shape name to update a model deployment>
    + new_model_id = <new model ocid if you want to update a deployment with new model>
This script covers:
    + creating a model deployment
    + getting a model deployment info
    + making prediction using a model deployment url
    + updating an active model deployment with display name, instance shape name and model id
    + activating a model deployment
    + deactivating a model deployment
    + deleting a model deployment
For other use cases: see details in the documentation https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/api/data_science.html
"""

import oci
import oci.data_science as data_science
from oci.signer import Signer
from oci.data_science.models import CreateModelDeploymentDetails, ModelConfigurationDetails
from oci.data_science.models import InstanceConfiguration, FixedSizeScalingPolicy
from oci.data_science.models import UpdateModelDeploymentDetails, UpdateModelConfigurationDetails, UpdateSingleModelDeploymentConfigurationDetails
from oci.data_science.models import CategoryLogDetails, LogDetails, UpdateCategoryLogDetails
import json
import requests

# --- Set up
# TODO: Change the below variables to prepare for model deployment activities
config_file = "<config file>"  # '~/.oci/config'

# TODO: Change the compartment id and project id
compartment_id = "<compartment ocid>"
project_id = "<project ocid>"

# TODO: Change configuration details for deploying a model
deployment_name = "my_deployment"
model_id = "<model ocid>"
instance_shape_name = "VM.Standard2.1"
instance_count = 1
bandwidth_mbps = 10
# this is an option to set up logs for a model deployment. If no logs, setting log-related variables to an empty string
access_log_id = "<access log ocid>"
predict_log_id = "<predict log ocid>"
log_group_id = "<log group ocid>"

# TODO: Set the input to make a prediction using the newly created model deployment
input_body = "<input json format>"

# TODO: Change the variables for updating model deployment
new_deployment_name = "my_new_model_deployment"  # new name of the model deployment
new_instance_shape_name = "<new instance shape name to update a model deployment>"
new_model_id = "<new model ocid if you want to update a deployment with new model>"


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
            """
            Using resource principal, a user can take the identity of the resource (for example notebook session) and
               the notebook session has to be authorized to create a model deployment.
               auth = Signer.get_resource_principals_signer()
               data_science_client = DataScienceClient({}, signer=auth)
            Or using the OCI configuration file and API key as below:
            """
            # read oci_config file
            self.oci_config = oci.config.from_file(self.config_file, "DEFAULT")
            self.data_science_client = data_science.DataScienceClient(config=self.oci_config)
            print("Setting up a data science client succeeded!")
            self.data_science_composite_client = data_science.DataScienceClientCompositeOperations(self.data_science_client)
            print("Setting up a data science composite client succeeded!")
            self.auth = Signer(tenancy=self.oci_config['tenancy'], user=self.oci_config['user'], fingerprint=self.oci_config['fingerprint'], private_key_file_location=self.oci_config['key_file'], pass_phrase=self.oci_config['pass_phrase'])
        except Exception as e:
            print("Setting up a data science client failed!!!")
            raise e

    def create_model_deployment(self, deployment_name, instance_shape_name, instance_count, bandwidth_mbps, model_id, log_group_id=None, access_log_id=None, predict_log_id=None):
        # -- Create a model deployment
        print("------------------------------------")
        print("*** Creating a model deployment ...")
        try:
            self.deployment_name = deployment_name
            self.instance_configuration = InstanceConfiguration()  # model deployment instance configuration
            self.instance_configuration.instance_shape_name = instance_shape_name

            self.scaling_policy = FixedSizeScalingPolicy()  # the fixed size scaling policy for model deployment
            self.scaling_policy.instance_count = instance_count
            self.model_id = model_id
            self.bandwidth_mbps = bandwidth_mbps

            # create a model confifguration details object
            model_config_details = ModelConfigurationDetails(model_id=self.model_id, bandwidth_mbps=self.bandwidth_mbps, instance_configuration=self.instance_configuration, scaling_policy=self.scaling_policy)

            # create a model type deployment
            single_model_deployment_config_details = data_science.models.SingleModelDeploymentConfigurationDetails(deployment_type="SINGLE_MODEL", model_configuration_details=model_config_details)

            # set up parameters required to create a new model deployment.
            create_model_deployment_details = CreateModelDeploymentDetails(display_name=deployment_name, model_deployment_configuration_details=single_model_deployment_config_details, compartment_id=self.compartment_id, project_id=self.project_id)

            # for logging uncomment the line below
            # create_model_deployment_details.category_log_details = self.create_logging(log_group_id, access_log_id, predict_log_id, is_create = True)

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

    def get_model_deployment_info(self):
        # -- Get the model deployment info
        print("------------------------------------")
        print("*** Getting the model deployment details ... ")
        try:
            model_deployment = self.data_science_client.get_model_deployment(model_deployment_id=self.model_deployment_id)
            print(model_deployment.data)
            self.model_deployment_url = model_deployment.data.model_deployment_url
        except Exception as e:
            print("The model deployment has not created. Should run create_model_deployment method first!")
            raise e

    def make_prediction(self, input_body):
        # -- Make predictions
        print("------------------------------------")
        print("*** Making prediction ...")
        try:
            if self.model_deployment_url is None:
                self.get_model_deployment_info()
            prediction = requests.post(self.model_deployment_url + "/predict", data=json.dumps(input_body), auth=self.auth)  # make a prediction request
            if prediction.status_code == 200:
                print(prediction.json())
            else:
                print("Making predictions failed!!!")
        except Exception as e:
            print("Making predictions failed!!!")
            raise e

    def deactivate_model_deployment(self):
        # -- Deactivate a model deployment
        print("------------------------------------")
        print("*** Deactivating the model deployment ...")
        try:
            deactivate_model_deployment_response = self.data_science_composite_client.deactivate_model_deployment_and_wait_for_state(model_deployment_id=self.model_deployment_id, wait_for_states=["SUCCEEDED", "FAILED"])
            if deactivate_model_deployment_response.data.status == "SUCCEEDED":
                print("Deactivating the model deployment succeeded, model_deployment_id = ", self.model_deployment_id)
                self.active = False
            else:
                print("Deactivating the model deployment failed!!!")
        except Exception as e:
            print("Deactivating the model deployment failed!!!")
            raise e

    def activate_model_deployment(self):
        # -- Activate a model deployment
        print("------------------------------------")
        print("*** Activating the model deployment ...")
        try:
            if not self.active:
                activate_model_deployment_response = self.data_science_composite_client.activate_model_deployment_and_wait_for_state(model_deployment_id=self.model_deployment_id, wait_for_states=["SUCCEEDED", "FAILED"])
                if activate_model_deployment_response.data.status == "SUCCEEDED":
                    print("Activating the model deployment succeeded, model_deployment_id = ", self.model_deployment_id)
                    self.active = True
                else:
                    print("Activating the model deployment failed!!!")
        except Exception as e:
            print("Activating the model deployment failed!!!")
            raise e

    def update_model_deployment(self, new_deployment_name, new_instance_shape_name, new_model_id, log_group_id=None, access_log_id=None, predict_log_id=None):
        # -- Update a model deployment with changing display name, instance shape name, and model_id when the model deployment is active
        print("------------------------------------")
        print("*** Updating the model deployment ... ")
        self.model_deployment_name = new_deployment_name
        self.instance_configuration.instance_shape_name = new_instance_shape_name
        self.model_id = new_model_id
        try:
            update_model_config_details = UpdateModelConfigurationDetails(bandwidth_mbps=self.bandwidth_mbps, instance_configuration=self.instance_configuration, model_id=self.model_id, scaling_policy=self.scaling_policy)
            update_model_deployment_config_details = UpdateSingleModelDeploymentConfigurationDetails(deployment_type="SINGLE_MODEL", model_configuration_details=update_model_config_details)
            update_model_deployment_details = UpdateModelDeploymentDetails(display_name=self.model_deployment_name, model_deployment_configuration_details=update_model_deployment_config_details)

            # for logging, uncomment the line below
            # update_model_deployment_details.category_log_details = self.create_logging(log_group_id, access_log_id, predict_log_id, is_create=False)

            update_model_deployment_response = self.data_science_composite_client.update_model_deployment_and_wait_for_state(model_deployment_id=self.model_deployment_id, update_model_deployment_details=update_model_deployment_details, wait_for_states=["SUCCEEDED", "FAILED"])
            if update_model_deployment_response.data.status == "SUCCEEDED":
                print("Updating the model deployment succeeded, model_deployment_id = ", self.model_deployment_id)
            else:
                print("Updating the model deployment failed!!!")
        except Exception as e:
            print("Updating the model deployment failed!!!")
            raise e

    def delete_model_deployoment(self):
        # -- Delete the model deployment
        print("------------------------------------")
        print("*** Deleting the model deployment ... ")
        try:
            delete_model_deployment_response = self.data_science_composite_client.delete_model_deployment_and_wait_for_state(model_deployment_id=self.model_deployment_id, wait_for_states=["SUCCEEDED", "FAILED"])
            if delete_model_deployment_response.data.status == "SUCCEEDED":
                print("Deleting the model deployment succeeded, model_deployment_id = ", self.model_deployment_id)
                self.model_deployment_id = None
                self.model_deployment_name = None
                self.model_deployment_url = None
            else:
                print("Deleting the model deployment failed!!! ")
        except Exception as e:
            print("Deleting the model deployment failed!!!")
            raise e

    def create_logging(self, log_group_id, access_log_id, predict_log_id, is_create=True):
        try:
            access_log_details = LogDetails()
            access_log_details.log_id = access_log_id
            access_log_details.log_group_id = log_group_id

            predict_log_details = LogDetails()
            predict_log_details.log_id = predict_log_id
            predict_log_details.log_group_id = log_group_id

            if is_create:
                category_log_details = CategoryLogDetails()
                category_log_details.access = access_log_details
                category_log_details.predict = predict_log_details
                return category_log_details
            else:
                update_category_log_details = UpdateCategoryLogDetails()
                update_category_log_details.access = access_log_details
                update_category_log_details.predict = predict_log_details
                return update_category_log_details
        except Exception as e:
            print("Creating logs failed!!!")
            raise e


if __name__ == "__main__":
    """
    All variables can be specified above by user.
    A user can select the methods to run.
    """
    try:
        md = ModelDeployment(config_file, compartment_id, project_id)  # initialize a model deployment
        md.create_model_deployment(deployment_name, instance_shape_name, instance_count, bandwidth_mbps, model_id, log_group_id, access_log_id, predict_log_id)  # create a model deployment

        md.get_model_deployment_info()  # get a model deployment
        md.make_prediction(input_body)  # make a prediction using a newly created model deployment
        md.deactivate_model_deployment()  # deactivate a model deployment
        md.activate_model_deployment()  # activate a model deployment
        md.update_model_deployment(new_deployment_name, new_instance_shape_name, new_model_id, log_group_id, access_log_id, predict_log_id)  # update a model deployment configurations
        md.delete_model_deployoment()  # delete a model deployment
    except Exception as e:
        print("ERROR: ", e)
        if md.model_deployment_id is not None:
            print("*** Starting clean up ... ")
            md.delete_model_deployoment()
