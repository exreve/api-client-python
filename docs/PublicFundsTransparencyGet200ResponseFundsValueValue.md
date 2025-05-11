# PublicFundsTransparencyGet200ResponseFundsValueValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **float** |  | 
**in_cold** | **float** |  | 
**free** | **float** |  | 
**locked** | **float** |  | 
**address_count** | **float** |  | 
**addresses** | **List[str]** |  | 

## Example

```python
from exapi_client_python.models.public_funds_transparency_get200_response_funds_value_value import PublicFundsTransparencyGet200ResponseFundsValueValue

# TODO update the JSON string below
json = "{}"
# create an instance of PublicFundsTransparencyGet200ResponseFundsValueValue from a JSON string
public_funds_transparency_get200_response_funds_value_value_instance = PublicFundsTransparencyGet200ResponseFundsValueValue.from_json(json)
# print the JSON string representation of the object
print(PublicFundsTransparencyGet200ResponseFundsValueValue.to_json())

# convert the object into a dict
public_funds_transparency_get200_response_funds_value_value_dict = public_funds_transparency_get200_response_funds_value_value_instance.to_dict()
# create an instance of PublicFundsTransparencyGet200ResponseFundsValueValue from a dict
public_funds_transparency_get200_response_funds_value_value_from_dict = PublicFundsTransparencyGet200ResponseFundsValueValue.from_dict(public_funds_transparency_get200_response_funds_value_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


