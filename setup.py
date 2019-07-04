from setuptools import setup

setup(name='Address Book',
      version='1.0',
      description='Simple Command-Line Address Book Application',
      classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent", 
      ],
      author='Didem Nursal Kome',
      author_email='didemkome@gmail.com',
      url='https://github.com/didmkme/Address-Book',
      packages=['Address-book'],
      package_dir={'Address-book': 'D:\Address-book'},
      package_data={'Address-book': ['Address-book\*.db']},
     )