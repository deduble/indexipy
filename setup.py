import setuptools


setuptools.setup(name='indexipy',
                 version='1.0.0',
                 description='[PoC] Improved Python Indexing For Pure Python Containers - Like NumPy.',
                 long_description=open('README.md').read().strip(),
                 author='Yunus Kayalıdere',
                 author_email='yunus.kayalidere@gmail.com',
                 url='https://github.com/deduble/indexipy',
                 py_modules=['indexipy'],
                 install_requires=[],
                 license='MIT License',
                 zip_safe=False,
                 keywords='container search object parse nested indexing',
                 classifiers=['Search', 'Containers', 'Objects', 'Indexing'])
