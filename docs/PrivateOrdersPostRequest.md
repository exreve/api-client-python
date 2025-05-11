# PrivateOrdersPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**symbol** | **str** |  | 
**type** | **str** |  | 
**side** | **str** |  | 
**quantity** | **str** |  | [optional] 
**cost** | **str** |  | [optional] 
**price** | **str** |  | [optional] 
**client_order_id** | **str** |  | [optional] 

## Example

```python
from exapi_client_python.models.private_orders_post_request import PrivateOrdersPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PrivateOrdersPostRequest from a JSON string
private_orders_post_request_instance = PrivateOrdersPostRequest.from_json(json)
# print the JSON string representation of the object
print(PrivateOrdersPostRequest.to_json())

# convert the object into a dict
private_orders_post_request_dict = private_orders_post_request_instance.to_dict()
# create an instance of PrivateOrdersPostRequest from a dict
private_orders_post_request_from_dict = PrivateOrdersPostRequest.from_dict(private_orders_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


