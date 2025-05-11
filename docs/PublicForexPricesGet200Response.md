# PublicForexPricesGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prices_usd** | **Dict[str, float]** |  | 
**symb_to_name** | **Dict[str, str]** |  | 

## Example

```python
from exapi_client_python.models.public_forex_prices_get200_response import PublicForexPricesGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PublicForexPricesGet200Response from a JSON string
public_forex_prices_get200_response_instance = PublicForexPricesGet200Response.from_json(json)
# print the JSON string representation of the object
print(PublicForexPricesGet200Response.to_json())

# convert the object into a dict
public_forex_prices_get200_response_dict = public_forex_prices_get200_response_instance.to_dict()
# create an instance of PublicForexPricesGet200Response from a dict
public_forex_prices_get200_response_from_dict = PublicForexPricesGet200Response.from_dict(public_forex_prices_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


