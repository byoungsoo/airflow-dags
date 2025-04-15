from airflow.providers.cncf.kubernetes.operators.pod import KubernetesPodOperator
from kubernetes.client import models as k8s
from airflow.providers.cncf.kubernetes.secret import Secret
from airflow import DAG
import pendulum

args = {
    "project_id": "model_deploy-0415062835",
}

dag = DAG(
    dag_id="model_deploy-0415062835",
    default_args=args,
    schedule="@once",
    start_date=pendulum.today("UTC").add(days=-1),
    description="""
Created with Elyra 3.15.0 pipeline editor using `model_deploy.pipeline`.
    """,
    is_paused_upon_creation=False,
)


# Operator source: Machine-Learning-on-Kubernetes/Chapter07/model_deploy_pipeline/model_build_push/build_push_image.py

op_05b70e06_79ee_4046_8e38_d81304c8c267 = KubernetesPodOperator(
    name="build_push_image",
    namespace="airflow",
    image="202949997891.dkr.ecr.ap-northeast-2.amazonaws.com/common/build:kaniko",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.15.0/elyra/airflow/bootstrapper.py' && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.15.0/elyra/airflow/bootstrapper.py --output bootstrapper.py && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.15.0/etc/generic/requirements-elyra.txt' && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.15.0/etc/generic/requirements-elyra.txt --output requirements-elyra.txt && python3 -m pip install packaging && python3 -m pip freeze > requirements-current.txt && python3 bootstrapper.py --pipeline-name 'model_deploy' --cos-endpoint http://minio.minio.svc.cluster.local:9000 --cos-bucket minio-airflow --cos-directory 'model_deploy-0415062835' --cos-dependencies-archive 'build_push_image-05b70e06-79ee-4046-8e38-d81304c8c267.tar.gz' --file 'Machine-Learning-on-Kubernetes/Chapter07/model_deploy_pipeline/model_build_push/build_push_image.py' "
    ],
    task_id="build_push_image",
    env_vars={
        "MLFLOW_S3_ENDPOINT_URL": "http://minio.minio.svc.cluster.local:9000",
        "MODEL_NAME": "mlflow-demo",
        "MODEL_VERSION": "v1",
        "CONTAINER_REGISTRY": "558846430793.dkr.ecr.ap-northeast-2.amazonaws.com/model",
        "MLFLOW_TRACKING_USERNAME": "admin",
        "MLFLOW_TRACKING_PASSWORD": "admin",
        "CONTAINER_TAG": "latest",
        "CONTAINER_REPOSIOTRY": "model",
        "ELYRA_RUNTIME_ENV": "airflow",
        "AWS_ACCESS_KEY_ID": "airflow",
        "AWS_SECRET_ACCESS_KEY": "minioairflow",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "ELYRA_RUN_NAME": "model_deploy-{{ ts_nodash }}",
    },
    container_resources=k8s.V1ResourceRequirements(
        requests={
            "cpu": "4",
            "memory": "8G",
        },
        limits={},
    ),
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

op_05b70e06_79ee_4046_8e38_d81304c8c267.image_pull_policy = "Always"
