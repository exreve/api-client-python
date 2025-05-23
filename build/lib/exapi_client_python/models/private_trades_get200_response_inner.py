# coding: utf-8

"""
    ExKoin API Documentation

    API documentation for ExKoin Crypto exchange

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, StrictFloat, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, Optional, Union
from exapi_client_python.models.private_orders_get200_response_inner_fee import PrivateOrdersGet200ResponseInnerFee
from typing import Optional, Set
from typing_extensions import Self

class PrivateTradesGet200ResponseInner(BaseModel):
    """
    PrivateTradesGet200ResponseInner
    """ # noqa: E501
    id: StrictStr
    order_id: StrictStr
    client_order_id: Optional[StrictStr] = None
    symbol: StrictStr
    type: StrictStr
    side: StrictStr
    taker_or_maker: StrictStr
    price: StrictStr
    amount: StrictStr
    cost: StrictStr
    fee: PrivateOrdersGet200ResponseInnerFee
    created_at: Union[StrictFloat, StrictInt]
    __properties: ClassVar[List[str]] = ["id", "order_id", "client_order_id", "symbol", "type", "side", "taker_or_maker", "price", "amount", "cost", "fee", "created_at"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['market', 'limit']):
            raise ValueError("must be one of enum values ('market', 'limit')")
        return value

    @field_validator('side')
    def side_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['buy', 'sell']):
            raise ValueError("must be one of enum values ('buy', 'sell')")
        return value

    @field_validator('taker_or_maker')
    def taker_or_maker_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['taker', 'maker']):
            raise ValueError("must be one of enum values ('taker', 'maker')")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of PrivateTradesGet200ResponseInner from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of fee
        if self.fee:
            _dict['fee'] = self.fee.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PrivateTradesGet200ResponseInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "order_id": obj.get("order_id"),
            "client_order_id": obj.get("client_order_id"),
            "symbol": obj.get("symbol"),
            "type": obj.get("type"),
            "side": obj.get("side"),
            "taker_or_maker": obj.get("taker_or_maker"),
            "price": obj.get("price"),
            "amount": obj.get("amount"),
            "cost": obj.get("cost"),
            "fee": PrivateOrdersGet200ResponseInnerFee.from_dict(obj["fee"]) if obj.get("fee") is not None else None,
            "created_at": obj.get("created_at")
        })
        return _obj


