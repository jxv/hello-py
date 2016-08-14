try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Hello',
    'author': 'jxv',
    'url': 'github.com/jxv/hello-py.',
    'download_url': 'github.com/jxv/hello-py',
    'author_email': 'github.com/jxv',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['Hello'],
    'scripts': [],
    'name': 'hello'
}

setup(**config)
