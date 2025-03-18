from airflow.providers.cncf.kubernetes.operators.pod import KubernetesPodOperator
from kubernetes.client import models as k8s
from airflow.providers.cncf.kubernetes.secret import Secret
from airflow import DAG
import pendulum

args = {
    "project_id": "hello_world-0318064748",
}

dag = DAG(
    dag_id="hello_world-0318064748",
    default_args=args,
    schedule="@once",
    start_date=pendulum.today("UTC").add(days=-1),
    description="""
Created with Elyra 3.15.0 pipeline editor using `hello_world.pipeline`.
    """,
    is_paused_upon_creation=False,
)


# Operator source: Machine-Learning-on-Kubernetes/Chapter07/hello.py

op_34a3682f_474a_4b8a_ac2a_b4ff77350071 = KubernetesPodOperator(
    name="hello",
    namespace="airflow",
    image="202949997891.dkr.ecr.ap-northeast-2.amazonaws.com/common/build:kaniko",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.15.0/elyra/airflow/bootstrapper.py' && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.15.0/elyra/airflow/bootstrapper.py --output bootstrapper.py && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.15.0/etc/generic/requirements-elyra.txt' && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.15.0/etc/generic/requirements-elyra.txt --output requirements-elyra.txt && python3 -m pip install packaging && python3 -m pip freeze > requirements-current.txt && python3 bootstrapper.py --pipeline-name 'hello_world' --cos-endpoint http://minio.minio.svc.cluster.local:9000 --cos-bucket minio-airflow --cos-directory 'hello_world-0318064748' --cos-dependencies-archive 'hello-34a3682f-474a-4b8a-ac2a-b4ff77350071.tar.gz' --file 'Machine-Learning-on-Kubernetes/Chapter07/hello.py' "
    ],
    task_id="hello",
    env_vars={
        "ELYRA_RUNTIME_ENV": "airflow",
        "AWS_ACCESS_KEY_ID": "airflow",
        "AWS_SECRET_ACCESS_KEY": "minioairflow",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "ELYRA_RUN_NAME": "hello_world-{{ ts_nodash }}",
    },
    volumes=[],
    volume_mounts=[],
    secrets=[],
    annotations={},
    labels={},
    tolerations=[],
    in_cluster=True,
    config_file=None,
    dag=dag,
)

op_34a3682f_474a_4b8a_ac2a_b4ff77350071.image_pull_policy = "Always"


# Operator source: Machine-Learning-on-Kubernetes/Chapter07/world.py

op_383509d1_5f45_476c_83a3_ad1f7e188f56 = KubernetesPodOperator(
    name="world",
    namespace="airflow",
    image="apache/airflow:latest-python3.12",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.15.0/elyra/airflow/bootstrapper.py' && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.15.0/elyra/airflow/bootstrapper.py --output bootstrapper.py && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.15.0/etc/generic/requirements-elyra.txt' && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.15.0/etc/generic/requirements-elyra.txt --output requirements-elyra.txt && python3 -m pip install packaging && python3 -m pip freeze > requirements-current.txt && python3 bootstrapper.py --pipeline-name 'hello_world' --cos-endpoint http://minio.minio.svc.cluster.local:9000 --cos-bucket minio-airflow --cos-directory 'hello_world-0318064748' --cos-dependencies-archive 'world-383509d1-5f45-476c-83a3-ad1f7e188f56.tar.gz' --file 'Machine-Learning-on-Kubernetes/Chapter07/world.py' "
    ],
    task_id="world",
    env_vars={
        "ELYRA_RUNTIME_ENV": "airflow",
        "AWS_ACCESS_KEY_ID": "airflow",
        "AWS_SECRET_ACCESS_KEY": "minioairflow",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "ELYRA_RUN_NAME": "hello_world-{{ ts_nodash }}",
    },
    volumes=[],
    volume_mounts=[],
    secrets=[],
    annotations={},
    labels={},
    tolerations=[],
    in_cluster=True,
    config_file=None,
    dag=dag,
)

op_383509d1_5f45_476c_83a3_ad1f7e188f56.image_pull_policy = "IfNotPresent"

op_383509d1_5f45_476c_83a3_ad1f7e188f56 << op_34a3682f_474a_4b8a_ac2a_b4ff77350071
