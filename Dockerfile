FROM cccs/assemblyline-v4-service-base:latest

ENV SERVICE_PATH unfurl.Unfurl

USER root

RUN apt update
RUN apt install -y git
RUN pip3 install dfir-unfurl
RUN git clone https://github.com/obsidianforensics/unfurl.git

USER assemblyline

WORKDIR /opt/al_service
COPY . .

ARG version=4.0.0.dev1
USER root
RUN sed -i -e "s/\$SERVICE_TAG/$version/g" service_manifest.yml

USER assemblyline