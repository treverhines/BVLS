from numpy.distutils.core import setup, Extension
ext = []
ext.append(Extension('_bvls',
                     sources = ['bvls/_bvls.f90',
                                'bvls/_bvls.pyf']))
setup(
   name='BVLS',
   packages=['bvls'],
   version='0.1.0',
   description='Python wrapper for the bounded value least squares algorithm',
   author='Trever Hines',
   author_email='hinest@umich.edu',
   url='https://github.com/treverhines/BVLS',
   ext_modules=ext)


