#!/bin/sh

yum -y install sudo

# Needed for Python 2.7.5 installation
yum -y install patch

yum -y install gcc libffi-devel python-devel openssl-devel
yum -y install python-setuptools python-setuptools-devel

# easy_install of pip without a version specifier fails on older Oracle Linux and CentOS versions because
# they have Python 2.6 installed by default and pip >= 10 has dropped support for Python 2.6. Pinning to
# a specific pip version avoids issues for now
easy_install pip==9.0.3
pip install --upgrade pip   # WARNING: pip 18 will not work with python 2.6

# Needed for PyEnv installation
yum -y install git-all readline bzip2 sqlite zlib-devel bzip2-devel readline-devel sqlite-devel openssl-devel xz xz-devel

# Needed since we use make in the script to construct the wheel
yum -y install make

yum -y install git
yum -y install tar
yum -y install which
yum -y install openssl

echo "Install pyenv and virtualenv"
curl -L https://raw.githubusercontent.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash
pip install virtualenv
export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv init --path)"
eval "$(pyenv virtualenv-init -)"
# pyenv update
pyenv --version

pyenv install 2.7.5 -s
pyenv install 3.6.5 -s

# one-time
pyenv shell 3.6.5
#pip install --upgrade pip
pyenv virtualenv --copies 3.6.5 cli-3
pyenv shell 2.7.5

echo 'export PATH="$HOME/.pyenv/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init -)"' >> ~/.bashrc
echo 'eval "$(pyenv init --path)"' >> ~/.bashrc
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc
