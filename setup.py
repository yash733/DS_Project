from setuptools import find_packages, setup
#for making the get_requirements outputformat ``List`` work we will call
from typing import List

def get_requirements(file_path:str)-> List[str]:

      '''this will return the list of requirements'''
      require=[]
      with open(file_path) as file_read:
            require=file_read.readlines()
            #['python\n'...] \n will come now need to remove it

            require=[i.replace("\n","")for i in require]

            if "-e ." in require:
                  require.remove("-e .")
      return require

setup(name="DS ETE Project",
      version="0.0.1",
      description="This is my fist end to end project",
      author_email="yash733622@gmail.com",
      author="Yash gupta",
      packages=find_packages(),
      #install_requires=["pandas","numpy","seaborn"]
      install_requires=get_requirements('requirements.txt')
      )