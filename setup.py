import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="bloxapi", 
    version="0.0.1",
    author="dareal",
    author_email="sikling247@gmail.com",
    description="A modern & simple to use API wrapper that handles ROBLOX interactions.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/darealzz/bloxapi",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)