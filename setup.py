from setuptools import setup, find_namespace_packages

# -- Apps Definition -- #
app_package = 'django_param'
release_package = app_package

# -- Python Dependencies -- #
dependencies = ['pytest-django', 'pytest']

setup(
    name=release_package,
    version='0.0.1',
    description='',
    long_description='',
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
