# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SteeringPolicyAnswer(object):
    """
    DNS record data with metadata for processing in a steering policy.


    **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SteeringPolicyAnswer object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this SteeringPolicyAnswer.
        :type name: str

        :param rtype:
            The value to assign to the rtype property of this SteeringPolicyAnswer.
        :type rtype: str

        :param rdata:
            The value to assign to the rdata property of this SteeringPolicyAnswer.
        :type rdata: str

        :param pool:
            The value to assign to the pool property of this SteeringPolicyAnswer.
        :type pool: str

        :param is_disabled:
            The value to assign to the is_disabled property of this SteeringPolicyAnswer.
        :type is_disabled: bool

        """
        self.swagger_types = {
            'name': 'str',
            'rtype': 'str',
            'rdata': 'str',
            'pool': 'str',
            'is_disabled': 'bool'
        }

        self.attribute_map = {
            'name': 'name',
            'rtype': 'rtype',
            'rdata': 'rdata',
            'pool': 'pool',
            'is_disabled': 'isDisabled'
        }

        self._name = None
        self._rtype = None
        self._rdata = None
        self._pool = None
        self._is_disabled = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this SteeringPolicyAnswer.
        A user-friendly name for the answer, unique within the steering policy.
        An answer's `name` property can be referenced in `answerCondition` properties
        of rules using `answer.name`.

        **Example:**

          \"rules\": [
            {
              \"ruleType\": \"FILTER\",
              \"defaultAnswerData\":  [
                {
                  \"answerCondition\": \"answer.name == 'server 1'\",
                  \"shouldKeep\": true
                }
              ]
            }
          ]


        :return: The name of this SteeringPolicyAnswer.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this SteeringPolicyAnswer.
        A user-friendly name for the answer, unique within the steering policy.
        An answer's `name` property can be referenced in `answerCondition` properties
        of rules using `answer.name`.

        **Example:**

          \"rules\": [
            {
              \"ruleType\": \"FILTER\",
              \"defaultAnswerData\":  [
                {
                  \"answerCondition\": \"answer.name == 'server 1'\",
                  \"shouldKeep\": true
                }
              ]
            }
          ]


        :param name: The name of this SteeringPolicyAnswer.
        :type: str
        """
        self._name = name

    @property
    def rtype(self):
        """
        **[Required]** Gets the rtype of this SteeringPolicyAnswer.
        The canonical name for the record's type. Only A, AAAA, and CNAME are supported. For more
        information, see `Supported DNS Resource Record Types`__.

        __ https://docs.cloud.oracle.com/iaas/Content/DNS/Reference/supporteddnsresource.htm


        :return: The rtype of this SteeringPolicyAnswer.
        :rtype: str
        """
        return self._rtype

    @rtype.setter
    def rtype(self, rtype):
        """
        Sets the rtype of this SteeringPolicyAnswer.
        The canonical name for the record's type. Only A, AAAA, and CNAME are supported. For more
        information, see `Supported DNS Resource Record Types`__.

        __ https://docs.cloud.oracle.com/iaas/Content/DNS/Reference/supporteddnsresource.htm


        :param rtype: The rtype of this SteeringPolicyAnswer.
        :type: str
        """
        self._rtype = rtype

    @property
    def rdata(self):
        """
        **[Required]** Gets the rdata of this SteeringPolicyAnswer.
        The record's data, as whitespace-delimited tokens in
        type-specific presentation format. All RDATA is normalized and the
        returned presentation of your RDATA may differ from its initial input.
        For more information about RDATA, see `Supported DNS Resource Record Types`__.

        __ https://docs.cloud.oracle.com/iaas/Content/DNS/Reference/supporteddnsresource.htm


        :return: The rdata of this SteeringPolicyAnswer.
        :rtype: str
        """
        return self._rdata

    @rdata.setter
    def rdata(self, rdata):
        """
        Sets the rdata of this SteeringPolicyAnswer.
        The record's data, as whitespace-delimited tokens in
        type-specific presentation format. All RDATA is normalized and the
        returned presentation of your RDATA may differ from its initial input.
        For more information about RDATA, see `Supported DNS Resource Record Types`__.

        __ https://docs.cloud.oracle.com/iaas/Content/DNS/Reference/supporteddnsresource.htm


        :param rdata: The rdata of this SteeringPolicyAnswer.
        :type: str
        """
        self._rdata = rdata

    @property
    def pool(self):
        """
        Gets the pool of this SteeringPolicyAnswer.
        The freeform name of a group of one or more records in which this record is included,
        such as \"LAX data center\". An answer's `pool` property can be referenced in `answerCondition`
        properties of rules using `answer.pool`.

        **Example:**

          \"rules\": [
            {
              \"ruleType\": \"FILTER\",
              \"defaultAnswerData\":  [
                {
                  \"answerCondition\": \"answer.pool == 'US East Servers'\",
                  \"shouldKeep\": true
                }
              ]
            }
          ]


        :return: The pool of this SteeringPolicyAnswer.
        :rtype: str
        """
        return self._pool

    @pool.setter
    def pool(self, pool):
        """
        Sets the pool of this SteeringPolicyAnswer.
        The freeform name of a group of one or more records in which this record is included,
        such as \"LAX data center\". An answer's `pool` property can be referenced in `answerCondition`
        properties of rules using `answer.pool`.

        **Example:**

          \"rules\": [
            {
              \"ruleType\": \"FILTER\",
              \"defaultAnswerData\":  [
                {
                  \"answerCondition\": \"answer.pool == 'US East Servers'\",
                  \"shouldKeep\": true
                }
              ]
            }
          ]


        :param pool: The pool of this SteeringPolicyAnswer.
        :type: str
        """
        self._pool = pool

    @property
    def is_disabled(self):
        """
        Gets the is_disabled of this SteeringPolicyAnswer.
        Set this property to `true` to indicate that the answer is administratively disabled,
        such as when the corresponding server is down for maintenance. An answer's `isDisabled`
        property can be referenced in `answerCondition` properties in rules using `answer.isDisabled`.

        **Example:**
          \"rules\": [
            {
              \"ruleType\": \"FILTER\",
              \"defaultAnswerData\": [
                {
                  \"answerCondition\": \"answer.isDisabled != true\",
                  \"shouldKeep\": true
                }
              ]
            },


        :return: The is_disabled of this SteeringPolicyAnswer.
        :rtype: bool
        """
        return self._is_disabled

    @is_disabled.setter
    def is_disabled(self, is_disabled):
        """
        Sets the is_disabled of this SteeringPolicyAnswer.
        Set this property to `true` to indicate that the answer is administratively disabled,
        such as when the corresponding server is down for maintenance. An answer's `isDisabled`
        property can be referenced in `answerCondition` properties in rules using `answer.isDisabled`.

        **Example:**
          \"rules\": [
            {
              \"ruleType\": \"FILTER\",
              \"defaultAnswerData\": [
                {
                  \"answerCondition\": \"answer.isDisabled != true\",
                  \"shouldKeep\": true
                }
              ]
            },


        :param is_disabled: The is_disabled of this SteeringPolicyAnswer.
        :type: bool
        """
        self._is_disabled = is_disabled

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
