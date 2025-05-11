# PrivatePoolJoinPost200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**task_id** | **str** |  | 

## Example

```python
from exapi_client_python.models.private_pool_join_post200_response import PrivatePoolJoinPost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PrivatePoolJoinPost200Response from a JSON string
private_pool_join_post200_response_instance = PrivatePoolJoinPost200Response.from_json(json)
# print the JSON string representation of the object
print(PrivatePoolJoinPost200Response.to_json())

# convert the object into a dict
private_pool_join_post200_response_dict = private_pool_join_post200_response_instance.to_dict()
# create an instance of PrivatePoolJoinPost200Response from a dict
private_pool_join_post200_response_from_dict = PrivatePoolJoinPost200Response.from_dict(private_pool_join_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


