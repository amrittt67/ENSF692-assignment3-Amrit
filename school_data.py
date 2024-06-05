# school_data.py
# Amrit Kaur
#
# A terminal-based application for computing and printing statistics based on given input.
# You must include the main listed below. You may add your own additional classes, functions, variables, etc. 
# You may import any modules from the standard Python library.
# Remember to include docstrings and comments.


import sys
import numpy as np
from given_data import year_2013, year_2014, year_2015, year_2016, year_2017, year_2018, year_2019, year_2020, year_2021, year_2022

# Declare any global variables needed to store the data here

# List of all the school names available
schoolNames = [
    'Centennial High School', 'Robert Thirsk School', 'Louise Dean School', 'Queen Elizabeth High School', 'Forest Lawn High School',
    'Crescent Heights High School', 'Western Canada High School', 'Central Memorial High School', 'James Fowler High School', 'Ernest Manning High School',
    'William Aberhart High School', 'National Sport School', 'Henry Wise Wood High School', 'Bowness High School', 'Lord Beaverbrook High School',
    'Jack James High School', 'Sir Winston Churchill High School', 'Dr. E. P. Scarlett High School', 'John G Diefenbaker High School', 'Lester B. Pearson High School'
]

# List of all the school codes available
schoolCodes = [
    '1224', '1679', '9626', '9806', '9813', '9815', '9816', '9823', '9825', '9826',
    '9829', '9830', '9836', '9847', '9850', '9856', '9857', '9858', '9860', '9865'
]

# You may add your own additional classes, functions, variables, etc.


def main():
    print("ENSF 692 School Enrollment Statistics")

    # Print Stage 1 requirements here
    # Import all the years data into variable
    base = np.array([
        year_2013, year_2014, year_2015, year_2016, year_2017, year_2018, year_2019, year_2020, year_2021, year_2022
    ])
    
    # Reshape data variable to a 3-dimensional numpy array
    base = base.reshape(10, 20, 3)
    
    # Printing shape and dimensions of our data variable
    print('Shape of full data array:', base.shape)
    print('Dimensions of full data array:', base.ndim)

    '''
    schoolIndex: contains index of schoolName or schoolCode from global variables schoolNames and schoolcodes
    based on if user entered school name or school code during prompt
    '''
    schoolIndex = 0
    schoolName = ''
    schoolCode = ''
    
    # Prompt for user input
    school = input('Please enter the high school name or school code: ')
    
    '''
    If school is a number, we look for its index in schoolCodes array,
    Otherwise it may contain school name, and we look in schoolNames array for index
    '''
    if school.isdigit():
        schoolIndex = schoolCodes.index(school)
    else:
        schoolIndex = schoolNames.index(school)
    
    '''
    In case no school code or school name matches any value in above arrays,
    We conclude the user has entered an invalid data, hence we raise ValueError,
    And we terminate the program
    '''
    if schoolName == -1 or schoolCode == -1:
        raise ValueError('You must enter a valid school name or code.')
        sys.exit(1)
    
    
    # Print Stage 2 requirements here
    print("\n***Requested School Statistics***\n")
    # Print school name and school code using the schoolIndex
    print(f'School Name: {schoolNames[schoolIndex]}, School Code: {schoolCodes[schoolIndex]}')
    
    # Created new sub array data variable with values of required school data
    schoolBase = base[:, schoolIndex, :]
    
    # Print Mean enrollment for Grades XX
    for i in range(3):
        print(f'Mean enrollment for Grade 1{i}:', int(np.nansum(schoolBase, axis=0)[i] / schoolBase.shape[0]))
    
    # Print Highest and Lowest enrollment data
    print('Highest enrollment for a single grade:', int(np.nanmax(schoolBase)))
    print('Lowest enrollment for a single grade:', int(np.nanmin(schoolBase)))
    
    # Print Total enrollment for Grade year wise
    for i in range(10):
        print(f'Total enrollment for Grade {2013 + i}:', int(np.nansum(schoolBase, axis=1)[i]))
    
    # Print Total enrollment
    print('Total ten year enrollment:', int(np.nansum(np.nansum(schoolBase, axis=1), axis=0)))
    print('Mean total enrollment over 10 years:', int(np.nansum(np.nansum(schoolBase, axis=1), axis=0) / schoolBase.shape[0]))
    
    # Create filter for data variable, and create filtered data variable, finally print required data
    filter500 = schoolBase > 500
    filteredSchoolBase = schoolBase[filter500]
    if len(filteredSchoolBase) == 0:
        print('No enrollments over 500')
    else:
        print('For all enrollments over 500, the median value was:', int(np.median(filteredSchoolBase)))
    
    # Print Stage 3 requirements here
    print("\n***General Statistics for All Schools***\n")
    
    # Print required data
    print('Mean enrollment in 2013:', int(np.nanmean(base[0])))
    print('Mean enrollment in 2022:', int(np.nanmean(base[-1])))
    print('Total graduating class of 2022:', int(np.nansum(base[-1, :, 2])))
    print('Highest enrollment for a single grade:', int(np.nanmax(base)))
    print('Lowest enrollment for a single grade:', int(np.nanmin(base)))
    
if __name__ == '__main__':
    main()
