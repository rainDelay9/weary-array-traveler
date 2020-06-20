from setuptools import setup

setup(
    name="weary",
    version='2.3',
    py_modules=['path_finder'],
    install_requires=[
        'attrs==19.3.0',
        'click==7.1.2',
        'more-itertools==8.4.0',
        'nose==1.3.7',
        'packaging==20.4',
        'pluggy==0.13.1',
        'py==1.8.2',
        'pyparsing==2.4.7',
        'pytest==5.4.3',
        'six==1.15.0',
        'wcwidth==0.2.4',
        'weary'
    ],
    entry_points='''
        [console_scripts]
        weary=path_finder:find_path
    ''',
)