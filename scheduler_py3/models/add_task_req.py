# coding: utf-8

"""
    

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from scheduler_py3.configuration import Configuration


class AddTaskReq(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'session_id': 'str',
        'name': 'str',
        'input': 'str',
        'task_type': 'str'
    }

    attribute_map = {
        'session_id': 'session_id',
        'name': 'name',
        'input': 'input',
        'task_type': 'task_type'
    }

    def __init__(self, session_id=None, name=None, input=None, task_type=None, _configuration=None):  # noqa: E501
        """AddTaskReq - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._session_id = None
        self._name = None
        self._input = None
        self._task_type = None
        self.discriminator = None

        self.session_id = session_id
        self.name = name
        self.input = input
        self.task_type = task_type

    @property
    def session_id(self):
        """Gets the session_id of this AddTaskReq.  # noqa: E501


        :return: The session_id of this AddTaskReq.  # noqa: E501
        :rtype: str
        """
        return self._session_id

    @session_id.setter
    def session_id(self, session_id):
        """Sets the session_id of this AddTaskReq.


        :param session_id: The session_id of this AddTaskReq.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and session_id is None:
            raise ValueError("Invalid value for `session_id`, must not be `None`")  # noqa: E501

        self._session_id = session_id

    @property
    def name(self):
        """Gets the name of this AddTaskReq.  # noqa: E501


        :return: The name of this AddTaskReq.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AddTaskReq.


        :param name: The name of this AddTaskReq.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def input(self):
        """Gets the input of this AddTaskReq.  # noqa: E501


        :return: The input of this AddTaskReq.  # noqa: E501
        :rtype: str
        """
        return self._input

    @input.setter
    def input(self, input):
        """Sets the input of this AddTaskReq.


        :param input: The input of this AddTaskReq.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and input is None:
            raise ValueError("Invalid value for `input`, must not be `None`")  # noqa: E501

        self._input = input

    @property
    def task_type(self):
        """Gets the task_type of this AddTaskReq.  # noqa: E501


        :return: The task_type of this AddTaskReq.  # noqa: E501
        :rtype: str
        """
        return self._task_type

    @task_type.setter
    def task_type(self, task_type):
        """Sets the task_type of this AddTaskReq.


        :param task_type: The task_type of this AddTaskReq.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and task_type is None:
            raise ValueError("Invalid value for `task_type`, must not be `None`")  # noqa: E501

        self._task_type = task_type

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
                result[attr] = value
        if issubclass(AddTaskReq, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AddTaskReq):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AddTaskReq):
            return True

        return self.to_dict() != other.to_dict()