import sys
from distutils.core import setup, Extension

if __name__ == '__main__':
    if "--force" in sys.argv:
        run_build = True
        sys.argv.remove('--force')
    else:
        non_build_actions = ['--help-commands', 'egg_info', 'clean', '--version']
        if '--help' in sys.argv[1:] or sys.argv[1] in non_build_actions:
            run_build = False
        else:
            run_build = True

    metadata = dict(
        name='naturalneighbor',
        version='0.2.1.dev1',
        description='Fast, discrete natural neighbor interpolation in 3D on a CPU.',
        long_description=open('README.rst', 'r').read(),
        author='Reece Stevens',
        author_email='rstevens@innolitics.com',
        license='MIT',
        classifiers=[
            'Development Status :: 4 - Beta',
            'Intended Audience :: Developers',
            'Intended Audience :: Science/Research',
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.8',
            'Programming Language :: Python :: Implementation :: CPython',
            'Topic :: Scientific/Engineering',
            'Topic :: Software Development',
        ],
        keywords='interpolation scipy griddata numpy sibson',
        install_requires=[
            'numpy>=1.13',
        ],
        url='https://github.com/innolitics/natural-neighbor-interpolation',
        packages=['naturalneighbor'],
    )

    if run_build:
        import numpy.distutils.misc_util

        module = Extension(
            'cnaturalneighbor',
            include_dirs=numpy.distutils.misc_util.get_numpy_include_dirs(),
            library_dirs=['/usr/local/lib'],
            extra_compile_args=['--std=c++11', '-O3'],
            sources=[
                'naturalneighbor/cnaturalneighbor.cpp',
            ],
        )

        metadata['ext_modules'] = [module]

    setup(**metadata)
