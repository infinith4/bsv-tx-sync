# bsv-tx-sync
synchronize bsv transaction

python3 -m venv .venv
source .venv/bin/activate
pip3 install pipenv

pipenv --python 3.7
pipenv install pymongo
pipenv install dnspython~=1.16.0

## restore from pipfile
 
pipenv install


## Start

pipenv run start

