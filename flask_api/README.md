# Installation

- Install these dependencies:
  - [Docker]
  - [Scikit-Learn]
  - [Flask-Restful]
  - [Pandas] 
  - [Keras]
  - [TensorFlow]
  - [JSON]
- Clone this repo.
- From the root of this repo build the Docker image:

  ```
  docker build --force-rm=true -t python_poker .
  ```

- Now run the Docker image with:

  ```
  docker run --net host -d --name web_poker python_poker
  ```

- The app's JSON API is now listening on port `5000` of this host.  Congrats! You just deployed your first dockerized data science application.  Now go forth and develop, train, test, validate, dockerize, and deploy more.
