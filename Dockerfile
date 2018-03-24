FROM python:3

ADD JenkinsConfiguration.py /
ADD JenkinsUtils.py /
ADD requirements.txt /


RUN pip install -r requirements.txt
RUN python  --version

ENTRYPOINT ["python", "JenkinsUtils.py" ]

