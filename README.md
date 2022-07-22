<p align="center">
  <a href="//architect.io" target="blank"><img src="https://docs.architect.io/img/logo.svg" width="320" alt="Architect Logo" /></a>
</p>

<p align="center">
  A dynamic microservices framework for building, connecting, and deploying cloud-native applications.
</p>

---

# Running Flask on Architect

This example will show you the use-case for using Python on Architect leveraging the Flask tutorial application – [Flaskr](https://flask.palletsprojects.com/en/2.1.x/tutorial/). In this example, we've written a component spec (the `architect.yml` file) that defines a component to run a Flask based web application.

[Learn more about the architect.yml file](//docs.architect.io/components/architect-yml/)

## Running locally

Architect component specs are declarative, so it can be run locally or remotely with a single deploy command:

```sh
# Clone the repository and navigate to this directory
$ git clone https://github.com/architect-templates/flask.git
$ cd flask

# Deploy using the dev command
$ architect dev architect.yml
```

Once the deploy has completed, you can reach your new service by going to http://web.arc.localhost/.
