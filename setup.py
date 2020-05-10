from setuptools import setup

setup(
    name='downloader',
    version="0.1.0",
    packages=["downloader"],
    auhtor="abderrahman elasri",
    entry_points = {
        'console_scripts': [
            'downloader = downloader.__main__:main'
        ]
    }
)