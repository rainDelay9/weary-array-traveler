from setuptools import setup

setup(
    name="wearypath",
    version='2.3',
    py_modules=['path_finder'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        wearypath=path_finder:find_path
    ''',
)