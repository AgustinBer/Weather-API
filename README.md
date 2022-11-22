# Simple Weather ETL

This is a simple ETL using Airflow. First, we get data from API. Then, we drop unused columns, convert to CSV, and validate the data. Finally, we load the transformed data to postgres DataBase