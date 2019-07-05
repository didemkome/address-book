from setuptools import setup
from address_book import VERSION

def readme():
      with open('README.md') as file:
            return file.read()

setup(name='Address Book',
      version=VERSION,
      description='Simple Command-Line Address Book Application',
      long_description=readme(),
      classifiers=[
            "Programming Language :: Python :: 3.7",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent", 
      ],
      author='Didem Nursal Kome',
      author_email='didemkome@gmail.com',
      url='https://github.com/didmkme/Address-Book',
      license='MIT',
      packages=['Address-book'],
      package_dir={'Address-book': 'D:\\Address-book'},
      package_data={'Address-book': ['Address-book\\*.db']},
      entry_points={
            'console_scripts': ['addressbook = addressbook.addressbook_cmd:main']
      },
      #include_package_data=True,
      zip_safe=False)