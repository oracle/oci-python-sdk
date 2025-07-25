# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20241201


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateListingRevisionPackageDetails(object):
    """
    The model for an Oracle Cloud Infrastructure Marketplace Publisher listing revision package.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateListingRevisionPackageDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param listing_revision_id:
            The value to assign to the listing_revision_id property of this CreateListingRevisionPackageDetails.
        :type listing_revision_id: str

        :param package_version:
            The value to assign to the package_version property of this CreateListingRevisionPackageDetails.
        :type package_version: str

        :param display_name:
            The value to assign to the display_name property of this CreateListingRevisionPackageDetails.
        :type display_name: str

        :param description:
            The value to assign to the description property of this CreateListingRevisionPackageDetails.
        :type description: str

        :param artifact_id:
            The value to assign to the artifact_id property of this CreateListingRevisionPackageDetails.
        :type artifact_id: str

        :param term_id:
            The value to assign to the term_id property of this CreateListingRevisionPackageDetails.
        :type term_id: str

        :param is_default:
            The value to assign to the is_default property of this CreateListingRevisionPackageDetails.
        :type is_default: bool

        :param are_security_upgrades_provided:
            The value to assign to the are_security_upgrades_provided property of this CreateListingRevisionPackageDetails.
        :type are_security_upgrades_provided: bool

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateListingRevisionPackageDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateListingRevisionPackageDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'listing_revision_id': 'str',
            'package_version': 'str',
            'display_name': 'str',
            'description': 'str',
            'artifact_id': 'str',
            'term_id': 'str',
            'is_default': 'bool',
            'are_security_upgrades_provided': 'bool',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }
        self.attribute_map = {
            'listing_revision_id': 'listingRevisionId',
            'package_version': 'packageVersion',
            'display_name': 'displayName',
            'description': 'description',
            'artifact_id': 'artifactId',
            'term_id': 'termId',
            'is_default': 'isDefault',
            'are_security_upgrades_provided': 'areSecurityUpgradesProvided',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }
        self._listing_revision_id = None
        self._package_version = None
        self._display_name = None
        self._description = None
        self._artifact_id = None
        self._term_id = None
        self._is_default = None
        self._are_security_upgrades_provided = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def listing_revision_id(self):
        """
        **[Required]** Gets the listing_revision_id of this CreateListingRevisionPackageDetails.
        The OCID for the listing revision in Marketplace Publisher.


        :return: The listing_revision_id of this CreateListingRevisionPackageDetails.
        :rtype: str
        """
        return self._listing_revision_id

    @listing_revision_id.setter
    def listing_revision_id(self, listing_revision_id):
        """
        Sets the listing_revision_id of this CreateListingRevisionPackageDetails.
        The OCID for the listing revision in Marketplace Publisher.


        :param listing_revision_id: The listing_revision_id of this CreateListingRevisionPackageDetails.
        :type: str
        """
        self._listing_revision_id = listing_revision_id

    @property
    def package_version(self):
        """
        **[Required]** Gets the package_version of this CreateListingRevisionPackageDetails.
        The version for the package.


        :return: The package_version of this CreateListingRevisionPackageDetails.
        :rtype: str
        """
        return self._package_version

    @package_version.setter
    def package_version(self, package_version):
        """
        Sets the package_version of this CreateListingRevisionPackageDetails.
        The version for the package.


        :param package_version: The package_version of this CreateListingRevisionPackageDetails.
        :type: str
        """
        self._package_version = package_version

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateListingRevisionPackageDetails.
        The name for the listing revision package.


        :return: The display_name of this CreateListingRevisionPackageDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateListingRevisionPackageDetails.
        The name for the listing revision package.


        :param display_name: The display_name of this CreateListingRevisionPackageDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this CreateListingRevisionPackageDetails.
        Description for this package.


        :return: The description of this CreateListingRevisionPackageDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreateListingRevisionPackageDetails.
        Description for this package.


        :param description: The description of this CreateListingRevisionPackageDetails.
        :type: str
        """
        self._description = description

    @property
    def artifact_id(self):
        """
        **[Required]** Gets the artifact_id of this CreateListingRevisionPackageDetails.
        The unique identifier for the artifact.


        :return: The artifact_id of this CreateListingRevisionPackageDetails.
        :rtype: str
        """
        return self._artifact_id

    @artifact_id.setter
    def artifact_id(self, artifact_id):
        """
        Sets the artifact_id of this CreateListingRevisionPackageDetails.
        The unique identifier for the artifact.


        :param artifact_id: The artifact_id of this CreateListingRevisionPackageDetails.
        :type: str
        """
        self._artifact_id = artifact_id

    @property
    def term_id(self):
        """
        **[Required]** Gets the term_id of this CreateListingRevisionPackageDetails.
        The unique identifier for the term.


        :return: The term_id of this CreateListingRevisionPackageDetails.
        :rtype: str
        """
        return self._term_id

    @term_id.setter
    def term_id(self, term_id):
        """
        Sets the term_id of this CreateListingRevisionPackageDetails.
        The unique identifier for the term.


        :param term_id: The term_id of this CreateListingRevisionPackageDetails.
        :type: str
        """
        self._term_id = term_id

    @property
    def is_default(self):
        """
        Gets the is_default of this CreateListingRevisionPackageDetails.
        Identifies that this will be default package for the listing revision.


        :return: The is_default of this CreateListingRevisionPackageDetails.
        :rtype: bool
        """
        return self._is_default

    @is_default.setter
    def is_default(self, is_default):
        """
        Sets the is_default of this CreateListingRevisionPackageDetails.
        Identifies that this will be default package for the listing revision.


        :param is_default: The is_default of this CreateListingRevisionPackageDetails.
        :type: bool
        """
        self._is_default = is_default

    @property
    def are_security_upgrades_provided(self):
        """
        **[Required]** Gets the are_security_upgrades_provided of this CreateListingRevisionPackageDetails.
        Identifies whether security upgrades will be provided for this package.


        :return: The are_security_upgrades_provided of this CreateListingRevisionPackageDetails.
        :rtype: bool
        """
        return self._are_security_upgrades_provided

    @are_security_upgrades_provided.setter
    def are_security_upgrades_provided(self, are_security_upgrades_provided):
        """
        Sets the are_security_upgrades_provided of this CreateListingRevisionPackageDetails.
        Identifies whether security upgrades will be provided for this package.


        :param are_security_upgrades_provided: The are_security_upgrades_provided of this CreateListingRevisionPackageDetails.
        :type: bool
        """
        self._are_security_upgrades_provided = are_security_upgrades_provided

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateListingRevisionPackageDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this CreateListingRevisionPackageDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateListingRevisionPackageDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this CreateListingRevisionPackageDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateListingRevisionPackageDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this CreateListingRevisionPackageDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateListingRevisionPackageDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this CreateListingRevisionPackageDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
