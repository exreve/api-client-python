# PublicGainsLossesTransparencyGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **float** |  | 
**currencies** | [**Dict[str, PublicGainsLossesTransparencyGet200ResponseCurrenciesValue]**](PublicGainsLossesTransparencyGet200ResponseCurrenciesValue.md) |  | 
**last_20** | [**List[PublicGainsLossesTransparencyGet200ResponseLast20Inner]**](PublicGainsLossesTransparencyGet200ResponseLast20Inner.md) |  | 

## Example

```python
from exapi_client_python.models.public_gains_losses_transparency_get200_response import PublicGainsLossesTransparencyGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PublicGainsLossesTransparencyGet200Response from a JSON string
public_gains_losses_transparency_get200_response_instance = PublicGainsLossesTransparencyGet200Response.from_json(json)
# print the JSON string representation of the object
print(PublicGainsLossesTransparencyGet200Response.to_json())

# convert the object into a dict
public_gains_losses_transparency_get200_response_dict = public_gains_losses_transparency_get200_response_instance.to_dict()
# create an instance of PublicGainsLossesTransparencyGet200Response from a dict
public_gains_losses_transparency_get200_response_from_dict = PublicGainsLossesTransparencyGet200Response.from_dict(public_gains_losses_transparency_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


