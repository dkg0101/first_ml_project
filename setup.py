from setuptools import setup,find_packages
from typing import List






PROJECT_NAME = "Housing Predictor"
VERSION = "0.0.2"
AUTHOR = "Dhananjay Gurav"
DESCRIPTION = 'This is first FSDS batch Machine Learning Project'
PACKAGES =['housing']
REQUREMENT_FILE_NAME = "requirements.txt"


def get_requirements_list()-> List[str]:
    """
    Description: This function is going to return list of requirement
    mention in requirements.txt file

    return This function is going to return a list which will conttain mean of libraries 
    mentioned in requirements.txt file
    """
    with open(REQUREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines().remove("-e .")

setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    packages=find_packages(), 
    install_requires=get_requirements_list()
    

)



if __name__=="__main__":
    print(get_requirements_list())