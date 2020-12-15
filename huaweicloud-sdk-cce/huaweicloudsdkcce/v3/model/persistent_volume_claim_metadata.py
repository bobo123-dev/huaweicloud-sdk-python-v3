# coding: utf-8

import pprint
import re

import six





class PersistentVolumeClaimMetadata:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'labels': 'str',
        'name': 'str'
    }

    attribute_map = {
        'labels': 'labels',
        'name': 'name'
    }

    def __init__(self, labels=None, name=None):
        """PersistentVolumeClaimMetadata - a model defined in huaweicloud sdk"""
        
        

        self._labels = None
        self._name = None
        self.discriminator = None

        if labels is not None:
            self.labels = labels
        self.name = name

    @property
    def labels(self):
        """Gets the labels of this PersistentVolumeClaimMetadata.

        PersistentVolumeClaim标签，key/value对格式。 - Key：必须以字母或数字开头，可以包含字母、数字、连字符、下划线和点，最长63个字符；另外可以使用DNS子域作为前缀，例如example.com/my-key， DNS子域最长253个字符。 - Value：可以为空或者非空字符串，非空字符串必须以字符或数字开头，可以包含字母、数字、连字符、下划线和点，最长63个字符。

        :return: The labels of this PersistentVolumeClaimMetadata.
        :rtype: str
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this PersistentVolumeClaimMetadata.

        PersistentVolumeClaim标签，key/value对格式。 - Key：必须以字母或数字开头，可以包含字母、数字、连字符、下划线和点，最长63个字符；另外可以使用DNS子域作为前缀，例如example.com/my-key， DNS子域最长253个字符。 - Value：可以为空或者非空字符串，非空字符串必须以字符或数字开头，可以包含字母、数字、连字符、下划线和点，最长63个字符。

        :param labels: The labels of this PersistentVolumeClaimMetadata.
        :type: str
        """
        self._labels = labels

    @property
    def name(self):
        """Gets the name of this PersistentVolumeClaimMetadata.

        PersistentVolumeClaim名称，可以包含小写字母、数字、连字符和点，开头和结尾必须是字母或数字，最长253个字符，同一namespace下name不能重复。

        :return: The name of this PersistentVolumeClaimMetadata.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PersistentVolumeClaimMetadata.

        PersistentVolumeClaim名称，可以包含小写字母、数字、连字符和点，开头和结尾必须是字母或数字，最长253个字符，同一namespace下name不能重复。

        :param name: The name of this PersistentVolumeClaimMetadata.
        :type: str
        """
        self._name = name

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
        if not isinstance(other, PersistentVolumeClaimMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
