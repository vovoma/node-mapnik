{
  'target_defaults': {
    'default_configuration': 'Release',
    'msbuild_toolset':'v140',
    'msvs_disabled_warnings': [ 4068,4244,4005,4506,4345,4804,4805,4661 ],
    'cflags_cc' : [
      '-std=c++11',
    ],
    'configurations': {
      'Debug': {
        'defines!': [
          'NDEBUG'
        ],
        'cflags_cc!': [
          '-O3',
          '-Os',
          '-DNDEBUG'
        ],
        'xcode_settings': {
          'OTHER_CPLUSPLUSFLAGS!': [
            '-O3',
            '-Os',
            '-DDEBUG'
          ],
          'GCC_OPTIMIZATION_LEVEL': '0',
          'GCC_GENERATE_DEBUGGING_SYMBOLS': 'YES'
        },
        'msvs_settings': {
          'VCCLCompilerTool': {
            'ExceptionHandling': 1, # /EHsc
            'RuntimeTypeInfo': 'true', # /GR
            'RuntimeLibrary': '2' # /MD
          }
        }
      },
      'Release': {
        'defines': [
          'NDEBUG'
        ],
        'xcode_settings': {
          'OTHER_CPLUSPLUSFLAGS!': [
            '-Os',
            '-O2'
          ],
          'GCC_OPTIMIZATION_LEVEL': '3',
          'GCC_GENERATE_DEBUGGING_SYMBOLS': 'NO',
          'DEAD_CODE_STRIPPING': 'YES',
          'GCC_INLINES_ARE_PRIVATE_EXTERN': 'YES'
        },
        'ldflags': [
          '-Wl,-s'
        ],
        'msvs_settings': {
          'VCCLCompilerTool': {
            'ExceptionHandling': 1, # /EHsc
            'RuntimeTypeInfo': 'true', # /GR
            'RuntimeLibrary': '2' # /MD
          }
        }
      }
    }
  }
}
