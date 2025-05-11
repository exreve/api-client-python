# PrivateWithdrawalsPreparePost200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | [**PublicCurrenciesGet200ResponseInner**](PublicCurrenciesGet200ResponseInner.md) |  | 
**amount_you_receive** | **str** |  | 
**fee** | **str** |  | 
**amount_you_pay** | **str** |  | 
**address** | **str** |  | 
**network** | [**PublicNetworksGet200ResponseInner**](PublicNetworksGet200ResponseInner.md) |  | 
**memo** | **str** |  | [optional] 
**payload** | **str** |  | 
**expire_in_ms** | **float** |  | 

## Example

```python
from exapi_client_python.models.private_withdrawals_prepare_post200_response import PrivateWithdrawalsPreparePost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PrivateWithdrawalsPreparePost200Response from a JSON string
private_withdrawals_prepare_post200_response_instance = PrivateWithdrawalsPreparePost200Response.from_json(json)
# print the JSON string representation of the object
print(PrivateWithdrawalsPreparePost200Response.to_json())

# convert the object into a dict
private_withdrawals_prepare_post200_response_dict = private_withdrawals_prepare_post200_response_instance.to_dict()
# create an instance of PrivateWithdrawalsPreparePost200Response from a dict
private_withdrawals_prepare_post200_response_from_dict = PrivateWithdrawalsPreparePost200Response.from_dict(private_withdrawals_prepare_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


