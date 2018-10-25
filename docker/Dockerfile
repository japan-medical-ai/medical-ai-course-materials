FROM nvidia/cuda:9.2-cudnn7-devel-ubuntu16.04

RUN apt-get update -y && \
    apt-get install -y --no-install-recommends \
    ffmpeg \
    curl \
    git \
    build-essential \
    gfortran \
    nasm \
    tmux \
    sudo \
    openssh-client \
    libgoogle-glog-dev \
    rsync \
    wget \
    cmake \
    automake \
    libgmp3-dev \
    cpio \
    libtool \
    libyaml-dev \
    realpath \
    valgrind \
    software-properties-common \
    unzip \
    libz-dev \
    vim \
    emacs \
    zsh \
    locales \
    python \
    python-dev \
    python-pip \
    python-pip \
    python-wheel \
    python-setuptools \
    python3 \
    python3-dev \
    python3-pip \
    python3-wheel \
    python3-setuptools \
    libibverbs-dev \
    libibumad-dev \
    libmlx4-1 \
    infiniband-diags \
    ibverbs-utils \
    perftest && \
    rm -rf /var/lib/apt/lists/* /var/cache/apt/archives/* && \
    echo "en_US.UTF-8 UTF-8" > /etc/locale.gen && locale-gen
ARG GROUP_ID=51000
RUN addgroup --gid ${GROUP_ID} fulltime

# Install OpenMPI with cuda & verbs
RUN mkdir /root/lib && cd /root/lib && \
    curl -L -O https://download.open-mpi.org/release/open-mpi/v3.1/openmpi-3.1.1.tar.gz && \
    tar zxvf openmpi-3.1.1.tar.gz && rm -rf openmpi-3.1.1.tar.gz && \
    cd openmpi-3.1.1 && \
    ./configure --with-cuda --with-verbs && \
    make -j8 install

ARG USER_ID=1000
ARG USER_NAME=ubuntu
RUN mkdir -p /home/${USER_NAME}
RUN useradd -d /home/${USER_NAME} -g ${GROUP_ID} -u ${USER_ID} ${USER_NAME}
RUN chown ${USER_NAME}:root /home/${USER_NAME}
RUN chsh -s /usr/bin/zsh ${USER_NAME}
USER ${USER_NAME}
WORKDIR /home/${USER_NAME}
ENV HOME /home/${USER_NAME}

# Install oh-my-zsh
RUN git clone https://github.com/robbyrussell/oh-my-zsh.git ~/.oh-my-zsh && \
    cp ~/.oh-my-zsh/templates/zshrc.zsh-template ~/.zshrc

# Install pyenv
RUN git clone https://github.com/pyenv/pyenv.git ~/.pyenv && \
    echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc && \
    echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc && \
    echo 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.zshrc
ENV PYENV_ROOT $HOME/.pyenv
ENV PATH $PYENV_ROOT/bin:$PATH
RUN eval "$(pyenv init -)"

# Install miniconda3-4.3.0
RUN pyenv install miniconda3-4.3.30 && \
    pyenv global miniconda3-4.3.30 && \
    pyenv rehash

RUN CONDA=$(pyenv which conda) && \
    PIP=$(pyenv which pip) && \
    $PIP install -U pip && \
    $PIP install PyHamcrest && \
    $CONDA install -y numpy scipy scikit-learn jupyter matplotlib cython protobuf pandas h5py

ENV LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/lib
ENV LIBRARY_PATH=$LIBRARY_PATH:/usr/local/lib
ENV CPATH=$CPATH:/usr/local/include
RUN echo 'export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/lib' >> ~/.zshrc && \
    echo 'export LIBRARY_PATH=$LIBRARY_PATH:/usr/local/lib' >> ~/.zshrc && \
    echo 'export CPATH=$CPATH:/usr/local/include' >> ~/.zshrc

RUN PIP=$(pyenv which pip) && \
    $PIP install mpi4py && \
    $PIP install chainer==5.0.0b4 && \
    $PIP install cupy-cuda92==5.0.0b4 && \
    $PIP install chainermn==1.3.0 && \
    $PIP install chainercv==0.10.0 && \
    $PIP install jupyterthemes && \
    JT=$(pyenv which jt) && \
    $JT -f dejavu -T -N && \
    $PIP install xlrd && \
    $PIP install imageio && \
    $PIP install tqdm && \
    $PIP install pyyaml
