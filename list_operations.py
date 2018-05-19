lst1 = ['java', 'cloud', 1995, 2010];
lst2 = [3, 6,9,12,15];
lst3 = ["p", "q", "r", "s"]
print "various list operations"
print " lst1[0]: ", lst1[0]
print "list split operations"
print "lst2[1:5]: ", lst2[1:5]
print "value available at index 2: "
print lst1[2]
print "Insert elements into the list"
lst1[2] = 2001;
print "new value in lst1 at index 2 is "
print lst1[2]
print "modified lst1"
print lst1
print "delete from lst1"
del lst1[2];
print "after deletion at index 2 is: "
print lst1
print ' length of lst1'
print len(lst1)
print "Max() and Min() on lst for numeric"
print max(lst1)
print min(lst1)
print "sum() on numeric lsts"
print sum(lst2)
print "avg on numeric lists"
print sum(lst2)/len(lst2)
print "del() for multiple elements in the list"
del lst1[1:4]
print "modified lst1"
print lst1
print " remove() on lst3"
lst3.remove('p')
print "sort() on lst2"
lst2.sort()
print "after sort()"
print lst2
print "append() on lst2"
lst2.append('18')
print "lst2 after append", lst2
print "split operations"
lst1[2:4]
lst2[1:5]
lst3[2:]
print "lst1 split"
print lst1
print "lst2 split"
print lst2
print " lst3 split"
print lst3
print "for loop on lists"
for i in range(len(lst2)):
	lst2[i] = lst2[i]*3
print lst2
print " creating list in another way"
a = 'python'
b = list(a)
print a
print b
c = 'welcome to python programming'
print c
d = c.split()
print d
print " slice of d"
print d[1:3]
print d[:2]
h = "python-programming-is-easy"
print h
delim ='-'
h.split(delim)
print "after split and delim"
print h
delim = '***'
delim.join(h)
print "join () on lsts"
print h
print " cmp() on lsts"
print cmp(lst1, lst2)
print cmp(lst2, lst1)
lst4 = lst3+ [ 786];
print cmp(lst3 , lst4)
print "Max values"
print " maximun value element: ", max(lst1)
print " maximun value element: ", max(lst2)
print " maximun value element: ", max(lst3)
print "Min Values"
print " minimum value element: ", min(lst1)
print " minimum value element: ", min(lst2)
print " minimum value element: ", min(lst3)
print "new lat5 from existing lst2"
lst5 = list(lst2)
print " pop on list"
print "list elements", lst5
print "lst2: ", lst2.pop(2)
print "reverse() on lst"
lst2.reverse()
print "sort() on lst"
print lst2
lst2.sort()
print "after sort", lst2
print "end of chapter"