import sys
import os
import io
import time

from pathlib import Path

project_root = str(Path(__file__).resolve().parent.parent.parent)
sys.path.append(project_root)

import pathlib
import tempfile
import shutil
from src.utils.minio_crud import MinioCRUDClient
import numpy as np
import pytest
from minio.error import S3Error
from PIL import Image


ENDPOINT = os.environ.get("MINIO_ENDPOINT", "192.168.49.2:32000")
ACCESS_KEY = "3JnbRlFAACF1v5YG"
SECRET_KEY = "lYFakKmgSpQbcKREnjPid3CXkujxPbJ8"

client = MinioCRUDClient(ENDPOINT, ACCESS_KEY, SECRET_KEY, secure=False)


def test_object_ops():
    
    bucket_name = "test-bucket"
    object_name = "test-img.png"
    
    image_array = np.random.randint(0, 256, (100, 100, 3), dtype=np.uint8)
    test_content = Image.fromarray(image_array) 
    
    #Test create bucket
    assert client.create_bucket(bucket_name)
    assert any(bucket.name == bucket_name for bucket in client.list_buckets())

    # Test object write
    with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as temp_file:
        test_content.save(temp_file, format="PNG")
        temp_file.flush()
        assert client.write_file(bucket_name, object_name, temp_file.name)

    # Test object read
    with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as temp_file:
        assert client.read_file(bucket_name, object_name, temp_file.name)
        temp_file.seek(0)
        assert Image.open(temp_file.name).tobytes() == test_content.tobytes()

    # Test object listing
    objects = list(client.list_objects(bucket_name))
    assert len(objects) == 1
    assert objects[0].object_name == object_name
    
    time.sleep(1)

    # Test object deletion
    assert client.delete_object(bucket_name, object_name)
    objects = list(client.list_objects(bucket_name))
    assert len(objects) == 0

    # Clean delete bucket
    assert client.delete_bucket(bucket_name)
    assert not any(bucket.name == bucket_name for bucket in client.list_buckets())
