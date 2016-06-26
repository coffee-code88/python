def gotham(f):
    def inside_gotham():
        print "Gotham needs Batman"
        f()
    return inside_gotham

@gotham
def batman():
    print "Batman Here! Gotham is saved! "

batman()
