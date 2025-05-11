# PublicTradesGet200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**side** | **str** |  | 
**price** | **str** |  | 
**amount** | **str** |  | 
**cost** | **str** |  | 
**created_at** | **float** |  | 

## Example

```python
from exapi_client_python.models.public_trades_get200_response_inner import PublicTradesGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of PublicTradesGet200ResponseInner from a JSON string
public_trades_get200_response_inner_instance = PublicTradesGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(PublicTradesGet200ResponseInner.to_json())

# convert the object into a dict
public_trades_get200_response_inner_dict = public_trades_get200_response_inner_instance.to_dict()
# create an instance of PublicTradesGet200ResponseInner from a dict
public_trades_get200_response_inner_from_dict = PublicTradesGet200ResponseInner.from_dict(public_trades_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


