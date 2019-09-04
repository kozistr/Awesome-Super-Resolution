from setuptools import setup

setup_requires = [
]

install_requires = [
    'tensorflow-gpu<2.0',
    'opencv-python',
    'numpy',
]

dependency_links = [
]

setup(
    name='sr_models',
    version='0.0.1',
    description='single image super resolution model collections in Tensorflow',
    author='HyeongChan Kim',
    author_email='kozistr@gmail.com',
    url='https://github.com/kozistr/Awesome-Super-Resolution',
    license='MIT',
    include_package_data=True,
    install_requires=install_requires,
    setup_requires=setup_requires,
    dependency_links=dependency_links,
    # scripts=['manage.py'],
    entry_points={
        'console_scripts': [
        ],
        "egg_info.writers": [
            "sr.txt = setuptools.command.egg_info:write_arg",
        ],
    },
)
