from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="aether-cli",
    version="0.1.0",
    author="AirTouch666",
    author_email="me@airtouch.top",
    description="A command-line interface for interacting with various AI models.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AirTouch666/aether",
    project_urls={
        "Bug Tracker": "https://github.com/AirTouch666/aether/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(),
    python_requires=">=3.7",
    install_requires=[
        "click",
        "openai",
        "google-generativeai",
        "aiohttp",
        "websockets",
        "requests",
        "halo",
        "certifi"
    ],
    entry_points={
        "console_scripts": [
            "ask=aether.cli:main",
        ],
    },
) 