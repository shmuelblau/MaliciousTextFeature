
oc apply -f ../infra/mongoDB.yml
oc apply -f mongoDB-service.yml
oc apply -f server.yml
oc apply -f server-service.yml


oc apply -f ../infra/openshift/deploy/dataretrieval.yml
oc apply -f ../infra/openshift/deploy/enricher.yml
oc apply -f ../infra/openshift/deploy/kafka.yml
oc apply -f ../infra/openshift/deploy/mongoDB.yml
oc apply -f ../infra/openshift/deploy/persister.yml
oc apply -f ../infra/openshift/deploy/preprocessor.yml
oc apply -f ../infra/openshift/deploy/retriever.yml


oc apply -f ../infra/openshift/services/dataretrieval-service.yml
oc apply -f ../infra/openshift/services/kafka-service.yml
oc apply -f ../infra/openshift/services/mongoDB-service.yml

oc expose service/dataretrieval 

