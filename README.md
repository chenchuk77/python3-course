# Python3 introduction course

Course materials and code snippets

### Dependencies

* Python3 interpreter
* Docker runtime (only for using jupyter-notebook)

### Notes

written with linux so if using windows - maybe some modifications is necessary

### Running a Jupyter-Notebook

Bash script provided to launch a docker container running jupyter-noteboook. The script created a notbook folder and map it to the container, providing a persistent storage

```bash

~ $ git clone https://github.com/chenchuk77/python3-course.git
~ $ cd python3-course
~/python3-course $ ./start-notebook.sh

```
Once running, open http://localhost:8888 to access the jupyter-notebook. requirements.txt is a list of packages to install when launching the container. if installation of packages is necessary during runtime - it can be done by invoking pip inside the container:

```bash
~/python3-course $ docker exec -ti jupyter-notebook /opt/ds/bin/pip install elasticsearch

```

## Authors

* [Chen Alkabets](chenchuk@gmail.com)

## Community

* [Slack channel](https://remote-python.slack.com/messages/CJMDAJCQZ/)

## License

This project is free, and is use for examples only

