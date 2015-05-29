from setuptools import setup, find_packages
import os

version = '0.1.3.maven'


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

long_description = ''
#long_description = (
    #read('README.txt')
    #+ '\n' +
    #read('js', 'jquery', 'test_jquery.txt')
    #+ '\n' +
    #read('CHANGES.txt'))

setup(
    name='twitter_bootstrap',
    version=version,
    description="Twiter Bootstrap library with Maven modifications.",
    long_description=long_description,
    classifiers=[],
    keywords='',
    #author='vsobol',
    #author_email='vsobol@maven.co',
    #url='https://bitbucket.org/fanstatic/js.jquery',
    license='BSD',
    packages=find_packages(),
    #namespace_packages=['twitter_bootstrap'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'fanstatic',
        'setuptools',
    ],
    entry_points={
        'fanstatic.libraries': [
            'twitter_bootstrap = twitter_bootstrap:library',
        ],
    },
)
