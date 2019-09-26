FROM nvidia/cuda:10.1-cudnn7-devel-ubuntu18.04

ARG CHAINER_VERSION=5.4.0
ARG CUPY_VERSION=5.4.0
ARG NUMPY_VERSION=1.16.5

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update -y && \
    apt-get install -y --no-install-recommends \
    wget \
    python3 \
    python3-dev

RUN wget https://bootstrap.pypa.io/get-pip.py \
    && python3 get-pip.py \
    && rm -rf get-pip.py

RUN pip install \
    chainer==${CHAINER_VERSION} \
    cupy-cuda101==${CUPY_VERSION} \
    numpy==${NUMPY_VERSION}

RUN pip install nbsphinx recommonmark sphinx_rtd_theme beautifulsoup4 ipython jupyter

RUN pip install matplotlib pandas scipy seaborn