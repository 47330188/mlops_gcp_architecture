import boto3

AWS_ACCESS_KEY_ID="AKIARVQEJTZRAVCUMZ7M"
AWS_SECRET_ACCESS_KEY="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"
AWS_REGION="us-west-1"
AWS_BUCKET_NAME="datapath-mlops-1"

def upload_file_to_s3(file_path, bucket_name, object_name):
    # Credenciales de AWS
    aws_access_key_id = AWS_ACCESS_KEY_ID
    aws_secret_access_key = AWS_SECRET_ACCESS_KEY
    aws_region = AWS_REGION

    # Crear cliente de S3
    s3_client = boto3.client(
        's3',
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
        region_name=aws_region
    )

    # Subir archivo al bucket de S3
    try:
        s3_client.upload_file(file_path, bucket_name, object_name)
        print("Archivo subido exitosamente a S3.")
    except Exception as e:
        print("Error al subir el archivo a S3:", str(e))

# Ejemplo de uso
file_path = '../testing/test.txt' # Source
bucket_name = AWS_BUCKET_NAME
object_name = 'testing/archivo.txt' # Destination

upload_file_to_s3(file_path, bucket_name, object_name)
