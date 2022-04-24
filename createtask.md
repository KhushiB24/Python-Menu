{% include navigation.html %}

## Code Image

<img width="900" alt="Screen Shot 2022-04-24 at 11 46 46" src="https://user-images.githubusercontent.com/89240973/164991778-d257cf72-f94c-4e53-9730-42c9222a84d4.jpg">


<img width="852" alt="Screen Shot 2022-04-24 at 11 47 38 AM" src="https://user-images.githubusercontent.com/89240973/164993972-be055c2d-fff6-4725-a2a5-675aeac5beb2.jpg">


## 3a. i. Describes the overall purpose of the program 

Answer: The overall purpose of the program is to have a Mean, Median, Mode Math Quiz Game. In this game, the users are asked if they liked to add a number in the numlist, where then they are pormpted to answer with "y" for yes and "n" for no. If user selects "y", they are asked to enter a number to add to their numlist, if selected "n" the game ends and exits. 

## 3a. ii. Describes what functionality of the program is demonstrated in the video

Answer: The functionality of the program that is demonstrated in the video would be how we can refresh the page as well as for the Math Quiz, the users can enter lists of numbers that they would want to use for the Math Quiz.

## 3a. iii. Describes the input and output of the program demonstrated in the video

Answer: The input and output of the program demonstrated in the video would be how the Math Quiz and how the users can choose what numbers they would like to add to their list. Then, the output would be the mean, median, mode, min, and max that becomes the result of the numbers the users chose.

## 3 b. Capture and paste two program code segments you developed during the administration of this task that contain a list (or other collection type) being used to manage complexity in your program.

### i. The first program code segment must show how data have been stored in the list. 
```python
        try:
            itemInput = int(input('What number would you like to add?'))
        except:
            print('Oh no! That wasn\'t an expected answer. Exiting...')
            break
        numList.append(itemInput)
        print('Number inputted.')
```


### ii. The second program code segment must show the data in the same list being used, such as creating new data from the existing data or accessing multiple elements in the list, as part of fulfilling the program’s purpose.

```python 
mean = mean(numList)
median = median(numList)
mode = mode(numList)
min = min(numList)
max = max(numList)
    
```

### iii. Identifies the name of the list being used in this response

Answer: The name of the list being used in this response would be (numList). The numList only contains the values that are identified as valid and accepted by the program according to when and where the user had given the input values. 

### iv. Describes what the data contained in the list represent in your program

Answer: The data contained in the list that represents in my program would be the numbers that the user had decided to use. Additionally, if asked if there would be another number that the user would like to input, where if the user puts a number directly or says no the program would end right there. 

### v. Explains how the selected list manages complexity in your program code by explaining why your program code could not be written, or how it would be written differently, if you did not use the list 

Answer: The selected list manages complexity in the program code by how the code would have been written differently if I didn’t use a list would be to let the user use random numbers that had pre-stored in the code. The new code would give the users to manually pick which numbers they would like to use according to what is given. The word count is 157.

## 3 c. Capture and paste two program code segments you developed during the administration of this task that contain a student-developed procedure that implements an algorithm used in your program and a call to that procedure. 

### i. The first program code segment must be a student-developed procedure that: 
□ Defines the procedure’s name and return type (if necessary) 

□ Contains and uses one or more parameters that have an effect on the functionality of the procedure 

□ Implements an algorithm that includes sequencing, selection, and iteration

```python
def OR(input, first, second):
    bool = input == first or input == second
    return bool
```

```python
if OR(addInput, 'y', 'yes'):
 try:
   itemInput = int(input('What number would you like to add?'))
 except:
   print('Oh no! That wasn\'t an expected answer. Exiting...')
   break
 numList.append(itemInput)
 print('Number inputted.')
elif OR(addInput, 'n', 'no'):
 print('Ok! Exiting...')
 break
else:
 print('Oh no! That wasn\'t an expected answer. Exiting...')
 break
```


### ii. The second program code segment must show where your student-developed procedure is being called in your program.

```python
statInput = input('Would you like to see the list and the stastistics of the list? (y/n)')
if OR(statInput, 'y', 'yes'):
 print('The list is: ' + str(numList))
 print('The mean is ' + str(mean) + '.')
 print('The median is ' + str(median) + '.')
 print('The mode is ' + str(mode) + '.')
 print('The range is ' + str(min) + ' --> ' + str(max) + '.')
elif OR(statInput, 'n', 'no'):
 print('Ok! End of Program.')
```

Then, provide a written response that does both of the following: 
### iii. Describes in general what the identified procedure does and how it contributes to the overall functionality of the program 

Answer: In general, the identified procedure defines a Boolean expression which is later used for if and else statements, where the input is equal to first or input is equal to second, and either can be true to return the Boolean value. Then, with the if and else statements allow the users to enter a “y” or “n” for going on to add a numerical value. If the conditions aren’t met, the selection occurs where the program exists as the user input is not what is required. Thereafter, after the next input value that stops the program, further gives the user to choose to look at the statistics of the list they made, displaying the mean, median, mode, and range.



### iv. Explains in detailed steps how the algorithm implemented in the identified procedure works. Your explanation must be detailed enough for someone else to recreate it.

Answer: First step: enter an input, no certain restrictions. Make sure that every time a value has been inputted, that the first answer is “y” or else the program would close. Second step: you can enter as many values as would like, the important step is to remember to answer the question reasonably and to give the exact answer that the program asks. Third step: decide if the statistics of the list can be displayed. If said no, the program would agree and closes the program. If said yes, the program will give you the numList, the mean, median, mode, and range as the minimum and maximum values have been sorted while running the program. 
