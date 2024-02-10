from setuptools import find_packages, setup


def get_requirement(filepath):
    with open(filepath,"r") as f:
        req = f.read()
    req=req.split('\n')
    return req



setup(
    name="Finding Number Game",
    version="0.0.6",
    description="The game to find a computer generated number",
    author="Tarun",
    packages=find_packages(),
    install_requires=get_requirement('requirements.txt')
)

'''
if __name__ == "__main__":
    x=get_requirement('requirements.txt')
    print(x)
'''
