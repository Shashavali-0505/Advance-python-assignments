# Task 1: can blocks exist one without another (try ,except, else, finally) 
#       2: try nested try and except blocks
# Task1
# 1. try + except
try:
    a = int(input('enter a num:'))
    b = int(input('enter a num:'))
    print(a/b)
except Exception as e:
    print(e)
    print('divisible by zero is not posssibe for any integer')

# 2. try + finally
try:
    a = int(input('enter a num:'))
    b = int(input('enter a num:'))
    print(a+b)
finally:
    print('executed successfully')
    
# 3. try + except + finally
try:
    a = int(input('enter a num:'))
    b = int(input('enter a num:'))
    print(a+b)
except Exception as e:
    print(e)
finally:
    print('executed successfully')

# 4. try + except + else
try:
    a = int(input('enter a num:'))
    b = int(input('enter a num:'))
    print(a+b)
except Exception as e:
    print(e)
else:
    print('only else block executes when try block executed successfully')

# 5. try + except + else + finally
try:
    a = int(input('enter a num:'))
    b = int(input('enter a num:'))
    print(a/b)
except (ZeroDivisionError,ValueError) as e:
    print(e)
except Exception as e:
    print(e)
else:
    print('Else block: only executes when try block executed successfully')
finally:
    print('Finally block: always executes irrespective of any exceptions raised')

#  can blocks exist one without another (try ,except, else, finally) 

# 1. we can not write except,else,finally blocks without a try block 
# 2. try after else block - no

# Task2 - Nested try and except blocks
try:
    print('Outer try block')
    try:
        print('Inner try block')
        a = int(input('enter a num:'))
        b = int(input('enter a num:'))
        print(a+b)
    except ValueError as e:
        print(e)
        print('Please check your entered inputs once!!')
    except Exception as e:
        print(e)
    else:
        print('Inner block executed successfully')
    finally:
        print('Inner try and except blocks completed')
    
    c = int(input('enter a num:'))
    d = int(input('enter a num:'))
    print(c/d)
except ZeroDivisionError as e:
    print(e)
    print('divisible by zero is not posssibe for any integer')
except ValueError as e:
    print(e)
    print('Please check your entered inputs once!!')
except Exception as e:
    print(e)
else:
    print('Outer try block executed successfully')
finally:
    print('Outer try and except blocks completed')