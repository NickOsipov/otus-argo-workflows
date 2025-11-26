IMAGE_NAME := nickosipov/otus-argo-workflows
IMAGE_TAG := latest
ARGO_VERSION := v3.7.4
ARGO_URL := https://github.com/argoproj/argo-workflows/releases/download

pre-commit:
	pre-commit run --all-files

build:
	docker build -t $(IMAGE_NAME):$(IMAGE_TAG) .
	docker push $(IMAGE_NAME):$(IMAGE_TAG)	

run:
	docker run -it $(IMAGE_NAME):$(IMAGE_TAG) bash

minikube-start:
	minikube start

minikube-stop:
	minikube stop

setup-kube-config:
	export KUBECONFIG=~/.kube/config

argo-workflows-install:
	kubectl create namespace argo
	kubectl apply \
		-n argo \
		-f "$(ARGO_URL)/$(ARGO_VERSION)/quick-start-minimal.yaml"

argo-workflows-uninstall:
	kubectl delete namespace argo

deploy:
	argo submit -n argo k8s/pipeline.yaml 

ui:
	kubectl port-forward svc/argo-server -n argo 2746:2746

