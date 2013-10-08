{
  "targets": [
    {
      "target_name": "sos",
      "sources": [
        "src/binding.cpp",
        "src/nodeSos.cpp"
      ],
      "cflags": ['-fexceptions'],
      "cflags_cc": ['-fexceptions'],
      "conditions" : [
        [
          'OS=="mac"', {
            'xcode_settings': {
              'GCC_ENABLE_CPP_EXCEPTIONS': 'YES'
            }
          }
        ],
        [
          'OS!="win"', {
            "libraries" : [
              '-lusb'
            ]
          }
        ],
        [
          'OS=="win"', {
            "libraries" : [
            ]
          }
        ]
      ]
    }
  ]
}
