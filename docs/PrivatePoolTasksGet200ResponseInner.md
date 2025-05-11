# PrivatePoolTasksGet200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**pool_id** | **str** |  | 
**type** | **str** |  | 
**status** | **str** |  | 
**created_at** | **float** |  | 
**updated_at** | **float** |  | 
**spent** | [**List[PrivatePoolTasksGet200ResponseInnerSpentInner]**](PrivatePoolTasksGet200ResponseInnerSpentInner.md) |  | 
**got** | [**List[PrivatePoolTasksGet200ResponseInnerSpentInner]**](PrivatePoolTasksGet200ResponseInnerSpentInner.md) |  | 

## Example

```python
from exapi_client_python.models.private_pool_tasks_get200_response_inner import PrivatePoolTasksGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of PrivatePoolTasksGet200ResponseInner from a JSON string
private_pool_tasks_get200_response_inner_instance = PrivatePoolTasksGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(PrivatePoolTasksGet200ResponseInner.to_json())

# convert the object into a dict
private_pool_tasks_get200_response_inner_dict = private_pool_tasks_get200_response_inner_instance.to_dict()
# create an instance of PrivatePoolTasksGet200ResponseInner from a dict
private_pool_tasks_get200_response_inner_from_dict = PrivatePoolTasksGet200ResponseInner.from_dict(private_pool_tasks_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


