def arithmetric_arranger(x,y = False):
    nums1 = ''
    nums2 = ''
    lines = ''
    answers = ''
    #checks number of problems
    if len(x) < 1 or len(x) > 5:
        print("Error: Too many problems.")
        return
    else:
        #splits into 3 varibles
        for string in x:
            a = string.split()
            num1, operator, num2 = a[0],a[1],a[2] 
            #more error checking
            if len(num1) > 4 or len(num2) > 4:
                print("Error: Numbers cannot be more than four digits.")
                return
            if not num1.isdigit() and num2.isdigit():
                print("Error: Numbers must only contain digits.")
                return
            if ('*' or '/') in operator:
                print("Error: Operator must be '+' or '-'.")
                return
            #adds whitespace to operator
            if operator == '+':
                answer = int(num1) + int(num2)
                answer = str(answer)
            else:
                answer = int(num1) - int(num2)
                answer = str(answer)
            if len(num2) >= len(num1):
                operator = operator + " "
            elif len(num2) == (len(num1) - 1):
                operator = operator + "  "
            elif len(num2) == (len(num1) - 2):
                operator = operator + "   "
            elif len(num2) == (len(num1) - 3):
                operator = operator + "    "
            #adds whitespace to num1 and answer
            if len(num1) >= len(num2):
                num1 = '  ' + num1
            elif (len(num1) + 1) == len(num2):
                num1 = '   ' + num1
            elif (len(num1) + 2) == len(num2):
                num1 = '    ' + num1
            elif (len(num1) + 3) == len(num2):
                num1 = '     ' + num1
            if len(str(answer)) == (len(num1) - 1):
                answer = ' ' + answer + '    '
            elif len(str(answer)) == (len(num1) - 2):
                answer = '  ' + answer + '    '
            elif len(str(answer)) == (len(num1) - 3):
                answer = '   ' + answer + '    '
            #adds -s to line and 4 whitespace to others 
            line = '-' * len(num1) + '    '
            num2 = operator + num2 + '    '
            num1 = num1 + '    '
            #adds numbers that we have been working on to a place we can add them all to as we make them
            nums1 = nums1 + num1
            nums2 = nums2 + num2
            lines = lines + line
            answers = answers + answer
        #checks if we need answer or not and prints
        if y == True:
            print(nums1 + '\n' + nums2 + '\n' + lines + '\n' + answers)
        else:
            print(nums1 + '\n' + nums2 + '\n' + lines)

Q1 = ["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"]
arithmetric_arranger(Q1, True)
