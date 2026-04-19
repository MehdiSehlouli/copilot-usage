from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

import src.app as app_module


@pytest.fixture
def client():
    return TestClient(app_module.app)


@pytest.fixture(autouse=True)
def reset_activities_state():
    """Keep tests isolated from in-memory mutations."""
    # Arrange
    original_activities = deepcopy(app_module.activities)

    yield

    # Assert cleanup
    app_module.activities.clear()
    app_module.activities.update(original_activities)
