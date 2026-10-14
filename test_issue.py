from fhirclient.models.contract import Contract

data = {
    "resourceType": "Contract",
    "subtype": "wrong"
}

contract = Contract(data)
print(contract)