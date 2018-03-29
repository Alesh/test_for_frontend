from setuptools import setup, find_packages

setup(**{
    'name': 'test_for_frontend',
    'packages': find_packages(),
    'install_requires': [
        'tornado'
    ]
})
