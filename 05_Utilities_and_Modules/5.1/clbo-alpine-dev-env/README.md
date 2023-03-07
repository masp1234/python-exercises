# clbo-alpine-dev-env

Repository used for Docker and requirements teachings



Clone this repository:

````
  git clone https://github.com/python-elective-kea/clbo-alpine-dev-env.git

````

Change directory

````
  cd clbo-alpine-dev-env/
````

Build the image:

````
  docker build --tag clbo/python:latest
````

Run the container:


````
  docker run -it --rm -v${PWD}:/docs clbo/python 
````
