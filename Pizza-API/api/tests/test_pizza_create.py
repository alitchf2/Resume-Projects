from fastapi.testclient import TestClient
from ..controllers import staff as controller
from ..main import app
import pytest
from ..models import pizza as model

# Create a test client for the app
client = TestClient(app)


@pytest.fixture
def db_session(mocker):
    return mocker.Mock()


def test_create_pizza(db_session):
    pizza_data = {
        "name": "Test name",
        "price": 10,
        "calories":1000,
        "category":"Main"
    }

    pizza_object = model.Pizza(**pizza_data)

    created_pizza = controller.create_pizza(db_session, pizza_object)

    assert created_pizza is not None
    assert created_pizza.name == "Test name"
    assert created_pizza.price == 10
    assert created_pizza.calories == 1000
    assert created_pizza.category == "Main"
