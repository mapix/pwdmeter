PWDMeter

Features
--------

* 大小写检查
* 字母数字字符混合
* 常用密码检查
* 长度检查
* 非英文字母检查
* 重复性检查


Examples
--------

::

    In [1]: from pwdmeter import test

    In [2]: test('pass')
    Out[2]:
    (0.001796569654667007,
     {'casemix': 'Use a good mix of upper case and lower case letters',
      'charmix': 'Use a good mix of numbers, letters, and symbols',
      'length': 'Increase the length of the password',
      'non_ascii': 'Use non-ASCII chars',
      'non_dictionary': 'Avoid using most common passwords',
      'variety': 'Minimize character duplicates and repetitions'})
