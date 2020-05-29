import setuptools


# Long description
with open('README.md', 'r') as fh:
    long_description = fh.read()


# Requirements
def get_requirements():
    return [
        'selenium>=3.14',
        'pillow>=7.1.2',
        'webdriver-manager>=2.5.2'
    ]


setuptools.setup(
    name="tweetshot",
    version="0.0.1",
    author="Antonio Verdone",
    author_email="averdones@gmail.com",
    description="Take a tweet screenshot",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/averdones/tweetshot",
    packages=setuptools.find_packages(),
    install_requires=get_requirements(),
    entry_points={
        "console_scripts": ["tweetshot=tweetshot.cli_scripts:main"]},
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords="keyframes iframes video extractor",
    python_requires=">=3.6"
)
