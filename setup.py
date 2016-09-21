def configuration(parent_package='',top_path=None):
    from numpy.distutils.misc_util import Configuration
    config = Configuration(None, parent_package, top_path)
    config.add_extension('bvls',sources=['bvls/bvls.pyf','bvls/bvls.f90']) 
    return config

if __name__ == '__main__':
    from numpy.distutils.core import setup
    setup(name = 'BVLS',
          configuration=configuration)



