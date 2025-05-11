# PublicOrderbookGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bids** | **List[List[str]]** |  | 
**asks** | **List[List[str]]** |  | 
**timestamp** | **float** |  | 

## Example

```python
from exapi_client_python.models.public_orderbook_get200_response import PublicOrderbookGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PublicOrderbookGet200Response from a JSON string
public_orderbook_get200_response_instance = PublicOrderbookGet200Response.from_json(json)
# print the JSON string representation of the object
print(PublicOrderbookGet200Response.to_json())

# convert the object into a dict
public_orderbook_get200_response_dict = public_orderbook_get200_response_instance.to_dict()
# create an instance of PublicOrderbookGet200Response from a dict
public_orderbook_get200_response_from_dict = PublicOrderbookGet200Response.from_dict(public_orderbook_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


