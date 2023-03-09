# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class User(object):
    """
    User Account
    """

    #: A constant which can be used with the idcs_prevented_operations property of a User.
    #: This constant has a value of "replace"
    IDCS_PREVENTED_OPERATIONS_REPLACE = "replace"

    #: A constant which can be used with the idcs_prevented_operations property of a User.
    #: This constant has a value of "update"
    IDCS_PREVENTED_OPERATIONS_UPDATE = "update"

    #: A constant which can be used with the idcs_prevented_operations property of a User.
    #: This constant has a value of "delete"
    IDCS_PREVENTED_OPERATIONS_DELETE = "delete"

    #: A constant which can be used with the user_type property of a User.
    #: This constant has a value of "Contractor"
    USER_TYPE_CONTRACTOR = "Contractor"

    #: A constant which can be used with the user_type property of a User.
    #: This constant has a value of "Employee"
    USER_TYPE_EMPLOYEE = "Employee"

    #: A constant which can be used with the user_type property of a User.
    #: This constant has a value of "Intern"
    USER_TYPE_INTERN = "Intern"

    #: A constant which can be used with the user_type property of a User.
    #: This constant has a value of "Temp"
    USER_TYPE_TEMP = "Temp"

    #: A constant which can be used with the user_type property of a User.
    #: This constant has a value of "External"
    USER_TYPE_EXTERNAL = "External"

    #: A constant which can be used with the user_type property of a User.
    #: This constant has a value of "Service"
    USER_TYPE_SERVICE = "Service"

    #: A constant which can be used with the user_type property of a User.
    #: This constant has a value of "Generic"
    USER_TYPE_GENERIC = "Generic"

    def __init__(self, **kwargs):
        """
        Initializes a new User object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this User.
        :type id: str

        :param ocid:
            The value to assign to the ocid property of this User.
        :type ocid: str

        :param schemas:
            The value to assign to the schemas property of this User.
        :type schemas: list[str]

        :param meta:
            The value to assign to the meta property of this User.
        :type meta: oci.identity_domains.models.Meta

        :param idcs_created_by:
            The value to assign to the idcs_created_by property of this User.
        :type idcs_created_by: oci.identity_domains.models.IdcsCreatedBy

        :param idcs_last_modified_by:
            The value to assign to the idcs_last_modified_by property of this User.
        :type idcs_last_modified_by: oci.identity_domains.models.IdcsLastModifiedBy

        :param idcs_prevented_operations:
            The value to assign to the idcs_prevented_operations property of this User.
            Allowed values for items in this list are: "replace", "update", "delete", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type idcs_prevented_operations: list[str]

        :param tags:
            The value to assign to the tags property of this User.
        :type tags: list[oci.identity_domains.models.Tags]

        :param delete_in_progress:
            The value to assign to the delete_in_progress property of this User.
        :type delete_in_progress: bool

        :param idcs_last_upgraded_in_release:
            The value to assign to the idcs_last_upgraded_in_release property of this User.
        :type idcs_last_upgraded_in_release: str

        :param domain_ocid:
            The value to assign to the domain_ocid property of this User.
        :type domain_ocid: str

        :param compartment_ocid:
            The value to assign to the compartment_ocid property of this User.
        :type compartment_ocid: str

        :param tenancy_ocid:
            The value to assign to the tenancy_ocid property of this User.
        :type tenancy_ocid: str

        :param external_id:
            The value to assign to the external_id property of this User.
        :type external_id: str

        :param user_name:
            The value to assign to the user_name property of this User.
        :type user_name: str

        :param description:
            The value to assign to the description property of this User.
        :type description: str

        :param display_name:
            The value to assign to the display_name property of this User.
        :type display_name: str

        :param nick_name:
            The value to assign to the nick_name property of this User.
        :type nick_name: str

        :param profile_url:
            The value to assign to the profile_url property of this User.
        :type profile_url: str

        :param title:
            The value to assign to the title property of this User.
        :type title: str

        :param user_type:
            The value to assign to the user_type property of this User.
            Allowed values for this property are: "Contractor", "Employee", "Intern", "Temp", "External", "Service", "Generic", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type user_type: str

        :param locale:
            The value to assign to the locale property of this User.
        :type locale: str

        :param preferred_language:
            The value to assign to the preferred_language property of this User.
        :type preferred_language: str

        :param timezone:
            The value to assign to the timezone property of this User.
        :type timezone: str

        :param active:
            The value to assign to the active property of this User.
        :type active: bool

        :param password:
            The value to assign to the password property of this User.
        :type password: str

        :param name:
            The value to assign to the name property of this User.
        :type name: oci.identity_domains.models.UserName

        :param emails:
            The value to assign to the emails property of this User.
        :type emails: list[oci.identity_domains.models.UserEmails]

        :param phone_numbers:
            The value to assign to the phone_numbers property of this User.
        :type phone_numbers: list[oci.identity_domains.models.UserPhoneNumbers]

        :param ims:
            The value to assign to the ims property of this User.
        :type ims: list[oci.identity_domains.models.UserIms]

        :param photos:
            The value to assign to the photos property of this User.
        :type photos: list[oci.identity_domains.models.UserPhotos]

        :param addresses:
            The value to assign to the addresses property of this User.
        :type addresses: list[oci.identity_domains.models.Addresses]

        :param groups:
            The value to assign to the groups property of this User.
        :type groups: list[oci.identity_domains.models.UserGroups]

        :param entitlements:
            The value to assign to the entitlements property of this User.
        :type entitlements: list[oci.identity_domains.models.UserEntitlements]

        :param roles:
            The value to assign to the roles property of this User.
        :type roles: list[oci.identity_domains.models.UserRoles]

        :param x509_certificates:
            The value to assign to the x509_certificates property of this User.
        :type x509_certificates: list[oci.identity_domains.models.UserX509Certificates]

        :param urnietfparamsscimschemasextensionenterprise2_0_user:
            The value to assign to the urnietfparamsscimschemasextensionenterprise2_0_user property of this User.
        :type urnietfparamsscimschemasextensionenterprise2_0_user: oci.identity_domains.models.ExtensionEnterprise20User

        :param urnietfparamsscimschemasoracleidcsextensionuser_user:
            The value to assign to the urnietfparamsscimschemasoracleidcsextensionuser_user property of this User.
        :type urnietfparamsscimschemasoracleidcsextensionuser_user: oci.identity_domains.models.ExtensionUserUser

        :param urnietfparamsscimschemasoracleidcsextensionpassword_state_user:
            The value to assign to the urnietfparamsscimschemasoracleidcsextensionpassword_state_user property of this User.
        :type urnietfparamsscimschemasoracleidcsextensionpassword_state_user: oci.identity_domains.models.ExtensionPasswordStateUser

        :param urnietfparamsscimschemasoracleidcsextensionuser_state_user:
            The value to assign to the urnietfparamsscimschemasoracleidcsextensionuser_state_user property of this User.
        :type urnietfparamsscimschemasoracleidcsextensionuser_state_user: oci.identity_domains.models.ExtensionUserStateUser

        :param urnietfparamsscimschemasoracleidcsextensionposix_user:
            The value to assign to the urnietfparamsscimschemasoracleidcsextensionposix_user property of this User.
        :type urnietfparamsscimschemasoracleidcsextensionposix_user: oci.identity_domains.models.ExtensionPosixUser

        :param urnietfparamsscimschemasoracleidcsextensionkerberos_user_user:
            The value to assign to the urnietfparamsscimschemasoracleidcsextensionkerberos_user_user property of this User.
        :type urnietfparamsscimschemasoracleidcsextensionkerberos_user_user: oci.identity_domains.models.ExtensionKerberosUserUser

        :param urnietfparamsscimschemasoracleidcsextensionmfa_user:
            The value to assign to the urnietfparamsscimschemasoracleidcsextensionmfa_user property of this User.
        :type urnietfparamsscimschemasoracleidcsextensionmfa_user: oci.identity_domains.models.ExtensionMfaUser

        :param urnietfparamsscimschemasoracleidcsextensionadaptive_user:
            The value to assign to the urnietfparamsscimschemasoracleidcsextensionadaptive_user property of this User.
        :type urnietfparamsscimschemasoracleidcsextensionadaptive_user: oci.identity_domains.models.ExtensionAdaptiveUser

        :param urnietfparamsscimschemasoracleidcsextensionsff_user:
            The value to assign to the urnietfparamsscimschemasoracleidcsextensionsff_user property of this User.
        :type urnietfparamsscimschemasoracleidcsextensionsff_user: oci.identity_domains.models.ExtensionSffUser

        :param urnietfparamsscimschemasoracleidcsextensionsecurity_questions_user:
            The value to assign to the urnietfparamsscimschemasoracleidcsextensionsecurity_questions_user property of this User.
        :type urnietfparamsscimschemasoracleidcsextensionsecurity_questions_user: oci.identity_domains.models.ExtensionSecurityQuestionsUser

        :param urnietfparamsscimschemasoracleidcsextensionself_registration_user:
            The value to assign to the urnietfparamsscimschemasoracleidcsextensionself_registration_user property of this User.
        :type urnietfparamsscimschemasoracleidcsextensionself_registration_user: oci.identity_domains.models.ExtensionSelfRegistrationUser

        :param urnietfparamsscimschemasoracleidcsextensionsocial_account_user:
            The value to assign to the urnietfparamsscimschemasoracleidcsextensionsocial_account_user property of this User.
        :type urnietfparamsscimschemasoracleidcsextensionsocial_account_user: oci.identity_domains.models.ExtensionSocialAccountUser

        :param urnietfparamsscimschemasoracleidcsextensiondb_user_user:
            The value to assign to the urnietfparamsscimschemasoracleidcsextensiondb_user_user property of this User.
        :type urnietfparamsscimschemasoracleidcsextensiondb_user_user: oci.identity_domains.models.ExtensionDbUserUser

        :param urnietfparamsscimschemasoracleidcsextensionterms_of_use_user:
            The value to assign to the urnietfparamsscimschemasoracleidcsextensionterms_of_use_user property of this User.
        :type urnietfparamsscimschemasoracleidcsextensionterms_of_use_user: oci.identity_domains.models.ExtensionTermsOfUseUser

        :param urnietfparamsscimschemasoracleidcsextensionpasswordless_user:
            The value to assign to the urnietfparamsscimschemasoracleidcsextensionpasswordless_user property of this User.
        :type urnietfparamsscimschemasoracleidcsextensionpasswordless_user: oci.identity_domains.models.ExtensionPasswordlessUser

        :param urnietfparamsscimschemasoracleidcsextension_oci_tags:
            The value to assign to the urnietfparamsscimschemasoracleidcsextension_oci_tags property of this User.
        :type urnietfparamsscimschemasoracleidcsextension_oci_tags: oci.identity_domains.models.ExtensionOCITags

        :param urnietfparamsscimschemasoracleidcsextensionuser_credentials_user:
            The value to assign to the urnietfparamsscimschemasoracleidcsextensionuser_credentials_user property of this User.
        :type urnietfparamsscimschemasoracleidcsextensionuser_credentials_user: oci.identity_domains.models.ExtensionUserCredentialsUser

        :param urnietfparamsscimschemasoracleidcsextensioncapabilities_user:
            The value to assign to the urnietfparamsscimschemasoracleidcsextensioncapabilities_user property of this User.
        :type urnietfparamsscimschemasoracleidcsextensioncapabilities_user: oci.identity_domains.models.ExtensionCapabilitiesUser

        :param urnietfparamsscimschemasoracleidcsextensiondb_credentials_user:
            The value to assign to the urnietfparamsscimschemasoracleidcsextensiondb_credentials_user property of this User.
        :type urnietfparamsscimschemasoracleidcsextensiondb_credentials_user: oci.identity_domains.models.ExtensionDbCredentialsUser

        :param urnietfparamsscimschemasoracleidcsextensionself_change_user:
            The value to assign to the urnietfparamsscimschemasoracleidcsextensionself_change_user property of this User.
        :type urnietfparamsscimschemasoracleidcsextensionself_change_user: oci.identity_domains.models.ExtensionSelfChangeUser

        """
        self.swagger_types = {
            'id': 'str',
            'ocid': 'str',
            'schemas': 'list[str]',
            'meta': 'Meta',
            'idcs_created_by': 'IdcsCreatedBy',
            'idcs_last_modified_by': 'IdcsLastModifiedBy',
            'idcs_prevented_operations': 'list[str]',
            'tags': 'list[Tags]',
            'delete_in_progress': 'bool',
            'idcs_last_upgraded_in_release': 'str',
            'domain_ocid': 'str',
            'compartment_ocid': 'str',
            'tenancy_ocid': 'str',
            'external_id': 'str',
            'user_name': 'str',
            'description': 'str',
            'display_name': 'str',
            'nick_name': 'str',
            'profile_url': 'str',
            'title': 'str',
            'user_type': 'str',
            'locale': 'str',
            'preferred_language': 'str',
            'timezone': 'str',
            'active': 'bool',
            'password': 'str',
            'name': 'UserName',
            'emails': 'list[UserEmails]',
            'phone_numbers': 'list[UserPhoneNumbers]',
            'ims': 'list[UserIms]',
            'photos': 'list[UserPhotos]',
            'addresses': 'list[Addresses]',
            'groups': 'list[UserGroups]',
            'entitlements': 'list[UserEntitlements]',
            'roles': 'list[UserRoles]',
            'x509_certificates': 'list[UserX509Certificates]',
            'urnietfparamsscimschemasextensionenterprise2_0_user': 'ExtensionEnterprise20User',
            'urnietfparamsscimschemasoracleidcsextensionuser_user': 'ExtensionUserUser',
            'urnietfparamsscimschemasoracleidcsextensionpassword_state_user': 'ExtensionPasswordStateUser',
            'urnietfparamsscimschemasoracleidcsextensionuser_state_user': 'ExtensionUserStateUser',
            'urnietfparamsscimschemasoracleidcsextensionposix_user': 'ExtensionPosixUser',
            'urnietfparamsscimschemasoracleidcsextensionkerberos_user_user': 'ExtensionKerberosUserUser',
            'urnietfparamsscimschemasoracleidcsextensionmfa_user': 'ExtensionMfaUser',
            'urnietfparamsscimschemasoracleidcsextensionadaptive_user': 'ExtensionAdaptiveUser',
            'urnietfparamsscimschemasoracleidcsextensionsff_user': 'ExtensionSffUser',
            'urnietfparamsscimschemasoracleidcsextensionsecurity_questions_user': 'ExtensionSecurityQuestionsUser',
            'urnietfparamsscimschemasoracleidcsextensionself_registration_user': 'ExtensionSelfRegistrationUser',
            'urnietfparamsscimschemasoracleidcsextensionsocial_account_user': 'ExtensionSocialAccountUser',
            'urnietfparamsscimschemasoracleidcsextensiondb_user_user': 'ExtensionDbUserUser',
            'urnietfparamsscimschemasoracleidcsextensionterms_of_use_user': 'ExtensionTermsOfUseUser',
            'urnietfparamsscimschemasoracleidcsextensionpasswordless_user': 'ExtensionPasswordlessUser',
            'urnietfparamsscimschemasoracleidcsextension_oci_tags': 'ExtensionOCITags',
            'urnietfparamsscimschemasoracleidcsextensionuser_credentials_user': 'ExtensionUserCredentialsUser',
            'urnietfparamsscimschemasoracleidcsextensioncapabilities_user': 'ExtensionCapabilitiesUser',
            'urnietfparamsscimschemasoracleidcsextensiondb_credentials_user': 'ExtensionDbCredentialsUser',
            'urnietfparamsscimschemasoracleidcsextensionself_change_user': 'ExtensionSelfChangeUser'
        }

        self.attribute_map = {
            'id': 'id',
            'ocid': 'ocid',
            'schemas': 'schemas',
            'meta': 'meta',
            'idcs_created_by': 'idcsCreatedBy',
            'idcs_last_modified_by': 'idcsLastModifiedBy',
            'idcs_prevented_operations': 'idcsPreventedOperations',
            'tags': 'tags',
            'delete_in_progress': 'deleteInProgress',
            'idcs_last_upgraded_in_release': 'idcsLastUpgradedInRelease',
            'domain_ocid': 'domainOcid',
            'compartment_ocid': 'compartmentOcid',
            'tenancy_ocid': 'tenancyOcid',
            'external_id': 'externalId',
            'user_name': 'userName',
            'description': 'description',
            'display_name': 'displayName',
            'nick_name': 'nickName',
            'profile_url': 'profileUrl',
            'title': 'title',
            'user_type': 'userType',
            'locale': 'locale',
            'preferred_language': 'preferredLanguage',
            'timezone': 'timezone',
            'active': 'active',
            'password': 'password',
            'name': 'name',
            'emails': 'emails',
            'phone_numbers': 'phoneNumbers',
            'ims': 'ims',
            'photos': 'photos',
            'addresses': 'addresses',
            'groups': 'groups',
            'entitlements': 'entitlements',
            'roles': 'roles',
            'x509_certificates': 'x509Certificates',
            'urnietfparamsscimschemasextensionenterprise2_0_user': 'urn:ietf:params:scim:schemas:extension:enterprise:2.0:User',
            'urnietfparamsscimschemasoracleidcsextensionuser_user': 'urn:ietf:params:scim:schemas:oracle:idcs:extension:user:User',
            'urnietfparamsscimschemasoracleidcsextensionpassword_state_user': 'urn:ietf:params:scim:schemas:oracle:idcs:extension:passwordState:User',
            'urnietfparamsscimschemasoracleidcsextensionuser_state_user': 'urn:ietf:params:scim:schemas:oracle:idcs:extension:userState:User',
            'urnietfparamsscimschemasoracleidcsextensionposix_user': 'urn:ietf:params:scim:schemas:oracle:idcs:extension:posix:User',
            'urnietfparamsscimschemasoracleidcsextensionkerberos_user_user': 'urn:ietf:params:scim:schemas:oracle:idcs:extension:kerberosUser:User',
            'urnietfparamsscimschemasoracleidcsextensionmfa_user': 'urn:ietf:params:scim:schemas:oracle:idcs:extension:mfa:User',
            'urnietfparamsscimschemasoracleidcsextensionadaptive_user': 'urn:ietf:params:scim:schemas:oracle:idcs:extension:adaptive:User',
            'urnietfparamsscimschemasoracleidcsextensionsff_user': 'urn:ietf:params:scim:schemas:oracle:idcs:extension:sff:User',
            'urnietfparamsscimschemasoracleidcsextensionsecurity_questions_user': 'urn:ietf:params:scim:schemas:oracle:idcs:extension:securityQuestions:User',
            'urnietfparamsscimschemasoracleidcsextensionself_registration_user': 'urn:ietf:params:scim:schemas:oracle:idcs:extension:selfRegistration:User',
            'urnietfparamsscimschemasoracleidcsextensionsocial_account_user': 'urn:ietf:params:scim:schemas:oracle:idcs:extension:socialAccount:User',
            'urnietfparamsscimschemasoracleidcsextensiondb_user_user': 'urn:ietf:params:scim:schemas:oracle:idcs:extension:dbUser:User',
            'urnietfparamsscimschemasoracleidcsextensionterms_of_use_user': 'urn:ietf:params:scim:schemas:oracle:idcs:extension:termsOfUse:User',
            'urnietfparamsscimschemasoracleidcsextensionpasswordless_user': 'urn:ietf:params:scim:schemas:oracle:idcs:extension:passwordless:User',
            'urnietfparamsscimschemasoracleidcsextension_oci_tags': 'urn:ietf:params:scim:schemas:oracle:idcs:extension:OCITags',
            'urnietfparamsscimschemasoracleidcsextensionuser_credentials_user': 'urn:ietf:params:scim:schemas:oracle:idcs:extension:userCredentials:User',
            'urnietfparamsscimschemasoracleidcsextensioncapabilities_user': 'urn:ietf:params:scim:schemas:oracle:idcs:extension:capabilities:User',
            'urnietfparamsscimschemasoracleidcsextensiondb_credentials_user': 'urn:ietf:params:scim:schemas:oracle:idcs:extension:dbCredentials:User',
            'urnietfparamsscimschemasoracleidcsextensionself_change_user': 'urn:ietf:params:scim:schemas:oracle:idcs:extension:selfChange:User'
        }

        self._id = None
        self._ocid = None
        self._schemas = None
        self._meta = None
        self._idcs_created_by = None
        self._idcs_last_modified_by = None
        self._idcs_prevented_operations = None
        self._tags = None
        self._delete_in_progress = None
        self._idcs_last_upgraded_in_release = None
        self._domain_ocid = None
        self._compartment_ocid = None
        self._tenancy_ocid = None
        self._external_id = None
        self._user_name = None
        self._description = None
        self._display_name = None
        self._nick_name = None
        self._profile_url = None
        self._title = None
        self._user_type = None
        self._locale = None
        self._preferred_language = None
        self._timezone = None
        self._active = None
        self._password = None
        self._name = None
        self._emails = None
        self._phone_numbers = None
        self._ims = None
        self._photos = None
        self._addresses = None
        self._groups = None
        self._entitlements = None
        self._roles = None
        self._x509_certificates = None
        self._urnietfparamsscimschemasextensionenterprise2_0_user = None
        self._urnietfparamsscimschemasoracleidcsextensionuser_user = None
        self._urnietfparamsscimschemasoracleidcsextensionpassword_state_user = None
        self._urnietfparamsscimschemasoracleidcsextensionuser_state_user = None
        self._urnietfparamsscimschemasoracleidcsextensionposix_user = None
        self._urnietfparamsscimschemasoracleidcsextensionkerberos_user_user = None
        self._urnietfparamsscimschemasoracleidcsextensionmfa_user = None
        self._urnietfparamsscimschemasoracleidcsextensionadaptive_user = None
        self._urnietfparamsscimschemasoracleidcsextensionsff_user = None
        self._urnietfparamsscimschemasoracleidcsextensionsecurity_questions_user = None
        self._urnietfparamsscimschemasoracleidcsextensionself_registration_user = None
        self._urnietfparamsscimschemasoracleidcsextensionsocial_account_user = None
        self._urnietfparamsscimschemasoracleidcsextensiondb_user_user = None
        self._urnietfparamsscimschemasoracleidcsextensionterms_of_use_user = None
        self._urnietfparamsscimschemasoracleidcsextensionpasswordless_user = None
        self._urnietfparamsscimschemasoracleidcsextension_oci_tags = None
        self._urnietfparamsscimschemasoracleidcsextensionuser_credentials_user = None
        self._urnietfparamsscimschemasoracleidcsextensioncapabilities_user = None
        self._urnietfparamsscimschemasoracleidcsextensiondb_credentials_user = None
        self._urnietfparamsscimschemasoracleidcsextensionself_change_user = None

    @property
    def id(self):
        """
        Gets the id of this User.
        Unique identifier for the SCIM Resource as defined by the Service Provider. Each representation of the Resource MUST include a non-empty id value. This identifier MUST be unique across the Service Provider's entire set of Resources. It MUST be a stable, non-reassignable identifier that does not change when the same Resource is returned in subsequent requests. The value of the id attribute is always issued by the Service Provider and MUST never be specified by the Service Consumer. bulkId: is a reserved keyword and MUST NOT be used in the unique identifier.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: always
         - type: string
         - uniqueness: global


        :return: The id of this User.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this User.
        Unique identifier for the SCIM Resource as defined by the Service Provider. Each representation of the Resource MUST include a non-empty id value. This identifier MUST be unique across the Service Provider's entire set of Resources. It MUST be a stable, non-reassignable identifier that does not change when the same Resource is returned in subsequent requests. The value of the id attribute is always issued by the Service Provider and MUST never be specified by the Service Consumer. bulkId: is a reserved keyword and MUST NOT be used in the unique identifier.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: always
         - type: string
         - uniqueness: global


        :param id: The id of this User.
        :type: str
        """
        self._id = id

    @property
    def ocid(self):
        """
        Gets the ocid of this User.
        Unique OCI identifier for the SCIM Resource.

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: immutable
         - required: false
         - returned: default
         - type: string
         - uniqueness: global


        :return: The ocid of this User.
        :rtype: str
        """
        return self._ocid

    @ocid.setter
    def ocid(self, ocid):
        """
        Sets the ocid of this User.
        Unique OCI identifier for the SCIM Resource.

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: immutable
         - required: false
         - returned: default
         - type: string
         - uniqueness: global


        :param ocid: The ocid of this User.
        :type: str
        """
        self._ocid = ocid

    @property
    def schemas(self):
        """
        **[Required]** Gets the schemas of this User.
        REQUIRED. The schemas attribute is an array of Strings which allows introspection of the supported schema version for a SCIM representation as well any schema extensions supported by that representation. Each String value must be a unique URI. This specification defines URIs for User, Group, and a standard \\\"enterprise\\\" extension. All representations of SCIM schema MUST include a non-zero value array with value(s) of the URIs supported by that representation. Duplicate values MUST NOT be included. Value order is not specified and MUST not impact behavior.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: true
         - mutability: readWrite
         - required: true
         - returned: default
         - type: string
         - uniqueness: none


        :return: The schemas of this User.
        :rtype: list[str]
        """
        return self._schemas

    @schemas.setter
    def schemas(self, schemas):
        """
        Sets the schemas of this User.
        REQUIRED. The schemas attribute is an array of Strings which allows introspection of the supported schema version for a SCIM representation as well any schema extensions supported by that representation. Each String value must be a unique URI. This specification defines URIs for User, Group, and a standard \\\"enterprise\\\" extension. All representations of SCIM schema MUST include a non-zero value array with value(s) of the URIs supported by that representation. Duplicate values MUST NOT be included. Value order is not specified and MUST not impact behavior.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: true
         - mutability: readWrite
         - required: true
         - returned: default
         - type: string
         - uniqueness: none


        :param schemas: The schemas of this User.
        :type: list[str]
        """
        self._schemas = schemas

    @property
    def meta(self):
        """
        Gets the meta of this User.

        :return: The meta of this User.
        :rtype: oci.identity_domains.models.Meta
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """
        Sets the meta of this User.

        :param meta: The meta of this User.
        :type: oci.identity_domains.models.Meta
        """
        self._meta = meta

    @property
    def idcs_created_by(self):
        """
        Gets the idcs_created_by of this User.

        :return: The idcs_created_by of this User.
        :rtype: oci.identity_domains.models.IdcsCreatedBy
        """
        return self._idcs_created_by

    @idcs_created_by.setter
    def idcs_created_by(self, idcs_created_by):
        """
        Sets the idcs_created_by of this User.

        :param idcs_created_by: The idcs_created_by of this User.
        :type: oci.identity_domains.models.IdcsCreatedBy
        """
        self._idcs_created_by = idcs_created_by

    @property
    def idcs_last_modified_by(self):
        """
        Gets the idcs_last_modified_by of this User.

        :return: The idcs_last_modified_by of this User.
        :rtype: oci.identity_domains.models.IdcsLastModifiedBy
        """
        return self._idcs_last_modified_by

    @idcs_last_modified_by.setter
    def idcs_last_modified_by(self, idcs_last_modified_by):
        """
        Sets the idcs_last_modified_by of this User.

        :param idcs_last_modified_by: The idcs_last_modified_by of this User.
        :type: oci.identity_domains.models.IdcsLastModifiedBy
        """
        self._idcs_last_modified_by = idcs_last_modified_by

    @property
    def idcs_prevented_operations(self):
        """
        Gets the idcs_prevented_operations of this User.
        Each value of this attribute specifies an operation that only an internal client may perform on this particular resource.

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: true
         - mutability: readOnly
         - required: false
         - returned: request
         - type: string
         - uniqueness: none

        Allowed values for items in this list are: "replace", "update", "delete", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The idcs_prevented_operations of this User.
        :rtype: list[str]
        """
        return self._idcs_prevented_operations

    @idcs_prevented_operations.setter
    def idcs_prevented_operations(self, idcs_prevented_operations):
        """
        Sets the idcs_prevented_operations of this User.
        Each value of this attribute specifies an operation that only an internal client may perform on this particular resource.

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: true
         - mutability: readOnly
         - required: false
         - returned: request
         - type: string
         - uniqueness: none


        :param idcs_prevented_operations: The idcs_prevented_operations of this User.
        :type: list[str]
        """
        allowed_values = ["replace", "update", "delete"]
        if idcs_prevented_operations:
            idcs_prevented_operations[:] = ['UNKNOWN_ENUM_VALUE' if not value_allowed_none_or_none_sentinel(x, allowed_values) else x for x in idcs_prevented_operations]
        self._idcs_prevented_operations = idcs_prevented_operations

    @property
    def tags(self):
        """
        Gets the tags of this User.
        A list of tags on this resource.

        **SCIM++ Properties:**
         - idcsCompositeKey: [key, value]
         - idcsSearchable: true
         - multiValued: true
         - mutability: readWrite
         - required: false
         - returned: request
         - type: complex
         - uniqueness: none


        :return: The tags of this User.
        :rtype: list[oci.identity_domains.models.Tags]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this User.
        A list of tags on this resource.

        **SCIM++ Properties:**
         - idcsCompositeKey: [key, value]
         - idcsSearchable: true
         - multiValued: true
         - mutability: readWrite
         - required: false
         - returned: request
         - type: complex
         - uniqueness: none


        :param tags: The tags of this User.
        :type: list[oci.identity_domains.models.Tags]
        """
        self._tags = tags

    @property
    def delete_in_progress(self):
        """
        Gets the delete_in_progress of this User.
        A boolean flag indicating this resource in the process of being deleted. Usually set to true when synchronous deletion of the resource would take too long.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: boolean
         - uniqueness: none


        :return: The delete_in_progress of this User.
        :rtype: bool
        """
        return self._delete_in_progress

    @delete_in_progress.setter
    def delete_in_progress(self, delete_in_progress):
        """
        Sets the delete_in_progress of this User.
        A boolean flag indicating this resource in the process of being deleted. Usually set to true when synchronous deletion of the resource would take too long.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: boolean
         - uniqueness: none


        :param delete_in_progress: The delete_in_progress of this User.
        :type: bool
        """
        self._delete_in_progress = delete_in_progress

    @property
    def idcs_last_upgraded_in_release(self):
        """
        Gets the idcs_last_upgraded_in_release of this User.
        The release number when the resource was upgraded.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: request
         - type: string
         - uniqueness: none


        :return: The idcs_last_upgraded_in_release of this User.
        :rtype: str
        """
        return self._idcs_last_upgraded_in_release

    @idcs_last_upgraded_in_release.setter
    def idcs_last_upgraded_in_release(self, idcs_last_upgraded_in_release):
        """
        Sets the idcs_last_upgraded_in_release of this User.
        The release number when the resource was upgraded.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: request
         - type: string
         - uniqueness: none


        :param idcs_last_upgraded_in_release: The idcs_last_upgraded_in_release of this User.
        :type: str
        """
        self._idcs_last_upgraded_in_release = idcs_last_upgraded_in_release

    @property
    def domain_ocid(self):
        """
        Gets the domain_ocid of this User.
        OCI Domain Id (ocid) in which the resource lives.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :return: The domain_ocid of this User.
        :rtype: str
        """
        return self._domain_ocid

    @domain_ocid.setter
    def domain_ocid(self, domain_ocid):
        """
        Sets the domain_ocid of this User.
        OCI Domain Id (ocid) in which the resource lives.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param domain_ocid: The domain_ocid of this User.
        :type: str
        """
        self._domain_ocid = domain_ocid

    @property
    def compartment_ocid(self):
        """
        Gets the compartment_ocid of this User.
        OCI Compartment Id (ocid) in which the resource lives.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :return: The compartment_ocid of this User.
        :rtype: str
        """
        return self._compartment_ocid

    @compartment_ocid.setter
    def compartment_ocid(self, compartment_ocid):
        """
        Sets the compartment_ocid of this User.
        OCI Compartment Id (ocid) in which the resource lives.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param compartment_ocid: The compartment_ocid of this User.
        :type: str
        """
        self._compartment_ocid = compartment_ocid

    @property
    def tenancy_ocid(self):
        """
        Gets the tenancy_ocid of this User.
        OCI Tenant Id (ocid) in which the resource lives.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :return: The tenancy_ocid of this User.
        :rtype: str
        """
        return self._tenancy_ocid

    @tenancy_ocid.setter
    def tenancy_ocid(self, tenancy_ocid):
        """
        Sets the tenancy_ocid of this User.
        OCI Tenant Id (ocid) in which the resource lives.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param tenancy_ocid: The tenancy_ocid of this User.
        :type: str
        """
        self._tenancy_ocid = tenancy_ocid

    @property
    def external_id(self):
        """
        Gets the external_id of this User.
        An identifier for the Resource as defined by the Service Consumer. The externalId may simplify identification of the Resource between Service Consumer and Service Provider by allowing the Consumer to refer to the Resource with its own identifier, obviating the need to store a local mapping between the local identifier of the Resource and the identifier used by the Service Provider. Each Resource MAY include a non-empty externalId value. The value of the externalId attribute is always issued by the Service Consumer and can never be specified by the Service Provider. The Service Provider MUST always interpret the externalId as scoped to the Service Consumer's tenant.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsCsvAttributeNameMappings: [[columnHeaderName:External Id]]
         - idcsPii: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :return: The external_id of this User.
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """
        Sets the external_id of this User.
        An identifier for the Resource as defined by the Service Consumer. The externalId may simplify identification of the Resource between Service Consumer and Service Provider by allowing the Consumer to refer to the Resource with its own identifier, obviating the need to store a local mapping between the local identifier of the Resource and the identifier used by the Service Provider. Each Resource MAY include a non-empty externalId value. The value of the externalId attribute is always issued by the Service Consumer and can never be specified by the Service Provider. The Service Provider MUST always interpret the externalId as scoped to the Service Consumer's tenant.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsCsvAttributeNameMappings: [[columnHeaderName:External Id]]
         - idcsPii: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param external_id: The external_id of this User.
        :type: str
        """
        self._external_id = external_id

    @property
    def user_name(self):
        """
        **[Required]** Gets the user_name of this User.
        User name

        **SCIM++ Properties:**
         - caseExact: false
         - idcsCsvAttributeName: User ID
         - idcsCsvAttributeNameMappings: [[columnHeaderName:User Name, deprecatedColumnHeaderName:User ID]]
         - idcsPii: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: always
         - type: string
         - uniqueness: global


        :return: The user_name of this User.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """
        Sets the user_name of this User.
        User name

        **SCIM++ Properties:**
         - caseExact: false
         - idcsCsvAttributeName: User ID
         - idcsCsvAttributeNameMappings: [[columnHeaderName:User Name, deprecatedColumnHeaderName:User ID]]
         - idcsPii: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: always
         - type: string
         - uniqueness: global


        :param user_name: The user_name of this User.
        :type: str
        """
        self._user_name = user_name

    @property
    def description(self):
        """
        Gets the description of this User.
        Description of the user

        **Added In:** 2012271618

        **SCIM++ Properties:**
         - caseExact: false
         - idcsPii: true
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :return: The description of this User.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this User.
        Description of the user

        **Added In:** 2012271618

        **SCIM++ Properties:**
         - caseExact: false
         - idcsPii: true
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param description: The description of this User.
        :type: str
        """
        self._description = description

    @property
    def display_name(self):
        """
        Gets the display_name of this User.
        Display name

        **SCIM++ Properties:**
         - caseExact: false
         - idcsCsvAttributeName: Display Name
         - idcsCsvAttributeNameMappings: [[columnHeaderName:Display Name]]
         - idcsPii: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :return: The display_name of this User.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this User.
        Display name

        **SCIM++ Properties:**
         - caseExact: false
         - idcsCsvAttributeName: Display Name
         - idcsCsvAttributeNameMappings: [[columnHeaderName:Display Name]]
         - idcsPii: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param display_name: The display_name of this User.
        :type: str
        """
        self._display_name = display_name

    @property
    def nick_name(self):
        """
        Gets the nick_name of this User.
        Nick name

        **SCIM++ Properties:**
         - caseExact: false
         - idcsCsvAttributeName: Nick Name
         - idcsCsvAttributeNameMappings: [[columnHeaderName:Nick Name]]
         - idcsPii: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :return: The nick_name of this User.
        :rtype: str
        """
        return self._nick_name

    @nick_name.setter
    def nick_name(self, nick_name):
        """
        Sets the nick_name of this User.
        Nick name

        **SCIM++ Properties:**
         - caseExact: false
         - idcsCsvAttributeName: Nick Name
         - idcsCsvAttributeNameMappings: [[columnHeaderName:Nick Name]]
         - idcsPii: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param nick_name: The nick_name of this User.
        :type: str
        """
        self._nick_name = nick_name

    @property
    def profile_url(self):
        """
        Gets the profile_url of this User.
        A fully-qualified URL to a page representing the User's online profile

        **SCIM++ Properties:**
         - caseExact: false
         - idcsCsvAttributeName: Profile URL
         - idcsCsvAttributeNameMappings: [[columnHeaderName:Profile Url]]
         - idcsPii: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: reference
         - uniqueness: none


        :return: The profile_url of this User.
        :rtype: str
        """
        return self._profile_url

    @profile_url.setter
    def profile_url(self, profile_url):
        """
        Sets the profile_url of this User.
        A fully-qualified URL to a page representing the User's online profile

        **SCIM++ Properties:**
         - caseExact: false
         - idcsCsvAttributeName: Profile URL
         - idcsCsvAttributeNameMappings: [[columnHeaderName:Profile Url]]
         - idcsPii: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: reference
         - uniqueness: none


        :param profile_url: The profile_url of this User.
        :type: str
        """
        self._profile_url = profile_url

    @property
    def title(self):
        """
        Gets the title of this User.
        Title

        **SCIM++ Properties:**
         - caseExact: false
         - idcsCsvAttributeName: Title
         - idcsCsvAttributeNameMappings: [[columnHeaderName:Title]]
         - idcsPii: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :return: The title of this User.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """
        Sets the title of this User.
        Title

        **SCIM++ Properties:**
         - caseExact: false
         - idcsCsvAttributeName: Title
         - idcsCsvAttributeNameMappings: [[columnHeaderName:Title]]
         - idcsPii: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param title: The title of this User.
        :type: str
        """
        self._title = title

    @property
    def user_type(self):
        """
        Gets the user_type of this User.
        Used to identify the organization-to-user relationship

        **SCIM++ Properties:**
         - caseExact: false
         - idcsCsvAttributeName: User Type
         - idcsCsvAttributeNameMappings: [[columnHeaderName:User Type]]
         - idcsPii: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string
         - uniqueness: none

        Allowed values for this property are: "Contractor", "Employee", "Intern", "Temp", "External", "Service", "Generic", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The user_type of this User.
        :rtype: str
        """
        return self._user_type

    @user_type.setter
    def user_type(self, user_type):
        """
        Sets the user_type of this User.
        Used to identify the organization-to-user relationship

        **SCIM++ Properties:**
         - caseExact: false
         - idcsCsvAttributeName: User Type
         - idcsCsvAttributeNameMappings: [[columnHeaderName:User Type]]
         - idcsPii: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param user_type: The user_type of this User.
        :type: str
        """
        allowed_values = ["Contractor", "Employee", "Intern", "Temp", "External", "Service", "Generic"]
        if not value_allowed_none_or_none_sentinel(user_type, allowed_values):
            user_type = 'UNKNOWN_ENUM_VALUE'
        self._user_type = user_type

    @property
    def locale(self):
        """
        Gets the locale of this User.
        Used to indicate the User's default location for purposes of localizing items such as currency, date and time format, numerical representations, and so on.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsCsvAttributeName: Locale
         - idcsCsvAttributeNameMappings: [[columnHeaderName:Locale]]
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :return: The locale of this User.
        :rtype: str
        """
        return self._locale

    @locale.setter
    def locale(self, locale):
        """
        Sets the locale of this User.
        Used to indicate the User's default location for purposes of localizing items such as currency, date and time format, numerical representations, and so on.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsCsvAttributeName: Locale
         - idcsCsvAttributeNameMappings: [[columnHeaderName:Locale]]
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param locale: The locale of this User.
        :type: str
        """
        self._locale = locale

    @property
    def preferred_language(self):
        """
        Gets the preferred_language of this User.
        User's preferred written or spoken language used for localized user interfaces

        **SCIM++ Properties:**
         - caseExact: false
         - idcsCsvAttributeName: Preferred Language
         - idcsCsvAttributeNameMappings: [[columnHeaderName:Preferred Language]]
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :return: The preferred_language of this User.
        :rtype: str
        """
        return self._preferred_language

    @preferred_language.setter
    def preferred_language(self, preferred_language):
        """
        Sets the preferred_language of this User.
        User's preferred written or spoken language used for localized user interfaces

        **SCIM++ Properties:**
         - caseExact: false
         - idcsCsvAttributeName: Preferred Language
         - idcsCsvAttributeNameMappings: [[columnHeaderName:Preferred Language]]
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param preferred_language: The preferred_language of this User.
        :type: str
        """
        self._preferred_language = preferred_language

    @property
    def timezone(self):
        """
        Gets the timezone of this User.
        User's timezone

        **SCIM++ Properties:**
         - caseExact: false
         - idcsCanonicalValueSourceFilter: attrName eq \"timezones\" and attrValues.value eq \"$(timezone)\"
         - idcsCanonicalValueSourceResourceType: AllowedValue
         - idcsCsvAttributeName: TimeZone
         - idcsCsvAttributeNameMappings: [[columnHeaderName:Time Zone, deprecatedColumnHeaderName:TimeZone]]
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :return: The timezone of this User.
        :rtype: str
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """
        Sets the timezone of this User.
        User's timezone

        **SCIM++ Properties:**
         - caseExact: false
         - idcsCanonicalValueSourceFilter: attrName eq \"timezones\" and attrValues.value eq \"$(timezone)\"
         - idcsCanonicalValueSourceResourceType: AllowedValue
         - idcsCsvAttributeName: TimeZone
         - idcsCsvAttributeNameMappings: [[columnHeaderName:Time Zone, deprecatedColumnHeaderName:TimeZone]]
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param timezone: The timezone of this User.
        :type: str
        """
        self._timezone = timezone

    @property
    def active(self):
        """
        Gets the active of this User.
        User status

        **SCIM++ Properties:**
         - caseExact: false
         - idcsCsvAttributeName: Active
         - idcsCsvAttributeNameMappings: [[columnHeaderName:Active]]
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: boolean
         - uniqueness: none


        :return: The active of this User.
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """
        Sets the active of this User.
        User status

        **SCIM++ Properties:**
         - caseExact: false
         - idcsCsvAttributeName: Active
         - idcsCsvAttributeNameMappings: [[columnHeaderName:Active]]
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: boolean
         - uniqueness: none


        :param active: The active of this User.
        :type: bool
        """
        self._active = active

    @property
    def password(self):
        """
        Gets the password of this User.
        Password attribute. Max length for password is controlled via Password Policy.

        **SCIM++ Properties:**
         - idcsCsvAttributeName: Password
         - idcsCsvAttributeNameMappings: [[columnHeaderName:Password]]
         - idcsPii: true
         - idcsSearchable: false
         - idcsSensitive: hash
         - multiValued: false
         - mutability: writeOnly
         - required: false
         - returned: never
         - type: string
         - uniqueness: none


        :return: The password of this User.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """
        Sets the password of this User.
        Password attribute. Max length for password is controlled via Password Policy.

        **SCIM++ Properties:**
         - idcsCsvAttributeName: Password
         - idcsCsvAttributeNameMappings: [[columnHeaderName:Password]]
         - idcsPii: true
         - idcsSearchable: false
         - idcsSensitive: hash
         - multiValued: false
         - mutability: writeOnly
         - required: false
         - returned: never
         - type: string
         - uniqueness: none


        :param password: The password of this User.
        :type: str
        """
        self._password = password

    @property
    def name(self):
        """
        **[Required]** Gets the name of this User.

        :return: The name of this User.
        :rtype: oci.identity_domains.models.UserName
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this User.

        :param name: The name of this User.
        :type: oci.identity_domains.models.UserName
        """
        self._name = name

    @property
    def emails(self):
        """
        Gets the emails of this User.
        A complex attribute representing emails

        **SCIM++ Properties:**
         - idcsCompositeKey: [value, type]
         - idcsCsvAttributeNameMappings: [[columnHeaderName:Work Email, mapsTo:emails[work].value], [columnHeaderName:Home Email, mapsTo:emails[home].value], [columnHeaderName:Primary Email Type, mapsTo:emails[$(type)].primary], [columnHeaderName:Other Email, mapsTo:emails[other].value], [columnHeaderName:Recovery Email, mapsTo:emails[recovery].value], [columnHeaderName:Work Email Verified, mapsTo:emails[work].verified], [columnHeaderName:Home Email Verified, mapsTo:emails[home].verified], [columnHeaderName:Other Email Verified, mapsTo:emails[other].verified], [columnHeaderName:Recovery Email Verified, mapsTo:emails[recovery].verified]]
         - idcsPii: true
         - multiValued: true
         - mutability: readWrite
         - required: false
         - returned: default
         - type: complex
         - uniqueness: none


        :return: The emails of this User.
        :rtype: list[oci.identity_domains.models.UserEmails]
        """
        return self._emails

    @emails.setter
    def emails(self, emails):
        """
        Sets the emails of this User.
        A complex attribute representing emails

        **SCIM++ Properties:**
         - idcsCompositeKey: [value, type]
         - idcsCsvAttributeNameMappings: [[columnHeaderName:Work Email, mapsTo:emails[work].value], [columnHeaderName:Home Email, mapsTo:emails[home].value], [columnHeaderName:Primary Email Type, mapsTo:emails[$(type)].primary], [columnHeaderName:Other Email, mapsTo:emails[other].value], [columnHeaderName:Recovery Email, mapsTo:emails[recovery].value], [columnHeaderName:Work Email Verified, mapsTo:emails[work].verified], [columnHeaderName:Home Email Verified, mapsTo:emails[home].verified], [columnHeaderName:Other Email Verified, mapsTo:emails[other].verified], [columnHeaderName:Recovery Email Verified, mapsTo:emails[recovery].verified]]
         - idcsPii: true
         - multiValued: true
         - mutability: readWrite
         - required: false
         - returned: default
         - type: complex
         - uniqueness: none


        :param emails: The emails of this User.
        :type: list[oci.identity_domains.models.UserEmails]
        """
        self._emails = emails

    @property
    def phone_numbers(self):
        """
        Gets the phone_numbers of this User.
        Phone numbers

        **SCIM++ Properties:**
         - idcsCompositeKey: [value, type]
         - idcsCsvAttributeNameMappings: [[columnHeaderName:Work Phone, mapsTo:phoneNumbers[work].value], [columnHeaderName:Mobile No, mapsTo:phoneNumbers[mobile].value], [columnHeaderName:Home Phone, mapsTo:phoneNumbers[home].value], [columnHeaderName:Fax, mapsTo:phoneNumbers[fax].value], [columnHeaderName:Pager, mapsTo:phoneNumbers[pager].value], [columnHeaderName:Other Phone, mapsTo:phoneNumbers[other].value], [columnHeaderName:Recovery Phone, mapsTo:phoneNumbers[recovery].value], [columnHeaderName:Primary Phone Type, mapsTo:phoneNumbers[$(type)].primary]]
         - idcsPii: true
         - multiValued: true
         - mutability: readWrite
         - required: false
         - returned: default
         - type: complex
         - uniqueness: none


        :return: The phone_numbers of this User.
        :rtype: list[oci.identity_domains.models.UserPhoneNumbers]
        """
        return self._phone_numbers

    @phone_numbers.setter
    def phone_numbers(self, phone_numbers):
        """
        Sets the phone_numbers of this User.
        Phone numbers

        **SCIM++ Properties:**
         - idcsCompositeKey: [value, type]
         - idcsCsvAttributeNameMappings: [[columnHeaderName:Work Phone, mapsTo:phoneNumbers[work].value], [columnHeaderName:Mobile No, mapsTo:phoneNumbers[mobile].value], [columnHeaderName:Home Phone, mapsTo:phoneNumbers[home].value], [columnHeaderName:Fax, mapsTo:phoneNumbers[fax].value], [columnHeaderName:Pager, mapsTo:phoneNumbers[pager].value], [columnHeaderName:Other Phone, mapsTo:phoneNumbers[other].value], [columnHeaderName:Recovery Phone, mapsTo:phoneNumbers[recovery].value], [columnHeaderName:Primary Phone Type, mapsTo:phoneNumbers[$(type)].primary]]
         - idcsPii: true
         - multiValued: true
         - mutability: readWrite
         - required: false
         - returned: default
         - type: complex
         - uniqueness: none


        :param phone_numbers: The phone_numbers of this User.
        :type: list[oci.identity_domains.models.UserPhoneNumbers]
        """
        self._phone_numbers = phone_numbers

    @property
    def ims(self):
        """
        Gets the ims of this User.
        User's instant messaging addresses

        **SCIM++ Properties:**
         - idcsCompositeKey: [value, type]
         - idcsPii: true
         - multiValued: true
         - mutability: readWrite
         - required: false
         - returned: default
         - type: complex
         - uniqueness: none


        :return: The ims of this User.
        :rtype: list[oci.identity_domains.models.UserIms]
        """
        return self._ims

    @ims.setter
    def ims(self, ims):
        """
        Sets the ims of this User.
        User's instant messaging addresses

        **SCIM++ Properties:**
         - idcsCompositeKey: [value, type]
         - idcsPii: true
         - multiValued: true
         - mutability: readWrite
         - required: false
         - returned: default
         - type: complex
         - uniqueness: none


        :param ims: The ims of this User.
        :type: list[oci.identity_domains.models.UserIms]
        """
        self._ims = ims

    @property
    def photos(self):
        """
        Gets the photos of this User.
        URLs of photos for the User

        **SCIM++ Properties:**
         - idcsCompositeKey: [value, type]
         - idcsPii: true
         - multiValued: true
         - mutability: readWrite
         - required: false
         - returned: default
         - type: complex
         - uniqueness: none


        :return: The photos of this User.
        :rtype: list[oci.identity_domains.models.UserPhotos]
        """
        return self._photos

    @photos.setter
    def photos(self, photos):
        """
        Sets the photos of this User.
        URLs of photos for the User

        **SCIM++ Properties:**
         - idcsCompositeKey: [value, type]
         - idcsPii: true
         - multiValued: true
         - mutability: readWrite
         - required: false
         - returned: default
         - type: complex
         - uniqueness: none


        :param photos: The photos of this User.
        :type: list[oci.identity_domains.models.UserPhotos]
        """
        self._photos = photos

    @property
    def addresses(self):
        """
        Gets the addresses of this User.
        A physical mailing address for this User, as described in (address Element). Canonical Type Values of work, home, and other. The value attribute is a complex type with the following sub-attributes.

        **SCIM++ Properties:**
         - idcsCompositeKey: [type]
         - idcsCsvAttributeNameMappings: [[columnHeaderName:Work Address Street, deprecatedColumnHeaderName:Work Street Address, mapsTo:addresses[work].streetAddress], [columnHeaderName:Work Address Locality, deprecatedColumnHeaderName:Work City, mapsTo:addresses[work].locality], [columnHeaderName:Work Address Region, deprecatedColumnHeaderName:Work State, mapsTo:addresses[work].region], [columnHeaderName:Work Address Postal Code, deprecatedColumnHeaderName:Work Postal Code, mapsTo:addresses[work].postalCode], [columnHeaderName:Work Address Country, deprecatedColumnHeaderName:Work Country, mapsTo:addresses[work].country], [columnHeaderName:Work Address Formatted, mapsTo:addresses[work].formatted], [columnHeaderName:Home Address Formatted, mapsTo:addresses[home].formatted], [columnHeaderName:Other Address Formatted, mapsTo:addresses[other].formatted], [columnHeaderName:Home Address Street, mapsTo:addresses[home].streetAddress], [columnHeaderName:Other Address Street, mapsTo:addresses[other].streetAddress], [columnHeaderName:Home Address Locality, mapsTo:addresses[home].locality], [columnHeaderName:Other Address Locality, mapsTo:addresses[other].locality], [columnHeaderName:Home Address Region, mapsTo:addresses[home].region], [columnHeaderName:Other Address Region, mapsTo:addresses[other].region], [columnHeaderName:Home Address Country, mapsTo:addresses[home].country], [columnHeaderName:Other Address Country, mapsTo:addresses[other].country], [columnHeaderName:Home Address Postal Code, mapsTo:addresses[home].postalCode], [columnHeaderName:Other Address Postal Code, mapsTo:addresses[other].postalCode], [columnHeaderName:Primary Address Type, mapsTo:addresses[$(type)].primary]]
         - idcsPii: true
         - multiValued: true
         - mutability: readWrite
         - required: false
         - returned: default
         - type: complex
         - uniqueness: none


        :return: The addresses of this User.
        :rtype: list[oci.identity_domains.models.Addresses]
        """
        return self._addresses

    @addresses.setter
    def addresses(self, addresses):
        """
        Sets the addresses of this User.
        A physical mailing address for this User, as described in (address Element). Canonical Type Values of work, home, and other. The value attribute is a complex type with the following sub-attributes.

        **SCIM++ Properties:**
         - idcsCompositeKey: [type]
         - idcsCsvAttributeNameMappings: [[columnHeaderName:Work Address Street, deprecatedColumnHeaderName:Work Street Address, mapsTo:addresses[work].streetAddress], [columnHeaderName:Work Address Locality, deprecatedColumnHeaderName:Work City, mapsTo:addresses[work].locality], [columnHeaderName:Work Address Region, deprecatedColumnHeaderName:Work State, mapsTo:addresses[work].region], [columnHeaderName:Work Address Postal Code, deprecatedColumnHeaderName:Work Postal Code, mapsTo:addresses[work].postalCode], [columnHeaderName:Work Address Country, deprecatedColumnHeaderName:Work Country, mapsTo:addresses[work].country], [columnHeaderName:Work Address Formatted, mapsTo:addresses[work].formatted], [columnHeaderName:Home Address Formatted, mapsTo:addresses[home].formatted], [columnHeaderName:Other Address Formatted, mapsTo:addresses[other].formatted], [columnHeaderName:Home Address Street, mapsTo:addresses[home].streetAddress], [columnHeaderName:Other Address Street, mapsTo:addresses[other].streetAddress], [columnHeaderName:Home Address Locality, mapsTo:addresses[home].locality], [columnHeaderName:Other Address Locality, mapsTo:addresses[other].locality], [columnHeaderName:Home Address Region, mapsTo:addresses[home].region], [columnHeaderName:Other Address Region, mapsTo:addresses[other].region], [columnHeaderName:Home Address Country, mapsTo:addresses[home].country], [columnHeaderName:Other Address Country, mapsTo:addresses[other].country], [columnHeaderName:Home Address Postal Code, mapsTo:addresses[home].postalCode], [columnHeaderName:Other Address Postal Code, mapsTo:addresses[other].postalCode], [columnHeaderName:Primary Address Type, mapsTo:addresses[$(type)].primary]]
         - idcsPii: true
         - multiValued: true
         - mutability: readWrite
         - required: false
         - returned: default
         - type: complex
         - uniqueness: none


        :param addresses: The addresses of this User.
        :type: list[oci.identity_domains.models.Addresses]
        """
        self._addresses = addresses

    @property
    def groups(self):
        """
        Gets the groups of this User.
        A list of groups that the user belongs to, either thorough direct membership, nested groups, or dynamically calculated

        **SCIM++ Properties:**
         - idcsCompositeKey: [value]
         - idcsSearchable: true
         - multiValued: true
         - mutability: readOnly
         - required: false
         - returned: request
         - type: complex
         - uniqueness: none


        :return: The groups of this User.
        :rtype: list[oci.identity_domains.models.UserGroups]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """
        Sets the groups of this User.
        A list of groups that the user belongs to, either thorough direct membership, nested groups, or dynamically calculated

        **SCIM++ Properties:**
         - idcsCompositeKey: [value]
         - idcsSearchable: true
         - multiValued: true
         - mutability: readOnly
         - required: false
         - returned: request
         - type: complex
         - uniqueness: none


        :param groups: The groups of this User.
        :type: list[oci.identity_domains.models.UserGroups]
        """
        self._groups = groups

    @property
    def entitlements(self):
        """
        Gets the entitlements of this User.
        A list of entitlements for the User that represent a thing the User has.

        **SCIM++ Properties:**
         - idcsCompositeKey: [value, type]
         - multiValued: true
         - mutability: readWrite
         - required: false
         - returned: default
         - type: complex
         - uniqueness: none


        :return: The entitlements of this User.
        :rtype: list[oci.identity_domains.models.UserEntitlements]
        """
        return self._entitlements

    @entitlements.setter
    def entitlements(self, entitlements):
        """
        Sets the entitlements of this User.
        A list of entitlements for the User that represent a thing the User has.

        **SCIM++ Properties:**
         - idcsCompositeKey: [value, type]
         - multiValued: true
         - mutability: readWrite
         - required: false
         - returned: default
         - type: complex
         - uniqueness: none


        :param entitlements: The entitlements of this User.
        :type: list[oci.identity_domains.models.UserEntitlements]
        """
        self._entitlements = entitlements

    @property
    def roles(self):
        """
        Gets the roles of this User.
        A list of roles for the User that collectively represent who the User is; e.g., 'Student', 'Faculty'.

        **SCIM++ Properties:**
         - idcsCompositeKey: [value, type]
         - multiValued: true
         - mutability: readWrite
         - required: false
         - returned: default
         - type: complex
         - uniqueness: none


        :return: The roles of this User.
        :rtype: list[oci.identity_domains.models.UserRoles]
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        """
        Sets the roles of this User.
        A list of roles for the User that collectively represent who the User is; e.g., 'Student', 'Faculty'.

        **SCIM++ Properties:**
         - idcsCompositeKey: [value, type]
         - multiValued: true
         - mutability: readWrite
         - required: false
         - returned: default
         - type: complex
         - uniqueness: none


        :param roles: The roles of this User.
        :type: list[oci.identity_domains.models.UserRoles]
        """
        self._roles = roles

    @property
    def x509_certificates(self):
        """
        Gets the x509_certificates of this User.
        A list of certificates issued to the User.

        **SCIM++ Properties:**
         - idcsCompositeKey: [value]
         - multiValued: true
         - mutability: readWrite
         - required: false
         - returned: default
         - type: complex
         - uniqueness: none


        :return: The x509_certificates of this User.
        :rtype: list[oci.identity_domains.models.UserX509Certificates]
        """
        return self._x509_certificates

    @x509_certificates.setter
    def x509_certificates(self, x509_certificates):
        """
        Sets the x509_certificates of this User.
        A list of certificates issued to the User.

        **SCIM++ Properties:**
         - idcsCompositeKey: [value]
         - multiValued: true
         - mutability: readWrite
         - required: false
         - returned: default
         - type: complex
         - uniqueness: none


        :param x509_certificates: The x509_certificates of this User.
        :type: list[oci.identity_domains.models.UserX509Certificates]
        """
        self._x509_certificates = x509_certificates

    @property
    def urnietfparamsscimschemasextensionenterprise2_0_user(self):
        """
        Gets the urnietfparamsscimschemasextensionenterprise2_0_user of this User.

        :return: The urnietfparamsscimschemasextensionenterprise2_0_user of this User.
        :rtype: oci.identity_domains.models.ExtensionEnterprise20User
        """
        return self._urnietfparamsscimschemasextensionenterprise2_0_user

    @urnietfparamsscimschemasextensionenterprise2_0_user.setter
    def urnietfparamsscimschemasextensionenterprise2_0_user(self, urnietfparamsscimschemasextensionenterprise2_0_user):
        """
        Sets the urnietfparamsscimschemasextensionenterprise2_0_user of this User.

        :param urnietfparamsscimschemasextensionenterprise2_0_user: The urnietfparamsscimschemasextensionenterprise2_0_user of this User.
        :type: oci.identity_domains.models.ExtensionEnterprise20User
        """
        self._urnietfparamsscimschemasextensionenterprise2_0_user = urnietfparamsscimschemasextensionenterprise2_0_user

    @property
    def urnietfparamsscimschemasoracleidcsextensionuser_user(self):
        """
        Gets the urnietfparamsscimschemasoracleidcsextensionuser_user of this User.

        :return: The urnietfparamsscimschemasoracleidcsextensionuser_user of this User.
        :rtype: oci.identity_domains.models.ExtensionUserUser
        """
        return self._urnietfparamsscimschemasoracleidcsextensionuser_user

    @urnietfparamsscimschemasoracleidcsextensionuser_user.setter
    def urnietfparamsscimschemasoracleidcsextensionuser_user(self, urnietfparamsscimschemasoracleidcsextensionuser_user):
        """
        Sets the urnietfparamsscimschemasoracleidcsextensionuser_user of this User.

        :param urnietfparamsscimschemasoracleidcsextensionuser_user: The urnietfparamsscimschemasoracleidcsextensionuser_user of this User.
        :type: oci.identity_domains.models.ExtensionUserUser
        """
        self._urnietfparamsscimschemasoracleidcsextensionuser_user = urnietfparamsscimschemasoracleidcsextensionuser_user

    @property
    def urnietfparamsscimschemasoracleidcsextensionpassword_state_user(self):
        """
        Gets the urnietfparamsscimschemasoracleidcsextensionpassword_state_user of this User.

        :return: The urnietfparamsscimschemasoracleidcsextensionpassword_state_user of this User.
        :rtype: oci.identity_domains.models.ExtensionPasswordStateUser
        """
        return self._urnietfparamsscimschemasoracleidcsextensionpassword_state_user

    @urnietfparamsscimschemasoracleidcsextensionpassword_state_user.setter
    def urnietfparamsscimschemasoracleidcsextensionpassword_state_user(self, urnietfparamsscimschemasoracleidcsextensionpassword_state_user):
        """
        Sets the urnietfparamsscimschemasoracleidcsextensionpassword_state_user of this User.

        :param urnietfparamsscimschemasoracleidcsextensionpassword_state_user: The urnietfparamsscimschemasoracleidcsextensionpassword_state_user of this User.
        :type: oci.identity_domains.models.ExtensionPasswordStateUser
        """
        self._urnietfparamsscimschemasoracleidcsextensionpassword_state_user = urnietfparamsscimschemasoracleidcsextensionpassword_state_user

    @property
    def urnietfparamsscimschemasoracleidcsextensionuser_state_user(self):
        """
        Gets the urnietfparamsscimschemasoracleidcsextensionuser_state_user of this User.

        :return: The urnietfparamsscimschemasoracleidcsextensionuser_state_user of this User.
        :rtype: oci.identity_domains.models.ExtensionUserStateUser
        """
        return self._urnietfparamsscimschemasoracleidcsextensionuser_state_user

    @urnietfparamsscimschemasoracleidcsextensionuser_state_user.setter
    def urnietfparamsscimschemasoracleidcsextensionuser_state_user(self, urnietfparamsscimschemasoracleidcsextensionuser_state_user):
        """
        Sets the urnietfparamsscimschemasoracleidcsextensionuser_state_user of this User.

        :param urnietfparamsscimschemasoracleidcsextensionuser_state_user: The urnietfparamsscimschemasoracleidcsextensionuser_state_user of this User.
        :type: oci.identity_domains.models.ExtensionUserStateUser
        """
        self._urnietfparamsscimschemasoracleidcsextensionuser_state_user = urnietfparamsscimschemasoracleidcsextensionuser_state_user

    @property
    def urnietfparamsscimschemasoracleidcsextensionposix_user(self):
        """
        Gets the urnietfparamsscimschemasoracleidcsextensionposix_user of this User.

        :return: The urnietfparamsscimschemasoracleidcsextensionposix_user of this User.
        :rtype: oci.identity_domains.models.ExtensionPosixUser
        """
        return self._urnietfparamsscimschemasoracleidcsextensionposix_user

    @urnietfparamsscimschemasoracleidcsextensionposix_user.setter
    def urnietfparamsscimschemasoracleidcsextensionposix_user(self, urnietfparamsscimschemasoracleidcsextensionposix_user):
        """
        Sets the urnietfparamsscimschemasoracleidcsextensionposix_user of this User.

        :param urnietfparamsscimschemasoracleidcsextensionposix_user: The urnietfparamsscimschemasoracleidcsextensionposix_user of this User.
        :type: oci.identity_domains.models.ExtensionPosixUser
        """
        self._urnietfparamsscimschemasoracleidcsextensionposix_user = urnietfparamsscimschemasoracleidcsextensionposix_user

    @property
    def urnietfparamsscimschemasoracleidcsextensionkerberos_user_user(self):
        """
        Gets the urnietfparamsscimschemasoracleidcsextensionkerberos_user_user of this User.

        :return: The urnietfparamsscimschemasoracleidcsextensionkerberos_user_user of this User.
        :rtype: oci.identity_domains.models.ExtensionKerberosUserUser
        """
        return self._urnietfparamsscimschemasoracleidcsextensionkerberos_user_user

    @urnietfparamsscimschemasoracleidcsextensionkerberos_user_user.setter
    def urnietfparamsscimschemasoracleidcsextensionkerberos_user_user(self, urnietfparamsscimschemasoracleidcsextensionkerberos_user_user):
        """
        Sets the urnietfparamsscimschemasoracleidcsextensionkerberos_user_user of this User.

        :param urnietfparamsscimschemasoracleidcsextensionkerberos_user_user: The urnietfparamsscimschemasoracleidcsextensionkerberos_user_user of this User.
        :type: oci.identity_domains.models.ExtensionKerberosUserUser
        """
        self._urnietfparamsscimschemasoracleidcsextensionkerberos_user_user = urnietfparamsscimschemasoracleidcsextensionkerberos_user_user

    @property
    def urnietfparamsscimschemasoracleidcsextensionmfa_user(self):
        """
        Gets the urnietfparamsscimschemasoracleidcsextensionmfa_user of this User.

        :return: The urnietfparamsscimschemasoracleidcsextensionmfa_user of this User.
        :rtype: oci.identity_domains.models.ExtensionMfaUser
        """
        return self._urnietfparamsscimschemasoracleidcsextensionmfa_user

    @urnietfparamsscimschemasoracleidcsextensionmfa_user.setter
    def urnietfparamsscimschemasoracleidcsextensionmfa_user(self, urnietfparamsscimschemasoracleidcsextensionmfa_user):
        """
        Sets the urnietfparamsscimschemasoracleidcsextensionmfa_user of this User.

        :param urnietfparamsscimschemasoracleidcsextensionmfa_user: The urnietfparamsscimschemasoracleidcsextensionmfa_user of this User.
        :type: oci.identity_domains.models.ExtensionMfaUser
        """
        self._urnietfparamsscimschemasoracleidcsextensionmfa_user = urnietfparamsscimschemasoracleidcsextensionmfa_user

    @property
    def urnietfparamsscimschemasoracleidcsextensionadaptive_user(self):
        """
        Gets the urnietfparamsscimschemasoracleidcsextensionadaptive_user of this User.

        :return: The urnietfparamsscimschemasoracleidcsextensionadaptive_user of this User.
        :rtype: oci.identity_domains.models.ExtensionAdaptiveUser
        """
        return self._urnietfparamsscimschemasoracleidcsextensionadaptive_user

    @urnietfparamsscimschemasoracleidcsextensionadaptive_user.setter
    def urnietfparamsscimschemasoracleidcsextensionadaptive_user(self, urnietfparamsscimschemasoracleidcsextensionadaptive_user):
        """
        Sets the urnietfparamsscimschemasoracleidcsextensionadaptive_user of this User.

        :param urnietfparamsscimschemasoracleidcsextensionadaptive_user: The urnietfparamsscimschemasoracleidcsextensionadaptive_user of this User.
        :type: oci.identity_domains.models.ExtensionAdaptiveUser
        """
        self._urnietfparamsscimschemasoracleidcsextensionadaptive_user = urnietfparamsscimschemasoracleidcsextensionadaptive_user

    @property
    def urnietfparamsscimschemasoracleidcsextensionsff_user(self):
        """
        Gets the urnietfparamsscimschemasoracleidcsextensionsff_user of this User.

        :return: The urnietfparamsscimschemasoracleidcsextensionsff_user of this User.
        :rtype: oci.identity_domains.models.ExtensionSffUser
        """
        return self._urnietfparamsscimschemasoracleidcsextensionsff_user

    @urnietfparamsscimschemasoracleidcsextensionsff_user.setter
    def urnietfparamsscimschemasoracleidcsextensionsff_user(self, urnietfparamsscimschemasoracleidcsextensionsff_user):
        """
        Sets the urnietfparamsscimschemasoracleidcsextensionsff_user of this User.

        :param urnietfparamsscimschemasoracleidcsextensionsff_user: The urnietfparamsscimschemasoracleidcsextensionsff_user of this User.
        :type: oci.identity_domains.models.ExtensionSffUser
        """
        self._urnietfparamsscimschemasoracleidcsextensionsff_user = urnietfparamsscimschemasoracleidcsextensionsff_user

    @property
    def urnietfparamsscimschemasoracleidcsextensionsecurity_questions_user(self):
        """
        Gets the urnietfparamsscimschemasoracleidcsextensionsecurity_questions_user of this User.

        :return: The urnietfparamsscimschemasoracleidcsextensionsecurity_questions_user of this User.
        :rtype: oci.identity_domains.models.ExtensionSecurityQuestionsUser
        """
        return self._urnietfparamsscimschemasoracleidcsextensionsecurity_questions_user

    @urnietfparamsscimschemasoracleidcsextensionsecurity_questions_user.setter
    def urnietfparamsscimschemasoracleidcsextensionsecurity_questions_user(self, urnietfparamsscimschemasoracleidcsextensionsecurity_questions_user):
        """
        Sets the urnietfparamsscimschemasoracleidcsextensionsecurity_questions_user of this User.

        :param urnietfparamsscimschemasoracleidcsextensionsecurity_questions_user: The urnietfparamsscimschemasoracleidcsextensionsecurity_questions_user of this User.
        :type: oci.identity_domains.models.ExtensionSecurityQuestionsUser
        """
        self._urnietfparamsscimschemasoracleidcsextensionsecurity_questions_user = urnietfparamsscimschemasoracleidcsextensionsecurity_questions_user

    @property
    def urnietfparamsscimschemasoracleidcsextensionself_registration_user(self):
        """
        Gets the urnietfparamsscimschemasoracleidcsextensionself_registration_user of this User.

        :return: The urnietfparamsscimschemasoracleidcsextensionself_registration_user of this User.
        :rtype: oci.identity_domains.models.ExtensionSelfRegistrationUser
        """
        return self._urnietfparamsscimschemasoracleidcsextensionself_registration_user

    @urnietfparamsscimschemasoracleidcsextensionself_registration_user.setter
    def urnietfparamsscimschemasoracleidcsextensionself_registration_user(self, urnietfparamsscimschemasoracleidcsextensionself_registration_user):
        """
        Sets the urnietfparamsscimschemasoracleidcsextensionself_registration_user of this User.

        :param urnietfparamsscimschemasoracleidcsextensionself_registration_user: The urnietfparamsscimschemasoracleidcsextensionself_registration_user of this User.
        :type: oci.identity_domains.models.ExtensionSelfRegistrationUser
        """
        self._urnietfparamsscimschemasoracleidcsextensionself_registration_user = urnietfparamsscimschemasoracleidcsextensionself_registration_user

    @property
    def urnietfparamsscimschemasoracleidcsextensionsocial_account_user(self):
        """
        Gets the urnietfparamsscimschemasoracleidcsextensionsocial_account_user of this User.

        :return: The urnietfparamsscimschemasoracleidcsextensionsocial_account_user of this User.
        :rtype: oci.identity_domains.models.ExtensionSocialAccountUser
        """
        return self._urnietfparamsscimschemasoracleidcsextensionsocial_account_user

    @urnietfparamsscimschemasoracleidcsextensionsocial_account_user.setter
    def urnietfparamsscimschemasoracleidcsextensionsocial_account_user(self, urnietfparamsscimschemasoracleidcsextensionsocial_account_user):
        """
        Sets the urnietfparamsscimschemasoracleidcsextensionsocial_account_user of this User.

        :param urnietfparamsscimschemasoracleidcsextensionsocial_account_user: The urnietfparamsscimschemasoracleidcsextensionsocial_account_user of this User.
        :type: oci.identity_domains.models.ExtensionSocialAccountUser
        """
        self._urnietfparamsscimschemasoracleidcsextensionsocial_account_user = urnietfparamsscimschemasoracleidcsextensionsocial_account_user

    @property
    def urnietfparamsscimschemasoracleidcsextensiondb_user_user(self):
        """
        Gets the urnietfparamsscimschemasoracleidcsextensiondb_user_user of this User.

        :return: The urnietfparamsscimschemasoracleidcsextensiondb_user_user of this User.
        :rtype: oci.identity_domains.models.ExtensionDbUserUser
        """
        return self._urnietfparamsscimschemasoracleidcsextensiondb_user_user

    @urnietfparamsscimschemasoracleidcsextensiondb_user_user.setter
    def urnietfparamsscimschemasoracleidcsextensiondb_user_user(self, urnietfparamsscimschemasoracleidcsextensiondb_user_user):
        """
        Sets the urnietfparamsscimschemasoracleidcsextensiondb_user_user of this User.

        :param urnietfparamsscimschemasoracleidcsextensiondb_user_user: The urnietfparamsscimschemasoracleidcsextensiondb_user_user of this User.
        :type: oci.identity_domains.models.ExtensionDbUserUser
        """
        self._urnietfparamsscimschemasoracleidcsextensiondb_user_user = urnietfparamsscimschemasoracleidcsextensiondb_user_user

    @property
    def urnietfparamsscimschemasoracleidcsextensionterms_of_use_user(self):
        """
        Gets the urnietfparamsscimschemasoracleidcsextensionterms_of_use_user of this User.

        :return: The urnietfparamsscimschemasoracleidcsextensionterms_of_use_user of this User.
        :rtype: oci.identity_domains.models.ExtensionTermsOfUseUser
        """
        return self._urnietfparamsscimschemasoracleidcsextensionterms_of_use_user

    @urnietfparamsscimschemasoracleidcsextensionterms_of_use_user.setter
    def urnietfparamsscimschemasoracleidcsextensionterms_of_use_user(self, urnietfparamsscimschemasoracleidcsextensionterms_of_use_user):
        """
        Sets the urnietfparamsscimschemasoracleidcsextensionterms_of_use_user of this User.

        :param urnietfparamsscimschemasoracleidcsextensionterms_of_use_user: The urnietfparamsscimschemasoracleidcsextensionterms_of_use_user of this User.
        :type: oci.identity_domains.models.ExtensionTermsOfUseUser
        """
        self._urnietfparamsscimschemasoracleidcsextensionterms_of_use_user = urnietfparamsscimschemasoracleidcsextensionterms_of_use_user

    @property
    def urnietfparamsscimschemasoracleidcsextensionpasswordless_user(self):
        """
        Gets the urnietfparamsscimschemasoracleidcsextensionpasswordless_user of this User.

        :return: The urnietfparamsscimschemasoracleidcsextensionpasswordless_user of this User.
        :rtype: oci.identity_domains.models.ExtensionPasswordlessUser
        """
        return self._urnietfparamsscimschemasoracleidcsextensionpasswordless_user

    @urnietfparamsscimschemasoracleidcsextensionpasswordless_user.setter
    def urnietfparamsscimschemasoracleidcsextensionpasswordless_user(self, urnietfparamsscimschemasoracleidcsextensionpasswordless_user):
        """
        Sets the urnietfparamsscimschemasoracleidcsextensionpasswordless_user of this User.

        :param urnietfparamsscimschemasoracleidcsextensionpasswordless_user: The urnietfparamsscimschemasoracleidcsextensionpasswordless_user of this User.
        :type: oci.identity_domains.models.ExtensionPasswordlessUser
        """
        self._urnietfparamsscimschemasoracleidcsextensionpasswordless_user = urnietfparamsscimschemasoracleidcsextensionpasswordless_user

    @property
    def urnietfparamsscimschemasoracleidcsextension_oci_tags(self):
        """
        Gets the urnietfparamsscimschemasoracleidcsextension_oci_tags of this User.

        :return: The urnietfparamsscimschemasoracleidcsextension_oci_tags of this User.
        :rtype: oci.identity_domains.models.ExtensionOCITags
        """
        return self._urnietfparamsscimschemasoracleidcsextension_oci_tags

    @urnietfparamsscimschemasoracleidcsextension_oci_tags.setter
    def urnietfparamsscimschemasoracleidcsextension_oci_tags(self, urnietfparamsscimschemasoracleidcsextension_oci_tags):
        """
        Sets the urnietfparamsscimschemasoracleidcsextension_oci_tags of this User.

        :param urnietfparamsscimschemasoracleidcsextension_oci_tags: The urnietfparamsscimschemasoracleidcsextension_oci_tags of this User.
        :type: oci.identity_domains.models.ExtensionOCITags
        """
        self._urnietfparamsscimschemasoracleidcsextension_oci_tags = urnietfparamsscimschemasoracleidcsextension_oci_tags

    @property
    def urnietfparamsscimschemasoracleidcsextensionuser_credentials_user(self):
        """
        Gets the urnietfparamsscimschemasoracleidcsextensionuser_credentials_user of this User.

        :return: The urnietfparamsscimschemasoracleidcsextensionuser_credentials_user of this User.
        :rtype: oci.identity_domains.models.ExtensionUserCredentialsUser
        """
        return self._urnietfparamsscimschemasoracleidcsextensionuser_credentials_user

    @urnietfparamsscimschemasoracleidcsextensionuser_credentials_user.setter
    def urnietfparamsscimschemasoracleidcsextensionuser_credentials_user(self, urnietfparamsscimschemasoracleidcsextensionuser_credentials_user):
        """
        Sets the urnietfparamsscimschemasoracleidcsextensionuser_credentials_user of this User.

        :param urnietfparamsscimschemasoracleidcsextensionuser_credentials_user: The urnietfparamsscimschemasoracleidcsextensionuser_credentials_user of this User.
        :type: oci.identity_domains.models.ExtensionUserCredentialsUser
        """
        self._urnietfparamsscimschemasoracleidcsextensionuser_credentials_user = urnietfparamsscimschemasoracleidcsextensionuser_credentials_user

    @property
    def urnietfparamsscimschemasoracleidcsextensioncapabilities_user(self):
        """
        Gets the urnietfparamsscimschemasoracleidcsextensioncapabilities_user of this User.

        :return: The urnietfparamsscimschemasoracleidcsextensioncapabilities_user of this User.
        :rtype: oci.identity_domains.models.ExtensionCapabilitiesUser
        """
        return self._urnietfparamsscimschemasoracleidcsextensioncapabilities_user

    @urnietfparamsscimschemasoracleidcsextensioncapabilities_user.setter
    def urnietfparamsscimschemasoracleidcsextensioncapabilities_user(self, urnietfparamsscimschemasoracleidcsextensioncapabilities_user):
        """
        Sets the urnietfparamsscimschemasoracleidcsextensioncapabilities_user of this User.

        :param urnietfparamsscimschemasoracleidcsextensioncapabilities_user: The urnietfparamsscimschemasoracleidcsextensioncapabilities_user of this User.
        :type: oci.identity_domains.models.ExtensionCapabilitiesUser
        """
        self._urnietfparamsscimschemasoracleidcsextensioncapabilities_user = urnietfparamsscimschemasoracleidcsextensioncapabilities_user

    @property
    def urnietfparamsscimschemasoracleidcsextensiondb_credentials_user(self):
        """
        Gets the urnietfparamsscimschemasoracleidcsextensiondb_credentials_user of this User.

        :return: The urnietfparamsscimschemasoracleidcsextensiondb_credentials_user of this User.
        :rtype: oci.identity_domains.models.ExtensionDbCredentialsUser
        """
        return self._urnietfparamsscimschemasoracleidcsextensiondb_credentials_user

    @urnietfparamsscimschemasoracleidcsextensiondb_credentials_user.setter
    def urnietfparamsscimschemasoracleidcsextensiondb_credentials_user(self, urnietfparamsscimschemasoracleidcsextensiondb_credentials_user):
        """
        Sets the urnietfparamsscimschemasoracleidcsextensiondb_credentials_user of this User.

        :param urnietfparamsscimschemasoracleidcsextensiondb_credentials_user: The urnietfparamsscimschemasoracleidcsextensiondb_credentials_user of this User.
        :type: oci.identity_domains.models.ExtensionDbCredentialsUser
        """
        self._urnietfparamsscimschemasoracleidcsextensiondb_credentials_user = urnietfparamsscimschemasoracleidcsextensiondb_credentials_user

    @property
    def urnietfparamsscimschemasoracleidcsextensionself_change_user(self):
        """
        Gets the urnietfparamsscimschemasoracleidcsextensionself_change_user of this User.

        :return: The urnietfparamsscimschemasoracleidcsextensionself_change_user of this User.
        :rtype: oci.identity_domains.models.ExtensionSelfChangeUser
        """
        return self._urnietfparamsscimschemasoracleidcsextensionself_change_user

    @urnietfparamsscimschemasoracleidcsextensionself_change_user.setter
    def urnietfparamsscimschemasoracleidcsextensionself_change_user(self, urnietfparamsscimschemasoracleidcsextensionself_change_user):
        """
        Sets the urnietfparamsscimschemasoracleidcsextensionself_change_user of this User.

        :param urnietfparamsscimschemasoracleidcsextensionself_change_user: The urnietfparamsscimschemasoracleidcsextensionself_change_user of this User.
        :type: oci.identity_domains.models.ExtensionSelfChangeUser
        """
        self._urnietfparamsscimschemasoracleidcsextensionself_change_user = urnietfparamsscimschemasoracleidcsextensionself_change_user

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
