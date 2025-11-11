# Range like generator
# increasing
start_range = int(input('enter your starting value:'))
end_range = int(input('enter your ending value:')) 

def range_Generator(first,last):
    start = first
    end = last
    while start <= end:
        if start == end+1:
            raise StopIteration
        temp = start
        start += 1
        yield temp

rg1 = range_Generator(start_range,end_range)
while start_range <= end_range:
    print(next(rg1))
    start_range += 1

# decreasing
start_range = int(input('enter your starting value:'))
end_range = int(input('enter your ending value:')) 

def range_Generator(first,last):
    start = first
    end = last
    while start >= end:
        if start == end-1:
            raise StopIteration
        temp = start
        start -= 1
        yield temp

rg1 = range_Generator(start_range,end_range)
while start_range >= end_range:
    print(next(rg1))
    start_range -= 1


# fibinocci using gnerators
fibnocci_series = int(input('enter upto the series of count you want:'))
def fibnocci_series_generator(series_upto):
    first_no = 0
    second_no = 1
    while series_upto > 0:
        yield first_no
        third_no = first_no + second_no
        first_no = second_no
        second_no = third_no
        series_upto -= 1

fsg1 = fibnocci_series_generator(fibnocci_series)
while fibnocci_series > 0:
    print(next(fsg1))
    fibnocci_series -= 1