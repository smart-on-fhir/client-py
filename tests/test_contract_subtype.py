def test_subtype_alias():
    from fhirclient.models.contract import Contract

    data = {
        "resourceType": "Contract",
        "subtype": "example"
    }

    contract = Contract(data)
    assert contract is not None