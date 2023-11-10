from setuptools import find_packages,setup

HYPHEN_E_DOT = "-e ."

def get_requirements(filepath:str):

    """ Reads and get all packages in requirement.txt file

    ARGS: filepath of requiremets.txt 
    return as str format    
    
    """


    requirements = []

    with open(filepath) as filepath_obj:
        requirements = filepath_obj.readlines()
        requirements = [req.replace("/n","") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements





setup(
    name= "Kideny_Disease_Classification",
    version= "0.0.0",
    author="Sai Surya Chandra Prasad",
    author_email="saisuryachandraprasad@gmail.com",
    packages=find_packages(),
    install_requirement = get_requirements("requirements.txt")
)