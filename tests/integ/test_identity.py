# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from . import util
from .. import test_config_container
import oci
import time

from .. import util as top_level_utils


class TestIdentity:

    RENAME_COMPARTMENT_PREFIX = 'PythonSDKTestCompartment-rename-'

    def test_all_operations(self, identity, config):
        with test_config_container.create_vcr().use_cassette('test_identity_all_operations.yml'):
            try:
                self.subtest_availability_domain_operations(identity, config)
                self.subtest_compartment_operations(identity, config)
                self.subtest_user_operations(identity, config)
                self.subtest_group_operations(identity, config)
                self.subtest_dynamic_group_operations(identity, config)
                self.subtest_user_group_membership_operations(identity, config)
                self.subtest_api_key_operations(identity)
                self.subtest_ui_password_operations(identity)
                self.subtest_swift_password_operations(identity)
                self.subtest_policy_operations(identity, config)
                self.subtest_compartment_rename(identity, config)
                self.subtest_smtp_credential_crud(identity, config)
            finally:
                self.subtest_cleanup(identity, config)

    def subtest_availability_domain_operations(self, identity, config):
        result = identity.list_availability_domains(config['tenancy'])
        self.validate_response(result)

    def subtest_compartment_operations(self, identity, config):
        result = identity.list_compartments(config['tenancy'], limit=1000)
        self.validate_response(result)

        result = identity.get_compartment(util.COMPARTMENT_ID)
        self.validate_response(result, expect_etag=True)

        update_description = 'Compartment used by Python SDK integration tests. {}'.format(top_level_utils.random_number_string())
        update_compartment_details = oci.identity.models.UpdateCompartmentDetails()
        update_compartment_details.description = update_description
        result = identity.update_compartment(util.COMPARTMENT_ID, update_compartment_details)

        self.validate_response(result, expect_etag=True)
        assert update_description == result.data.description

    def subtest_user_operations(self, identity, config):
        self.user_name = util.random_name('python_sdk_test_user')
        self.user_description = 'Created by Python SDK identity tests.'

        create_user_details = oci.identity.models.CreateUserDetails()
        create_user_details.name = self.user_name
        create_user_details.description = self.user_description
        create_user_details.compartment_id = config['tenancy']

        result = identity.create_user(create_user_details)
        self.user_ocid = result.data.id
        self.validate_response(result, extra_validation=self.validate_user, expect_etag=True)

        all_users_args = {'compartment_id': config['tenancy'], 'limit': 1000}
        all_users = util.get_all_pages(identity.list_users, ** all_users_args)
        self.validate_user_in_list(all_users)

        self.user_description = 'UPDATED ' + self.user_description
        update_user_details = oci.identity.models.UpdateUserDetails()
        update_user_details.description = self.user_description
        result = identity.update_user(self.user_ocid, update_user_details)
        self.validate_response(result, extra_validation=self.validate_user, expect_etag=True)

        update_state_details = oci.identity.models.UpdateStateDetails()
        update_state_details.blocked = False
        result = identity.update_user_state(self.user_ocid, update_state_details)
        self.validate_response(result, extra_validation=self.validate_user, expect_etag=True)

        result = identity.get_user(self.user_ocid)
        self.validate_response(result, extra_validation=self.validate_user, expect_etag=True)

    def subtest_group_operations(self, identity, config):
        self.group_name = util.random_name('python_sdk_test_group')
        self.group_description = 'Created by Python SDK identity tests.'

        create_group_details = oci.identity.models.CreateGroupDetails()
        create_group_details.name = self.group_name
        create_group_details.description = self.group_description
        create_group_details.compartment_id = config['tenancy']

        result = identity.create_group(create_group_details)
        self.group_ocid = result.data.id
        self.validate_response(result, extra_validation=self.validate_group, expect_etag=True)

        result = identity.list_groups(config['tenancy'], limit=1000)
        assert len(result.data) > 0
        self.validate_response(result)

        self.group_description = 'UPDATED ' + self.user_description
        update_group_details = oci.identity.models.UpdateGroupDetails()
        update_group_details.description = self.group_description
        result = identity.update_group(self.group_ocid, update_group_details)
        self.validate_response(result, extra_validation=self.validate_group, expect_etag=True)

        result = identity.get_group(self.group_ocid)
        self.validate_response(result, extra_validation=self.validate_group, expect_etag=True)

    def subtest_dynamic_group_operations(self, identity, config):
        dynamic_group_name = util.random_name('py_sdk_dynamic_group')
        dynamic_group_description = 'Created by Python SDK identity tests'

        create_group_details = oci.identity.models.CreateDynamicGroupDetails(
            compartment_id=config['tenancy'],
            name=dynamic_group_name,
            description=dynamic_group_description,
            matching_rule='ANY{{instance.compartment.id=\'{}\'}}'.format(util.COMPARTMENT_ID)
        )

        result = identity.create_dynamic_group(create_group_details)
        self.validate_response(result, expect_etag=True)
        assert result.data.id is not None
        self.dynamic_group_id = result.data.id
        assert create_group_details.name == result.data.name
        assert create_group_details.description == result.data.description
        assert create_group_details.matching_rule == result.data.matching_rule
        assert create_group_details.compartment_id == result.data.compartment_id

        update_group_details = oci.identity.models.UpdateDynamicGroupDetails(
            description='An updated description',
            matching_rule='ANY{{instance.compartment.id=\'{}\'}}'.format(config['tenancy'])
        )

        result = identity.update_dynamic_group(self.dynamic_group_id, update_group_details)
        self.validate_response(result, expect_etag=True)
        assert create_group_details.name == result.data.name
        assert update_group_details.description == result.data.description
        assert update_group_details.matching_rule == result.data.matching_rule

        result = identity.get_dynamic_group(self.dynamic_group_id)
        assert create_group_details.name == result.data.name
        assert update_group_details.description == result.data.description
        assert update_group_details.matching_rule == result.data.matching_rule
        assert create_group_details.compartment_id == result.data.compartment_id

        all_dynamic_groups_response = oci.pagination.list_call_get_all_results(identity.list_dynamic_groups, config['tenancy'])
        found_group = False
        for dg in all_dynamic_groups_response.data:
            if dg.id == self.dynamic_group_id:
                assert create_group_details.name == dg.name
                assert update_group_details.description == dg.description
                assert update_group_details.matching_rule == dg.matching_rule
                assert create_group_details.compartment_id == dg.compartment_id
                found_group = True
                break
        assert found_group

    def subtest_user_group_membership_operations(self, identity, config):
        add_user_to_group_details = oci.identity.models.AddUserToGroupDetails()
        add_user_to_group_details.group_id = self.group_ocid
        add_user_to_group_details.user_id = self.user_ocid
        result = identity.add_user_to_group(add_user_to_group_details)
        self.validate_response(result, expect_etag=True)

        result = identity.list_user_group_memberships(config['tenancy'], user_id=self.user_ocid)
        self.validate_response(result)
        assert len(result.data) == 1
        membership_ocid = result.data[0].id

        identity.remove_user_from_group(membership_ocid)
        self.validate_response(result)

        result = identity.list_user_group_memberships(config['tenancy'], user_id=self.user_ocid)
        self.validate_response(result)
        assert len(result.data) == 0

    def subtest_api_key_operations(self, identity):
        public_key = """-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA0j0c6GtzuzSBGCT8D/nj
yFtYIl5hsySErWQt/+eSm9bhSMpPBXdNNw/4StMfdtyDlJS6jNDwPAOXXTOU149m
j+CQKiqphy1gawtgMc7riDNA8ufLZ3TisCeXcaC5N/InR7OfERovi2jckB78luXm
jA9txdv1xDcd1akKoHiq7RPlmZnLlPfXzUA0LdppAM0t5poZeeR0l6t/ytWgSxQt
wy9vTSr5jUrHkY1QgKjNmgcRHvIjMSJxOozBiPmFuckuJtOfh+r8jctoLmykB0JY
P8ZM9xRukuJ4bnPTe8olOFB8UCCkAEmkUxtZI4vF90HvDKDOV0KY4OH5YESY6apH
3QIDAQAB
-----END PUBLIC KEY-----"""

        create_api_key_details = oci.identity.models.CreateApiKeyDetails()
        create_api_key_details.key = public_key
        result = identity.upload_api_key(self.user_ocid, create_api_key_details)
        self.validate_response(result)

        result = identity.list_api_keys(self.user_ocid)
        self.validate_response(result)
        assert len(result.data) == 1
        fingerprint = result.data[0].fingerprint

        identity.delete_api_key(self.user_ocid, fingerprint)

    def subtest_ui_password_operations(self, identity):
        result = identity.create_or_reset_ui_password(self.user_ocid)
        self.validate_response(result)
        password = result.data.password
        assert len(password) > 5

        # Get a new password, verify that it has changed.
        result = identity.create_or_reset_ui_password(self.user_ocid)
        self.validate_response(result)
        assert password != result.data.password

    def subtest_swift_password_operations(self, identity):
        description = "Password created by Python SDK integration tests."
        create_swift_password_details = oci.identity.models.CreateSwiftPasswordDetails()
        create_swift_password_details.description = description
        result = identity.create_swift_password(create_swift_password_details, self.user_ocid)
        self.validate_response(result, expect_etag=True)
        password_ocid = result.data.id
        password = result.data.password
        assert len(password) > 5
        assert description == result.data.description

        description = description + " UPDATED"
        update_swift_password_details = oci.identity.models.UpdateSwiftPasswordDetails()
        update_swift_password_details.description = description
        result = identity.update_swift_password(self.user_ocid, password_ocid, update_swift_password_details)
        self.validate_response(result, expect_etag=True)
        assert description == result.data.description

        result = identity.list_swift_passwords(self.user_ocid)
        self.validate_response(result)
        assert 1 == len(result.data)

        identity.delete_swift_password(self.user_ocid, password_ocid)

    def subtest_auth_token_operations(self, identity):
        description = "Password created by Python SDK integration tests."
        create_auth_token_details = oci.identity.models.CreateAuthTokenDetails()
        create_auth_token_details.description = description
        result = identity.create_auth_token(create_auth_token_details, self.user_ocid)
        self.validate_response(result, expect_etag=True)
        password_ocid = result.data.id
        password = result.data.password
        assert len(password) > 5
        assert description == result.data.description

        description = description + " UPDATED"
        update_auth_token_details = oci.identity.models.UpdateAuthTokenDetails()
        update_auth_token_details.description = description
        result = identity.update_auth_token(self.user_ocid, password_ocid, update_auth_token_details)
        self.validate_response(result, expect_etag=True)
        assert description == result.data.description

        result = identity.list_auth_tokens(self.user_ocid)
        self.validate_response(result)
        assert 1 == len(result.data)

        identity.delete_auth_token(self.user_ocid, password_ocid)

    def subtest_policy_operations(self, identity, config):
        policy_name = util.random_name('python_sdk_test_policy')
        policy_description = 'Created by Python SDK identity tests.'

        statement_a_base = 'Allow group {} to inspect volume-family in compartment'.format(self.group_name)
        statement_a = "{policy_base} {compartment_name}".format(policy_base=statement_a_base, compartment_name=util.COMPARTMENT_NAME)

        statement_b_base = 'Allow group {} to inspect virtual-network-family in compartment'.format(self.group_name)
        statement_b = "{policy_base} {compartment_name}".format(policy_base=statement_b_base, compartment_name=util.COMPARTMENT_NAME)

        create_policy_details = oci.identity.models.CreatePolicyDetails()
        create_policy_details.name = policy_name
        create_policy_details.compartment_id = config['tenancy']
        create_policy_details.description = policy_description
        create_policy_details.statements = [statement_a]
        result = identity.create_policy(create_policy_details)
        policy_ocid = result.data.id
        self.validate_response(result, expect_etag=True)
        self.check_policy_statements_case_insensitive(statement_a_base, result.data.statements)

        # Update description only.
        policy_description = policy_description + "UPDATED!"
        update_policy_details = oci.identity.models.UpdatePolicyDetails()
        update_policy_details.description = policy_description
        result = identity.update_policy(policy_ocid, update_policy_details)
        self.validate_response(result, expect_etag=True)
        self.check_policy_statements_case_insensitive(statement_a_base, result.data.statements)

        statements = [statement_a, statement_b]
        version_date = "2016-01-01"

        # Update statements and version_date
        update_policy_details = oci.identity.models.UpdatePolicyDetails()
        update_policy_details.statements = statements
        update_policy_details.version_date = version_date
        result = identity.update_policy(policy_ocid, update_policy_details)
        self.validate_response(result, expect_etag=True)
        self.check_policy_statements_case_insensitive(statement_a_base, result.data.statements)
        self.check_policy_statements_case_insensitive(statement_b_base, result.data.statements)
        assert version_date in result.data.version_date.isoformat()

        etag = result.headers['etag']
        # Set incorrect etag when updating statements
        update_policy_details = oci.identity.models.UpdatePolicyDetails()
        update_policy_details.statements = statements
        update_policy_details.version_date = version_date
        try:
            identity.update_policy(policy_ocid, update_policy_details, if_match='incorrect_etag')
        except Exception as error:
            assert error.code == 'NoEtagMatch'

        # Set incorrect etag when updating description
        policy_description = policy_description + " updated again"
        update_policy_details = oci.identity.models.UpdatePolicyDetails()
        update_policy_details.description = policy_description
        try:
            identity.update_policy(policy_ocid, update_policy_details, if_match='incorrect_etag')
        except Exception as error:
            assert error.code == 'NoEtagMatch'

        # Set correct etag when updating statements.
        # Remove statement a, clear the version date
        statements = [statement_b]
        update_policy_details = oci.identity.models.UpdatePolicyDetails()
        update_policy_details.statements = statements
        result = identity.update_policy(policy_ocid, update_policy_details, if_match=etag)
        self.validate_response(result, expect_etag=True)
        self.check_policy_statements_case_insensitive(statement_a_base, result.data.statements, check_not_in=True)
        self.check_policy_statements_case_insensitive(statement_b_base, result.data.statements)
        assert not result.data.version_date

        # Set correct etag when updating description
        etag = result.headers['etag']
        policy_description = policy_description + " updated again"
        update_policy_details.description = policy_description
        result = identity.update_policy(policy_ocid, update_policy_details, if_match=etag)
        self.validate_response(result, expect_etag=True)
        assert policy_description in result.data.description
        self.check_policy_statements_case_insensitive(statement_a_base, result.data.statements, check_not_in=True)
        self.check_policy_statements_case_insensitive(statement_b_base, result.data.statements)
        assert not result.data.version_date

        # Get policy
        result = identity.get_policy(policy_ocid)
        self.validate_response(result, expect_etag=True)
        assert policy_description in result.data.description
        self.check_policy_statements_case_insensitive(statement_a_base, result.data.statements, check_not_in=True)
        self.check_policy_statements_case_insensitive(statement_b_base, result.data.statements)
        assert not result.data.version_date

        # List policies
        result = identity.list_policies(config['tenancy'], limit=1000)
        self.validate_response(result)
        found_policy = False
        for policy in result.data:
            if policy.id == policy_ocid:
                found_policy = True
                assert policy_description == policy.description
                self.check_policy_statements_case_insensitive(statement_a_base, policy.statements, check_not_in=True)
                self.check_policy_statements_case_insensitive(statement_b_base, policy.statements)

        assert found_policy, "Expected policy was not found in response for list policies."

        result = identity.list_policies(config['tenancy'], limit=1)
        self.validate_response(result)
        assert len(result.data) == 1

        # Delete policy
        identity.delete_policy(policy_ocid)

    def subtest_compartment_rename(self, identity, config):
        compartment_to_rename_id = self.find_compartment_to_rename(identity, config)

        update_compartment_details = oci.identity.models.UpdateCompartmentDetails()
        update_compartment_details.description = 'Updated compartment {}'.format(top_level_utils.random_number_string())
        update_compartment_details.name = '{}{}'.format(self.RENAME_COMPARTMENT_PREFIX, top_level_utils.random_number_string())

        update_compartment_response = identity.update_compartment(compartment_to_rename_id, update_compartment_details)

        assert compartment_to_rename_id == update_compartment_response.data.id
        assert update_compartment_details.name == update_compartment_response.data.name
        assert update_compartment_details.description == update_compartment_response.data.description
        assert update_compartment_response.request_id is not None
        assert update_compartment_response.headers["etag"]

    def subtest_smtp_credential_crud(self, identity, config):
        create_smtp_credential_response = identity.create_smtp_credential(
            oci.identity.models.CreateSmtpCredentialDetails(
                description='new credential'
            ),
            user_id=self.user_ocid
        )
        assert create_smtp_credential_response.request_id
        assert create_smtp_credential_response.data.id
        assert create_smtp_credential_response.data.username
        assert create_smtp_credential_response.data.password
        assert create_smtp_credential_response.data.user_id == self.user_ocid
        assert create_smtp_credential_response.data.description == 'new credential'
        assert create_smtp_credential_response.data.time_created
        assert create_smtp_credential_response.data.lifecycle_state

        update_smtp_credential_response = identity.update_smtp_credential(
            self.user_ocid,
            create_smtp_credential_response.data.id,
            oci.identity.models.UpdateSmtpCredentialDetails(
                description='updated credential description'
            )
        )
        assert update_smtp_credential_response.request_id
        assert update_smtp_credential_response.data.username == create_smtp_credential_response.data.username
        assert update_smtp_credential_response.data.user_id == self.user_ocid
        assert update_smtp_credential_response.data.description == 'updated credential description'
        assert update_smtp_credential_response.data.time_created == create_smtp_credential_response.data.time_created
        assert update_smtp_credential_response.data.lifecycle_state

        list_response = identity.list_smtp_credentials(self.user_ocid)
        assert list_response.request_id
        assert len(list_response.data) == 1
        assert list_response.data[0] == update_smtp_credential_response.data

        delete_response = identity.delete_smtp_credential(self.user_ocid, create_smtp_credential_response.data.id)
        assert delete_response.request_id

    def subtest_cleanup(self, identity, config):
        if self.user_ocid:
            identity.delete_user(self.user_ocid)

            result = identity.list_users(config['tenancy'], limit=1000)
            self.validate_response(result)
            for user in result.data:
                assert self.user_ocid != user.id

        if self.group_ocid:
            identity.delete_group(self.group_ocid)

        if hasattr(self, 'dynamic_group_id'):
            identity.delete_dynamic_group(self.dynamic_group_id)

    def validate_group(self, result):
        if hasattr(result.data, '__len__'):
            found_group = False
            for group in result.data:
                if self.group_ocid == group.id:
                    found_group = True
                    assert self.group_name == group.name
                    assert self.group_description == group.description

            assert found_group, "Expected group not found in list of groups"

        else:
            assert self.group_ocid == result.data.id
            assert self.group_name == result.data.name
            assert self.group_description == result.data.description

    def validate_user(self, result):
        if hasattr(result.data, '__len__'):
            self.validate_user_in_list(result.data)
        else:
            assert self.user_ocid == result.data.id
            assert self.user_name == result.data.name
            assert self.user_description == result.data.description

    def validate_user_in_list(self, user_list):
        found_user = False
        for user in user_list:
            if self.user_ocid == user.id:
                found_user = True
                assert self.user_name == user.name
                assert self.user_description == user.description

        assert found_user, "Expected user not found in list of users"

    def validate_response(self, result, extra_validation=None, expect_etag=False, ** args):
        def common_validation(result):
            if expect_etag:
                assert result.headers["etag"]

            if extra_validation:
                extra_validation(result)

        util.validate_response(result, extra_validation=common_validation, ** args)

    def check_policy_statements_case_insensitive(self, policy_base, statements, check_not_in=False):
        match_found = False
        for statement in statements:
            if statement.find(policy_base) == 0:
                match_found = True
                break

        if check_not_in:
            assert not match_found, 'Expected to not find {} in {}'.format(policy_base, statements)
        else:
            assert match_found, 'Expected to find {} in {}'.format(policy_base, statements)

    def find_compartment_to_rename(self, identity, config):
        keep_paginating = True
        next_page = None
        kwargs = {'limit': 1000}
        while keep_paginating:
            if next_page is not None:
                kwargs['page'] = next_page
            list_compartments_result = identity.list_compartments(config['tenancy'], **kwargs)

            for compartment in list_compartments_result.data:
                if compartment.name.find(self.RENAME_COMPARTMENT_PREFIX) == 0:
                    return compartment.id

            next_page = list_compartments_result.next_page
            keep_paginating = (next_page is not None)

        # Exhausted all pages of compartments without finding the one to rename, so create it
        create_compartment_details = oci.identity.models.CreateCompartmentDetails()
        create_compartment_details.compartment_id = config['tenancy']
        create_compartment_details.description = 'Compartment for Python SDK Rename Compartment Test'
        create_compartment_details.name = '{}{}'.format(self.RENAME_COMPARTMENT_PREFIX, int(time.time()))

        create_compartment_response = identity.create_compartment(create_compartment_details)
        return create_compartment_response.data.id
