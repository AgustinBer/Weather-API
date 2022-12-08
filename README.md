# Simple Weather ETL

This is a simple ETL using Airflow. First, we get data from API. Then, we drop unused columns, convert to CSV, and validate the data. Finally, we load the transformed data to postgres DataBase

This repository contains examples of Apache Airflow DAGs for automating recurrent queries. All DAGs run on Astronomer infrastructure installed on Ubuntu 20.04.3 LTS.

## Diagram

![alt text](https://i.gyazo.com/7bbfea7c0407bfda94f322d5aa1d8b1c.png)

## Installation

Before running examples make sure to set up the right environment:

* [Python3](https://www.python.org/downloads/)
* [Docker](https://www.docker.com/)
* [Astronomer](https://www.astronomer.io/)

### Astronomer
Astronomer is the managed provider that allows users to easily run and monitor Apache Airflow environments. The best way to initialize and run projects on Astronomer is to use [Astronomer CLI](https://www.astronomer.io/docs/cloud/stable/develop/cli-quickstart). To install its latest version on Ubuntu run:

```shell
curl -sSL https://install.astronomer.io | sudo bash
```

To make sure that Astronomer CLI is installed run:

```shell
astro version
```

For installation of Astronomer CLI on another operating system, please refer to the [official documentation](https://www.astronomer.io/docs/cloud/stable/develop/cli-quickstart).

## Project files

The project directory has the following file structure:

```
  ├── dags # directory containing all DAGs
  ├── .astro # project settings
  ├── Dockerfile # runtime overrides for Astronomer Docker image
  ├── init # additional setup-related scripts/database schemas
  └── requirements.txt # specification of Python packages
  └── setup.py # setup
```

In the [dags](dags) directory you can find the dags:

* [weather_dag.py](dags/weather_dag.py): performs a daily export of table data to a remote filesystem (in our case S3). Contains 3 tasks:

├──get_weather: We get London current weather using OpenWeatherMap API. If the API call was sucessful, get the json and dump it to a file with today's date as the title in GCS bucket.
├──transform_data: We read previous file, transform the data to the correct types and convert temp to celsius, then we load to another bucket (staging)
├──load_data: we read previous data, then load it into a table in postgres


## Start the project

To start the project on your local machine run:

```shell
astro dev start
```

To access the Apache Airflow UI go to `http://localhost:8081`.

From Airflow UI you can further manage running DAGs, check their status, the time of the next and last run and some metadata.

### Docker BuildKit issue

If your Docker environment has the [BuildKit feature](https://docs.docker.com/develop/develop-images/build_enhancements/) enabled, you may run into an error when starting the Astronomer project:

```shell
$ astro dev start
Env file ".env" found. Loading...
buildkit not supported by daemon
```

To overcome this issue, start Astronomer without the BuildKit feature: `DOCKER_BUILDKIT=0 astro dev start` (see the [Astronomer Forum](https://forum.astronomer.io/t/buildkit-not-supported-by-daemon-error-command-docker-build-t-airflow-astro-bcb837-airflow-latest-failed-failed-to-execute-cmd-exit-status-1/857)).

## Code linting

Before opening a pull request, please run [pylint](https://www.pylint.org) and [black](https://github.com/psf/black). To install all dependencies, run:

```shell
python -m pip install --upgrade -e ".[develop]"
python -m pip install --upgrade -r requirements.txt
```

Then run `pylint` and `black` using:

```shell
python -m pylint dags
python -m black .
```
