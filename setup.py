from setuptools import find_packages,setup

setup(
    name='mcqgenrator',
    version='0.0.1',
    author='suresh kumar',
    author_email='suresh.dev.ms@gmail.com',
    install_requires=["openai","langchain","streamlit","python-dotenv","PyPDF2", "pandas", "langchain-community"],
    packages=find_packages()
)