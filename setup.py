import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

REQUIREMENTS = [
    # Add your list of production dependencies here, eg:
    # 'requests == 2.*',
]

DEV_REQUIREMENTS = [
    'black == 22.*',
    'build == 0.7.*',
    'flake8 == 4.*',
    'isort == 5.*',
    'mypy == 0.942',
    'pytest == 7.*',
    'pytest-cov == 4.*',
    'twine == 4.*',
]

long_description = ''

setuptools.setup(
    name='100-movies-to-watch',
    version='1.0.0',
    description='Script generating txt file with list of 100 movies from empireonline.com',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='http://github.com/cinek5150/100-movies-to-watch',
    author='cinek5150',
    license='MIT',
    packages=setuptools.find_packages(
        exclude=[
            'examples',
            'test',
        ]
    ),
    package_data={
        '100-movies-to-watch': [
            'py.typed',
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=REQUIREMENTS,
    extras_require={
        'dev': DEV_REQUIREMENTS,
    },
    entry_points={
        'console_scripts': [
            '100-movies-to-watch=hundred_movies_to_watch.my_module:main',
        ]
    },
    python_requires='>=3.7, <4',
)
