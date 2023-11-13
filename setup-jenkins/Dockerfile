FROM jenkins/jenkins:lts

USER root
RUN apt-get update && apt-get install -y python3
RUN apt-get update && apt-get install -y python3-pip
RUN apt-get update && apt-get install -y lsb-release
RUN curl -fsSLo /usr/share/keyrings/docker-archive-keyring.asc \
  https://download.docker.com/linux/debian/gpg
RUN echo "deb [arch=$(dpkg --print-architecture) \
  signed-by=/usr/share/keyrings/docker-archive-keyring.asc] \
  https://download.docker.com/linux/debian \
  $(lsb_release -cs) stable" > /etc/apt/sources.list.d/docker.list
RUN apt-get update && apt-get install -y docker.io
# Install Docker Compose
RUN curl -L "https://github.com/docker/compose/releases/download/v2.5.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose \
    && chmod +x /usr/local/bin/docker-compose

# Switch back to the Jenkins user
USER jenkins
RUN jenkins-plugin-cli --plugins "blueocean docker-workflow"
RUN jenkins-plugin-cli --plugins "dependency-check-jenkins-plugin:5.4.3"
RUN jenkins-plugin-cli --plugins "sonar:2.16.1"
