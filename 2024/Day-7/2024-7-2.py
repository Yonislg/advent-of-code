f = open('2024/Day-7/2024-7-input.txt','r')
puzzle_input = f.read().split('\n')
f.close()

f2 = open('2024/Day-7/example.txt','r')
example = f2.read().split('\n')
f2.close()

def callibartion_sort(input):
    equations = []
    for row in input:
        answer, eq = row.split(':')
        eq = eq.split(' ')
        equations.append([int(answer), [int(x) for x in eq[1:]]])

    return equations

def calibration_check(ans, eq):
    for mult in range(2**(len(eq)-1)):
        specifier = '{0:0'+str(len(eq)-1)+'b}'
        bin_rev = specifier.format(mult)
        bin = bin_rev[::-1]
        sum = eq[0]
        for ii in range(len(eq)-1):
            if bin[ii] == '0':
                sum += eq[ii+1]
            else:
                sum *= eq[ii+1]
        if sum == ans:
            return True
    return False

def calibration_check_v2(ans, eq):
    for i in range(1,2**(len(eq)-1)):
        i_specifier = '{0:0'+str(len(eq)-1)+'b}'
        i_rev = i_specifier.format(i)
        concat = i_rev[::-1]
        for ii in range(2**(len(eq)-1)):
            ii_specifier = '{0:0'+str(len(eq)-1)+'b}'
            ii_rev = ii_specifier.format(ii)
            plustimes = ii_rev[::-1]
            sum = eq[0]
            for mult in range(len(eq)-1):
                if concat[mult] == '1':
                    sum = int(str(sum)+str(eq[mult+1]))
                else:
                    if plustimes[mult] == '0':
                        sum += eq[mult+1]
                    else:
                        sum *= eq[mult+1]
                if sum > ans:
                    break
            if sum == ans:
                return True
    return False

def callibrators(equations):
    sum = 0
    ct = 0
    end = len(equations)
    for equation in equations:
        ans = equation[0]
        LHS = equation[1]
        if (calibration_check(ans,LHS)):
            sum += ans
        elif (calibration_check_v2(ans,LHS)):
            sum += ans
        ct += 1
        if (end-ct)%50 == 0:
            print(end-ct,' equations left to check')
    return sum

equations = callibartion_sort(puzzle_input)
# print(calibration_check(156,[15,6]))
print(callibrators(equations))