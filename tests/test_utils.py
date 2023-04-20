from dataclasses import asdict, dataclass

from livekit import _utils  # noqa


def test_camel_case_dict():
    @dataclass
    class MyTest:
        hello_world: str

    my_test = MyTest("hello")
    d = asdict(my_test, dict_factory=_utils.camel_case_dict)
    assert d == {"helloWorld": "hello"}
