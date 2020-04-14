from distutils.core import setup
setup(
  name = 'form_to_mail',         
  packages = ['form_to_mail'],   
  version = '1',      
  license='MIT',       
  description = 'Simple configuration system for mail, required for forms packages', 
  long_description='This library is recommended to integrate with the forms package. It works to simplify sending emails.',
  author = 'AndrásPataki',                   
  author_email = 'andras.h.pataki@gmail.com',     
  url = 'https://github.com/AndrasHPataki/form_to_mail',  
  download_url = 'https://github.com/AndrasHPataki/form_to_mail/archive/1.tar.gz',   
  keywords = ['Mail', 'Delivery', 'Form','Flask'],  
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
