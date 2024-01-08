# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['isx']

package_data = \
{'': ['*']}

install_requires = \
['beartype>=0.15.0', 'importlib-metadata>=7.0.1,<8.0.0', 'numpy>=1.26.2']

extras_require = \
{':extra == "docs"': ['mkdocs>=1.4.2,<2.0.0'],
 'dev': ['ipykernel>=6.20.1',
         'debugpy==1.6',
         'matplotlib>=3.8.2',
         'poetry2setup>=1.1.0,<2.0.0'],
 'docs': ['mkdocs-material-extensions>=1.1.1,<2.0.0',
          'mkdocs-material>=9.0.9,<10.0.0',
          'mkdocstrings>=0.24.0,<0.25.0',
          'mkdocstrings-python>=1.7.5,<2.0.0'],
 'test': ['pytest>=7.2.0',
          'coverage>=7.3.2',
          'poetry2setup>=1.1.0,<2.0.0',
          'requests>=2.31.0,<3.0.0']}

setup_kwargs = {
    'name': 'isx',
    'version': '1.0.0',
    'description': ' Python-based ISXD file reader',
    'long_description': '# py_isx\n\nExperimental pure-python API to read ISXD files. Please note \nthat this is a work in progress and not feature complete. \nUse at your own risk. \n\n## Support\n\n|  File type | Support |\n|  --------- | ------- |\n| CellSet   | ✅ |\n| Movie   | ✅ |\n| Events   | ❌ |\n| VesselSet   | 🚧 |\n| GPIO files   | ❌ |\n| IMU files   | ❌ |\n\n## Installation\n\n### Poetry\n\n```bash\npoetry add https://github.com/inscopix/py_isx\n```\n\n### pip\n\n\n```bash\npip install git+https://github.com/inscopix/py_isx.git@main\n```\n\n## Testing\n\nThis code is tested using GitHub Actions on the following python\nversions:\n\n- 3.9\n- 3.10\n- 3.11\n',
    'author': 'Srinivas Gorur-Shandilya',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)

