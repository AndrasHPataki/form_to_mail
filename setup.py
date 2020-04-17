from distutils.core import setup
setup(
  name = 'flask_extension_ftm',         
  packages = ['flask_extension_ftm'],   
  version = '1.5',      
  license='MIT',       
  description = 'Simple configuration system for mail, required for forms packages', 
  long_description="""
  #FORM TO MAIL (core Library)
  Pre-configured contact forms package system for sending MAIL
  **Description**

  Form to email is a new way to create contact forms in a few steps.
  Here are some advantages:

  1. Saves more than 25 lines of code

  2. Follows DOCKER style, where the user receives a package with pre-programmed formswith bootstrap4.

  3. Email routing with easy configuration

  4. Self-structured emails, with pre-defined body text.

  5. Data validation using TDD (Test Drive Development) concept

  6. Inserting only one variable, for all forms in your Html.

  7. You have complete freedom to edit your package, being able to make customizations.

  **This specific library is just the CORE for routing emails. The package form you download separately.**

  !!Follow the steps in the documentation to learn how to install Form-To-mail!!

  [README_DOCUMENTATION](https://form-to-mail.pataki.tech).

  This library is recommended to integrate with the forms package. 
  It works to simplify sending emails.""",
  long_description_content_type='text/markdown',
  author = 'AndrásPataki',                   
  author_email = 'andras.h.pataki@gmail.com',     
  url = 'https://github.com/AndrasHPataki/flask_extension_ftm/',  
  download_url = 'https://github.com/AndrasHPataki/flask_extension_ftm/archive/1.5.tar.gz',   
  keywords = ['Mail', 'Delivery', 'Form','Flask','flask-extension'],  
  install_requires=[            
          'Flask-Mail','flask-wtf'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      
    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3',     
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
