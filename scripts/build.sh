set -e

docker-compose -f docker-compose-build.yaml up --build -d
docker-compose down

sudo chmod -R 777 dist