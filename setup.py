from setuptools import setup

setup(
    name='the-chosen',
    version='dev',
    packages=['the_chosen'],
    url='https://github.com/tifrueh/the-chosen',
    license='GPL-3.0',
    author='Timo Früh',
    author_email='timo.frueh@icloud.com',
    description='A short text-adventure',
    install_requires=['clear-screen~=0.1.14'],
    package_data={'the_chosen': ['resources/*']},
    entry_points={'console_scripts': ['the-chosen=the_chosen.__main__:main']}
)
