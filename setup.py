from setuptools import setup

def readme():
      with open('README.md') as f:
            return f.read()

setup(name='gitissue',
      version='0.0.1',
      description='Integrated issue handler',
      long_description=readme(),
      packages=['gitissue'],
      entry_points = {
            'console_scripts': ['git-map=gitissue.command_line:main'],
      },
      classifiers=[
            'Development Status :: 3 - Alpha',
            'Intended Audience :: Developers',
            'Programming Language :: Python :: 3',
      ],
      url='https://github.com/PJSoftware/git-issue',
      author='Peter Jones',
      author_email='pjsoftware@petesplace.id.au',
      include_package_data=True,
      zip_safe=False)
