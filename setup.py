# responsible for creating ml projects as a package 
# use this package in my entire application
# even deploy in a pypi.
from typing import List
from setuptools import find_packages,setup 

HYPHEN_E_DOT='-e .'


def get_requirements(file_path:str)->List[str]:
    '''
    this func will return the list of requirements
    '''
    requirements=[]
    # with open closes the file for us
    with open(file_path) as file_obj:
        requirements=file_obj.readlines() #when we read lines then it will add on /n new lines
        requirements=[req.replace("\n","") for req in requirements]
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements
setup(
name="mlproject",
version="0.0.1",
author="shreya",
author_email="shreyathakuri1372@gmail.com",
packages=find_packages(),
install_requires=get_requirements('requirements.txt')
)