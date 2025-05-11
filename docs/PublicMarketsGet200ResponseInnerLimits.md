# PublicMarketsGet200ResponseInnerLimits


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**price** | [**PublicMarketsGet200ResponseInnerLimitsPrice**](PublicMarketsGet200ResponseInnerLimitsPrice.md) |  | 
**amount** | [**PublicMarketsGet200ResponseInnerLimitsPrice**](PublicMarketsGet200ResponseInnerLimitsPrice.md) |  | 
**cost** | [**PublicMarketsGet200ResponseInnerLimitsPrice**](PublicMarketsGet200ResponseInnerLimitsPrice.md) |  | 

## Example

```python
from exapi_client_python.models.public_markets_get200_response_inner_limits import PublicMarketsGet200ResponseInnerLimits

# TODO update the JSON string below
json = "{}"
# create an instance of PublicMarketsGet200ResponseInnerLimits from a JSON string
public_markets_get200_response_inner_limits_instance = PublicMarketsGet200ResponseInnerLimits.from_json(json)
# print the JSON string representation of the object
print(PublicMarketsGet200ResponseInnerLimits.to_json())

# convert the object into a dict
public_markets_get200_response_inner_limits_dict = public_markets_get200_response_inner_limits_instance.to_dict()
# create an instance of PublicMarketsGet200ResponseInnerLimits from a dict
public_markets_get200_response_inner_limits_from_dict = PublicMarketsGet200ResponseInnerLimits.from_dict(public_markets_get200_response_inner_limits_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


