# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.

import random
from . import util
import oci


class TestIdentity:

    def test_all_operations(self, identity, config):
        self.subtest_availability_domain_operations(identity, config)
        self.subtest_compartment_operations(identity, config)
        self.subtest_user_operations(identity, config)
        self.subtest_group_operations(identity, config)
        self.subtest_user_group_membership_operations(identity, config)
        self.subtest_api_key_operations(identity)
        self.subtest_ui_password_operations(identity)
        self.subtest_swift_password_operations(identity)
        self.subtest_policy_operations(identity, config)
        self.subtest_cleanup(identity, config)

    def subtest_availability_domain_operations(self, identity, config):
        result = identity.list_availability_domains(config['tenancy'])
        self.validate_response(result)

    def subtest_compartment_operations(self, identity, config):
        result = identity.list_compartments(config['tenancy'], limit=1000)
        self.validate_response(result)

        result = identity.get_compartment(util.COMPARTMENT_ID)
        self.validate_response(result, expect_etag=True)

        update_description = 'Compartment used by Python SDK integration tests. ' + str(random.randint(0, 1000000))
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

        result = identity.list_users(config['tenancy'], limit=1000)
        self.validate_response(result, extra_validation=self.validate_user)
        assert result.headers["opc-next-page"]

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
        self.validate_response(result, extra_validation=self.validate_group)

        self.group_description = 'UPDATED ' + self.user_description
        update_group_details = oci.identity.models.UpdateGroupDetails()
        update_group_details.description = self.group_description
        result = identity.update_group(self.group_ocid, update_group_details)
        self.validate_response(result, extra_validation=self.validate_group, expect_etag=True)

        result = identity.get_group(self.group_ocid)
        self.validate_response(result, extra_validation=self.validate_group, expect_etag=True)

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

    def subtest_policy_operations(self, identity, config):
        policy_name = util.random_name('python_sdk_test_policy')
        policy_description = 'Created by Python SDK identity tests.'

        statement_a = "Allow group {group_name} to inspect volume-family in compartment {compartment_name}".format(group_name=self.group_name, compartment_name=util.COMPARTMENT_NAME)
        statement_b = "Allow group {group_name} to inspect virtual-network-family in compartment {compartment_name}".format(
            group_name=self.group_name, compartment_name=util.COMPARTMENT_NAME)

        create_policy_details = oci.identity.models.CreatePolicyDetails()
        create_policy_details.name = policy_name
        create_policy_details.compartment_id = config['tenancy']
        create_policy_details.description = policy_description
        create_policy_details.statements = [statement_a]
        result = identity.create_policy(create_policy_details)
        policy_ocid = result.data.id
        self.validate_response(result, expect_etag=True)
        assert statement_a in result.data.statements

        # Update description only.
        policy_description = policy_description + "UPDATED!"
        update_policy_details = oci.identity.models.UpdatePolicyDetails()
        update_policy_details.description = policy_description
        result = identity.update_policy(policy_ocid, update_policy_details)
        self.validate_response(result, expect_etag=True)
        assert statement_a in result.data.statements

        statements = [statement_a, statement_b]
        version_date = "2016-01-01"

        # Update statements and version_date
        update_policy_details = oci.identity.models.UpdatePolicyDetails()
        update_policy_details.statements = statements
        update_policy_details.version_date = version_date
        result = identity.update_policy(policy_ocid, update_policy_details)
        self.validate_response(result, expect_etag=True)
        assert statement_a in result.data.statements
        assert statement_b in result.data.statements
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
        assert statement_a not in result.data.statements
        assert statement_b in result.data.statements
        assert not result.data.version_date

        # Set correct etag when updating description
        etag = result.headers['etag']
        policy_description = policy_description + " updated again"
        update_policy_details.description = policy_description
        result = identity.update_policy(policy_ocid, update_policy_details, if_match=etag)
        self.validate_response(result, expect_etag=True)
        assert policy_description in result.data.description
        assert statement_a not in result.data.statements
        assert statement_b in result.data.statements
        assert not result.data.version_date

        # Get policy
        result = identity.get_policy(policy_ocid)
        self.validate_response(result, expect_etag=True)
        assert policy_description in result.data.description
        assert statement_a not in result.data.statements
        assert statement_b in result.data.statements
        assert not result.data.version_date

        # List policies
        result = identity.list_policies(config['tenancy'], limit=1000)
        self.validate_response(result)
        found_policy = False
        for policy in result.data:
            if policy.id == policy_ocid:
                found_policy = True
                assert policy_description == policy.description
                assert statement_a not in policy.statements
                assert statement_b in policy.statements

        assert found_policy, "Expected policy was not found in response for list policies."

        result = identity.list_policies(config['tenancy'], limit=1)
        self.validate_response(result)
        assert len(result.data) == 1

        # Delete policy
        identity.delete_policy(policy_ocid)

    def subtest_cleanup(self, identity, config):
        identity.delete_user(self.user_ocid)

        result = identity.list_users(config['tenancy'], limit=1000)
        self.validate_response(result)
        for user in result.data:
            assert self.user_ocid != user.id

        identity.delete_group(self.group_ocid)

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
            found_user = False
            for user in result.data:
                if self.user_ocid == user.id:
                    found_user = True
                    assert self.user_name == user.name
                    assert self.user_description == user.description

            assert found_user, "Expected user not found in list of users"

        else:
            assert self.user_ocid == result.data.id
            assert self.user_name == result.data.name
            assert self.user_description == result.data.description

    def validate_response(self, result, extra_validation=None, expect_etag=False, ** args):
        def common_validation(result):
            if expect_etag:
                assert result.headers["etag"]

            if extra_validation:
                extra_validation(result)

        util.validate_response(result, extra_validation=common_validation, ** args)
