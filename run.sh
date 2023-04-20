#!/bin/bash 

# set -euo pipefail 
DOCKER_USR="opetliak"
docker build -t $DOCKER_USR/ml_image:latest .
docker push $DOCKER_USR/ml_image:latest
docker run --rm -it -p 8080:8080 $DOCKER_USR/ml_image