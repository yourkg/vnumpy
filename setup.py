# setup.py
from setuptools import setup, find_packages

setup(
    name='vnumpy', 
    version='0.1.4', 
    packages=find_packages(), 
    include_package_data=True, 
    package_data={
        'vnumpy': ['v_dll/*.dll'], 
    },
    description='vision numpy',  
    long_description=open('README.md').read(),  
    long_description_content_type='text/markdown',  
    author='yourkg',  
    author_email='mail@yourkg.com', 
    url='https://github.com/yourkg/vnumpy',  
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  
)
