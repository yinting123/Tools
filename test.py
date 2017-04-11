#-*-coding:utf-8-*-

import md5

src = "hello"
m1 = md5.new()
m1.update(src)
print m1.hexdigest()