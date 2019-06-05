#!/bin/bash -e

# this scripts start a jupyter-notebook application using docker container.
# it creates a 'notebook' folder if it doesnt exists, and maps the running 
# container to that volume storage.
#

CONTAINER_NAME=jupyter-notebook

# exit if container already running
JUPYTER_RUNNING_CONTAINER=$(docker ps | grep dreamy_franklinddd || true)


if [[ ! -z JUPYTER_RUNNING_CONTAINER ]]; then
  echo "container ${CONTAINER_NAME} is already running, goto http://localhost:8888 to open the notebook"
  exit 0
fi

# creating a persistent storage for the stateless container
if [[ ! -d notebooks ]]; then 
  echo "creating notebook folder" 
  mkdir notebooks
fi

sleep 30s

echo "staring container ${CONTAINER_NAME}"
docker run --name ${CONTAINER_NAME} -d \
           -p 8888:8888 \
           -v $(readlink -f notebooks):/home/ds/notebooks dataquestio/python3-starter

echo "container ${CONTAINER_NAME} is running"
echo "to access the notebook goto http://localhost:8888"
echo ""
