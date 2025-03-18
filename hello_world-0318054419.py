from airflow.contrib.operators.kubernetes_pod_operator import KubernetesPodOperator
from airflow.contrib.kubernetes.volume_mount import VolumeMount
from airflow.contrib.kubernetes.volume import Volume
from airflow.kubernetes.secret import Secret
from airflow import DAG
from airflow.utils.dates import days_ago

args = {
    "project_id": "hello_world-0318054419",
}

dag = DAG(
    "hello_world-0318054419",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="""
Created with Elyra 3.15.0 pipeline editor using `hello_world.pipeline`.
    """,
    is_paused_upon_creation=False,
)


# Operator source: Machine-Learning-on-Kubernetes/Chapter07/hello.py

op_61ba40d6_4f92_466c_b261_8dbdbc2f91c2 = KubernetesPodOperator(
    name="hello",
    namespace="airflow",
    image="gcr.io/kaniko-project/executor:latest",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.15.0/elyra/airflow/bootstrapper.py' && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.15.0/elyra/airflow/bootstrapper.py --output bootstrapper.py && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.15.0/etc/generic/requirements-elyra.txt' && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.15.0/etc/generic/requirements-elyra.txt --output requirements-elyra.txt && python3 -m pip install packaging && python3 -m pip freeze > requirements-current.txt && python3 bootstrapper.py --pipeline-name 'hello_world' --cos-endpoint http://minio.minio.svc.cluster.local:9000 --cos-bucket minio-airflow --cos-directory 'hello_world-0318054419' --cos-dependencies-archive 'hello-61ba40d6-4f92-466c-b261-8dbdbc2f91c2.tar.gz' --file 'Machine-Learning-on-Kubernetes/Chapter07/hello.py' "
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
    config_file="None",
    dag=dag,
)

op_61ba40d6_4f92_466c_b261_8dbdbc2f91c2.image_pull_policy = "IfNotPresent"


# Operator source: Machine-Learning-on-Kubernetes/Chapter07/world.py

op_de1208cd_667f_45b8_abcc_ef8aada7764f = KubernetesPodOperator(
    name="world",
    namespace="airflow",
    image="apache/airflow:latest-python3.12",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.15.0/elyra/airflow/bootstrapper.py' && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.15.0/elyra/airflow/bootstrapper.py --output bootstrapper.py && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.15.0/etc/generic/requirements-elyra.txt' && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.15.0/etc/generic/requirements-elyra.txt --output requirements-elyra.txt && python3 -m pip install packaging && python3 -m pip freeze > requirements-current.txt && python3 bootstrapper.py --pipeline-name 'hello_world' --cos-endpoint http://minio.minio.svc.cluster.local:9000 --cos-bucket minio-airflow --cos-directory 'hello_world-0318054419' --cos-dependencies-archive 'world-de1208cd-667f-45b8-abcc-ef8aada7764f.tar.gz' --file 'Machine-Learning-on-Kubernetes/Chapter07/world.py' "
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
    config_file="None",
    dag=dag,
)

op_de1208cd_667f_45b8_abcc_ef8aada7764f.image_pull_policy = "IfNotPresent"

op_de1208cd_667f_45b8_abcc_ef8aada7764f << op_61ba40d6_4f92_466c_b261_8dbdbc2f91c2
