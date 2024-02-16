from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    '''This function will return the list of requirements'''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n', '') for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

# Use correct file_path in the get_requirements call
requirements_list = get_requirements('requirements.txt')

setup(
    name='MLProjects',
    version='0.0.1',
    author='Avinash',
    author_email='Avinash12011994@gmail.com',
    packages=find_packages(),
    install_requires=requirements_list
)
