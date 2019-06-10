#!/bin/bash -e

# this scripts start a jupyter-notebook application using docker container.
# it creates a 'notebook' folder if it doesnt exists, and maps the running 
# container to that volume storage.
#

# to add modules to a running container use this:
# docker exec -ti jupyter-notebook /opt/ds/bin/pip install elasticsearch

CONTAINER_NAME=jupyter-notebook

# exit if container already running
docker ps    | grep -q jupyter-notebook && IS_RUNNING=true || IS_RUNNING=false
if [[ "${IS_RUNNING}" = "true" ]]; then
  echo "container ${CONTAINER_NAME} is already running, goto http://localhost:8888 to open the notebook"
  exit 0
fi

# creating a persistent storage for the stateless container
if [[ ! -d notebooks ]]; then 
  echo "creating notebook folder" 
  mkdir notebooks
fi

# start container if exists
docker ps -a | grep -q jupyter-notebook && IS_STOPPED=true || IS_RUNNING=false
if [[ "${IS_STOPPED}" = "true" ]]; then
  echo "container ${CONTAINER_NAME} stopped. starting ..."
  docker start ${CONTAINER_NAME}
  echo "goto http://localhost:8888 to open the notebook"
  exit 0
fi

# creating a new container
echo "staring container ${CONTAINER_NAME}"
docker run --name ${CONTAINER_NAME} -d \
           -p 8888:8888 \
           -v $(readlink -f notebooks):/home/ds/notebooks dataquestio/python3-starter



echo "container ${CONTAINER_NAME} is running"
echo "to access the notebook goto http://localhost:8888"
COMMAND=$(echo -n "/opt/ds/bin/pip install " ; for line in $(cat requirements.txt) ; do echo -n "$line "  ; done)
echo "installing pip packages from requirements.txt"
echo "command: ${COMMAND}"
docker exec -ti ${CONTAINER_NAME} ${COMMAND}
