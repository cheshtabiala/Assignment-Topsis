from setuptools import setup, find_packages

DESCRIPTION = 'Implementation of Topsis'

try:
    with open('README.md', 'r', encoding='utf-8') as f:
        long_description = f.read()
except FileNotFoundError:
    long_description = DESCRIPTION

VERSION = '1.0.0'

setup(
    name="Topsis-CheshtaBiala-102103545",
    version=VERSION,
    author="Cheshta Biala",
    author_email="cbiala_be21@thapar.edu",
    license='MIT License',
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=['pandas', 'numpy'],
    project_urls={
        'Project Link': 'https://github.com/cheshtabiala/Assignment-Topsis'
    },
    keywords=['Topsis', 'Topsis-CheshtaBiala-102103545', 'Cheshta', 'Topsis-Cheshta', '102103545'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
    ]
)
