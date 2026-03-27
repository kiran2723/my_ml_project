from setuptools import find_packages, setup
from typing import List

# Constant to trigger the editable install of the package itself
HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    '''
    This function returns the list of requirements from a file.
    '''
    requirements = []
    with open(file_path) as file_obj:
        # Read lines and strip newline characters
        requirements = [req.replace("\n", "") for req in file_obj.readlines()]

        # Remove the editable trigger if present in requirements.txt
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
            
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Kiran Patil',
    author_email='ml.kiranpatil@gmail.com',
    packages=find_packages(),
    # Use the function to dynamically load requirements
    install_requires=get_requirements('requirements.txt'), 
)