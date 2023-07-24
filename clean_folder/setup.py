from setuptools import setup, find_packages
setup(
    name='clean_folder',
    version='1.0.0',
    description='Very useful code for cleaning',
    url='https://github.com/vrnks/goit-homework-06',
    author='Veronika',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'clean-folder = clean_folder.clean_folder.clean:main'
        ]
    }
)