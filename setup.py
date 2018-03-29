from setuptools import setup, find_packages

setup(**{
    'name': 'test_backend',
    'packages': find_packages(),
    'install_requires': [
        'tornado'
    ]
})
