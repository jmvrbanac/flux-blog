FROM nginx:latest
MAINTAINER John Vrbanac <john.vrbanac@linux.com>

RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y python-dev python-pip make

ADD . /prj-src
WORKDIR /prj-src
RUN pip install -r requirements.txt
RUN make html
RUN cp -R output/* /usr/share/nginx/html/

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
