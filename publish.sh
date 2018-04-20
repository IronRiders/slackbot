#!/bin/bash
echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin
docker tag ironriders-bot ironriders/slackbot
docker push ironriders/slackbot