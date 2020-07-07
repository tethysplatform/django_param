from setuptools import setup, find_namespace_packages

# -- Apps Definition -- #
app_package = 'django_param'
release_package = app_package

# -- Python Dependencies -- #
dependencies = ['pytest-django', 'pytest']

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name=release_package,
    version='0.0.1',
    description='',
    # other arguments omitted
    long_description=long_description,
    long_description_content_type='text/x-rst',
    keywords='',
    author='Aquaveo',
    author_email='',
    url='',
    license='',
    packages=find_namespace_packages(),
    package_data={},
    include_package_data=True,
    zip_safe=False,
    install_requires=dependencies,
    test_suite='tests'
)
