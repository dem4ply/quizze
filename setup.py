try:
    from setuptools import setup, find_packages
except:
    from distutils.core import setup, find_packages

setup(
    name='quizze',
    version='1.0',
    description='',
    license='',
    author='',
    author_email='',
    packages=find_packages(),
    install_requires=[],
    dependency_links=[],
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Programming Language :: Python', ] )
