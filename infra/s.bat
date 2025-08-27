docker build -t shmuelblau/retriever:2 ../services/Retriever
docker push shmuelblau/retriever:2

docker build -t shmuelblau/preprocessor:2 ../services/Preprocessor
docker push shmuelblau/preprocessor:2  

docker build -t shmuelblau/enricher:2 ../services/Enricher
docker push shmuelblau/enricher:2  

docker compose up