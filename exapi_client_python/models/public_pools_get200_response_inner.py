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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, Optional
from exapi_client_python.models.public_pools_get200_response_inner_earned24h import PublicPoolsGet200ResponseInnerEarned24h
from typing import Optional, Set
from typing_extensions import Self

class PublicPoolsGet200ResponseInner(BaseModel):
    """
    PublicPoolsGet200ResponseInner
    """ # noqa: E501
    id: StrictStr
    active: Optional[Any] = None
    base_currency: StrictStr
    quote_currency: StrictStr
    base_reserve: StrictStr
    quote_reserve: StrictStr
    token_id: StrictStr
    token_supply: StrictStr
    earned_24h: PublicPoolsGet200ResponseInnerEarned24h
    apy_estimated_on_fees_24h: StrictStr = Field(alias="APY_estimated_on_fees_24h")
    __properties: ClassVar[List[str]] = ["id", "active", "base_currency", "quote_currency", "base_reserve", "quote_reserve", "token_id", "token_supply", "earned_24h", "APY_estimated_on_fees_24h"]

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
        """Create an instance of PublicPoolsGet200ResponseInner from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of earned_24h
        if self.earned_24h:
            _dict['earned_24h'] = self.earned_24h.to_dict()
        # set to None if active (nullable) is None
        # and model_fields_set contains the field
        if self.active is None and "active" in self.model_fields_set:
            _dict['active'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PublicPoolsGet200ResponseInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "active": obj.get("active"),
            "base_currency": obj.get("base_currency"),
            "quote_currency": obj.get("quote_currency"),
            "base_reserve": obj.get("base_reserve"),
            "quote_reserve": obj.get("quote_reserve"),
            "token_id": obj.get("token_id"),
            "token_supply": obj.get("token_supply"),
            "earned_24h": PublicPoolsGet200ResponseInnerEarned24h.from_dict(obj["earned_24h"]) if obj.get("earned_24h") is not None else None,
            "APY_estimated_on_fees_24h": obj.get("APY_estimated_on_fees_24h")
        })
        return _obj


