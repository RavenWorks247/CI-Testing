from app import app
from bs4 import BeautifulSoup

client = app.test_client()


def test_page_contains_title():
    response = client.get("/")

    soup = BeautifulSoup(response.data, "html.parser")

    assert soup.title.string == "CI/CD Demo"


def test_button_exists():
    response = client.get("/")

    soup = BeautifulSoup(response.data, "html.parser")

    button = soup.find("button")

    assert button is not None
