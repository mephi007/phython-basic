''' phyton program to demostrate various string functions and operations'''
str1 = "python program" 
str2 = "string operations"
print " length of the strings"
print len(str1)
print len(str2)
print "first occurence of o in str1 and r in str2 is "
print str1.index("o")
print str2.index("r")
print "number of occurrence in str1 and str2 are"
print str1.count("0")
print str2.count("i")
print "str1 string slice operations"
print str1[2:9]
print str1[2:9:2]
print str1[2:7]
print str1[2:9:1]
print str1[::-1]
print "str2 string slice operations"
print str2[1:6]
print str1[2:8:2]
print str1[2:8]
print str1[2:8:1]
print str1[::-1]
print "strings are in upper case"
print str1.upper()
print str2.upper()
print "strings are in lower case"
print str1.lower()
print str2.lower()
print "str1 and str2 string functions starts with"
print str1.startswith("python")
print str2.startswith("asdfsdf")
print "str1 and str2 string ends with"
print str1.endswith("sfsdfsd")
print str2.endswith("operations")
print "str1 and str2 split operations"
strsplit1 = str1.split(" ")
print strsplit1
strsplit2 = str2.split(" ")
print strsplit2
print "string concatenation"
print str1+ " "+str2