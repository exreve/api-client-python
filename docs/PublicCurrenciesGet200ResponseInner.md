# PublicCurrenciesGet200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**precision** | **float** |  | 
**deposit_enabled** | **object** |  | [optional] 
**withdrawal_enabled** | **object** |  | [optional] 
**value_usd** | **str** |  | 
**logo_url** | **str** |  | 
**networks** | [**List[PublicCurrenciesGet200ResponseInnerNetworksInner]**](PublicCurrenciesGet200ResponseInnerNetworksInner.md) |  | 
**lp_token_of** | **str** |  | [optional] 

## Example

```python
from exapi_client_python.models.public_currencies_get200_response_inner import PublicCurrenciesGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of PublicCurrenciesGet200ResponseInner from a JSON string
public_currencies_get200_response_inner_instance = PublicCurrenciesGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(PublicCurrenciesGet200ResponseInner.to_json())

# convert the object into a dict
public_currencies_get200_response_inner_dict = public_currencies_get200_response_inner_instance.to_dict()
# create an instance of PublicCurrenciesGet200ResponseInner from a dict
public_currencies_get200_response_inner_from_dict = PublicCurrenciesGet200ResponseInner.from_dict(public_currencies_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


