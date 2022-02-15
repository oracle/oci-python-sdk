# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MaskDataDetails(object):
    """
    Details to mask data.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new MaskDataDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param target_id:
            The value to assign to the target_id property of this MaskDataDetails.
        :type target_id: str

        :param is_decrypt:
            The value to assign to the is_decrypt property of this MaskDataDetails.
        :type is_decrypt: bool

        :param is_rerun:
            The value to assign to the is_rerun property of this MaskDataDetails.
        :type is_rerun: bool

        :param tablespace:
            The value to assign to the tablespace property of this MaskDataDetails.
        :type tablespace: str

        :param is_ignore_errors_enabled:
            The value to assign to the is_ignore_errors_enabled property of this MaskDataDetails.
        :type is_ignore_errors_enabled: bool

        :param seed:
            The value to assign to the seed property of this MaskDataDetails.
        :type seed: str

        :param is_move_interim_tables_enabled:
            The value to assign to the is_move_interim_tables_enabled property of this MaskDataDetails.
        :type is_move_interim_tables_enabled: bool

        :param is_execute_saved_script_enabled:
            The value to assign to the is_execute_saved_script_enabled property of this MaskDataDetails.
        :type is_execute_saved_script_enabled: bool

        """
        self.swagger_types = {
            'target_id': 'str',
            'is_decrypt': 'bool',
            'is_rerun': 'bool',
            'tablespace': 'str',
            'is_ignore_errors_enabled': 'bool',
            'seed': 'str',
            'is_move_interim_tables_enabled': 'bool',
            'is_execute_saved_script_enabled': 'bool'
        }

        self.attribute_map = {
            'target_id': 'targetId',
            'is_decrypt': 'isDecrypt',
            'is_rerun': 'isRerun',
            'tablespace': 'tablespace',
            'is_ignore_errors_enabled': 'isIgnoreErrorsEnabled',
            'seed': 'seed',
            'is_move_interim_tables_enabled': 'isMoveInterimTablesEnabled',
            'is_execute_saved_script_enabled': 'isExecuteSavedScriptEnabled'
        }

        self._target_id = None
        self._is_decrypt = None
        self._is_rerun = None
        self._tablespace = None
        self._is_ignore_errors_enabled = None
        self._seed = None
        self._is_move_interim_tables_enabled = None
        self._is_execute_saved_script_enabled = None

    @property
    def target_id(self):
        """
        Gets the target_id of this MaskDataDetails.
        The OCID of the target database to be masked. If it's not provided, the value of the
        targetId attribute in the MaskingPolicy resource is used. The OCID of the target
        database to be masked. If it's not provided, the value of the targetId attribute in
        the MaskingPolicy resource is used.


        :return: The target_id of this MaskDataDetails.
        :rtype: str
        """
        return self._target_id

    @target_id.setter
    def target_id(self, target_id):
        """
        Sets the target_id of this MaskDataDetails.
        The OCID of the target database to be masked. If it's not provided, the value of the
        targetId attribute in the MaskingPolicy resource is used. The OCID of the target
        database to be masked. If it's not provided, the value of the targetId attribute in
        the MaskingPolicy resource is used.


        :param target_id: The target_id of this MaskDataDetails.
        :type: str
        """
        self._target_id = target_id

    @property
    def is_decrypt(self):
        """
        Gets the is_decrypt of this MaskDataDetails.
        Indicates if the masking request is to decrypt the data values previously encrypted using Deterministic Encryption. Note that, to
        correctly decrypt the encrypted data values, it requires the same seed value that was provided to encrypt those data values.


        :return: The is_decrypt of this MaskDataDetails.
        :rtype: bool
        """
        return self._is_decrypt

    @is_decrypt.setter
    def is_decrypt(self, is_decrypt):
        """
        Sets the is_decrypt of this MaskDataDetails.
        Indicates if the masking request is to decrypt the data values previously encrypted using Deterministic Encryption. Note that, to
        correctly decrypt the encrypted data values, it requires the same seed value that was provided to encrypt those data values.


        :param is_decrypt: The is_decrypt of this MaskDataDetails.
        :type: bool
        """
        self._is_decrypt = is_decrypt

    @property
    def is_rerun(self):
        """
        Gets the is_rerun of this MaskDataDetails.
        Indicates if the masking request is to rerun the previously failed masking steps. If a masking request is submitted with the
        isIgnoreErrorsEnabled attribute set to true, the masking process tracks the failed masking steps. Another masking request can be
        submitted with the isRun attribute set to true to rerun those failed masking steps. It helps save time by executing only the failed
        masking steps and not doing the whole masking again.


        :return: The is_rerun of this MaskDataDetails.
        :rtype: bool
        """
        return self._is_rerun

    @is_rerun.setter
    def is_rerun(self, is_rerun):
        """
        Sets the is_rerun of this MaskDataDetails.
        Indicates if the masking request is to rerun the previously failed masking steps. If a masking request is submitted with the
        isIgnoreErrorsEnabled attribute set to true, the masking process tracks the failed masking steps. Another masking request can be
        submitted with the isRun attribute set to true to rerun those failed masking steps. It helps save time by executing only the failed
        masking steps and not doing the whole masking again.


        :param is_rerun: The is_rerun of this MaskDataDetails.
        :type: bool
        """
        self._is_rerun = is_rerun

    @property
    def tablespace(self):
        """
        Gets the tablespace of this MaskDataDetails.
        The tablespace that should be used to create the mapping tables, DMASK objects, and other temporary tables for data masking.
        If no tablespace is provided, the DEFAULT tablespace is used.


        :return: The tablespace of this MaskDataDetails.
        :rtype: str
        """
        return self._tablespace

    @tablespace.setter
    def tablespace(self, tablespace):
        """
        Sets the tablespace of this MaskDataDetails.
        The tablespace that should be used to create the mapping tables, DMASK objects, and other temporary tables for data masking.
        If no tablespace is provided, the DEFAULT tablespace is used.


        :param tablespace: The tablespace of this MaskDataDetails.
        :type: str
        """
        self._tablespace = tablespace

    @property
    def is_ignore_errors_enabled(self):
        """
        Gets the is_ignore_errors_enabled of this MaskDataDetails.
        Indicates if the masking process should continue on hitting an error. It provides fault tolerance support and is enabled by
        default. In fault-tolerant mode, the masking process saves the failed step and continues. You can then submit another masking
        request (with isRerun attribute set to true) to execute only the failed steps.


        :return: The is_ignore_errors_enabled of this MaskDataDetails.
        :rtype: bool
        """
        return self._is_ignore_errors_enabled

    @is_ignore_errors_enabled.setter
    def is_ignore_errors_enabled(self, is_ignore_errors_enabled):
        """
        Sets the is_ignore_errors_enabled of this MaskDataDetails.
        Indicates if the masking process should continue on hitting an error. It provides fault tolerance support and is enabled by
        default. In fault-tolerant mode, the masking process saves the failed step and continues. You can then submit another masking
        request (with isRerun attribute set to true) to execute only the failed steps.


        :param is_ignore_errors_enabled: The is_ignore_errors_enabled of this MaskDataDetails.
        :type: bool
        """
        self._is_ignore_errors_enabled = is_ignore_errors_enabled

    @property
    def seed(self):
        """
        Gets the seed of this MaskDataDetails.
        The seed value to be used in case of Deterministic Encryption and Deterministic Substitution masking formats.


        :return: The seed of this MaskDataDetails.
        :rtype: str
        """
        return self._seed

    @seed.setter
    def seed(self, seed):
        """
        Sets the seed of this MaskDataDetails.
        The seed value to be used in case of Deterministic Encryption and Deterministic Substitution masking formats.


        :param seed: The seed of this MaskDataDetails.
        :type: str
        """
        self._seed = seed

    @property
    def is_move_interim_tables_enabled(self):
        """
        Gets the is_move_interim_tables_enabled of this MaskDataDetails.
        Indicates if the interim DMASK tables should be moved to the user-specified tablespace. As interim tables can be large in size,
        set it to false if moving them causes performance overhead during masking.


        :return: The is_move_interim_tables_enabled of this MaskDataDetails.
        :rtype: bool
        """
        return self._is_move_interim_tables_enabled

    @is_move_interim_tables_enabled.setter
    def is_move_interim_tables_enabled(self, is_move_interim_tables_enabled):
        """
        Sets the is_move_interim_tables_enabled of this MaskDataDetails.
        Indicates if the interim DMASK tables should be moved to the user-specified tablespace. As interim tables can be large in size,
        set it to false if moving them causes performance overhead during masking.


        :param is_move_interim_tables_enabled: The is_move_interim_tables_enabled of this MaskDataDetails.
        :type: bool
        """
        self._is_move_interim_tables_enabled = is_move_interim_tables_enabled

    @property
    def is_execute_saved_script_enabled(self):
        """
        Gets the is_execute_saved_script_enabled of this MaskDataDetails.
        Indicates if data masking should be performed using a saved masking script. Setting this attribute to true skips masking script
        generation and executes the masking script stored in the Data Safe repository. It helps save time if there are no changes in
        the database tables and their dependencies.


        :return: The is_execute_saved_script_enabled of this MaskDataDetails.
        :rtype: bool
        """
        return self._is_execute_saved_script_enabled

    @is_execute_saved_script_enabled.setter
    def is_execute_saved_script_enabled(self, is_execute_saved_script_enabled):
        """
        Sets the is_execute_saved_script_enabled of this MaskDataDetails.
        Indicates if data masking should be performed using a saved masking script. Setting this attribute to true skips masking script
        generation and executes the masking script stored in the Data Safe repository. It helps save time if there are no changes in
        the database tables and their dependencies.


        :param is_execute_saved_script_enabled: The is_execute_saved_script_enabled of this MaskDataDetails.
        :type: bool
        """
        self._is_execute_saved_script_enabled = is_execute_saved_script_enabled

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
