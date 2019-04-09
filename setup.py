#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

version='1.0.0'

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='guideseq_wf',
    version=version,
    description="An easy to use bioinformatic pipeline for the GUIDE-seq assay.",
    long_description=readme,
    author="based on work from Shengdar Q Tsai, Martin Aryee, Ved V Topkar, extended by Lukas Heumos",
    author_email='STSAI4@mgh.harvard.edu, Aryee.Martin@mgh.harvard.edu, vedtopkar@gmail.com, lukas.heumos@posteo.net',
    url='https://github.com/Zethson/guide_seq_wf',
    scripts=['scripts/guideseq'],
    install_requires=required,
    include_package_data=True,
    packages=find_packages(),
    license=license,
    keywords='guideseq'
)



