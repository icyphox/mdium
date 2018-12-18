from setuptools import setup
from mdium import __version__

with open('readme.md') as f:
    long_description = f.read()

setup(
        author='Anirudh',
        author_email='icyph0x@pm.me',
        long_description=long_description,
        long_description_content_type='text/markdown',
        name='mdium',
        version=__version__,
        description='Publish your markdown to Medium, from the CLI',
        url='https://github.com/icyphox/mdium',
        license='MIT',
        packages=['mdium'],
        install_requires=[
            'python-frontmatter', 'requests',
            ],
        entry_points={
            'console_scripts': [
                'mdium = mdium.cli:main',
                ]
            },
)
