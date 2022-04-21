
# Import the app variable from app.py
from app import app

def test_hello():

    # put the app into testing mode
    app.config.update({"TESTING": True,})
    # get the test client
    client = app.test_client()

    # use the test client to call the / endpoint, save the response
    response = client.get('/')

    # verify that the data of the response is what we expect
    assert b"<h1>Hello World</h1>" in response.data
