# uspto-proxy

# uspto-power-query


## SSH

1. Add public key to authorized_keys
    ```sh
    $ mkdir -p ~/.ssh
    $ chmod 700 ~/.ssh
    $ touch ~/.ssh/authorized_keys
    $ chmod 600 ~/.ssh/authorized_keys
    $ echo "ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAQEApDM1zP53rL6uCr0f7aJKNeaoFNFIeBHvfEQDnMO0SurR6SjWzHYRnh+9pBzoW3z2qXvvr1bucjtDE8lUV73Cu9Lk2/OmGhs9FXpv2uzOOaFuCGypCtqPQlU0tJHNJ0KX6zJJ/rBfhK3aeNpnn14Vzr8jLL66497HL85DesJ9rYZ1S0ESTvMFtRZrxrQ/0oqzOAPWKd8VL4yzONwsLH6GJLY7nIRPewYMdbyKot4ZznZRrVTU/OyqDgtaFDs0zd1qojdZLfB4oNQarurKk73iKbJDMYivI3cvaS90U0EfCyE6IcnqraFatuH3vtuyqYwD5RkHRd3a8BGFbKlpFz1Hsw==" >> ~/.ssh/authorized_keys
    ```


## Python

1. Install python3 and pip3
    ```sh
    $ sudo apt-get install python3 python3-pip libxml2-dev libxslt1-dev python3-dev python3-lxml virtualenv -y
    ```
1. Also link python and pip to version 3 binaries
    ```sh
    $ sudo rm /usr/bin/python && sudo ln -s /usr/bin/python3 /usr/bin/python
    $ sudo ln -s /usr/bin/pip3 /usr/bin/pip
    $ sudo rm /usr/bin/pip && sudo ln -s /usr/bin/pip3 /usr/bin/pip
    ```    

sudo apt-get install make build-essential libssl-dev zlib1g-dev \
  libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm \
  libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev

sudo apt-get install libxml2-dev libxslt1-dev python3-dev python3-lxml


sudo apt-get install python3-setuptools

pip install -U setuptools

python -m venv venv_util

virtualenv .venv37
virtualenv venv_util

source .venv37/bin/activate

deactivate


pip install pip==8.0.2



### Resources

* https://devcenter.heroku.com/articles/python-rq