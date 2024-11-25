from setuptools import setup, find_packages

with open("README.md", "r") as fh:
  long_description = fh.read()

setup(
  name="RFAccess",
  version="1.0.1",
  description="A library for communicating to LLRP compliant RFID readers.",
  long_description=long_description,
  long_description_content_type="text/markdown",
  author="Dylan Gillespie",
  author_email="dylantannergillespie@gmail.com",
  url="https://github.com/DTGillespie/RFAccess",
  packages=find_packages(),
  include_package_data=True,
  install_requires=[],
  classifiers=[
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
  ],
  python_requires=">=3.6",
)
