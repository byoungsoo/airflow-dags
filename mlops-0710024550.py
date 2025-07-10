from airflow.providers.cncf.kubernetes.operators.pod import KubernetesPodOperator
from kubernetes.client import models as k8s
from airflow.providers.cncf.kubernetes.secret import Secret
from airflow import DAG
import pendulum

args = {
    "project_id": "mlops-0710024550",
}

dag = DAG(
    dag_id="mlops-0710024550",
    default_args=args,
    schedule="@once",
    start_date=pendulum.today("UTC").add(days=-1),
    description="""
Created with Elyra 3.15.0 pipeline editor using `mlops.pipeline`.
    """,
    is_paused_upon_creation=False,
)


# Operator source: lab-env/pipeline/02_create_spark_crd.py

op_9c809039_2397_4ca6_a828_f2cb4b926203 = KubernetesPodOperator(
    name="02_create_spark_crd",
    namespace="default",
    image="dksshddl/python:3.11",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.15.0/elyra/airflow/bootstrapper.py' && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.15.0/elyra/airflow/bootstrapper.py --output bootstrapper.py && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.15.0/etc/generic/requirements-elyra.txt' && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.15.0/etc/generic/requirements-elyra.txt --output requirements-elyra.txt && python3 -m pip install packaging && python3 -m pip freeze > requirements-current.txt && python3 bootstrapper.py --pipeline-name 'mlops' --cos-endpoint http://minio.minio --cos-bucket airflow-dags --cos-directory 'mlops-0710024550' --cos-dependencies-archive '02_create_spark_crd-9c809039-2397-4ca6-a828-f2cb4b926203.tar.gz' --file 'lab-env/pipeline/02_create_spark_crd.py' "
    ],
    task_id="02_create_spark_crd",
    env_vars={
        "ELYRA_RUNTIME_ENV": "airflow",
        "AWS_ACCESS_KEY_ID": "admin",
        "AWS_SECRET_ACCESS_KEY": "admin123",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "ELYRA_RUN_NAME": "mlops-{{ ts_nodash }}",
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


# Operator source: lab-env/pipeline/03_learn_model.py

op_34a75240_0f24_401e_b59c_ce3ede0120b8 = KubernetesPodOperator(
    name="03_learn_model",
    namespace="default",
    image="dksshddl/python:3.11",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.15.0/elyra/airflow/bootstrapper.py' && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.15.0/elyra/airflow/bootstrapper.py --output bootstrapper.py && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.15.0/etc/generic/requirements-elyra.txt' && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.15.0/etc/generic/requirements-elyra.txt --output requirements-elyra.txt && python3 -m pip install packaging && python3 -m pip freeze > requirements-current.txt && python3 bootstrapper.py --pipeline-name 'mlops' --cos-endpoint http://minio.minio --cos-bucket airflow-dags --cos-directory 'mlops-0710024550' --cos-dependencies-archive '03_learn_model-34a75240-0f24-401e-b59c-ce3ede0120b8.tar.gz' --file 'lab-env/pipeline/03_learn_model.py' "
    ],
    task_id="03_learn_model",
    env_vars={
        "ELYRA_RUNTIME_ENV": "airflow",
        "AWS_ACCESS_KEY_ID": "admin",
        "AWS_SECRET_ACCESS_KEY": "admin123",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "ELYRA_RUN_NAME": "mlops-{{ ts_nodash }}",
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

op_34a75240_0f24_401e_b59c_ce3ede0120b8 << op_9c809039_2397_4ca6_a828_f2cb4b926203


# Operator source: lab-env/pipeline/04_build_model_kaniko.py

op_062ee84a_188f_42e8_9717_1635ee863d96 = KubernetesPodOperator(
    name="04_build_model_kaniko",
    namespace="default",
    image="dksshddl/kaniko-builder",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.15.0/elyra/airflow/bootstrapper.py' && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.15.0/elyra/airflow/bootstrapper.py --output bootstrapper.py && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.15.0/etc/generic/requirements-elyra.txt' && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.15.0/etc/generic/requirements-elyra.txt --output requirements-elyra.txt && python3 -m pip install packaging && python3 -m pip freeze > requirements-current.txt && python3 bootstrapper.py --pipeline-name 'mlops' --cos-endpoint http://minio.minio --cos-bucket airflow-dags --cos-directory 'mlops-0710024550' --cos-dependencies-archive '04_build_model_kaniko-062ee84a-188f-42e8-9717-1635ee863d96.tar.gz' --file 'lab-env/pipeline/04_build_model_kaniko.py' "
    ],
    task_id="04_build_model_kaniko",
    env_vars={
        "CONTAINER_REGISTRY": "558846430793.dkr.ecr.ap-northeast-2.amazonaws.com",
        "ELYRA_RUNTIME_ENV": "airflow",
        "AWS_ACCESS_KEY_ID": "admin",
        "AWS_SECRET_ACCESS_KEY": "admin123",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "ELYRA_RUN_NAME": "mlops-{{ ts_nodash }}",
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

op_062ee84a_188f_42e8_9717_1635ee863d96 << op_34a75240_0f24_401e_b59c_ce3ede0120b8


# Operator source: lab-env/pipeline/05_deploy.py

op_90f52c9d_eb61_4ce4_ba9c_e247290a10b9 = KubernetesPodOperator(
    name="05_deploy",
    namespace="default",
    image="dksshddl/python:3.11",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.15.0/elyra/airflow/bootstrapper.py' && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.15.0/elyra/airflow/bootstrapper.py --output bootstrapper.py && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.15.0/etc/generic/requirements-elyra.txt' && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.15.0/etc/generic/requirements-elyra.txt --output requirements-elyra.txt && python3 -m pip install packaging && python3 -m pip freeze > requirements-current.txt && python3 bootstrapper.py --pipeline-name 'mlops' --cos-endpoint http://minio.minio --cos-bucket airflow-dags --cos-directory 'mlops-0710024550' --cos-dependencies-archive '05_deploy-90f52c9d-eb61-4ce4-ba9c-e247290a10b9.tar.gz' --file 'lab-env/pipeline/05_deploy.py' "
    ],
    task_id="05_deploy",
    env_vars={
        "EXPERIMENT_ID": "Bike Rental Prediction",
        "MODEL_NAME": "seoulbike-rental-prediction-xgboost",
        "MODEL_COORDINATES": "558846430793.dkr.ecr.ap-northeast-2.amazonaws.com/mlops/basic-model",
        "INGRESS_HOST": "model.bys.people.aws.dev",
        "ELYRA_RUNTIME_ENV": "airflow",
        "AWS_ACCESS_KEY_ID": "admin",
        "AWS_SECRET_ACCESS_KEY": "admin123",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "ELYRA_RUN_NAME": "mlops-{{ ts_nodash }}",
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

op_90f52c9d_eb61_4ce4_ba9c_e247290a10b9 << op_062ee84a_188f_42e8_9717_1635ee863d96
