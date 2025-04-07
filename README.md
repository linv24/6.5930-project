# 6.5930 Project: Modeling FlexDCIM

## TODO

- [ ] `workspace/project/models/include/defines.yaml` is copied directly from lab-5, but still needs to be double-checked for whether all variables are compatible with FlexDCIM

## Using Docker

Please start the Docker and the Jupyter server like in Lab 0. Please pull
the docker first and then start with `docker-compose up`.

```
cd <your-repository-directory>
export DOCKER_ARCH=amd64

# If you are using arm CPU (Apple M1/M2),
# export DOCKER_ARCH=arm64

docker-compose pull
docker-compose up

# Complete the lab then run the following from within the docker container
# make submit
```