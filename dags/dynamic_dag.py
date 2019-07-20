"""
Code that goes along with the Airflow located at:
http://airflow.readthedocs.org/en/latest/tutorial.html
"""
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta


default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2019, 7, 20, 15, 10),
    "email": ["airflow@airflow.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=1),
    # 'queue': 'bash_queue',
    # 'priority_weight': 10,
}

buffer = []

dag = DAG("dynamic_dag", default_args=default_args, schedule_interval=timedelta(seconds=15), catchup=False)

with open("/usr/local/airflow/dags/data.txt") as data:
    names = map(str.strip, data.readlines())

for name in names:
    cowsay = BashOperator(task_id=f"{name}_say_hi",
             bash_command=f"python /usr/local/airflow/dags/scripts/hi.py --name {name}",
             dag=dag)

    buffer.append(cowsay)