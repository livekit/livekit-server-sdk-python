import os

import pytest

from livekit import DataPacketKind, Room, RoomServiceClient


@pytest.fixture
def client() -> RoomServiceClient:
    host = os.environ.get("LIVEKIT_HOST", "http://localhost:7880")
    api_key = os.environ["LIVEKIT_API_KEY"]
    api_secret = os.environ["LIVEKIT_API_SECRET"]
    return RoomServiceClient(host, api_key, api_secret)


@pytest.fixture
def name() -> str:
    return "Test Room"


@pytest.fixture
def create_room(client) -> Room:
    return client.create_room("Test Room")


def test_create_room(client, create_room):
    name = "Test Room"
    room = client.create_room(name)
    assert room.name == name


def test_list_rooms(client, create_room):
    rooms = client.list_rooms()
    assert isinstance(rooms, list)


def test_delete_room(client, create_room):
    client.delete_room(create_room.name)


def test_list_participants(client, create_room):
    participants = client.list_participants(create_room.name)
    assert isinstance(participants, list)


def test_get_participant(client):
    # TODO: need to add a participant first
    pass


def test_remove_participant(client, create_room):
    # TODO: need to add a participant first
    # client.remove_participant(create_room.name, 'foo')
    pass


def test_update_participant(client, create_room):
    # TODO: need to add a participant first
    pass


def test_update_subscription(client, create_room):
    # TODO: need to add a participant first
    pass


def test_update_room_metadata(client, create_room):
    metadata = "some super duper metadata"
    client.update_room_metadata(create_room.name, metadata)


def test_send_data(client, create_room):
    data = b"some awesome data"
    client.send_data(create_room.name, data, DataPacketKind.RELIABLE)
