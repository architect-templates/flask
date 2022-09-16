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

# Flask Starter Project
It is extremely common to run a REST API with a backend database as a standalone service so that it can be consumed by
multiple, disparate applications.

In this example, you'll learn how to capture an API written with [Flask](https://flask.palletsprojects.com/en/2.2.x/) with a [ZDJTODO UPDATE](https://www.postgresql.org/)
database backend in an Architect Component to enable automated deployments, networking and network security for your application - wherever it gets deployed.

In the `architect.yml` file for this project, we describe this API as two deployable services. However, we also
leverage Architect's [service discovery](//docs.architect.io/components/service-discovery) features to populate environment
secrets by reference. This not only allows us to automatically connect the services to each other, but it also allows
Architect to build strict network policies to whitelist the traffic between these services. Now we won't have any work ahead
of us to promote this stack from local dev all the way through to production!

[Learn more about the architect.yml file](//docs.architect.io/configuration)

## Using the API
This API implements basic CRUD functionality for a simple `Items` schema consisting of a `name` and a `rating` between 1 and 5.
You could use it to gather data about anything you want to rate, from your favorite restaurants, movies, and more!

### The `Items` Schema:

```
  {
    "name": "string",
    "rating": "integer"
  }
```

The GET request returns the Items records in the following JSON payload:
```
 [
   {
    "name": "string",
    "rating": "integer",
    "created_at": "string",
    "updated_at": "string"
  }
 ]
```

## Running Locally
The `architect.yml` file is declarative, which allows the Architect Component it describes to be run in any environment,
from local development all the way to production. Follow these steps to clone this repository and run the application
locally.

Once the deployment has completed, you can reach your new service by going to https://api.localhost.architect.sh.

```sh
# Clone the repository and navigate to this directory
$ git clone git@github.com:architect-templates/node-rest-api.git
$ cd ./node-rest-api

# Deploy locally using the dev command
$ architect dev .
```


## Deploying to the Cloud

Want to try deploying this to a cloud environment? Architect's got you covered there, too! It only takes a minute to
[sign up for a free account](https://auth.architect.io/u/signup?state=hKFo2SAtSnhOdXljdy1nelBHb2NlajNhZkkybTlLOEJHcWRFeaFur3VuaXZlcnNhbC1sb2dpbqN0aWTZIFNCNEZUUFBHaWpBdlA3UVlVV0xFNk1rQVJvUHBzdF9Bo2NpZNkgbElwVzlmcTlJRlFCQmpUZ2xsaE42RUkwMVRYTWhSVm0).

You can then [register the component](https://docs.architect.io/getting-started/?_ga=2.19805311.635236263.1652126693-1328677302.1650395826#register-a-component)
to your free environment and [deploy the component](https://docs.architect.io/getting-started/introduction/#deploy-to-the-cloud)
using the commands below from the `node-rest-api` directory.

The `<account-name>` is the name you used when you created your account in Architect Cloud. Use "example-environment" for
the `<environment-name>` to deploy to the free environment that is created when you register with Architect.

```sh
# Register and tag the component with Architect Cloud's component registry
$ architect register . --tag latest --account <account-name>

# Deploy to Architect Cloud
$ architect deploy node-rest-api -a <account-name> -e <environment-name>
```

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
