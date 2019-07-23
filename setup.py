from setuptools import setup

setup(
    name="variant_tools",
    version="0.0.1",
    description="Tools for working with variants.",
    author="Guy Allard, LUMC",
    author_email="wgallard AT lumc DOT nl",
    url="https://github.com/;umc-pgx/variant-tools",
    license="MIT",
    platforms=['any'],
    packages=["variant_tools"],
    install_requires=[
        'numpy==1.13.1',
        'biopython==1.69',
        'edlib>=1.2.3',
        'pyinterval==1.2.0'
    ],
    tests_requires=['pytest'],
    entry_points={
      "console_scripts": [
          "vcf2sequence = variant_tools.cli:vcf2sequence"
      ]
    },
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Scientific/Engineering',
        'License :: MIT License',
    ],
    keywords = 'bioinformatics'
)
