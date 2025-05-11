# PrivateOrdersCancelPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **str** |  | 
**symbol** | **str** |  | 

## Example

```python
from exapi_client_python.models.private_orders_cancel_post_request import PrivateOrdersCancelPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PrivateOrdersCancelPostRequest from a JSON string
private_orders_cancel_post_request_instance = PrivateOrdersCancelPostRequest.from_json(json)
# print the JSON string representation of the object
print(PrivateOrdersCancelPostRequest.to_json())

# convert the object into a dict
private_orders_cancel_post_request_dict = private_orders_cancel_post_request_instance.to_dict()
# create an instance of PrivateOrdersCancelPostRequest from a dict
private_orders_cancel_post_request_from_dict = PrivateOrdersCancelPostRequest.from_dict(private_orders_cancel_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


