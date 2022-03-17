#!/bin/zsh

docker build . -t convert-data-into-parquet:1.0

echo "docker run -v $PWD/app:/app convert-data-into-parquet:1.0 "
docker run -v $PWD/app:/app convert-data-into-parquet:1.0