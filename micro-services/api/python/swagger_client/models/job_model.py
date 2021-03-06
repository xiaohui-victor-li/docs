# coding: utf-8

"""
    QES Quant Service API

    QES Quant Service API provides easy access to Risk/Optimization API   # noqa: E501

    OpenAPI spec version: 0.0.4
    Contact: luo.qes@wolferesearch.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class JobModel(object):
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
        'typeid': 'str',
        'user_': 'str',
        'uuid': 'str',
        'starttime': 'str',
        'status': 'str',
        'endtime': 'str',
        'message': 'str'
    }

    attribute_map = {
        'typeid': 'TYPEID',
        'user_': 'USER_',
        'uuid': 'UUID',
        'starttime': 'STARTTIME',
        'status': 'STATUS',
        'endtime': 'ENDTIME',
        'message': 'MESSAGE'
    }

    def __init__(self, typeid=None, user_=None, uuid=None, starttime=None, status=None, endtime=None, message=None):  # noqa: E501
        """JobModel - a model defined in Swagger"""  # noqa: E501

        self._typeid = None
        self._user_ = None
        self._uuid = None
        self._starttime = None
        self._status = None
        self._endtime = None
        self._message = None
        self.discriminator = None

        if typeid is not None:
            self.typeid = typeid
        if user_ is not None:
            self.user_ = user_
        if uuid is not None:
            self.uuid = uuid
        if starttime is not None:
            self.starttime = starttime
        if status is not None:
            self.status = status
        if endtime is not None:
            self.endtime = endtime
        if message is not None:
            self.message = message

    @property
    def typeid(self):
        """Gets the typeid of this JobModel.  # noqa: E501

        Unique id of the risk model  # noqa: E501

        :return: The typeid of this JobModel.  # noqa: E501
        :rtype: str
        """
        return self._typeid

    @typeid.setter
    def typeid(self, typeid):
        """Sets the typeid of this JobModel.

        Unique id of the risk model  # noqa: E501

        :param typeid: The typeid of this JobModel.  # noqa: E501
        :type: str
        """

        self._typeid = typeid

    @property
    def user_(self):
        """Gets the user_ of this JobModel.  # noqa: E501

        Template used for risk model  # noqa: E501

        :return: The user_ of this JobModel.  # noqa: E501
        :rtype: str
        """
        return self._user_

    @user_.setter
    def user_(self, user_):
        """Sets the user_ of this JobModel.

        Template used for risk model  # noqa: E501

        :param user_: The user_ of this JobModel.  # noqa: E501
        :type: str
        """

        self._user_ = user_

    @property
    def uuid(self):
        """Gets the uuid of this JobModel.  # noqa: E501

        Date on which riks model was created  # noqa: E501

        :return: The uuid of this JobModel.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this JobModel.

        Date on which riks model was created  # noqa: E501

        :param uuid: The uuid of this JobModel.  # noqa: E501
        :type: str
        """

        self._uuid = uuid

    @property
    def starttime(self):
        """Gets the starttime of this JobModel.  # noqa: E501

        Date on which riks model was created  # noqa: E501

        :return: The starttime of this JobModel.  # noqa: E501
        :rtype: str
        """
        return self._starttime

    @starttime.setter
    def starttime(self, starttime):
        """Sets the starttime of this JobModel.

        Date on which riks model was created  # noqa: E501

        :param starttime: The starttime of this JobModel.  # noqa: E501
        :type: str
        """

        self._starttime = starttime

    @property
    def status(self):
        """Gets the status of this JobModel.  # noqa: E501

        Date on which riks model was created  # noqa: E501

        :return: The status of this JobModel.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this JobModel.

        Date on which riks model was created  # noqa: E501

        :param status: The status of this JobModel.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def endtime(self):
        """Gets the endtime of this JobModel.  # noqa: E501

        Date on which riks model was created  # noqa: E501

        :return: The endtime of this JobModel.  # noqa: E501
        :rtype: str
        """
        return self._endtime

    @endtime.setter
    def endtime(self, endtime):
        """Sets the endtime of this JobModel.

        Date on which riks model was created  # noqa: E501

        :param endtime: The endtime of this JobModel.  # noqa: E501
        :type: str
        """

        self._endtime = endtime

    @property
    def message(self):
        """Gets the message of this JobModel.  # noqa: E501

        Date on which riks model was created  # noqa: E501

        :return: The message of this JobModel.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this JobModel.

        Date on which riks model was created  # noqa: E501

        :param message: The message of this JobModel.  # noqa: E501
        :type: str
        """

        self._message = message

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
        if issubclass(JobModel, dict):
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
        if not isinstance(other, JobModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
