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

from pydantic import BaseModel, ConfigDict, StrictFloat, StrictInt
from typing import Any, ClassVar, Dict, List, Union
from exapi_client_python.models.public_gains_losses_transparency_get200_response_currencies_value import PublicGainsLossesTransparencyGet200ResponseCurrenciesValue
from exapi_client_python.models.public_gains_losses_transparency_get200_response_last20_inner import PublicGainsLossesTransparencyGet200ResponseLast20Inner
from typing import Optional, Set
from typing_extensions import Self

class PublicGainsLossesTransparencyGet200Response(BaseModel):
    """
    PublicGainsLossesTransparencyGet200Response
    """ # noqa: E501
    timestamp: Union[StrictFloat, StrictInt]
    currencies: Dict[str, PublicGainsLossesTransparencyGet200ResponseCurrenciesValue]
    last_20: List[PublicGainsLossesTransparencyGet200ResponseLast20Inner]
    __properties: ClassVar[List[str]] = ["timestamp", "currencies", "last_20"]

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
        """Create an instance of PublicGainsLossesTransparencyGet200Response from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each value in currencies (dict)
        _field_dict = {}
        if self.currencies:
            for _key_currencies in self.currencies:
                if self.currencies[_key_currencies]:
                    _field_dict[_key_currencies] = self.currencies[_key_currencies].to_dict()
            _dict['currencies'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of each item in last_20 (list)
        _items = []
        if self.last_20:
            for _item_last_20 in self.last_20:
                if _item_last_20:
                    _items.append(_item_last_20.to_dict())
            _dict['last_20'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PublicGainsLossesTransparencyGet200Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "timestamp": obj.get("timestamp"),
            "currencies": dict(
                (_k, PublicGainsLossesTransparencyGet200ResponseCurrenciesValue.from_dict(_v))
                for _k, _v in obj["currencies"].items()
            )
            if obj.get("currencies") is not None
            else None,
            "last_20": [PublicGainsLossesTransparencyGet200ResponseLast20Inner.from_dict(_item) for _item in obj["last_20"]] if obj.get("last_20") is not None else None
        })
        return _obj


