from setuptools import setup, find_packages

setup(
    name='line_notify',
    version='0.1.4',
    description='A Simple Wrapper for LINE Messenger Notify',
    license='MIT',
    author='Jin Kim',
    author_email='golbin@gmail.com',
    url='https://github.com/golbin/line-notify',
    keywords=['line', 'notify'],
    install_requires=[
        'requests'
    ],
    packages=find_packages(exclude=['tests']),
    long_description=open('README.md').read(),
    zip_safe=False
)
