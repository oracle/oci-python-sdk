# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateDatabaseDetails(object):
    """
    Details for creating a database backup.

    **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.
    """

    #: A constant which can be used with the db_workload property of a CreateDatabaseDetails.
    #: This constant has a value of "OLTP"
    DB_WORKLOAD_OLTP = "OLTP"

    #: A constant which can be used with the db_workload property of a CreateDatabaseDetails.
    #: This constant has a value of "DSS"
    DB_WORKLOAD_DSS = "DSS"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateDatabaseDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param admin_password:
            The value to assign to the admin_password property of this CreateDatabaseDetails.
        :type admin_password: str

        :param character_set:
            The value to assign to the character_set property of this CreateDatabaseDetails.
        :type character_set: str

        :param db_backup_config:
            The value to assign to the db_backup_config property of this CreateDatabaseDetails.
        :type db_backup_config: DbBackupConfig

        :param db_name:
            The value to assign to the db_name property of this CreateDatabaseDetails.
        :type db_name: str

        :param db_workload:
            The value to assign to the db_workload property of this CreateDatabaseDetails.
            Allowed values for this property are: "OLTP", "DSS"
        :type db_workload: str

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateDatabaseDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateDatabaseDetails.
        :type freeform_tags: dict(str, str)

        :param ncharacter_set:
            The value to assign to the ncharacter_set property of this CreateDatabaseDetails.
        :type ncharacter_set: str

        :param pdb_name:
            The value to assign to the pdb_name property of this CreateDatabaseDetails.
        :type pdb_name: str

        """
        self.swagger_types = {
            'admin_password': 'str',
            'character_set': 'str',
            'db_backup_config': 'DbBackupConfig',
            'db_name': 'str',
            'db_workload': 'str',
            'defined_tags': 'dict(str, dict(str, object))',
            'freeform_tags': 'dict(str, str)',
            'ncharacter_set': 'str',
            'pdb_name': 'str'
        }

        self.attribute_map = {
            'admin_password': 'adminPassword',
            'character_set': 'characterSet',
            'db_backup_config': 'dbBackupConfig',
            'db_name': 'dbName',
            'db_workload': 'dbWorkload',
            'defined_tags': 'definedTags',
            'freeform_tags': 'freeformTags',
            'ncharacter_set': 'ncharacterSet',
            'pdb_name': 'pdbName'
        }

        self._admin_password = None
        self._character_set = None
        self._db_backup_config = None
        self._db_name = None
        self._db_workload = None
        self._defined_tags = None
        self._freeform_tags = None
        self._ncharacter_set = None
        self._pdb_name = None

    @property
    def admin_password(self):
        """
        **[Required]** Gets the admin_password of this CreateDatabaseDetails.
        A strong password for SYS, SYSTEM, and PDB Admin. The password must be at least nine characters and contain at least two uppercase, two lowercase, two numbers, and two special characters. The special characters must be _, \\#, or -.


        :return: The admin_password of this CreateDatabaseDetails.
        :rtype: str
        """
        return self._admin_password

    @admin_password.setter
    def admin_password(self, admin_password):
        """
        Sets the admin_password of this CreateDatabaseDetails.
        A strong password for SYS, SYSTEM, and PDB Admin. The password must be at least nine characters and contain at least two uppercase, two lowercase, two numbers, and two special characters. The special characters must be _, \\#, or -.


        :param admin_password: The admin_password of this CreateDatabaseDetails.
        :type: str
        """
        self._admin_password = admin_password

    @property
    def character_set(self):
        """
        Gets the character_set of this CreateDatabaseDetails.
        The character set for the database.  The default is AL32UTF8. Allowed values are:

        AL32UTF8, AR8ADOS710, AR8ADOS720, AR8APTEC715, AR8ARABICMACS, AR8ASMO8X, AR8ISO8859P6, AR8MSWIN1256, AR8MUSSAD768, AR8NAFITHA711, AR8NAFITHA721, AR8SAKHR706, AR8SAKHR707, AZ8ISO8859P9E, BG8MSWIN, BG8PC437S, BLT8CP921, BLT8ISO8859P13, BLT8MSWIN1257, BLT8PC775, BN8BSCII, CDN8PC863, CEL8ISO8859P14, CL8ISO8859P5, CL8ISOIR111, CL8KOI8R, CL8KOI8U, CL8MACCYRILLICS, CL8MSWIN1251, EE8ISO8859P2, EE8MACCES, EE8MACCROATIANS, EE8MSWIN1250, EE8PC852, EL8DEC, EL8ISO8859P7, EL8MACGREEKS, EL8MSWIN1253, EL8PC437S, EL8PC851, EL8PC869, ET8MSWIN923, HU8ABMOD, HU8CWI2, IN8ISCII, IS8PC861, IW8ISO8859P8, IW8MACHEBREWS, IW8MSWIN1255, IW8PC1507, JA16EUC, JA16EUCTILDE, JA16SJIS, JA16SJISTILDE, JA16VMS, KO16KSC5601, KO16KSCCS, KO16MSWIN949, LA8ISO6937, LA8PASSPORT, LT8MSWIN921, LT8PC772, LT8PC774, LV8PC1117, LV8PC8LR, LV8RST104090, N8PC865, NE8ISO8859P10, NEE8ISO8859P4, RU8BESTA, RU8PC855, RU8PC866, SE8ISO8859P3, TH8MACTHAIS, TH8TISASCII, TR8DEC, TR8MACTURKISHS, TR8MSWIN1254, TR8PC857, US7ASCII, US8PC437, UTF8, VN8MSWIN1258, VN8VN3, WE8DEC, WE8DG, WE8ISO8859P1, WE8ISO8859P15, WE8ISO8859P9, WE8MACROMAN8S, WE8MSWIN1252, WE8NCR4970, WE8NEXTSTEP, WE8PC850, WE8PC858, WE8PC860, WE8ROMAN8, ZHS16CGB231280, ZHS16GBK, ZHT16BIG5, ZHT16CCDC, ZHT16DBT, ZHT16HKSCS, ZHT16MSWIN950, ZHT32EUC, ZHT32SOPS, ZHT32TRIS


        :return: The character_set of this CreateDatabaseDetails.
        :rtype: str
        """
        return self._character_set

    @character_set.setter
    def character_set(self, character_set):
        """
        Sets the character_set of this CreateDatabaseDetails.
        The character set for the database.  The default is AL32UTF8. Allowed values are:

        AL32UTF8, AR8ADOS710, AR8ADOS720, AR8APTEC715, AR8ARABICMACS, AR8ASMO8X, AR8ISO8859P6, AR8MSWIN1256, AR8MUSSAD768, AR8NAFITHA711, AR8NAFITHA721, AR8SAKHR706, AR8SAKHR707, AZ8ISO8859P9E, BG8MSWIN, BG8PC437S, BLT8CP921, BLT8ISO8859P13, BLT8MSWIN1257, BLT8PC775, BN8BSCII, CDN8PC863, CEL8ISO8859P14, CL8ISO8859P5, CL8ISOIR111, CL8KOI8R, CL8KOI8U, CL8MACCYRILLICS, CL8MSWIN1251, EE8ISO8859P2, EE8MACCES, EE8MACCROATIANS, EE8MSWIN1250, EE8PC852, EL8DEC, EL8ISO8859P7, EL8MACGREEKS, EL8MSWIN1253, EL8PC437S, EL8PC851, EL8PC869, ET8MSWIN923, HU8ABMOD, HU8CWI2, IN8ISCII, IS8PC861, IW8ISO8859P8, IW8MACHEBREWS, IW8MSWIN1255, IW8PC1507, JA16EUC, JA16EUCTILDE, JA16SJIS, JA16SJISTILDE, JA16VMS, KO16KSC5601, KO16KSCCS, KO16MSWIN949, LA8ISO6937, LA8PASSPORT, LT8MSWIN921, LT8PC772, LT8PC774, LV8PC1117, LV8PC8LR, LV8RST104090, N8PC865, NE8ISO8859P10, NEE8ISO8859P4, RU8BESTA, RU8PC855, RU8PC866, SE8ISO8859P3, TH8MACTHAIS, TH8TISASCII, TR8DEC, TR8MACTURKISHS, TR8MSWIN1254, TR8PC857, US7ASCII, US8PC437, UTF8, VN8MSWIN1258, VN8VN3, WE8DEC, WE8DG, WE8ISO8859P1, WE8ISO8859P15, WE8ISO8859P9, WE8MACROMAN8S, WE8MSWIN1252, WE8NCR4970, WE8NEXTSTEP, WE8PC850, WE8PC858, WE8PC860, WE8ROMAN8, ZHS16CGB231280, ZHS16GBK, ZHT16BIG5, ZHT16CCDC, ZHT16DBT, ZHT16HKSCS, ZHT16MSWIN950, ZHT32EUC, ZHT32SOPS, ZHT32TRIS


        :param character_set: The character_set of this CreateDatabaseDetails.
        :type: str
        """
        self._character_set = character_set

    @property
    def db_backup_config(self):
        """
        Gets the db_backup_config of this CreateDatabaseDetails.

        :return: The db_backup_config of this CreateDatabaseDetails.
        :rtype: DbBackupConfig
        """
        return self._db_backup_config

    @db_backup_config.setter
    def db_backup_config(self, db_backup_config):
        """
        Sets the db_backup_config of this CreateDatabaseDetails.

        :param db_backup_config: The db_backup_config of this CreateDatabaseDetails.
        :type: DbBackupConfig
        """
        self._db_backup_config = db_backup_config

    @property
    def db_name(self):
        """
        **[Required]** Gets the db_name of this CreateDatabaseDetails.
        The database name. The name must begin with an alphabetic character and can contain a maximum of eight alphanumeric characters. Special characters are not permitted.


        :return: The db_name of this CreateDatabaseDetails.
        :rtype: str
        """
        return self._db_name

    @db_name.setter
    def db_name(self, db_name):
        """
        Sets the db_name of this CreateDatabaseDetails.
        The database name. The name must begin with an alphabetic character and can contain a maximum of eight alphanumeric characters. Special characters are not permitted.


        :param db_name: The db_name of this CreateDatabaseDetails.
        :type: str
        """
        self._db_name = db_name

    @property
    def db_workload(self):
        """
        Gets the db_workload of this CreateDatabaseDetails.
        The database workload type.

        Allowed values for this property are: "OLTP", "DSS"


        :return: The db_workload of this CreateDatabaseDetails.
        :rtype: str
        """
        return self._db_workload

    @db_workload.setter
    def db_workload(self, db_workload):
        """
        Sets the db_workload of this CreateDatabaseDetails.
        The database workload type.


        :param db_workload: The db_workload of this CreateDatabaseDetails.
        :type: str
        """
        allowed_values = ["OLTP", "DSS"]
        if not value_allowed_none_or_none_sentinel(db_workload, allowed_values):
            raise ValueError(
                "Invalid value for `db_workload`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._db_workload = db_workload

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateDatabaseDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CreateDatabaseDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateDatabaseDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CreateDatabaseDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateDatabaseDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CreateDatabaseDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateDatabaseDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CreateDatabaseDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def ncharacter_set(self):
        """
        Gets the ncharacter_set of this CreateDatabaseDetails.
        The national character set for the database.  The default is AL16UTF16. Allowed values are:
        AL16UTF16 or UTF8.


        :return: The ncharacter_set of this CreateDatabaseDetails.
        :rtype: str
        """
        return self._ncharacter_set

    @ncharacter_set.setter
    def ncharacter_set(self, ncharacter_set):
        """
        Sets the ncharacter_set of this CreateDatabaseDetails.
        The national character set for the database.  The default is AL16UTF16. Allowed values are:
        AL16UTF16 or UTF8.


        :param ncharacter_set: The ncharacter_set of this CreateDatabaseDetails.
        :type: str
        """
        self._ncharacter_set = ncharacter_set

    @property
    def pdb_name(self):
        """
        Gets the pdb_name of this CreateDatabaseDetails.
        The name of the pluggable database. The name must begin with an alphabetic character and can contain a maximum of eight alphanumeric characters. Special characters are not permitted. Pluggable database should not be same as database name.


        :return: The pdb_name of this CreateDatabaseDetails.
        :rtype: str
        """
        return self._pdb_name

    @pdb_name.setter
    def pdb_name(self, pdb_name):
        """
        Sets the pdb_name of this CreateDatabaseDetails.
        The name of the pluggable database. The name must begin with an alphabetic character and can contain a maximum of eight alphanumeric characters. Special characters are not permitted. Pluggable database should not be same as database name.


        :param pdb_name: The pdb_name of this CreateDatabaseDetails.
        :type: str
        """
        self._pdb_name = pdb_name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
