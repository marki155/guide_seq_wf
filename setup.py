#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

requirements = [line.strip() for line in open('requirements.txt')]

setup(
    name='guideseq_wf',
    version='1.0.0',
    description="An easy to use bioinformatic pipeline for the GUIDE-seq assay.",
    author="based on work from Shengdar Q Tsai, Martin Aryee, Ved V Topkar, extended by Lukas Heumos",
    author_email='STSAI4@mgh.harvard.edu, Aryee.Martin@mgh.harvard.edu, vedtopkar@gmail.com, lukas.heumos@posteo.net',
    url='https://github.com/Zethson/guide_seq_wf',
    scripts=['scripts/guideseq'],
    install_requires=requirements,
    license="AGPL",
    keywords='guideseq',
    classifiers=[
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Topic :: Scientific/Engineering :: Visualization',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Operating System :: Unix',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7'
    ]
)
