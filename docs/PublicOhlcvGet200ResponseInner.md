# PublicOhlcvGet200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time** | **float** |  | 
**open** | **str** |  | 
**high** | **str** |  | 
**low** | **str** |  | 
**close** | **str** |  | 
**volume** | **str** |  | 

## Example

```python
from exapi_client_python.models.public_ohlcv_get200_response_inner import PublicOhlcvGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of PublicOhlcvGet200ResponseInner from a JSON string
public_ohlcv_get200_response_inner_instance = PublicOhlcvGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(PublicOhlcvGet200ResponseInner.to_json())

# convert the object into a dict
public_ohlcv_get200_response_inner_dict = public_ohlcv_get200_response_inner_instance.to_dict()
# create an instance of PublicOhlcvGet200ResponseInner from a dict
public_ohlcv_get200_response_inner_from_dict = PublicOhlcvGet200ResponseInner.from_dict(public_ohlcv_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


