# myDjangoApp

Python 2.7 (for now !)

## Objectives

Discover Django framework and build an MVP app with no fancy integration for now.

## Features

- Simple webApp with few features
- Django uses SQLite3 locally for managing sessions and users
- Deployement made on AWS BeanStalk

## Deployement on AWS Beanstalk

### Install AWS ElasticBeanstalk CLI

```
pip install --upgrade --user awsebcli

alias eb='~/Library/Python/2.7/bin/eb'
export eb

eb init -p python2.7 myDjangoApp

aws elasticbeanstalk describe-applications

eb create django-env

aws elasticbeanstalk describe-environments
```

Reference :

* [http://docs.aws.amazon.com/fr_fr/elasticbeanstalk/latest/dg/create-deploy-python-django.html](http://docs.aws.amazon.com/fr_fr/elasticbeanstalk/latest/dg/create-deploy-python-django.html)

