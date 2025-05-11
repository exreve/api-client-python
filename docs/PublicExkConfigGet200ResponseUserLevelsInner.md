# PublicExkConfigGet200ResponseUserLevelsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**points_factor** | **float** |  | 
**name** | **str** |  | 
**description** | **str** |  | 
**icon** | **str** |  | 
**required_points** | **float** |  | 
**benefits** | **List[str]** |  | 

## Example

```python
from exapi_client_python.models.public_exk_config_get200_response_user_levels_inner import PublicExkConfigGet200ResponseUserLevelsInner

# TODO update the JSON string below
json = "{}"
# create an instance of PublicExkConfigGet200ResponseUserLevelsInner from a JSON string
public_exk_config_get200_response_user_levels_inner_instance = PublicExkConfigGet200ResponseUserLevelsInner.from_json(json)
# print the JSON string representation of the object
print(PublicExkConfigGet200ResponseUserLevelsInner.to_json())

# convert the object into a dict
public_exk_config_get200_response_user_levels_inner_dict = public_exk_config_get200_response_user_levels_inner_instance.to_dict()
# create an instance of PublicExkConfigGet200ResponseUserLevelsInner from a dict
public_exk_config_get200_response_user_levels_inner_from_dict = PublicExkConfigGet200ResponseUserLevelsInner.from_dict(public_exk_config_get200_response_user_levels_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


