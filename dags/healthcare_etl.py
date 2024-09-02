from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
import pandas as pd
import sqlite3
import requests

default_args = {
    'owner': 'airflow',
    'start_date': days_ago(1),
    'retries': 1,
}

def extract_data():
    url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'
    response = requests.get(url)
    with open('/tmp/covid19_data.csv', 'wb') as f:
        f.write(response.content)

def transform_data():
    df = pd.read_csv('/tmp/covid19_data.csv')
    df = df.groupby('Country/Region').sum().drop(columns=['Lat', 'Long'])
    df.to_csv('/tmp/covid19_data_transformed.csv')

def load_data():
    conn = sqlite3.connect('/tmp/healthcare_data.db')
    df = pd.read_csv('/tmp/covid19_data_transformed.csv')
    df.to_sql('covid19_data', conn, if_exists='replace', index=False)
    conn.close()

with DAG(
    'healthcare_etl',
    default_args=default_args,
    description='A simple healthcare ETL process',
    schedule_interval='@daily',
    catchup=False,
) as dag:

    extract_task = PythonOperator(
        task_id='extract_data',
        python_callable=extract_data,
    )

    transform_task = PythonOperator(
        task_id='transform_data',
        python_callable=transform_data,
    )

    load_task = PythonOperator(
        task_id='load_data',
        python_callable=load_data,
    )

    extract_task >> transform_task >> load_task
