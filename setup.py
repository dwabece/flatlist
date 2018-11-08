import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="flatlist",
    version="0.0.1",
    author="MJ Krakowski",
    author_email="mjk@c40.pl",
    description="Recursively flattens a list of any depth. Made just to check pypi ;)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: WTFPL-2.0",
        "Operating System :: OS Independent",
    ],
)