from setuptools import setup

setup(
    name='asyncbing',
    version='2.0.0',
    author='TennisBowling',
    author_email='tennisbowling@tennisbowling.com',
    packages=['asyncbing'],
    url='https://github.com/TennisBowling/asyncbing',
    license='LICENSE.md',
    description='A api wrapper for the bing apis.',
    long_description_content_type='text/markdown',
    long_description=open('README.md').read(),
    install_requires=[
        'aiohttp',
        'asyncio',
    ],
)
