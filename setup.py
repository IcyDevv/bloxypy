import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="bloxy", 
    version="1.2.2",
    author="Icy",
    author_email="icydevv026@gmail.com",
    description="A modern & simple to use API wrapper that handles ROBLOX interactions.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/IcyDevv/bloxy.py",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
