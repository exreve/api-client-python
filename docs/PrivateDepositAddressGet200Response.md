# PrivateDepositAddressGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **object** |  | [optional] 
**address** | **str** |  | 
**memo** | **str** |  | [optional] 
**min_deposit_amount** | **str** |  | 
**currency_details** | [**PublicCurrenciesGet200ResponseInner**](PublicCurrenciesGet200ResponseInner.md) |  | 
**network_details** | [**PublicNetworksGet200ResponseInner**](PublicNetworksGet200ResponseInner.md) |  | 

## Example

```python
from exapi_client_python.models.private_deposit_address_get200_response import PrivateDepositAddressGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PrivateDepositAddressGet200Response from a JSON string
private_deposit_address_get200_response_instance = PrivateDepositAddressGet200Response.from_json(json)
# print the JSON string representation of the object
print(PrivateDepositAddressGet200Response.to_json())

# convert the object into a dict
private_deposit_address_get200_response_dict = private_deposit_address_get200_response_instance.to_dict()
# create an instance of PrivateDepositAddressGet200Response from a dict
private_deposit_address_get200_response_from_dict = PrivateDepositAddressGet200Response.from_dict(private_deposit_address_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


