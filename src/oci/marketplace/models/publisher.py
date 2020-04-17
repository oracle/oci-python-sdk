# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Publisher(object):
    """
    The model for a publisher.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Publisher object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this Publisher.
        :type id: str

        :param name:
            The value to assign to the name property of this Publisher.
        :type name: str

        :param description:
            The value to assign to the description property of this Publisher.
        :type description: str

        :param year_founded:
            The value to assign to the year_founded property of this Publisher.
        :type year_founded: int

        :param website_url:
            The value to assign to the website_url property of this Publisher.
        :type website_url: str

        :param contact_email:
            The value to assign to the contact_email property of this Publisher.
        :type contact_email: str

        :param contact_phone:
            The value to assign to the contact_phone property of this Publisher.
        :type contact_phone: str

        :param hq_address:
            The value to assign to the hq_address property of this Publisher.
        :type hq_address: str

        :param logo:
            The value to assign to the logo property of this Publisher.
        :type logo: UploadData

        :param links:
            The value to assign to the links property of this Publisher.
        :type links: list[Link]

        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'description': 'str',
            'year_founded': 'int',
            'website_url': 'str',
            'contact_email': 'str',
            'contact_phone': 'str',
            'hq_address': 'str',
            'logo': 'UploadData',
            'links': 'list[Link]'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'description': 'description',
            'year_founded': 'yearFounded',
            'website_url': 'websiteUrl',
            'contact_email': 'contactEmail',
            'contact_phone': 'contactPhone',
            'hq_address': 'hqAddress',
            'logo': 'logo',
            'links': 'links'
        }

        self._id = None
        self._name = None
        self._description = None
        self._year_founded = None
        self._website_url = None
        self._contact_email = None
        self._contact_phone = None
        self._hq_address = None
        self._logo = None
        self._links = None

    @property
    def id(self):
        """
        Gets the id of this Publisher.
        Unique identifier for the publisher.


        :return: The id of this Publisher.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Publisher.
        Unique identifier for the publisher.


        :param id: The id of this Publisher.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """
        Gets the name of this Publisher.
        The name of the publisher.


        :return: The name of this Publisher.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Publisher.
        The name of the publisher.


        :param name: The name of this Publisher.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """
        Gets the description of this Publisher.
        A description of the publisher.


        :return: The description of this Publisher.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this Publisher.
        A description of the publisher.


        :param description: The description of this Publisher.
        :type: str
        """
        self._description = description

    @property
    def year_founded(self):
        """
        Gets the year_founded of this Publisher.
        The year the publisher's company or organization was founded.


        :return: The year_founded of this Publisher.
        :rtype: int
        """
        return self._year_founded

    @year_founded.setter
    def year_founded(self, year_founded):
        """
        Sets the year_founded of this Publisher.
        The year the publisher's company or organization was founded.


        :param year_founded: The year_founded of this Publisher.
        :type: int
        """
        self._year_founded = year_founded

    @property
    def website_url(self):
        """
        Gets the website_url of this Publisher.
        The publisher's website.


        :return: The website_url of this Publisher.
        :rtype: str
        """
        return self._website_url

    @website_url.setter
    def website_url(self, website_url):
        """
        Sets the website_url of this Publisher.
        The publisher's website.


        :param website_url: The website_url of this Publisher.
        :type: str
        """
        self._website_url = website_url

    @property
    def contact_email(self):
        """
        Gets the contact_email of this Publisher.
        The email address of the publisher.


        :return: The contact_email of this Publisher.
        :rtype: str
        """
        return self._contact_email

    @contact_email.setter
    def contact_email(self, contact_email):
        """
        Sets the contact_email of this Publisher.
        The email address of the publisher.


        :param contact_email: The contact_email of this Publisher.
        :type: str
        """
        self._contact_email = contact_email

    @property
    def contact_phone(self):
        """
        Gets the contact_phone of this Publisher.
        The phone number of the publisher.


        :return: The contact_phone of this Publisher.
        :rtype: str
        """
        return self._contact_phone

    @contact_phone.setter
    def contact_phone(self, contact_phone):
        """
        Sets the contact_phone of this Publisher.
        The phone number of the publisher.


        :param contact_phone: The contact_phone of this Publisher.
        :type: str
        """
        self._contact_phone = contact_phone

    @property
    def hq_address(self):
        """
        Gets the hq_address of this Publisher.
        The address of the publisher's headquarters.


        :return: The hq_address of this Publisher.
        :rtype: str
        """
        return self._hq_address

    @hq_address.setter
    def hq_address(self, hq_address):
        """
        Sets the hq_address of this Publisher.
        The address of the publisher's headquarters.


        :param hq_address: The hq_address of this Publisher.
        :type: str
        """
        self._hq_address = hq_address

    @property
    def logo(self):
        """
        Gets the logo of this Publisher.

        :return: The logo of this Publisher.
        :rtype: UploadData
        """
        return self._logo

    @logo.setter
    def logo(self, logo):
        """
        Sets the logo of this Publisher.

        :param logo: The logo of this Publisher.
        :type: UploadData
        """
        self._logo = logo

    @property
    def links(self):
        """
        Gets the links of this Publisher.
        Reference links.


        :return: The links of this Publisher.
        :rtype: list[Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """
        Sets the links of this Publisher.
        Reference links.


        :param links: The links of this Publisher.
        :type: list[Link]
        """
        self._links = links

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
