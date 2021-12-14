import jwt
import pytest

from livekit import AccessToken, VideoGrant


def test_access_token():
    with pytest.raises(ValueError):
        grant = VideoGrant(room_join=True)
        _ = AccessToken("key", "secret", grant=grant, identity=None)


def test_access_token_jwt_with_identity():
    api_key = "key"
    api_secret = "secret"
    grant = VideoGrant()
    identity = "Bob"
    access_token = AccessToken(api_key, api_secret, grant=grant, identity=identity)
    token = access_token.to_jwt()
    decoded = jwt.decode(token, key=api_secret, algorithms=["HS256"])
    assert decoded["video"] == {}
    assert decoded["iss"] == api_key
    assert decoded["nbf"] < decoded["exp"]
    assert decoded["sub"] == identity
