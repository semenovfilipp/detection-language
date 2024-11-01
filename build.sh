#!/bin/bash

ROOT=$(dirname $0)
cd "$ROOT"

docker login -u "$DOCKER_USERNAME" -p "$DOCKER_PASSWORD"


echo "Building project..."
SERVICE_NAME="detectlanguage"
BUILD_BRANCH=$(git rev-parse --abbrev-ref HEAD)
BRANCH_NAME_LOWER=$(echo "$BUILD_BRANCH" | tr '[:upper:]' '[:lower:]')

IMAGE=semenovfilipp/caila-course/$SERVICE_NAME:$BRANCH_NAME_LOWER

DOCKER_BUILDKIT=1


echo "Building Docker image..."
docker build --build-arg IMAGE_NAME="$IMAGE" . -t "$IMAGE" || exit 1

echo "Pushing Docker image to Docker Hub..."
docker push "$IMAGE" || exit 1

echo --------------------------------------------------
echo Docker image: $IMAGE
echo --------------------------------------------------
