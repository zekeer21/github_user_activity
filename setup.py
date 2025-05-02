from setuptools import setup, find_packages

setup(
    name="github-activity",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["requests"],
    entry_points={
        "console_scripts": [
            "github-activity=github_activity.cli:main",
        ],
    },
    author="Zeke Achas",
    author_email="achas241@gmail.com",
    description="A CLI tool to fetch GitHub user activity",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/zekeer21/github_user_activity",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
