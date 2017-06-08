#!/usr/bin/env python

from setuptools import setup

if __name__ == '__main__':

    setup(
        name='localstack-client',
        version='0.1',
        description='A lightweight python client for localstack mocking.',
        author='Jeff Wu',
        author_email='jeffrey.yung.wu@gmail.com',
        url='https://bitbucket.org/atlassian/localstack',
        custom_headers={
            'Authorization': None
        },
        packages=['localstack_client'],
        # TODO: include a localstack config for services and ports here.
        package_data={},
        # TODO: include the docker-compose.yml file here.
        data_files={},
        install_requires=["boto3"],
        license="Apache License 2.0",
        classifiers=[
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 2.6",
            "Programming Language :: Python :: 2.7",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.3",
            "License :: OSI Approved :: Apache Software License",
            "Topic :: Software Development :: Testing",
        ]
    )
