# step -1

from airflow import DAG
from datetime import datetime, timedelta
from airflow.operator.dummy_operator import DummyOperator

#Step-2

default_args = {
	'owner': 'airflow',
	'depends_on_past': False,
	'start_date': datetime(2020, 11, 11),
	'retries': 0
}

#step -3 

dag = DAG(dag_id='DAG-1', default_args=default_args, catchup=False, schedule_interval='@once')

#step-4

start = DummyOperator(task_id='start',dag=dag)
end = DummyOperator(task_id='end', dag=dag)

#step-5
start >> end
