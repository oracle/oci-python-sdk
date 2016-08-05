# coding: utf-8

"""
This is a modified version of the same template from swagger-codegen.
The original can be found at https://github.com/swagger-api/swagger-codegen.
The original license is below.

    Copyright 2016 SmartBear Software

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Ref: https://github.com/swagger-api/swagger-codegen
"""

from __future__ import absolute_import

# python 2 and python 3 compatibility library
from six import iteritems

class VcnADServiceApi(object):

    def __init__(self, api_client):
        self.api_client = api_client


    def get_vnic(self, vnic_id, **kwargs):
        """
        GetVnic
        Gets the information for the specified Virtual Network Interface Card (VNIC), including the attached\ninstance's public and private IP addresses. Each instance automatically has a VNIC attached to it,\nand the VNIC connects the instance to the subnet. You can get the instance's VNIC OCID from the\nCloud Compute Service's [ListVnicAttachments](#listVnicAttachments) operation.\n

        :param str vnic_id: The VNIC's OCID. (required)
        :return: Vnic
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['vnic_id']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_vnic" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'vnic_id' is set
        if ('vnic_id' not in params) or (params['vnic_id'] is None):
            raise ValueError("Missing the required parameter `vnic_id` when calling `get_vnic`")

        resource_path = '/vnics/{vnicId}'
        path_params = {}
        if 'vnic_id' in params:
            path_params['vnicId'] = params['vnic_id']

        query_params = {}

        header_params = {}

        body_params = None

        header_params['accept'] = 'application/json'
        header_params['content-type'] = 'application/json'

        response = self.api_client.call_api(self.api_client.config.endpoint_vcn_ad_service_api,
                                            resource_path,
                                            'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            response_type='Vnic')
        return response
