import pytest

from agents.safe_xml import ParseError, fromstring


def test_parses_normal_rss_and_atom():
    root = fromstring(b"<rss><channel><item><title>x</title></item></channel></rss>")
    assert root.tag == "rss"
    assert fromstring("<feed><entry/></feed>").tag == "feed"


@pytest.mark.parametrize(
    "payload",
    [
        b'<?xml version="1.0"?><!DOCTYPE a [<!ENTITY x "y">]><a>&x;</a>',
        b'<!doctype a><a/>',
        '<!DOCTYPE a SYSTEM "http://evil/x.dtd"><a/>',
        '<!ENTITY lol "lol"><a/>',
        '<?xml version="1.0" encoding="utf-16"?><!DOCTYPE a><a/>'.encode("utf-16"),
    ],
)
def test_rejects_doctype_and_entities(payload):
    with pytest.raises(ParseError):
        fromstring(payload)


def test_malformed_xml_still_raises_parse_error():
    with pytest.raises(ParseError):
        fromstring(b"<a><b></a>")
