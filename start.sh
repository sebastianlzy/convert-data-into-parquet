#!/bin/zsh

docker build . -t convert-data-into-parquet:1.0

echo "docker run -v $PWD/hello_world:/hello_world convert-data-into-parquet:1.0 "
docker run -v $PWD/hello_world:/hello_world convert-data-into-parquet:1.0