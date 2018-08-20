# Poker_Tutorial
Tutorial to build and deploy a model to classify poker hands using Data Science tools. 

You can find a PDF with a tutorial and a poker.py that contains the code used for generating the model used at the Flask api.

Let us know if you have some feedback!

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
  For Linux hosts:
  ```
  docker run --net host -d --name web_poker python_poker
  ```
  For Windows hosts:
  ```
  docker run -p 5000:5000 -d --name web_poker python_poker
  ```
  
- The app's JSON API is now listening on port `5000` of this host. Access it at 127.0.0.1:5000.  Congrats! You just deployed your first dockerized data science application.  Now go forth and develop, train, test, validate, dockerize, and deploy more.

