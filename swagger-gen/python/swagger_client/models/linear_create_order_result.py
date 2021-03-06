# coding: utf-8

"""
    Bybit API

    ## REST API for the Bybit Exchange. Base URI: [https://api.bybit.com]    # noqa: E501

    OpenAPI spec version: 0.2.6
    Contact: support@bybit.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class LinearCreateOrderResult(object):
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
        'created_time': 'str',
        'cum_exec_fee': 'float',
        'cum_exec_qty': 'float',
        'cum_exec_value': 'float',
        'last_exec_price': 'float',
        'order_id': 'str',
        'order_link_id': 'str',
        'order_status': 'str',
        'order_type': 'str',
        'price': 'float',
        'qty': 'float',
        'reduce_only': 'bool',
        'side': 'str',
        'symbol': 'str',
        'time_in_force': 'str',
        'updated_time': 'str',
        'user_id': 'int'
    }

    attribute_map = {
        'created_time': 'created_time',
        'cum_exec_fee': 'cum_exec_fee',
        'cum_exec_qty': 'cum_exec_qty',
        'cum_exec_value': 'cum_exec_value',
        'last_exec_price': 'last_exec_price',
        'order_id': 'order_id',
        'order_link_id': 'order_link_id',
        'order_status': 'order_status',
        'order_type': 'order_type',
        'price': 'price',
        'qty': 'qty',
        'reduce_only': 'reduce_only',
        'side': 'side',
        'symbol': 'symbol',
        'time_in_force': 'time_in_force',
        'updated_time': 'updated_time',
        'user_id': 'user_id'
    }

    def __init__(self, created_time=None, cum_exec_fee=None, cum_exec_qty=None, cum_exec_value=None, last_exec_price=None, order_id=None, order_link_id=None, order_status=None, order_type=None, price=None, qty=None, reduce_only=None, side=None, symbol=None, time_in_force=None, updated_time=None, user_id=None):  # noqa: E501
        """LinearCreateOrderResult - a model defined in Swagger"""  # noqa: E501

        self._created_time = None
        self._cum_exec_fee = None
        self._cum_exec_qty = None
        self._cum_exec_value = None
        self._last_exec_price = None
        self._order_id = None
        self._order_link_id = None
        self._order_status = None
        self._order_type = None
        self._price = None
        self._qty = None
        self._reduce_only = None
        self._side = None
        self._symbol = None
        self._time_in_force = None
        self._updated_time = None
        self._user_id = None
        self.discriminator = None

        if created_time is not None:
            self.created_time = created_time
        if cum_exec_fee is not None:
            self.cum_exec_fee = cum_exec_fee
        if cum_exec_qty is not None:
            self.cum_exec_qty = cum_exec_qty
        if cum_exec_value is not None:
            self.cum_exec_value = cum_exec_value
        if last_exec_price is not None:
            self.last_exec_price = last_exec_price
        if order_id is not None:
            self.order_id = order_id
        if order_link_id is not None:
            self.order_link_id = order_link_id
        if order_status is not None:
            self.order_status = order_status
        if order_type is not None:
            self.order_type = order_type
        if price is not None:
            self.price = price
        if qty is not None:
            self.qty = qty
        if reduce_only is not None:
            self.reduce_only = reduce_only
        if side is not None:
            self.side = side
        if symbol is not None:
            self.symbol = symbol
        if time_in_force is not None:
            self.time_in_force = time_in_force
        if updated_time is not None:
            self.updated_time = updated_time
        if user_id is not None:
            self.user_id = user_id

    @property
    def created_time(self):
        """Gets the created_time of this LinearCreateOrderResult.  # noqa: E501


        :return: The created_time of this LinearCreateOrderResult.  # noqa: E501
        :rtype: str
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this LinearCreateOrderResult.


        :param created_time: The created_time of this LinearCreateOrderResult.  # noqa: E501
        :type: str
        """

        self._created_time = created_time

    @property
    def cum_exec_fee(self):
        """Gets the cum_exec_fee of this LinearCreateOrderResult.  # noqa: E501


        :return: The cum_exec_fee of this LinearCreateOrderResult.  # noqa: E501
        :rtype: float
        """
        return self._cum_exec_fee

    @cum_exec_fee.setter
    def cum_exec_fee(self, cum_exec_fee):
        """Sets the cum_exec_fee of this LinearCreateOrderResult.


        :param cum_exec_fee: The cum_exec_fee of this LinearCreateOrderResult.  # noqa: E501
        :type: float
        """

        self._cum_exec_fee = cum_exec_fee

    @property
    def cum_exec_qty(self):
        """Gets the cum_exec_qty of this LinearCreateOrderResult.  # noqa: E501


        :return: The cum_exec_qty of this LinearCreateOrderResult.  # noqa: E501
        :rtype: float
        """
        return self._cum_exec_qty

    @cum_exec_qty.setter
    def cum_exec_qty(self, cum_exec_qty):
        """Sets the cum_exec_qty of this LinearCreateOrderResult.


        :param cum_exec_qty: The cum_exec_qty of this LinearCreateOrderResult.  # noqa: E501
        :type: float
        """

        self._cum_exec_qty = cum_exec_qty

    @property
    def cum_exec_value(self):
        """Gets the cum_exec_value of this LinearCreateOrderResult.  # noqa: E501


        :return: The cum_exec_value of this LinearCreateOrderResult.  # noqa: E501
        :rtype: float
        """
        return self._cum_exec_value

    @cum_exec_value.setter
    def cum_exec_value(self, cum_exec_value):
        """Sets the cum_exec_value of this LinearCreateOrderResult.


        :param cum_exec_value: The cum_exec_value of this LinearCreateOrderResult.  # noqa: E501
        :type: float
        """

        self._cum_exec_value = cum_exec_value

    @property
    def last_exec_price(self):
        """Gets the last_exec_price of this LinearCreateOrderResult.  # noqa: E501


        :return: The last_exec_price of this LinearCreateOrderResult.  # noqa: E501
        :rtype: float
        """
        return self._last_exec_price

    @last_exec_price.setter
    def last_exec_price(self, last_exec_price):
        """Sets the last_exec_price of this LinearCreateOrderResult.


        :param last_exec_price: The last_exec_price of this LinearCreateOrderResult.  # noqa: E501
        :type: float
        """

        self._last_exec_price = last_exec_price

    @property
    def order_id(self):
        """Gets the order_id of this LinearCreateOrderResult.  # noqa: E501


        :return: The order_id of this LinearCreateOrderResult.  # noqa: E501
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this LinearCreateOrderResult.


        :param order_id: The order_id of this LinearCreateOrderResult.  # noqa: E501
        :type: str
        """

        self._order_id = order_id

    @property
    def order_link_id(self):
        """Gets the order_link_id of this LinearCreateOrderResult.  # noqa: E501


        :return: The order_link_id of this LinearCreateOrderResult.  # noqa: E501
        :rtype: str
        """
        return self._order_link_id

    @order_link_id.setter
    def order_link_id(self, order_link_id):
        """Sets the order_link_id of this LinearCreateOrderResult.


        :param order_link_id: The order_link_id of this LinearCreateOrderResult.  # noqa: E501
        :type: str
        """

        self._order_link_id = order_link_id

    @property
    def order_status(self):
        """Gets the order_status of this LinearCreateOrderResult.  # noqa: E501


        :return: The order_status of this LinearCreateOrderResult.  # noqa: E501
        :rtype: str
        """
        return self._order_status

    @order_status.setter
    def order_status(self, order_status):
        """Sets the order_status of this LinearCreateOrderResult.


        :param order_status: The order_status of this LinearCreateOrderResult.  # noqa: E501
        :type: str
        """

        self._order_status = order_status

    @property
    def order_type(self):
        """Gets the order_type of this LinearCreateOrderResult.  # noqa: E501


        :return: The order_type of this LinearCreateOrderResult.  # noqa: E501
        :rtype: str
        """
        return self._order_type

    @order_type.setter
    def order_type(self, order_type):
        """Sets the order_type of this LinearCreateOrderResult.


        :param order_type: The order_type of this LinearCreateOrderResult.  # noqa: E501
        :type: str
        """

        self._order_type = order_type

    @property
    def price(self):
        """Gets the price of this LinearCreateOrderResult.  # noqa: E501


        :return: The price of this LinearCreateOrderResult.  # noqa: E501
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this LinearCreateOrderResult.


        :param price: The price of this LinearCreateOrderResult.  # noqa: E501
        :type: float
        """

        self._price = price

    @property
    def qty(self):
        """Gets the qty of this LinearCreateOrderResult.  # noqa: E501


        :return: The qty of this LinearCreateOrderResult.  # noqa: E501
        :rtype: float
        """
        return self._qty

    @qty.setter
    def qty(self, qty):
        """Sets the qty of this LinearCreateOrderResult.


        :param qty: The qty of this LinearCreateOrderResult.  # noqa: E501
        :type: float
        """

        self._qty = qty

    @property
    def reduce_only(self):
        """Gets the reduce_only of this LinearCreateOrderResult.  # noqa: E501


        :return: The reduce_only of this LinearCreateOrderResult.  # noqa: E501
        :rtype: bool
        """
        return self._reduce_only

    @reduce_only.setter
    def reduce_only(self, reduce_only):
        """Sets the reduce_only of this LinearCreateOrderResult.


        :param reduce_only: The reduce_only of this LinearCreateOrderResult.  # noqa: E501
        :type: bool
        """

        self._reduce_only = reduce_only

    @property
    def side(self):
        """Gets the side of this LinearCreateOrderResult.  # noqa: E501


        :return: The side of this LinearCreateOrderResult.  # noqa: E501
        :rtype: str
        """
        return self._side

    @side.setter
    def side(self, side):
        """Sets the side of this LinearCreateOrderResult.


        :param side: The side of this LinearCreateOrderResult.  # noqa: E501
        :type: str
        """

        self._side = side

    @property
    def symbol(self):
        """Gets the symbol of this LinearCreateOrderResult.  # noqa: E501


        :return: The symbol of this LinearCreateOrderResult.  # noqa: E501
        :rtype: str
        """
        return self._symbol

    @symbol.setter
    def symbol(self, symbol):
        """Sets the symbol of this LinearCreateOrderResult.


        :param symbol: The symbol of this LinearCreateOrderResult.  # noqa: E501
        :type: str
        """

        self._symbol = symbol

    @property
    def time_in_force(self):
        """Gets the time_in_force of this LinearCreateOrderResult.  # noqa: E501


        :return: The time_in_force of this LinearCreateOrderResult.  # noqa: E501
        :rtype: str
        """
        return self._time_in_force

    @time_in_force.setter
    def time_in_force(self, time_in_force):
        """Sets the time_in_force of this LinearCreateOrderResult.


        :param time_in_force: The time_in_force of this LinearCreateOrderResult.  # noqa: E501
        :type: str
        """

        self._time_in_force = time_in_force

    @property
    def updated_time(self):
        """Gets the updated_time of this LinearCreateOrderResult.  # noqa: E501


        :return: The updated_time of this LinearCreateOrderResult.  # noqa: E501
        :rtype: str
        """
        return self._updated_time

    @updated_time.setter
    def updated_time(self, updated_time):
        """Sets the updated_time of this LinearCreateOrderResult.


        :param updated_time: The updated_time of this LinearCreateOrderResult.  # noqa: E501
        :type: str
        """

        self._updated_time = updated_time

    @property
    def user_id(self):
        """Gets the user_id of this LinearCreateOrderResult.  # noqa: E501


        :return: The user_id of this LinearCreateOrderResult.  # noqa: E501
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this LinearCreateOrderResult.


        :param user_id: The user_id of this LinearCreateOrderResult.  # noqa: E501
        :type: int
        """

        self._user_id = user_id

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
        if issubclass(LinearCreateOrderResult, dict):
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
        if not isinstance(other, LinearCreateOrderResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
