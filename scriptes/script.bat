docker build -t shmuelblau/retriever:1 .
docker push shmuelblau/retriever:1  

docker build -t shmuelblau/subscriber:1 services/Subscriber/.
docker push shmuelblau/subscriber:1  

docker compose up
