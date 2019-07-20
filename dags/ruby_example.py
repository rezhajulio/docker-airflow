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
    "start_date": datetime(2019, 7, 1),
    "email": ["airflow@airflow.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=1),
    # 'queue': 'bash_queue',
    # 'priority_weight': 10,
}

dag = DAG("ruby_example", default_args=default_args, schedule_interval=timedelta(seconds=10), catchup=False)

t1 = BashOperator(task_id="check_ruby_version", bash_command="ruby -v", dag=dag)

t2= BashOperator(task_id="run_ruby_program", bash_command="ruby /usr/local/airflow/dags/scripts/hello.rb", dag=dag)

t2.set_upstream(t1)