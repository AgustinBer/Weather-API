from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

from src.get_weather import get_weather
from src.transform_data import transform_data
from src.load_table import load_table
import requests
import json
import os


# Define the default dag arguments
default_args = {
    'owner': 'Agustin Bergoglio',
    'depends_on_past': False,
    'email': ['agustin.bergoglio@hotmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}


# Dag definition
dag = DAG(
    dag_id='weatherDag',
    default_args=default_args,
    schedule_interval=timedelta(minutes=1440))


# First task is to query get the weather from openweathermap.org.
task1 = PythonOperator(
    task_id='get_weather',
    provide_context=True,
    python_callable=get_weather,
    dag=dag)


# Second task is to transform the data
task2 = PythonOperator(
    task_id='transform_data',
    provide_context=True,
    python_callable=transform_data,
    dag=dag)

# Third task is to load data into the database.
task3 = PythonOperator(
    task_id='load_data',
    provide_context=True,
    python_callable=load_table,
    dag=dag)

# Set dependencies
task1 >> task2 >> task3