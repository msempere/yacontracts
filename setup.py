import os
from setuptools import setup



description = (
'YAContracts: Yet Another contracts package')

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

long_description = 'YAContracts: Yet Another contracts package'


def get_version(filename):
    import ast
    version = None
    with open(filename) as f:
        for line in f:
            if line.startswith('__version__'):
                version = ast.parse(line).body[0].value.s
                break
        else:
            raise ValueError('No version found in %r.' % filename)
    if version is None:
        raise ValueError(filename)
    return version

version = get_version(filename='src/__init__.py')


setup(name='yacontracts',
      author="MSempere",
      author_email="msempere@gmx.com",
      url='http://msempere.github.com/yacontracts/',

      description=description,
      long_description=long_description,
      keywords="type checking, value checking, contracts",
      license="MIT",

      classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Quality Assurance',
        'Topic :: Software Development :: Testing'
      ],

      version=version,
      download_url='http://github.com/msempere/yacontracts/tarball/%s' % version,

      package_dir={'':'src'},
      packages=[''],
      install_requires=['setuptools'],
      tests_require=['pytest'],
      entry_points={},
)
