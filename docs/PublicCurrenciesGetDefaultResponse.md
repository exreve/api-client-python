# PublicCurrenciesGetDefaultResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**code** | **str** |  | 
**error** | **str** |  | 
**details** | **str** |  | [optional] 
**params** | **object** |  | [optional] 

## Example

```python
from exapi_client_python.models.public_currencies_get_default_response import PublicCurrenciesGetDefaultResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PublicCurrenciesGetDefaultResponse from a JSON string
public_currencies_get_default_response_instance = PublicCurrenciesGetDefaultResponse.from_json(json)
# print the JSON string representation of the object
print(PublicCurrenciesGetDefaultResponse.to_json())

# convert the object into a dict
public_currencies_get_default_response_dict = public_currencies_get_default_response_instance.to_dict()
# create an instance of PublicCurrenciesGetDefaultResponse from a dict
public_currencies_get_default_response_from_dict = PublicCurrenciesGetDefaultResponse.from_dict(public_currencies_get_default_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


