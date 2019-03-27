def es_vocal(a):
      vocal=['a','e','i','o','u']
      if (a== vocal[0] or a== vocal[1] or a== vocal[2] or a== vocal[3] or a== vocal[4]):
          return ('True')
      return('False')


assert  (es_vocal('a')=='True')
assert  (es_vocal('b')=='False')
