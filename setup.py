#!/usr/bin/env python

from setuptools import setup

if __name__ == '__main__':

    setup(
        name='localstack-client',
        version='0.5',
        description='A lightweight python client for LocalStack.',
        author='Jeff Wu, Waldemar Hummer',
        author_email='jeffrey.yung.wu@gmail.com, waldemar.hummer@gmail.com',
        url='https://github.com/localstack/localstack-python-client',
        packages=['localstack_client'],
        package_data={},
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
