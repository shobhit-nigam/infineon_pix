i = int(input("enter a number less than 10:\n"))
try:
    assert (i<10), "should have entered a value less than 10"
except Exception as obje:
    print(obje)
