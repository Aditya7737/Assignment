FROM python:3.9
WORKDIR /opt/source-code/
COPY . /opt/source-code/
RUN pip install -r requirements.txt
RUN python Loading_the_model_&_Flask_code.py