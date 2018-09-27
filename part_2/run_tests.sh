source ./venv/bin/activate && \
pip install -r requirements.txt && \
nosetests test/ --with-coverage && \
deactivate
