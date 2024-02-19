from setuptools import setup, find_packages

setup(
    name='nyt_assignment',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # List your dependencies here
        'requests',
        'matplotlib',
        'pyyaml',
        'pandas',
        'wordcloud'
    ],
    entry_points={
        'console_scripts': [
            'nyt_assignment = nyt_assignment.nyt_assignment:main',
        ],
    },
    author='Andre Delaney',
    author_email='andre.delaney@gmail.com',
    description='Package for analysis of NYT articles',
    long_description='Package for analysis of NYT articles. Calculates mean of word count nad produces a plot',
    url='https://github.com/ASDelaney/nyt_assignment',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)