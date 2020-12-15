# coding: utf-8

import pprint
import re

import six





class CCEClusterNodeInformationMetadata:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'name': 'str'
    }

    attribute_map = {
        'name': 'name'
    }

    def __init__(self, name=None):
        """CCEClusterNodeInformationMetadata - a model defined in huaweicloud sdk"""
        
        

        self._name = None
        self.discriminator = None

        self.name = name

    @property
    def name(self):
        """Gets the name of this CCEClusterNodeInformationMetadata.

        节点名称  > 修改节点名称后，弹性云服务器名称（虚拟机名称）会同步修改。 > > 命名规则：以小写字母开头，由小写字母、数字、中划线(-)组成，长度范围1-56位，且不能以中划线(-)结尾。

        :return: The name of this CCEClusterNodeInformationMetadata.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CCEClusterNodeInformationMetadata.

        节点名称  > 修改节点名称后，弹性云服务器名称（虚拟机名称）会同步修改。 > > 命名规则：以小写字母开头，由小写字母、数字、中划线(-)组成，长度范围1-56位，且不能以中划线(-)结尾。

        :param name: The name of this CCEClusterNodeInformationMetadata.
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
        if not isinstance(other, CCEClusterNodeInformationMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
