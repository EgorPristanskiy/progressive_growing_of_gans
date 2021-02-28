from setuptools import setup
from pip_utils.req import parse_requirements

# TODO solve problem with author
setup(
    name             = 'pcgan',
    install_requires = parse_requirements("requirements-pip.txt"),
    version          = '0.1',
    packages         = ['pcgan'],
    package_dir      = {'pcgan': 'pcgan/',},
    url              = 'https://github.com/tkarras/progressive_growing_of_gans',
    author           = 'Tero Karras',
    author_email     = 'tkarras@nvidia.com',
    zip_safee        = False,
)
