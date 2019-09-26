FROM ubuntu:18.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update -y && apt-get install -y \
    python3 \
    python3-pip \
    python3-sphinx \
    texlive \
    wget \
    git \
    locales \
    language-pack-ja \
    && rm -rf /var/lib/apt/lists/* /var/cache/apt/archives/* \
    && echo "ja_JP.UTF-8 UTF-8" > /etc/locale.gen \
    && locale-gen

ENV LC_ALL=ja_JP.UTF-8
ENV LANG=ja_JP.UTF-8
ENV LANGUAGE=ja_JP.UTF-8
ENV PYTHONIOENCODING=utf-8

RUN wget https://github.com/jgm/pandoc/releases/download/1.19.2.1/pandoc-1.19.2.1-1-amd64.deb \
    && dpkg -i pandoc-1.19.2.1-1-amd64.deb

RUN pip3 install nbsphinx recommonmark sphinx_rtd_theme beautifulsoup4 ipython jupyter