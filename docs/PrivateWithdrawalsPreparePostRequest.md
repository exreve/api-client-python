# PrivateWithdrawalsPreparePostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **str** |  | 
**amount** | **str** |  | 
**address** | **str** |  | 
**network** | **str** |  | 
**memo** | **str** |  | [optional] 

## Example

```python
from exapi_client_python.models.private_withdrawals_prepare_post_request import PrivateWithdrawalsPreparePostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PrivateWithdrawalsPreparePostRequest from a JSON string
private_withdrawals_prepare_post_request_instance = PrivateWithdrawalsPreparePostRequest.from_json(json)
# print the JSON string representation of the object
print(PrivateWithdrawalsPreparePostRequest.to_json())

# convert the object into a dict
private_withdrawals_prepare_post_request_dict = private_withdrawals_prepare_post_request_instance.to_dict()
# create an instance of PrivateWithdrawalsPreparePostRequest from a dict
private_withdrawals_prepare_post_request_from_dict = PrivateWithdrawalsPreparePostRequest.from_dict(private_withdrawals_prepare_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


