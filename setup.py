import os
from distutils.dist import Distribution

from setuptools import setup, find_packages

import versioneer

with open('README.md') as readme_file:
    README = readme_file.read()

with open('requirements.txt') as requirements_file:
    REQUIREMENTS = requirements_file.read().split("\n")

FORCE_BINARY = 'FORCE_BINARY' in os.environ

try:
    from wheel.bdist_wheel import bdist_wheel as _bdist_wheel

    class bdist_wheel(_bdist_wheel):

        def __init__(self, dist: Distribution):
            super().__init__(dist)

        def finalize_options(self):
            _bdist_wheel.finalize_options(self)
            # Mark us as not a pure python package
            self.root_is_pure = False

        def get_tag(self):
            python, abi, plat = _bdist_wheel.get_tag(self)
            print(f'Tag: {python} {abi} {plat}')
            return python, abi, plat
except ImportError:
    bdist_wheel = None

if FORCE_BINARY:
    print('Binary forced')

setup_args = dict(
    name='plugp100',
    version=versioneer.get_version(),
    install_requires=REQUIREMENTS,
    description='Controller for TP-Link Tapo P100 and other devices',
    long_description_content_type="text/markdown",
    long_description=README,
    license='GPL3',
    packages=find_packages(),
    author='@petretiandrea',
    author_email='petretiandrea@gmail.com',
    keywords=['Tapo', 'P100'],
    url='https://github.com/petretiandrea/plugp100',
    download_url='https://github.com/petretiandrea/plugp100',
    classifiers=[
        # 'Development Status :: 4 - Beta',
        'Development Status :: 5 - Production/Stable'
    ],
    cmdclass={
        **({'bdist_wheel': bdist_wheel} if FORCE_BINARY else {}),
        **versioneer.get_cmdclass()
    }
)

if __name__ == "__main__":
    setup(**setup_args)