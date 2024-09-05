#!/bin/bash

docker build -t feature-unlocked . 
docker run --privileged --rm -p 1337:1337 -it feature-unlocked