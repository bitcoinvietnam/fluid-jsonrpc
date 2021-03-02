from unittest.mock import MagicMock

from fluid.network import JSONRPC


def test_dispatch_method_with_parameters():
    url = "http://example.com/json-rpc"
    dispatcher = JSONRPC(url=url)

    data = {"result": {"key": "value"}}
    mock = MagicMock()
    mock.configure_mock(**{"post.return_value": mock, "json.return_value": data})

    dispatcher.session = mock

    @dispatcher.dispatch()
    def func(string: str, number: int):
        pass

    result = func(string="test", number=0)

    assert result is data["result"]

    mock.post.assert_called_with(
        url,
        json={
            "id": 0,
            "jsonrpc": "2.0",
            "method": "func",
            "params": {
                "string": "test",
                "number": 0,
            },
        },
    )
