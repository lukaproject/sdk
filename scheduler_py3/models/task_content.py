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


class TaskContent(object):
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
        'id': 'str',
        'name': 'str',
        'task_type': 'str',
        'input': 'str',
        'output': 'str',
        'commit_time': 'int',
        'begin_time': 'int',
        'end_time': 'int',
        'status': 'str',
        'worker_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'task_type': 'task_type',
        'input': 'input',
        'output': 'output',
        'commit_time': 'commit_time',
        'begin_time': 'begin_time',
        'end_time': 'end_time',
        'status': 'status',
        'worker_id': 'worker_id'
    }

    def __init__(self, id=None, name=None, task_type=None, input=None, output=None, commit_time=None, begin_time=None, end_time=None, status=None, worker_id=None, _configuration=None):  # noqa: E501
        """TaskContent - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._name = None
        self._task_type = None
        self._input = None
        self._output = None
        self._commit_time = None
        self._begin_time = None
        self._end_time = None
        self._status = None
        self._worker_id = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.task_type = task_type
        if input is not None:
            self.input = input
        if output is not None:
            self.output = output
        if commit_time is not None:
            self.commit_time = commit_time
        if begin_time is not None:
            self.begin_time = begin_time
        if end_time is not None:
            self.end_time = end_time
        if status is not None:
            self.status = status
        if worker_id is not None:
            self.worker_id = worker_id

    @property
    def id(self):
        """Gets the id of this TaskContent.  # noqa: E501


        :return: The id of this TaskContent.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TaskContent.


        :param id: The id of this TaskContent.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this TaskContent.  # noqa: E501


        :return: The name of this TaskContent.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TaskContent.


        :param name: The name of this TaskContent.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def task_type(self):
        """Gets the task_type of this TaskContent.  # noqa: E501


        :return: The task_type of this TaskContent.  # noqa: E501
        :rtype: str
        """
        return self._task_type

    @task_type.setter
    def task_type(self, task_type):
        """Sets the task_type of this TaskContent.


        :param task_type: The task_type of this TaskContent.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and task_type is None:
            raise ValueError("Invalid value for `task_type`, must not be `None`")  # noqa: E501

        self._task_type = task_type

    @property
    def input(self):
        """Gets the input of this TaskContent.  # noqa: E501


        :return: The input of this TaskContent.  # noqa: E501
        :rtype: str
        """
        return self._input

    @input.setter
    def input(self, input):
        """Sets the input of this TaskContent.


        :param input: The input of this TaskContent.  # noqa: E501
        :type: str
        """

        self._input = input

    @property
    def output(self):
        """Gets the output of this TaskContent.  # noqa: E501


        :return: The output of this TaskContent.  # noqa: E501
        :rtype: str
        """
        return self._output

    @output.setter
    def output(self, output):
        """Sets the output of this TaskContent.


        :param output: The output of this TaskContent.  # noqa: E501
        :type: str
        """

        self._output = output

    @property
    def commit_time(self):
        """Gets the commit_time of this TaskContent.  # noqa: E501


        :return: The commit_time of this TaskContent.  # noqa: E501
        :rtype: int
        """
        return self._commit_time

    @commit_time.setter
    def commit_time(self, commit_time):
        """Sets the commit_time of this TaskContent.


        :param commit_time: The commit_time of this TaskContent.  # noqa: E501
        :type: int
        """

        self._commit_time = commit_time

    @property
    def begin_time(self):
        """Gets the begin_time of this TaskContent.  # noqa: E501


        :return: The begin_time of this TaskContent.  # noqa: E501
        :rtype: int
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        """Sets the begin_time of this TaskContent.


        :param begin_time: The begin_time of this TaskContent.  # noqa: E501
        :type: int
        """

        self._begin_time = begin_time

    @property
    def end_time(self):
        """Gets the end_time of this TaskContent.  # noqa: E501


        :return: The end_time of this TaskContent.  # noqa: E501
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this TaskContent.


        :param end_time: The end_time of this TaskContent.  # noqa: E501
        :type: int
        """

        self._end_time = end_time

    @property
    def status(self):
        """Gets the status of this TaskContent.  # noqa: E501


        :return: The status of this TaskContent.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this TaskContent.


        :param status: The status of this TaskContent.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def worker_id(self):
        """Gets the worker_id of this TaskContent.  # noqa: E501


        :return: The worker_id of this TaskContent.  # noqa: E501
        :rtype: str
        """
        return self._worker_id

    @worker_id.setter
    def worker_id(self, worker_id):
        """Sets the worker_id of this TaskContent.


        :param worker_id: The worker_id of this TaskContent.  # noqa: E501
        :type: str
        """

        self._worker_id = worker_id

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
        if issubclass(TaskContent, dict):
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
        if not isinstance(other, TaskContent):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TaskContent):
            return True

        return self.to_dict() != other.to_dict()
