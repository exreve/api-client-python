# PublicExkConfigGet200ResponseWeeklyDist


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cycle_id** | **float** |  | 
**timestamp_to_next_dist** | **float** |  | 
**total_points** | **float** |  | 
**points_for** | **Dict[str, float]** |  | 

## Example

```python
from exapi_client_python.models.public_exk_config_get200_response_weekly_dist import PublicExkConfigGet200ResponseWeeklyDist

# TODO update the JSON string below
json = "{}"
# create an instance of PublicExkConfigGet200ResponseWeeklyDist from a JSON string
public_exk_config_get200_response_weekly_dist_instance = PublicExkConfigGet200ResponseWeeklyDist.from_json(json)
# print the JSON string representation of the object
print(PublicExkConfigGet200ResponseWeeklyDist.to_json())

# convert the object into a dict
public_exk_config_get200_response_weekly_dist_dict = public_exk_config_get200_response_weekly_dist_instance.to_dict()
# create an instance of PublicExkConfigGet200ResponseWeeklyDist from a dict
public_exk_config_get200_response_weekly_dist_from_dict = PublicExkConfigGet200ResponseWeeklyDist.from_dict(public_exk_config_get200_response_weekly_dist_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


