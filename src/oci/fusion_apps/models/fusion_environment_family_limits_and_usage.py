# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class FusionEnvironmentFamilyLimitsAndUsage(object):
    """
    Details of EnvironmentLimits.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new FusionEnvironmentFamilyLimitsAndUsage object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param production_limit_and_usage:
            The value to assign to the production_limit_and_usage property of this FusionEnvironmentFamilyLimitsAndUsage.
        :type production_limit_and_usage: oci.fusion_apps.models.LimitAndUsage

        :param test_limit_and_usage:
            The value to assign to the test_limit_and_usage property of this FusionEnvironmentFamilyLimitsAndUsage.
        :type test_limit_and_usage: oci.fusion_apps.models.LimitAndUsage

        :param development_limit_and_usage:
            The value to assign to the development_limit_and_usage property of this FusionEnvironmentFamilyLimitsAndUsage.
        :type development_limit_and_usage: oci.fusion_apps.models.LimitAndUsage

        """
        self.swagger_types = {
            'production_limit_and_usage': 'LimitAndUsage',
            'test_limit_and_usage': 'LimitAndUsage',
            'development_limit_and_usage': 'LimitAndUsage'
        }

        self.attribute_map = {
            'production_limit_and_usage': 'productionLimitAndUsage',
            'test_limit_and_usage': 'testLimitAndUsage',
            'development_limit_and_usage': 'developmentLimitAndUsage'
        }

        self._production_limit_and_usage = None
        self._test_limit_and_usage = None
        self._development_limit_and_usage = None

    @property
    def production_limit_and_usage(self):
        """
        **[Required]** Gets the production_limit_and_usage of this FusionEnvironmentFamilyLimitsAndUsage.

        :return: The production_limit_and_usage of this FusionEnvironmentFamilyLimitsAndUsage.
        :rtype: oci.fusion_apps.models.LimitAndUsage
        """
        return self._production_limit_and_usage

    @production_limit_and_usage.setter
    def production_limit_and_usage(self, production_limit_and_usage):
        """
        Sets the production_limit_and_usage of this FusionEnvironmentFamilyLimitsAndUsage.

        :param production_limit_and_usage: The production_limit_and_usage of this FusionEnvironmentFamilyLimitsAndUsage.
        :type: oci.fusion_apps.models.LimitAndUsage
        """
        self._production_limit_and_usage = production_limit_and_usage

    @property
    def test_limit_and_usage(self):
        """
        **[Required]** Gets the test_limit_and_usage of this FusionEnvironmentFamilyLimitsAndUsage.

        :return: The test_limit_and_usage of this FusionEnvironmentFamilyLimitsAndUsage.
        :rtype: oci.fusion_apps.models.LimitAndUsage
        """
        return self._test_limit_and_usage

    @test_limit_and_usage.setter
    def test_limit_and_usage(self, test_limit_and_usage):
        """
        Sets the test_limit_and_usage of this FusionEnvironmentFamilyLimitsAndUsage.

        :param test_limit_and_usage: The test_limit_and_usage of this FusionEnvironmentFamilyLimitsAndUsage.
        :type: oci.fusion_apps.models.LimitAndUsage
        """
        self._test_limit_and_usage = test_limit_and_usage

    @property
    def development_limit_and_usage(self):
        """
        **[Required]** Gets the development_limit_and_usage of this FusionEnvironmentFamilyLimitsAndUsage.

        :return: The development_limit_and_usage of this FusionEnvironmentFamilyLimitsAndUsage.
        :rtype: oci.fusion_apps.models.LimitAndUsage
        """
        return self._development_limit_and_usage

    @development_limit_and_usage.setter
    def development_limit_and_usage(self, development_limit_and_usage):
        """
        Sets the development_limit_and_usage of this FusionEnvironmentFamilyLimitsAndUsage.

        :param development_limit_and_usage: The development_limit_and_usage of this FusionEnvironmentFamilyLimitsAndUsage.
        :type: oci.fusion_apps.models.LimitAndUsage
        """
        self._development_limit_and_usage = development_limit_and_usage

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
