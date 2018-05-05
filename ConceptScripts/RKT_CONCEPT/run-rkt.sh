rkt run --interactive \
        --volume=data,kind=host,source=$PWD\
        --mount volume=data,target=/data \
        quay.io/coreos/alpine-sh