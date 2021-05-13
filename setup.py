import setuptools

with open("VERSION", "r") as f:
    version = f.read().strip()

setuptools.setup(
    name="ircflags",
    version=version,
    author="examknow",
    author_email="me@zpld.me",
    description="easy IRC bot access control",
    url="https://github.com/examknow/ircflags",
    packages=setuptools.find_packages(),
    package_data={"ircflags": ["py.typed"]},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Operating System :: POSIX",
        "Operating System :: Microsoft :: Windows"
    ],
    python_requires='>=3.6',
)
