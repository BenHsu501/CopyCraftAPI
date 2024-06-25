from setuptools import setup, find_packages
###
setup(
    name='CopyCraftAPI',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'openai'
    ],
    entry_points={
        'console_scripts': [
            'copycraft=CopyCraftAPI.cli.main:main'
        ],
    },
    author="Ben Hsu",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/BenHsu501/CopyCraftAPI",
)