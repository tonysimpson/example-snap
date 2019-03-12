import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="treemaker",
    version="0.0.1",
    author="Tony Simpson",
    author_email="agjasimpson@gmail.com",
    description="Prints command line trees",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tonysimpson/example-snap",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
