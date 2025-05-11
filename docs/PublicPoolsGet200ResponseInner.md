# PublicPoolsGet200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**active** | **object** |  | [optional] 
**base_currency** | **str** |  | 
**quote_currency** | **str** |  | 
**base_reserve** | **str** |  | 
**quote_reserve** | **str** |  | 
**token_id** | **str** |  | 
**token_supply** | **str** |  | 
**earned_24h** | [**PublicPoolsGet200ResponseInnerEarned24h**](PublicPoolsGet200ResponseInnerEarned24h.md) |  | 
**apy_estimated_on_fees_24h** | **str** |  | 

## Example

```python
from exapi_client_python.models.public_pools_get200_response_inner import PublicPoolsGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of PublicPoolsGet200ResponseInner from a JSON string
public_pools_get200_response_inner_instance = PublicPoolsGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(PublicPoolsGet200ResponseInner.to_json())

# convert the object into a dict
public_pools_get200_response_inner_dict = public_pools_get200_response_inner_instance.to_dict()
# create an instance of PublicPoolsGet200ResponseInner from a dict
public_pools_get200_response_inner_from_dict = PublicPoolsGet200ResponseInner.from_dict(public_pools_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


