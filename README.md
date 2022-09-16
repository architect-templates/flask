<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://cdn.architect.io/logo/horizontal-inverted.png">
    <source media="(prefers-color-scheme: light)" srcset="https://cdn.architect.io/logo/horizontal.png">
    <img width="320" alt="Architect Logo" src="https://cdn.architect.io/logo/horizontal.png">
  </picture>
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

Once the deploy has completed, you can reach your new service by going to https://web.localhost.architect.sh/.

## Deploying to the Cloud

Want to try deploying this to a cloud environment? Architect's got you covered there, too! It only takes a minute to
[sign up for a free account](https://cloud.architect.io/signup).

You can then [deploy the application](https://docs.architect.io/getting-started/introduction/#deploy-to-the-cloud). To do this, run the following command. "example-environment" is the name of the free environment that is created when you register with Architect.

```sh
# Deploy to Architect Cloud
$ architect deploy architect.yml -e example-environment
```
