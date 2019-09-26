import setuptools

with open("README.md","r") as fh:
    long_description = fh.read()

setuptools.setup(
        name="release_info",
        version="0.0.1",
        author="dev@ridereport.com",
        author_email="dev@ridereport.com",
        description="Build libraries for Ridereport",
        long_description = long_description,
        long_description_content_type="text/markdown",
        url="https://github.com/Ridereport/release-info",
        packages=setuptools.find_packages(),
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
            ],
        python_requires=">=3.7",
        )
