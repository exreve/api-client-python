# PublicGainsLossesTransparencyGet200ResponseCurrenciesValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **str** |  | 
**trades** | **str** |  | 
**exk_program** | **str** |  | 
**withdrawals** | **str** |  | 
**transfers** | **str** |  | 
**admin_withdrawals** | **str** |  | 
**admin_deposits** | **str** |  | 

## Example

```python
from exapi_client_python.models.public_gains_losses_transparency_get200_response_currencies_value import PublicGainsLossesTransparencyGet200ResponseCurrenciesValue

# TODO update the JSON string below
json = "{}"
# create an instance of PublicGainsLossesTransparencyGet200ResponseCurrenciesValue from a JSON string
public_gains_losses_transparency_get200_response_currencies_value_instance = PublicGainsLossesTransparencyGet200ResponseCurrenciesValue.from_json(json)
# print the JSON string representation of the object
print(PublicGainsLossesTransparencyGet200ResponseCurrenciesValue.to_json())

# convert the object into a dict
public_gains_losses_transparency_get200_response_currencies_value_dict = public_gains_losses_transparency_get200_response_currencies_value_instance.to_dict()
# create an instance of PublicGainsLossesTransparencyGet200ResponseCurrenciesValue from a dict
public_gains_losses_transparency_get200_response_currencies_value_from_dict = PublicGainsLossesTransparencyGet200ResponseCurrenciesValue.from_dict(public_gains_losses_transparency_get200_response_currencies_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


