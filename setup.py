from setuptools import setup

setup(name='trustly',
        version='0.3',
        description='Trustly API Python client',
        url='http://github.com/trustly/trustly-client-python',
        author='Per lejontand',
        license='The MIT License (MIT)',
        packages=['trustly', 'trustly.data', 'trustly.api'],
        install_requires=['uuid', 'PyCryptodome', 'six'],
        zip_safe=False,
        package_data={'trustly.api': [ 'keys/*.public.pem' ]}
        )

