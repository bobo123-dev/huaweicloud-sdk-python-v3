# coding: utf-8

import pprint
import re

import six





class UpdateNodePoolRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'cluster_id': 'str',
        'nodepool_id': 'str',
        'content_type': 'str',
        'error_status': 'str',
        'body': 'NodePool'
    }

    attribute_map = {
        'cluster_id': 'cluster_id',
        'nodepool_id': 'nodepool_id',
        'content_type': 'Content-Type',
        'error_status': 'errorStatus',
        'body': 'body'
    }

    def __init__(self, cluster_id=None, nodepool_id=None, content_type='application/json', error_status=None, body=None):
        """UpdateNodePoolRequest - a model defined in huaweicloud sdk"""
        
        

        self._cluster_id = None
        self._nodepool_id = None
        self._content_type = None
        self._error_status = None
        self._body = None
        self.discriminator = None

        self.cluster_id = cluster_id
        self.nodepool_id = nodepool_id
        self.content_type = content_type
        if error_status is not None:
            self.error_status = error_status
        if body is not None:
            self.body = body

    @property
    def cluster_id(self):
        """Gets the cluster_id of this UpdateNodePoolRequest.


        :return: The cluster_id of this UpdateNodePoolRequest.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this UpdateNodePoolRequest.


        :param cluster_id: The cluster_id of this UpdateNodePoolRequest.
        :type: str
        """
        self._cluster_id = cluster_id

    @property
    def nodepool_id(self):
        """Gets the nodepool_id of this UpdateNodePoolRequest.


        :return: The nodepool_id of this UpdateNodePoolRequest.
        :rtype: str
        """
        return self._nodepool_id

    @nodepool_id.setter
    def nodepool_id(self, nodepool_id):
        """Sets the nodepool_id of this UpdateNodePoolRequest.


        :param nodepool_id: The nodepool_id of this UpdateNodePoolRequest.
        :type: str
        """
        self._nodepool_id = nodepool_id

    @property
    def content_type(self):
        """Gets the content_type of this UpdateNodePoolRequest.


        :return: The content_type of this UpdateNodePoolRequest.
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        """Sets the content_type of this UpdateNodePoolRequest.


        :param content_type: The content_type of this UpdateNodePoolRequest.
        :type: str
        """
        self._content_type = content_type

    @property
    def error_status(self):
        """Gets the error_status of this UpdateNodePoolRequest.


        :return: The error_status of this UpdateNodePoolRequest.
        :rtype: str
        """
        return self._error_status

    @error_status.setter
    def error_status(self, error_status):
        """Sets the error_status of this UpdateNodePoolRequest.


        :param error_status: The error_status of this UpdateNodePoolRequest.
        :type: str
        """
        self._error_status = error_status

    @property
    def body(self):
        """Gets the body of this UpdateNodePoolRequest.


        :return: The body of this UpdateNodePoolRequest.
        :rtype: NodePool
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this UpdateNodePoolRequest.


        :param body: The body of this UpdateNodePoolRequest.
        :type: NodePool
        """
        self._body = body

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                if attr in self.sensitive_list:
                    result[attr] = "****"
                else:
                    result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UpdateNodePoolRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
