# whitepaper

## Start virtual environment

    $ virtualenv -p python3 venv
    $ ./venv/bin/activate
    $ pip install -r requirements.txt

## Start tika server with docker

    $ docker pull logicalspark/docker-tikaserver # only on initial download/update
    $ docker run --rm -p 9998:9998 logicalspark/docker-tikaserver

## Start jupyter notebook

    $ jupyter notebook