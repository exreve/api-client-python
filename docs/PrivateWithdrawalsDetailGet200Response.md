# PrivateWithdrawalsDetailGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | [**PublicCurrenciesGet200ResponseInner**](PublicCurrenciesGet200ResponseInner.md) |  | 
**network** | [**PublicNetworksGet200ResponseInner**](PublicNetworksGet200ResponseInner.md) |  | 
**balance** | **str** |  | 
**fee_usd** | **str** |  | 
**fee_in_currency** | **str** |  | 
**max_withdraw_exchange** | **str** |  | 
**available_hot** | **Dict[str, str]** |  | 
**available_hot_and_cold** | **Dict[str, str]** |  | 
**address_regex** | **str** |  | 
**min_withdraw_amount** | **str** |  | 
**is_memo_required** | **object** |  | [optional] 

## Example

```python
from exapi_client_python.models.private_withdrawals_detail_get200_response import PrivateWithdrawalsDetailGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PrivateWithdrawalsDetailGet200Response from a JSON string
private_withdrawals_detail_get200_response_instance = PrivateWithdrawalsDetailGet200Response.from_json(json)
# print the JSON string representation of the object
print(PrivateWithdrawalsDetailGet200Response.to_json())

# convert the object into a dict
private_withdrawals_detail_get200_response_dict = private_withdrawals_detail_get200_response_instance.to_dict()
# create an instance of PrivateWithdrawalsDetailGet200Response from a dict
private_withdrawals_detail_get200_response_from_dict = PrivateWithdrawalsDetailGet200Response.from_dict(private_withdrawals_detail_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


