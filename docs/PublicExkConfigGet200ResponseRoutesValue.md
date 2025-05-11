# PublicExkConfigGet200ResponseRoutesValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**weight** | **float** |  | 
**description** | **str** |  | 
**free_amount** | **float** |  | 
**locked_amount** | **float** |  | 
**logs** | [**List[PublicExkConfigGet200ResponseRoutesValueLogsInner]**](PublicExkConfigGet200ResponseRoutesValueLogsInner.md) |  | 

## Example

```python
from exapi_client_python.models.public_exk_config_get200_response_routes_value import PublicExkConfigGet200ResponseRoutesValue

# TODO update the JSON string below
json = "{}"
# create an instance of PublicExkConfigGet200ResponseRoutesValue from a JSON string
public_exk_config_get200_response_routes_value_instance = PublicExkConfigGet200ResponseRoutesValue.from_json(json)
# print the JSON string representation of the object
print(PublicExkConfigGet200ResponseRoutesValue.to_json())

# convert the object into a dict
public_exk_config_get200_response_routes_value_dict = public_exk_config_get200_response_routes_value_instance.to_dict()
# create an instance of PublicExkConfigGet200ResponseRoutesValue from a dict
public_exk_config_get200_response_routes_value_from_dict = PublicExkConfigGet200ResponseRoutesValue.from_dict(public_exk_config_get200_response_routes_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


