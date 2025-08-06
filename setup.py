import os
from setuptools import setup, find_packages

# User-friendly description from README.md
current_directory = os.path.dirname(os.path.abspath(__file__))
try:
    with open(os.path.join(current_directory, 'README.md'), encoding='utf-8') as f:
        long_description = f.read()
except Exception:
    long_description = ''

setup(
    # Name of the package
    name='diseaseSpreadSimulator',
    # Packages to include into the distribution
    packages=find_packages('.'),
    # Version
    version='1.0.0',
    # License
    license='MIT',
    # Short description of your library
    description='A repository to simulate the spread of an infectious disease.',
    # Long description of your library
    long_description=long_description,
    long_description_content_type='text/markdown',
    # Your name
    author='G/Ker(f)≅Im(f)',
    # Project URL
    url='https://github.com/AlgAlg01/diseaseSpreadSimulator',
    # Download URL (usually a tagged release)
    download_url='https://github.com/AlgAlg01/diseaseSpreadSimulator/archive/refs/tags/v1.0.0.tar.gz',
    # List of keywords
    keywords=['simulation', 'epidemiology', 'infectious disease', 'modeling', 'python'],
    # List of packages to install with this one
    install_requires=[
        "matplotlib>=3.10.5",
		"networkx>=3.4.2"
    ],
    # Classifiers
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
    ]
)
