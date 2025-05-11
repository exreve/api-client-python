# PrivateWithdrawalsFinishPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payload** | **str** |  | 

## Example

```python
from exapi_client_python.models.private_withdrawals_finish_post_request import PrivateWithdrawalsFinishPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PrivateWithdrawalsFinishPostRequest from a JSON string
private_withdrawals_finish_post_request_instance = PrivateWithdrawalsFinishPostRequest.from_json(json)
# print the JSON string representation of the object
print(PrivateWithdrawalsFinishPostRequest.to_json())

# convert the object into a dict
private_withdrawals_finish_post_request_dict = private_withdrawals_finish_post_request_instance.to_dict()
# create an instance of PrivateWithdrawalsFinishPostRequest from a dict
private_withdrawals_finish_post_request_from_dict = PrivateWithdrawalsFinishPostRequest.from_dict(private_withdrawals_finish_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


