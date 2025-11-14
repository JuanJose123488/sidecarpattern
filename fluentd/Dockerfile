FROM fluent/fluentd:latest

USER root
RUN apt-get update && apt-get install -y build-essential ruby-dev
COPY fluent.conf /fluentd/etc/