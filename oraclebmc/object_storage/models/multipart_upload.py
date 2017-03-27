# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict


class MultipartUpload(object):

    def __init__(self):

        self.swagger_types = {
            'namespace': 'str',
            'bucket': 'str',
            'object': 'str',
            'upload_id': 'str',
            'time_created': 'datetime'
        }

        self.attribute_map = {
            'namespace': 'namespace',
            'bucket': 'bucket',
            'object': 'object',
            'upload_id': 'uploadId',
            'time_created': 'timeCreated'
        }

        self._namespace = None
        self._bucket = None
        self._object = None
        self._upload_id = None
        self._time_created = None

    @property
    def namespace(self):
        """
        Gets the namespace of this MultipartUpload.
        the namespace in which the in-progress upload lives.


        :return: The namespace of this MultipartUpload.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """
        Sets the namespace of this MultipartUpload.
        the namespace in which the in-progress upload lives.


        :param namespace: The namespace of this MultipartUpload.
        :type: str
        """
        self._namespace = namespace

    @property
    def bucket(self):
        """
        Gets the bucket of this MultipartUpload.
        the bucket in which the in-progress upload lives.


        :return: The bucket of this MultipartUpload.
        :rtype: str
        """
        return self._bucket

    @bucket.setter
    def bucket(self, bucket):
        """
        Sets the bucket of this MultipartUpload.
        the bucket in which the in-progress upload lives.


        :param bucket: The bucket of this MultipartUpload.
        :type: str
        """
        self._bucket = bucket

    @property
    def object(self):
        """
        Gets the object of this MultipartUpload.
        the object name for the in-progress upload.


        :return: The object of this MultipartUpload.
        :rtype: str
        """
        return self._object

    @object.setter
    def object(self, object):
        """
        Sets the object of this MultipartUpload.
        the object name for the in-progress upload.


        :param object: The object of this MultipartUpload.
        :type: str
        """
        self._object = object

    @property
    def upload_id(self):
        """
        Gets the upload_id of this MultipartUpload.
        the ID of the in-progress upload.


        :return: The upload_id of this MultipartUpload.
        :rtype: str
        """
        return self._upload_id

    @upload_id.setter
    def upload_id(self, upload_id):
        """
        Sets the upload_id of this MultipartUpload.
        the ID of the in-progress upload.


        :param upload_id: The upload_id of this MultipartUpload.
        :type: str
        """
        self._upload_id = upload_id

    @property
    def time_created(self):
        """
        Gets the time_created of this MultipartUpload.
        The date and time at which the upload was created.


        :return: The time_created of this MultipartUpload.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this MultipartUpload.
        The date and time at which the upload was created.


        :param time_created: The time_created of this MultipartUpload.
        :type: datetime
        """
        self._time_created = time_created

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
