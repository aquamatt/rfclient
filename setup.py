from setuptools import setup, find_packages

setup(
    name="rfclient",
    version="0.2.3",
    author="ReThought Ltd",
    author_email="code@rethought-solutions.com",
    url="https://github.com/aquamatt/rfclient",
    license="BSD",
    keywords="api",
    description="API to the RedFlash notification management system.",

    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
    ],
    packages=find_packages('.'),
    package_dir={'': '.'},
)
