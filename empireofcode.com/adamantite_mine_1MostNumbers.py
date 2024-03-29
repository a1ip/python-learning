#!/usr/bin/env python3

def most_difference(*args):
    if len(args) > 0:
     nums=sorted(args)
     min=nums[0]
     max=nums[-1]
     print (max,'-',min,'=',round(max-min,3))
     return round(max-min,3)
    return 0
    
if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    ##def almost_equal(checked, correct, significant_digits):
    ##  precision = 0.1 ** significant_digits
    ##    return correct - precision < checked < correct + precision

    ##assert almost_equal(most_difference(1, 2, 3), 2, 3), "3-1=2"
    ##assert almost_equal(most_difference(5, 5), 0, 3), "5-5=0"
    ##assert almost_equal(most_difference(10.2, 2.2, 0.00001, 1.1, 0.5), 10.199, 3), "10.2-(0.00001)=10.19999"
    ##assert almost_equal(most_difference(), 0, 3), "Empty"
	assert most_difference(1, 2, 3) == 2
	assert most_difference(5, -5) == 10
	assert most_difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4
	assert most_difference() == 0
	assert most_difference(-0.036, -0.11, -0.55, -64.0)
