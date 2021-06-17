from distutils.core import setup
setup(
  name = 'pybchain',         # How you named your package folder (MyLib)
  packages = ['pybchain'],   # Chose the same as "name"
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='mpl-2.0',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Simple blockchain concept package',   # Give a short description about your library
  author = 'unfuz3',                   # Type in your name
  author_email = 'mr.mendozamen@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/unfuz3/pybchain',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/user/reponame/archive/v_01.tar.gz',
  keywords = ['blockchain', 'python', 'concept'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'validators',
          'beautifulsoup4',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: Mozilla Public License 2.0',   # Again, pick a license
    'Programming Language :: Python :: 3.9',      #Specify which pyhton versions that you want to support,
  ],
)
