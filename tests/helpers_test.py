from fluid.helpers import make_payload


def test_make_payload_with_valid_values():
    result = make_payload("test", {"argument": "value"})

    assert result == {
        "id": 0,
        "jsonrpc": "2.0",
        "method": "test",
        "params": {"argument": "value"},
    }


def test_make_payload_skipping_null_values():
    result = make_payload("test", {"argument": None})

    assert result == {
        "id": 0,
        "jsonrpc": "2.0",
        "method": "test",
        "params": {},
    }
