x=open("filetip.txt","w+")
x.write(input("Enter a passage: "))
x.seek (0,0)
a=x.read()
def reverse(y):
    return y[::-1]
z=open("reversefiltip.txt","w+")
z.write(reverse(a))
z.seek(0,0)
print(z.read())
x.close()
z.close()
