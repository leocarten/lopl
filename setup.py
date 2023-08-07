from distutils.core import setup
setup(
  name = 'LOPL',         
  packages = ['LOPL'],   
  version = '0.1',     
  license='MIT',        
  description = "LOPL stands for Leo's Own Programming Language and can be used to help visualize behind the scene functionality in your code. I created this programming language while reading Crafting Interpreters. It is a mix of C and JavaScript, but uses the Python Virtual Machine.",
  author = 'Leo Carten',                   
  author_email = 'lcarten14@gmail.com',      
  url = 'https://github.com/leocarten/lopl',   
  download_url = 'https://github.com/leocarten/lopl/archive/refs/tags/v_01.tar.gz', 
  keywords = ['code visualizer', 'bytecode'],   
  install_requires=[            
          'dis'
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
