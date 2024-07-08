from setuptools import setup, find_packages
import os

print("Current Directory:", os.getcwd())
print("Included Packages:", find_packages())
#print("Files in cfg Directory:", os.listdir('cfg'))

setup(
    name='CopyCraftAPI',
    version='0.5.0',
    packages=find_packages() + ['CopyCraftAPI.cfg'],
    include_package_data=True,
    package_data={
        'CopyCraftAPI': ['CopyCraftAPI/cfg/**/*']
    },
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
