set -e

docker-compose -p docker-compose-aliases-build -f docker-compose-build.yaml up --build -d
docker-compose -p docker-compose-aliases-build -f docker-compose-build.yaml down

sudo chmod -R 777 dist