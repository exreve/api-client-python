# PrivateWithdrawalsFinishPost200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**currency** | **str** |  | 
**amount** | **str** |  | 
**user_fee** | **str** |  | 
**message** | **str** |  | 
**address** | **str** |  | 
**from_address** | **str** |  | 
**network** | **str** |  | 
**memo** | **str** |  | [optional] 
**txid** | **str** |  | [optional] 
**status** | **str** |  | 
**timestamp** | **float** |  | 

## Example

```python
from exapi_client_python.models.private_withdrawals_finish_post200_response import PrivateWithdrawalsFinishPost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PrivateWithdrawalsFinishPost200Response from a JSON string
private_withdrawals_finish_post200_response_instance = PrivateWithdrawalsFinishPost200Response.from_json(json)
# print the JSON string representation of the object
print(PrivateWithdrawalsFinishPost200Response.to_json())

# convert the object into a dict
private_withdrawals_finish_post200_response_dict = private_withdrawals_finish_post200_response_instance.to_dict()
# create an instance of PrivateWithdrawalsFinishPost200Response from a dict
private_withdrawals_finish_post200_response_from_dict = PrivateWithdrawalsFinishPost200Response.from_dict(private_withdrawals_finish_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


