from setuptools import setup

with open("./README.md", "r", encoding="utf-8") as readme:
    long_description = readme.read()

setup(
    name='linkmailLensApi',
    packages=['linkmailLensApi'],
    version='0.7',
    description='Api no oficial de Google lens creada por mi.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Linkmail',
    author_email='',  # Puedes añadir tu email aquí si lo deseas
    url='https://github.com/Linkmail16/linkmailLensApi',
    download_url='https://github.com/Linkmail16/linkmailLensApi/archive/refs/tags/v0.3.tar.gz',
    keywords=['api', 'google', 'google lens'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    license='MIT',
    include_package_data=True
)
