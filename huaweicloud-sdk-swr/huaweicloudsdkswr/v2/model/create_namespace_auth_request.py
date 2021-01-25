# coding: utf-8

import pprint
import re

import six





class CreateNamespaceAuthRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'namespace': 'str',
        'body': 'list[UserAuth]'
    }

    attribute_map = {
        'namespace': 'namespace',
        'body': 'body'
    }

    def __init__(self, namespace=None, body=None):
        """CreateNamespaceAuthRequest - a model defined in huaweicloud sdk"""
        
        

        self._namespace = None
        self._body = None
        self.discriminator = None

        self.namespace = namespace
        if body is not None:
            self.body = body

    @property
    def namespace(self):
        """Gets the namespace of this CreateNamespaceAuthRequest.


        :return: The namespace of this CreateNamespaceAuthRequest.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this CreateNamespaceAuthRequest.


        :param namespace: The namespace of this CreateNamespaceAuthRequest.
        :type: str
        """
        self._namespace = namespace

    @property
    def body(self):
        """Gets the body of this CreateNamespaceAuthRequest.


        :return: The body of this CreateNamespaceAuthRequest.
        :rtype: list[UserAuth]
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this CreateNamespaceAuthRequest.


        :param body: The body of this CreateNamespaceAuthRequest.
        :type: list[UserAuth]
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
        if not isinstance(other, CreateNamespaceAuthRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other