# PublicExkConfigGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**circulating_supply** | **float** |  | 
**last_reserve_value_usd** | **float** |  | 
**mint_rate** | **float** |  | 
**lp_share_percent_to_exk** | **float** |  | 
**routes** | [**Dict[str, PublicExkConfigGet200ResponseRoutesValue]**](PublicExkConfigGet200ResponseRoutesValue.md) |  | 
**user_levels** | [**List[PublicExkConfigGet200ResponseUserLevelsInner]**](PublicExkConfigGet200ResponseUserLevelsInner.md) |  | 
**weekly_dist** | [**PublicExkConfigGet200ResponseWeeklyDist**](PublicExkConfigGet200ResponseWeeklyDist.md) |  | 

## Example

```python
from exapi_client_python.models.public_exk_config_get200_response import PublicExkConfigGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PublicExkConfigGet200Response from a JSON string
public_exk_config_get200_response_instance = PublicExkConfigGet200Response.from_json(json)
# print the JSON string representation of the object
print(PublicExkConfigGet200Response.to_json())

# convert the object into a dict
public_exk_config_get200_response_dict = public_exk_config_get200_response_instance.to_dict()
# create an instance of PublicExkConfigGet200Response from a dict
public_exk_config_get200_response_from_dict = PublicExkConfigGet200Response.from_dict(public_exk_config_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


