import os
from minio import Minio
from minio.error import S3Error

class MinioCRUDClient:
    def __init__(self, endpoint, access_key, secret_key, secure=True):
        self.client = Minio(endpoint, access_key=access_key, secret_key=secret_key, secure=secure)

    def create_bucket(self, bucket_name):
        try:
            if not self.client.bucket_exists(bucket_name):
                self.client.make_bucket(bucket_name)    
        except S3Error as exc:
            raise exc  # Reraise the exception instead of returning a boolean value
        return True       

    def list_buckets(self):
        return self.client.list_buckets()

    def write_file(self, bucket_name, object_name, file_path):
        try:
            self.client.fput_object(bucket_name, object_name, file_path)
        except S3Error as exc:
            raise exc
        return True

    def read_file(self, bucket_name, object_name, file_path):
        try:
            self.client.fget_object(bucket_name, object_name, file_path)
        except S3Error as exc:
            raise exc
        return True

    def list_objects(self, bucket_name):
        return self.client.list_objects(bucket_name)

    def delete_object(self, bucket_name, object_name):
        try:
            self.client.remove_object(bucket_name, object_name)
        except S3Error as exc:
            raise exc
        return True

    def delete_bucket(self, bucket_name):
        try:
            if self.client.bucket_exists(bucket_name):
                self.client.remove_bucket(bucket_name)
        except S3Error as exc:
            raise exc
        return True
