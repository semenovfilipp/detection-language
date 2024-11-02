#!/bin/bash

ROOT=$(dirname $0)
cd "$ROOT"

DOCKER_USERNAME="ФЫВФЫВ"
DOCKER_PASSWORD="asdasdasd"

docker login -u "$DOCKER_USERNAME" -p "$DOCKER_PASSWORD"


echo "Building project..."
BUILD_BRANCH=$(git rev-parse --abbrev-ref HEAD)
BRANCH_NAME_LOWER=$(echo "$BUILD_BRANCH" | tr '[:upper:]' '[:lower:]')

IMAGE=semenovfilipp/caila-course:$BRANCH_NAME_LOWER

DOCKER_BUILDKIT=1 docker build --build-arg IMAGE_NAME=$IMAGE . -t "$IMAGE"

docker push "$IMAGE"

echo --------------------------------------------------
echo Docker image: $IMAGE
echo --------------------------------------------------
