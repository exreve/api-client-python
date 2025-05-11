# PublicMarketsGet200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**base** | **str** |  | 
**quote** | **str** |  | 
**active** | **object** |  | [optional] 
**precision** | [**PublicMarketsGet200ResponseInnerPrecision**](PublicMarketsGet200ResponseInnerPrecision.md) |  | 
**limits** | [**PublicMarketsGet200ResponseInnerLimits**](PublicMarketsGet200ResponseInnerLimits.md) |  | 

## Example

```python
from exapi_client_python.models.public_markets_get200_response_inner import PublicMarketsGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of PublicMarketsGet200ResponseInner from a JSON string
public_markets_get200_response_inner_instance = PublicMarketsGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(PublicMarketsGet200ResponseInner.to_json())

# convert the object into a dict
public_markets_get200_response_inner_dict = public_markets_get200_response_inner_instance.to_dict()
# create an instance of PublicMarketsGet200ResponseInner from a dict
public_markets_get200_response_inner_from_dict = PublicMarketsGet200ResponseInner.from_dict(public_markets_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


