# myDjangoApp :metal:

[![Build Status](https://travis-ci.org/vincedgy/myDjangoApp.svg?branch=master)](https://travis-ci.org/vincedgy/myDjangoApp)

Python 2.7 & 3.6 (managed through virtualenv)

## Objectives

Discover Django framework and build an MVP app with no fancy integration for now.

## Features

- Simple webApp with few features
- Django uses SQLite3 locally for managing sessions and users
- Deployement made on AWS BeanStalk

## Deployement on AWS Beanstalk

### Install AWS ElasticBeanstalk CLI

```bash
pip install --upgrade --user awsebcli

alias eb='~/Library/Python/2.7/bin/eb'
export eb

eb init -p python2.7 myDjangoApp -region eu-west-1

aws elasticbeanstalk describe-applications

eb create django-env

aws elasticbeanstalk describe-environments

eb deploy
```

### Reference :

#### AWS Beanstalk
* Step by step tutorial : <br> [http://docs.aws.amazon.com/fr_fr/elasticbeanstalk/latest/dg/create-deploy-python-django.html](http://docs.aws.amazon.com/fr_fr/elasticbeanstalk/latest/dg/create-deploy-python-django.html)

#### Tooling

* BPython : *incredible* useful python shell interpretor <br>
[https://bpython-interpreter.org/](https://bpython-interpreter.org/)

* selenium : automatic testing with ChromeDriver
    - [https://chromedriver.storage.googleapis.com/2.29/chromedriver_mac64.zip](https://chromedriver.storage.googleapis.com/2.29/chromedriver_mac64.zip)
    - [https://sites.google.com/a/chromium.org/chromedriver/getting-started](https://sites.google.com/a/chromium.org/chromedriver/getting-started)
    
##### CI/CD with Jenkins

- Jenkins installation<br>
visit [https://jenkins.io/](https://jenkins.io/), you gonna need a local installation 

