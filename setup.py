from setuptools import setup, find_packages
from codecs import open
import os


def read(filename):
    return open(os.path.join(os.path.dirname(__file__), filename)).read()


setup(name="security-git-hooks",
      author="HRMC Platform Security",
      description="Detect secrets prior to commit",
      url="https://github.com/hmrc/security-git-hooks/",
      long_description=read("README.md"),
      entry_points={
          "console_scripts": ["security-git-hooks-filecontent = security_git_hooks.secrets_filecontent:main",
                              "security-git-hooks-filename = security_git_hooks.secrets_filename:main"]
      },
      packages=find_packages(),
      install_requires=['PyYAML'],
      package_data={
          '': ['conf.yaml',],
      },
      )