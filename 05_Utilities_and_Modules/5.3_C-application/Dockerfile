FROM gcc:4.9
COPY . /usr/src/my-c-application
WORKDIR /usr/src/my-c-application
RUN gcc -o my-c-application main.c
CMD ["./my-c-application"]