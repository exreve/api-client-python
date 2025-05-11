# PublicFundsTransparencyGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **float** |  | 
**funds** | **Dict[str, Dict[str, PublicFundsTransparencyGet200ResponseFundsValueValue]]** |  | 
**stats** | [**Dict[str, PublicFundsTransparencyGet200ResponseStatsValue]**](PublicFundsTransparencyGet200ResponseStatsValue.md) |  | 
**addresses_labels** | **Dict[str, str]** |  | 

## Example

```python
from exapi_client_python.models.public_funds_transparency_get200_response import PublicFundsTransparencyGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PublicFundsTransparencyGet200Response from a JSON string
public_funds_transparency_get200_response_instance = PublicFundsTransparencyGet200Response.from_json(json)
# print the JSON string representation of the object
print(PublicFundsTransparencyGet200Response.to_json())

# convert the object into a dict
public_funds_transparency_get200_response_dict = public_funds_transparency_get200_response_instance.to_dict()
# create an instance of PublicFundsTransparencyGet200Response from a dict
public_funds_transparency_get200_response_from_dict = PublicFundsTransparencyGet200Response.from_dict(public_funds_transparency_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


