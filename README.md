# async_testing

This contains code for testing asynchronous process using  `multiprocessing`  module and AJAX requests.
A flask app and a JavaScript code interact with each other for testing this.

### How to:-

testserver.py is a simple Flask server that has 2 endpoints. A function `test` is defined that sleeps for 6 secs.

When you `GET /front`, it runs `test()` and returns 200 OK status with content `done`. 

While in `GET /back_async`,it adds the `test()` in the pool of processes and returns the 200 OK status.

Open the `index.html` file and click on `send` button. 