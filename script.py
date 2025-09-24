data = [
 "data = [",
 "]",
 "a, b, c, sep = 10, 11, 21, 44",
 "q, space, separator = chr(34), chr(32), chr(sep)",
 "for k in range(a,b):",
 "  print(data[k])",
 "for d in data:",
 "  print(space + q + d + q + separator)",
 "for k in range(b,c):",
 "  print(data[k])",
 "data = [",
 "]",
 "a, b, c, sep = 21, 22, 34, 44",
 "q, space, separator = 34.chr, 32.chr, sep.chr",
 "for k in a..b-1",
 "  puts data[k]",
 "end",
 "data.each { |d| puts space + q + d + q + separator}",
 "for k in b..c-1",
 "  puts data[k]",
 "end",
 "data = {",
 "}",
 "a, b, c, sep= 0, 1, 10, 44",
 "q, space, separator = string.char(34), string.char(32), string.char(sep)",
 "for k = a+1,b do",
 "  print(data[k])",
 "end",
 "for k = 1,#data do",
 "  print(space .. q .. data[k] .. q .. separator)",
 "end",
 "for k = b+1,c do",
 "  print(data[k])",
 "end",
]
a, b, c, sep = 10, 11, 21, 44
q, space, separator = chr(34), chr(32), chr(sep)
for k in range(a,b):
  print(data[k])
for d in data:
  print(space + q + d + q + separator)
for k in range(b,c):
  print(data[k])
