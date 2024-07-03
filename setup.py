from setuptools import setup

readme = open("./README.md", "r")


setup(
    name='linkmailLensApi',
    packages=['linkmailLensApi'],  # this must be the same as the name above
    version='1.0',
    description='Api no oficial de Google lens creada por mi.',
    long_description=readme.read(),
    long_description_content_type='text/markdown',
    author='Linkmail',
    author_email='',
    # use the URL to the github repo
    url='https://github.com/Linkmail16/linkmailLensApi',
    download_url='hhttps://github.com/Linkmail16/linkmailLensApi/tarball/0.1',
    keywords=['api', 'google', 'google lens'],
    classifiers=[ ],
    license='MIT',
    include_package_data=True
)
