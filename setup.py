from setuptools import setup, find_packages

setup(
    name="weary",
    version='2.3',
    py_modules=['path_finder'],
    # packages=find_packages(include=['.']),
    install_requires=[
        'click==7.1.2',
        'nose==1.3.7',
        'pytest==5.4.3',
    ],
    entry_points='''
        [console_scripts]
        weary=path_finder:find_path
    ''',
)
