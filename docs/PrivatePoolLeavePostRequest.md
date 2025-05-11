# PrivatePoolLeavePostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pool_id** | **str** |  | 
**token_amount** | **str** |  | 

## Example

```python
from exapi_client_python.models.private_pool_leave_post_request import PrivatePoolLeavePostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PrivatePoolLeavePostRequest from a JSON string
private_pool_leave_post_request_instance = PrivatePoolLeavePostRequest.from_json(json)
# print the JSON string representation of the object
print(PrivatePoolLeavePostRequest.to_json())

# convert the object into a dict
private_pool_leave_post_request_dict = private_pool_leave_post_request_instance.to_dict()
# create an instance of PrivatePoolLeavePostRequest from a dict
private_pool_leave_post_request_from_dict = PrivatePoolLeavePostRequest.from_dict(private_pool_leave_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


