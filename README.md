
## Flask Testing

This repo demonstrates how to test a [Flask](https://flask.palletsprojects.com/en/2.1.x/) application.


### Flask in Production

When we launch a Flask application, the web client interacts with the server, which is made up of three main subsystems:

![Flask App in Production](https://i.ibb.co/bLF631r/288709187bca.png)

The following steps occur whenever there is a request from a client:

* The **Flask Web Server** converts the HTTP message into a Request object and passes it to the **Flask Routing System**.
* The **Flask Routing System** takes a Request object and calls the appropriate **User Code**.
* The **User Code** performs whatever task we want and returns a Result to the **Flask Routing System**.
* The **Flask Routing System** converts the Result into an appropriate Response Object and sends it to the **Flask Web Server**.
* The **Flask Web Server** takes the Response Object and coverts it into an HTTP message.

### Flask in Testing

When we want to test a Flask application, we only need to test the **User Code** (It is the job of the Flask community to test the **Flask Routing System** and the **Flask Web Server**).  To do this, we replace the **Flask Web Server** with a **Flask Test Client**:

![Flask App in Testing](https://i.ibb.co/bX0G23v/8dc09aebf5ec.png)

* The **Pytest Test** puts the Flask app into testing mode and creates the **Flask Test Client**.  Using this client, the **Pytest Test** calls the `.get()` method for the endpoint we want to test.
* The **Flask Test Client** creates a Request object and passes it to the **Flask Routing System**.
* The **Flask Routing System** takes a Request object and calls the appropriate **User Code**.
* The **User Code** performs whatever task we want and returns a Result to the **Flask Routing System**.
* The **Flask Routing System** converts the Result into an appropriate Response Object and sends it to the **Flask Test Client**.
* The **Flask Test Client** returns the Response Object to the the test
* Our test can now `assert` that the response is correct.


### The Mechanics of Testing

* In `app.py` our Flask app is declared as a global variable named `app`
* In `test_app.py` we import `app` from `app.py`
* In the `test_hello` function we: 
  * put the `app` into testing mode
  * get the test client
  * use the test client to call the `.get()` method
  * assert that the `.data` of the response is what we expect

### How to Run These Tests

* Create a virtual environment

  ```
  python3 -m venv .venv
  ```

* Activate the virtual environment

  ```
  source .venv/bin/activate
  ```

  
* Install the required packages (`flask` and `pytest`)

  ```
  pip install -r requirements.txt
  ```
  
* Execute the tests

  ```
  pytest
  ```
  
