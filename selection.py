import collections
import re
import math
from functools import partial
from operator import ne


def square_digits(num):
    tempNum = list(str(num))
    newNum = []
    newStr = ""
    for i in range(len(tempNum)):
        temp = int(tempNum[i]) ** 2
        newNum.append(temp)

    for i in newNum:
        newStr += str(i)



def to_time(seconds):
    hours = seconds//3600
    minutes = hours//60
    if(seconds % 3600 != 0):
        ans = ("{} hour(s) and {} minute(s)".format(hours, minutes))
        return(ans)
    else:
        ans2 = ("{} hour(s) and {} minute(s)".format(hours, minutes))
        return(ans2)
        print(ans2)


def descending_order(num):
    newNum = list(str(num))
    print(newNum)
    e = len(newNum) - 1
    print(e)
    stri = ""
    for i in range(e, -1, -1):
        stri += newNum[i]
    print(stri)

def defending_order(num):
    nums = list(str(num))
    for i in range(1, len(nums)):
        key = nums[i]
        j = i - 1
        while j >= 0 and key > nums[j]:
            nums[j + 1] = nums[j]
            j = j - 1
        nums[j + 1] = key
    print(nums)

def fly_by(lamps, drone):
    if len(drone) > len(lamps):
        print(len(lamps) * 'o')
    else:
        theOs = len(drone) * 'o'
        theXs = (len(lamps)-len(drone)) * 'x'
        print(theOs + theXs)





def add_arrays(array1, array2):
    sum = 0



def filter_long_words(sentence, n):
    sentences = sentence.split()
    ans = []
    for i in range(len(sentences)):
        if len(sentences[i]) > n:
            ans.append(sentences[i])
    return(ans)


def stray(arr):
    uh = len(arr)
    ans = []
    for i in range(uh):
        print(str(i) +'i')
        for j in range(uh):
            print(str(j) +'j')
            if arr[j] != arr[i]:
                ans.append(arr[j])
    return(ans)


def beggars(values, n):
    # your code here
    temp = str(values)
    total = 0
    for x in values: total += x
    if(n>1):
        act = temp.split(',')

    else:
        print(total)



def switcheroo(s):
    ans = list(s)
    final = ""
    for i in range(len(s)):
        if(s[i] == 'a'):
            ans[i] = 'b'
        if(s[i] == 'b'):
            ans[i] = 'a'
    for j in ans:
        final += j
    return(final)

def high_and_low(numbers):
    ans = numbers.split(" ")
    temp = list(map(int, ans))
    answ = sorted(temp)
    last = len(answ) - 1
    hi = answ[last]
    lo = answ[0]
    return(hi, lo)

def task(w,n,c):
    workSchedule = {'Monday':'James', 'Tuesday':'John', 'Wednesday':'Robert', 'Thursday':'Jack', 'Friday':'Wiliam'}
    person = workSchedule[w]
    cost = n * c
    ans = f"It is {w} today, {person}, you have to work, you must spray {n} trees and you need {cost} dollars to buy liquid"
    print(ans)
    # your code

def likes(names):
    sum = ""
    log = len(names)
    greater = log - 2
    for i in names:
        sum += i
    if(log > 0 and log < 2):
        print(sum + " likes this")
    elif(log > 1 and log < 4):
        print(sum + " like this")
    elif(log > 4):
        print(sum + f" and {greater} others like this")
    elif(log == 0):
        print('no one likes this')


def number(bus_stops):
    on = 0
    nah = 0
    for i in range(0, len(bus_stops)):
        for j in range(0, 1):
            on += bus_stops[i][j]
    for x in range(0, len(bus_stops)):
        for y in range(1, 2):
            nah += bus_stops[x][y]

    ans = on - nah

    print(ans)
    print(str(on) + " THIS IS THE SUM")
    print(str(nah) + " THIS IS THE NEGATIVE")

def find_short(s):
    newS = list(s.split(" "))
    nS =[]
    for i in range(len(newS)):
        x = len(newS[i])
        nS.append(x)
    pt = min(nS)
    print(pt)
    ans = nS.index(pt)
    print(ans)


#find_short("bitcoin wh take over the world maybe who knows perhaps")

def reverse_words(text):
    duh = list(text.split())
    y=""
    for i in range(len(duh)):
        a = duh[i]
        b = a[::-1]
        duh[i] = b

    for i in range(len(duh)):
        y+= duh[i]

    print(y)
    print(text[::-1].split())

    #if (y == text[::-1]):
        #print('  '.join(duh))
   # else:
        #print(' '.join(duh))

def get_count(input_str):
    num_vowels = 0
    temp = list(input_str)
    print(temp)
    count = 0
    for i in temp:
        if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
            count+= 1
    print(count)

def word_to_bin(word):
    temp = ' '.join(format(ord(x), 'b') for x in word)
    ans = list(temp.split(" "))
    print(ans)

def likes(names):
    log = len(names)
    sum = ""
    for i in names:
        sum += i + " "
    if(log == 1):
        print(sum + "likes this")
    elif(log > 1 and log < 3):
        print(names[0] + " and " + names[1] + " like this" )
    elif(log == 3):
        print(names[0] + ", " + names[1] + ",and " + names[2] + " like this")
    elif(log > 3):
        print(names[0] + ", " + names[1] + " and " + str(log - 2) + " others like this")




def find_it(seq):
    seq.sort()
    res = 0
    x = len(seq)
    ans = []
    sc = []
    for i in range(x):
        for j in range(x):
            if j == seq[i]:
                ans.append(seq[i])
                res += 1
    for x in range(len(ans)):
        if ans[x] % 2 != 0:
            sc.append(ans[x])


    print(res)
    print(ans)
    print(sc)


def disemvowel(string_):
    ans = ""
    for i in string_:
        if i != 'a' and i != 'e' and i != 'o' and i != 'u' :
            ans += i
    print(ans)

def get_sum(a,b):
    sum = None
    if a == b:
        print(a)
    else:
        if a < b:
            for i in range(a, b+1):
                sum += i
            print(sum)
        else:
            for i in range(b, a+1):
                sum += i
            print(sum)


def create_phone_number(n):
    p1 = n[0:3]
    p2 = n[3:6]
    p3 = n[6:10]
    su = "("
    for i in p1:
        su += str(i)
    m = ")"
    sum = su + m
    sumTw = ""
    for i in p2:
        sumTw += str(i)
    s = "-"
    sumTwo = sumTw + s
    sumThre = ""
    for i in p3:
        sumThre += str(i)

    print(sum + " " +  sumTwo + sumThre)


def spin_words(sentence):
    news = list(sentence.split())
    print(news)
    for i in range(len(news)):
        if len(news[i]) > 4:
            temp = news[i]
            fin = temp[::-1]
            news[i] = fin
    print(news)

#TURN THIS ONE IN
def prime_factors(n):
    count = 0
    an = []
    anss = []
    if n > 1:
        while n % 2 == 0:
            an.append(2)
            n = n/2
        for i in range(3, int(math.sqrt(n))+1, 2):
            while n % i ==0:
                print(i)
                an.append(i)
                n = n/i
    anss = list(map(str, an))
    print()
    for z in range(len(anss)):
        te = anss[z]
        print(te, anss.count(te))

    print(anss)



def encode(st):
    ans = list(st)
    fin = ""
    for i in st:
        temp = ans.index(i)
        if i == "a":
            ans[temp] = '1'
        elif i == "e":
            ans[temp] = '2'
        elif i == "i":
            ans[temp] = '3'
        elif i == "o":
            ans[temp] = '4'
        elif i == "u":
            ans[temp] = '5'
    for j in ans:
        fin += j
    print(fin)

def pig_it(text):
    ans = list(text.split(" "))
    fin = []
    for i in ans:
        fin.append(i[1:] + i[0] + 'ay')
    return(" ".join(fin))


def make_readable(seconds):
    hour = seconds // 3600
    tempOne = seconds - (3600 * hour)
    minutes = tempOne // 60
    sec = seconds - ((60 * minutes) + (3600 * hour))
    if(seconds % 60 == 0):
        print()
    elif(seconds < 10):
        print(f'00:00:0{seconds}')
    elif(seconds < 60 and seconds > 9):
        print(f'00:00:{seconds}')
    elif(seconds >= 60 and seconds < 3600):
        if(minutes < 10):
            print(f'00:0{minutes}:{sec}')
        else:
            print(f'00:{minutes}:{sec}')
    elif(seconds/3600):
        print(f'{hour}:{minutes}:{sec}')



def move_zeros(array):
    rt = []
    for i in array:
        if i == 0:
            rt.append(i)
    print(rt)
    temp = list(filter((0).__ne__,array))
    print(temp)
    for j in rt:
        temp.append(j)
    print(temp)

def anagrams(word,words):
    sums = 0
    temp = 0
    ans = []
    for i in word:
        sums += int(ord(i))
    for j in words:
        temp = 0
        for x in j:
            temp += int(ord(x))
        if(sums == temp):
            ans.append(j)
        print(temp)
        print(str(sums) + " yuh")

    print(ans)
#anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada'])
#anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer'])
#anagrams('aabb', ['bbaa', 'abab', 'baba', 'baab', 'abbab', 'abbaa', 'babaa'])


def rot13(message):
    alphabet_lower = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    alphabet_upper = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    ans = []
    fin = ""
    for i in range(len(message)):
        if(message[i].islower()):
            rot = alphabet_lower.index(message[i]) + 13
            if(rot > 25):
                ans.append(alphabet_lower[rot - 26])
            else:
                ans.append(alphabet_lower[rot])
        elif(message[i].isupper()):
            rots = alphabet_upper.index(message[i]) +13
            if (rots > 25):
                ans.append(alphabet_upper[rots - 26])
            else:
                ans.append(alphabet_upper[rots])
        else:
            ans.append(message[i])
    for z in ans:
        fin += z
    print(fin)

def convert_fracts(lst):
    denoms = []
    nums = []
    for j in range(len(lst)):
        denoms.append(lst[j][1])
    final_denom = math.lcm(*denoms)
    for i in range(len(denoms)):
        nums.append(final_denom // denoms[i])
    for z in range(len(lst)):
        lst[z][1] = final_denom
        lst[z][0] = nums[z]
    return(lst)

def generate_hashtag(s):
    ss = s.title()
    new = ss.replace(" ", "")
    if(new == ""):
        return False
    else:
        print("#" + new)

    print(an)
    print(ans)

#generate_hashtag('Do We have A Hashtag')
#generate_hashtag("hi are you")

#an = list(ss)
 #   ans = list(filter(partial(ne, " "),an))

def nameList(names):
    ans = []
    for i in range(len(names)):
        ans.append(names[i]['name'])
    if(len(names) == 0):
        return('')
    elif(len(ans) == 1):
        return(ans[0])
    elif(len(ans) == 2):
        return(ans[0] + "&" + ans[1])
    else:
        start = ans[:len(ans)-2]
        end = ans[-2:]
        ending = (' & '.join([str(x) for x in end]))
        starting = (', '.join([str(x) for x in start]))
        mid = ', '
        return(starting + mid + ending)


#nameList([{'name': 'Bart'},{'name': 'Lisa'},{'name': 'Maggie'},{'name': 'Homer'},{'name': 'Marge'}])
def score(dice):
    ne = ''
    for x in dice:
        ne += str(x)
    sum = 0
    one = ne.count('1')
    two = ne.count('2')
    three = ne.count('3')
    four = ne.count('4')
    five = ne.count('5')
    six = ne.count('6')

    if(3 == one):
        sum += 1000
    if(4 == one):
        sum += 1100
    if(5 == one):
        sum += 1200
    if(3 == six):
        sum += 600
    if(3 == five):
        sum += 500
    if(4 == five):
        sum += 550
    if (5 == five):
        sum += 600
    if(3 == four):
        sum += 400
    if(3 == three):
        sum += 300
    if(3 == two):
        sum += 200
    if(1 == one):
        sum += 100
    if(1 == five):
        sum += 50
    else:
        sum += 0

    print(sum)

#score( [2, 3, 4, 6, 2] )
#score([4, 4, 4, 3, 3])
#score( [2, 4, 4, 5, 4] )
#score([1,1,1,1,1])
#score([3,3,3,2,4])

def count_bits(n):
    a = bin(n)
    be = a[2:]
    fin = []
    sum = 0
    for a in be:
        fin.append(a)

    for z in fin:
        sum += int(z)

    print(sum)

def snail(snail_map):

    top = snail_map[0][:-1]
    sideOne = []
    bottom = []
    leftSide = []
    #FOR TOP
    for j in range(len(snail_map)):
        sideOne.append(snail_map[j][len(snail_map)-1])

    # FOR BOTTOM
    for x in range(len(snail_map)-1):
        bottom.append(snail_map[len(snail_map)-1][x])

    # FOR LEFTSIDE
    if(len(snail_map) % 2 == 1):
        for x in range(len(snail_map)):
            leftSide.append(snail_map[len(snail_map)//2 ][x])
    else:
        for a in range(len(snail_map)):
            leftSide.append((snail_map)[len(snail_map)//2 ][x])

    bottom.reverse()
    ne = leftSide[0:len(leftSide)-1]
    final = top + sideOne + bottom + ne

    print(final)



#snail([[1,2,3],[4,5,6],[7,8,9]])
#snail([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])



def solution(string, markers):
    print(string)
    news = list(string)
    yuh = string.replace('a','b')
    print(yuh)

#############################

def extract_digits(lst):
    return [[el] for el in lst]


def order_weight(strng):
    strng = strng.split()
    print(strng)
    ans = []
    for j in range(len(strng)):
        temp = 0
        for x in range(len(strng[j])):
            temp += int(strng[j][x])
        ans.append(temp)
    print(ans)
    for j in range(len(strng)):
        for x in ans[j]:
            print(str(strng[j]) + '=' + str(x))
    ans.sort()
    print(ans)


    #res = {ans[i]: strng[i] for i in range(len(ans))}
    #print(res)
    #fin = []
    #for key in sorted(res):
     #   fin.append(res[key])
    #print(fin)
    #print(' '.join(fin))###

#order_weight("103 123 4444 99 2000")
#order_weight("2000 10003 1234000 44444444 9999 11 11 22 123")


def increment_string(strng):
    if(strng[len(strng)-1].isnumeric() == False):
        print(strng + '1')
    else:
        li = list(strng)
        s = ''
        for x in li:
            if x.isnumeric() == True:
                s += x
        print(s)

        #ans = int(s) + 1
        #strng = strng.replace(s,'')
        #print(strng + str(ans))

def is_digit(n):
    match = re.match(r'7', n)
    if match:
        print('found', match.group())
    else:
        print("Did not find")

def pick_peaks(arr):
    peaks = []
    pos = []

    for x in range(1,len(arr)-1):
        if(arr[x] > arr[x-1] and arr[x] > arr[x+1]):
            peaks.append(arr[x])
            pos.append(x)
        if (arr[x] > arr[x - 1]  and arr[x] == arr[x + 1]):
            peaks.append(arr[x])
            pos.append(x)

    a = dict()
    a['pos'] = pos
    a['peaks'] = peaks

    print(a)

#pick_peaks([3,2,3,6,4,1,2,3,2,1,2,2,2,1])
#pick_peaks([1,2,3,6,4,1,2,3,2,1])
#pick_peaks([2,1,3,1,2,2,2,2])


def duplicate_count(text):
    tup = []
    for a in range(len(text)):
        for j in range(1,len(text)):
            if text[j] == text[a]:
                tup.append(a)


    print(tup)


def div42by(divideBy):
    try:
        print(42/divideBy)
    except ZeroDivisionError:
        print('Error: You tried to divide by Zero.')



myCat = {'size' : 'fat', 'persona' : 'dumb'}

#print(myCat['size'])
#print(list(myCat.values()))

import re

message = "Call me 415-55-1011 tomorrow, or at 415-555-9990"

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.findall(message)



def kaprekar_split(n):
    squared = n * n
    sqList = [str(x) for x in str(squared)]
    half = len(sqList) // 2
    first = sqList[:half]
    second = sqList[half:]

    fi = ''
    si = ''

    for i in first:
        fi += i
    if fi != '':
        fi = int(fi)
    else:
        fi = 0

    for j in second:
        si += j
    if si != '':
        si = int(si)
    else:
        si = 0

def add_arrays(array1, array2):
    # your code here
    sum = []
    if len(array1) == len(array2):
        for i in range(len(array1)):
            sum.append(array1[i] + array2[i])
        print(sum)
    else:
        print("Error")


def diamond(n):
    tt = []
    for num in range(1, n+1):
        if num % 2 != 0:
            tt.append(num)
    if n % 2 == 0:
        print(None)
    else:
        mid = n / 2 + 1
        for x in tt:
            print(x * '*')
        tt.reverse()
        tt.remove(tt[0])
        for z in tt:
            print(z * '*')
            print("\n")

# Simple Lambda Function
x = lambda a : a + 10
#print(x(5))

sequence = ['g', 'e', 'e', 'j', 'k', 's', 'p', 'r']
fun = ['a', 'e', 'i', 'o', 'u']

#Filter Function
zaba = (filter(fun, sequence))


#import json

#x = '{ "name":"John", "age":30, "city":"New York"}'

#y = json.loads(x)

#print(y["age"])

#z = {
    #"name" : "John",
   # "age" : 30,
   # "city" : "New York"
#}

#ag = json.dumps(z)
#print(ag)

#print(json.dumps(True))

def over_the_road(address, n):
    print(n * 2 + address + 1)


def pos_average(s):
    av1 = 0
    av2 = 0
    av3 = 0
    sup = [int(x) for x in s.split(',')]
    print(sup)




#pos_average("466960, 069060, 494940, 060069, 060090, 640009, 496464, 606900, 004000, 944096")

def twoSum(nums, target):
    for x in range(len(nums)):
        for j in range(x + 1, len(nums)):
            if nums[x] + nums[j] == target:
                print(x, j)

#twoSum([3,2,3],6)
#twoSum([2,7,11,15],9)

def reverse(x):
    placeHolder = 0
    if x < 0:
        placeHolder = -1
    equalizer = abs(x)
    duh = [int(j) for j in str(equalizer)]
    duh.reverse()
    doi = [str(integer) for integer in duh]
    finOne = "".join(doi)
    finale = int(finOne)
    print(finale, "finale")
    print(placeHolder,  "placeholder")
    if placeHolder == 0:
        if (-2**31 <= finale <= (2**31 - 1)):
            print (finale)
        else:
            print (0)
    if placeHolder == -1:
        doi = (finale * placeHolder)
        if (-2**31 <= doi <= 2**31 - 1):
            print (doi)
        else:
            print (0)

#reverse(123)
#reverse(-12)



def isPalindrome(x):
    tiptop = str(x)
    halfs = len(tiptop) // 2
    checkOne = []
    checkTwo = []
    for j in tiptop[:halfs]:
        checkOne.append(j)
    for z in tiptop[halfs + 1:]:
        checkTwo.append(z)
    checkTwo.reverse()
    if (len(tiptop) % 2 == 0 or x < 0):
        print(False)
    if checkOne == checkTwo:
        print(True)



#isPalindrome(1032301)
#isPalindrome(10)

from functools import reduce



def persistence(n):
    res = [int(x) for x in str(n)]
    ad = reduce(lambda x, y: x*y, res)
    if(ad > 10):
        persistence(ad)
    else:
        return(ad)




#persistence(39)


#def fibbonaci(n):
    for x in range(0,n):
        for i in range(0,x+1):
            print(binomialCoeff(x,i),
                " ", end = "")
        print()


def binomialCoeff(n, k):
    res = 1
    if (k > n - k):
        k = n - k
    for i in range(0, k):
        res = res * (n - i)
        res = res // (i + 1)

    print(res)

#binomialCoeff(1,3)

import string

def listAlphabet(n):
    lower = list(string.ascii_lowercase)
    upper = list(string.ascii_uppercase)
    fin = []
    for i in range(len(n)):
        if n[i].islower():
            fin.append(str(lower.index(n[i])+1))
        elif n[i].isupper():
            fin.append(str(upper.index(n[i])+1))
    print(fin)
    print(" ".join(fin))

#listAlphabet("The sunset sets at twelve o' clock.")

def christmasTree(height):
    ayo = []
    for x in range(1, height):
        if x % 2 != 0:
            ayo.append(x)
    print(ayo)
    for j in ayo:
        print(j * '*')

#christmasTree(4)

def compute_sum(n):
    sum = 0
    if n < 10:
        for i in range(n+1):
            sum += i
        print(sum)
    else:
        te = 45
        for j in range(n+1):
            if j >= 10:
                for digit in str(j):
                    sum += int(digit)
        print(te + sum)

#compute_sum(10)
#compute_sum(12)


def dig_pow(n, p):
    ayo = []
    powpow = []
    for x in str(n):
        ayo.append(x)
    for j in range(p,len(ayo)+p):
        powpow.append(j)
    fin = 0
    for z in range(len(powpow)):
        fin += (int(ayo[z])**(powpow[z]))
    if fin % n == 0:
        print(fin // n)
    else:
        print(-1)

#dig_pow(46288, 3)
import collections

def highest_rank(arr):
    theCount = collections.Counter(arr)
    theKeys = []
    temp = 0
    fin = []
    for key in theCount.items():
        theKeys.append(key[1])
    for j in range(len(theKeys)):
        if theKeys[j] > temp:
            temp = theKeys[j]
    for number, count in theCount.items():
        if count == temp:
            fin.append(number)
    print(max(fin))

#highest_rank([12, 10, 8, 12, 7, 6, 4, 10, 12])
#highest_rank([12, 10, 8, 12, 7, 8, 4, 8, 12])


def find_even_index(arr):
    for j in range(len(arr)):
        if sum(arr[:j]) == sum(arr[j+1:]):
            print(j)
            break
    else:
        print


#find_even_index([1,2,3,4,3,2,1])
#find_even_index([1,100,50,-51,1,1])



#if sum(arr[:j]) == sum(arr[j+1:]):
    #print(arr[j])
    #break

def sum_pairs(ints, s):
    ans = []
    for x in ints:
        for j in ints[1:]:
            if x + j == s:
                ans.append(x)
                ans.append(j)
    if len(ans) > 0:
        print(ans[:2])
    else:
        print(None)


l1= [1, 4, 8, 7, 3, 15]
l2= [1, -2, 3, 0, -6, 1]
l3= [20, -13, 40]
l4= [1, 2, 3, 4, 1, 0]
l5= [10, 5, 2, 3, 7, 5]
l6= [4, -2, 3, 3, 4]
l7= [0, 2, 0]
l8= [5, 9, 13, -3]

from functools import reduce
import operator

def dum_pairs(ints, s):
    ints_dict = {}
    for i in range(len(ints)):
        int2expect = s - ints[i]
        print(s,ints[i])
        if int2expect in ints_dict:
            return [int2expect, ints[i]]
        ints_dict[ints[i]] = None
#dum_pairs(l4, 2)
#dum_pairs(l1, 8)
#dum_pairs(l2, -6)



def duplicate_count(text):
    d = collections.defaultdict(int)
    completeText = text.upper()
    for c in completeText:
        d[c] += 1

    counter = 0
    for j in d.values():
        if j > 1:
            counter += 1


    print(counter)

#duplicate_count(1,1,1,2,3,3,4)

def dirReduc(arr):
    z = collections.defaultdict(int)
    for c in arr:
        z[c] += 1
    ayo = []
    yah = []
    for a in z.items():
        if a[0] == 'NORTH' or a[0] == 'SOUTH':
            ayo.append(a)
        else:
            yah.append(a)
    if ayo[0][1] == ayo [1][1]:
        vert = True
    else:
        pass

    print(z)
    print(ayo)
    print(yah)
    print(vert)


#dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"])

#duplicate_count('abcdeaa')
#duplicate_count('abcdeaB')
#duplicate_count("Indivisibilities")

def find_uniq(arr):
    d = collections.defaultdict(int)
    for c in arr:
        d[c] += 1

    counter = 0
    for num, occurrence in d.items():
        if occurrence == 1:
            print(num)



#find_uniq([1,1,1,2,1,1])
#find_uniq([ 0, 0, 0.55, 0, 0 ])
#find_uniq([ 3, 10, 3, 3, 3 ])

def tribonacci(signature,n):
    z = 0
    if n == 0:
        return []
    if n < 3:
        return signature[:n]


    while len(signature) < n:
        signature.append(sum(signature[z:z+3]))
        z += 1
    print(signature)

#tribonacci([1, 1, 1], 10)



myset = set(['a','b','c'])
#print(myset)

theCs = {0:'A', 1 : 2, 2: 3, 3 : 4, 4 : 5, 5 : 6, 6 : 7, 7 : 8, 8 : 9, 9 : 'T', 10 : 'J', 11: 'Q', 12 : 'K'}
theDs = {13:'A', 14 : 2, 15: 3, 16 : 4, 17 : 5, 18 : 6, 19 : 7, 20 : 8, 21 : 9, 22 : 10, 23 : 11, 24: 12, 25: 'K'} # REdo all
theHs = {26:'A', 27 : 2, 28: 3, 29 : 4, 30 : 5, 31 : 6, 32 : 7, 33 : 8, 34 : 9, 35 : 10, 36 : 11, 23: 12}
theSs = {39:'A', 13 : 2, 14: 3, 15 : 4, 16 : 5, 17 : 6, 18 : 7, 19 : 8, 20 : 9, 21 : 10, 22 : 11, 23: 12}


def encode(cards):
    return

def decode(cards):
    returns


def valid_parentheses(string):
    x = []
    for j in string:
        if j == '(':
            x.append(j)
        elif j == ')':
            try:
                x.pop()
            except:
                print(False)

    if len(x) == 0:
        return True
    else:
        return False


#valid_parentheses("hi())(")

def DNA_strand(dna):
    theList = list(dna)
    for a in range(len(theList)):
        if 'A' == dna[a]:
            theList[a] = 'T'
        elif 'T' == dna[a]:
            theList[a] = 'A'
        elif 'G' == dna[a]:
            theList[a] = 'C'
        elif 'C' == dna[a]:
            theList[a] = 'G'

    print(theList)

#DNA_strand("AAAA")


def is_valid_walk(walk):
    d = collections.defaultdict(int)
    for c in walk:
        d[c] += 1
    vert = []
    side = []
    for dum, pair in d.items():
        if dum == 'n' or dum == 's':
            vert.append(pair)
        else:
            side.append(pair)

    if vert[0] == vert[1]:
        duh = True
    else:
        duh = False

    if len(walk) == 10:
        if duh & yuh == True:
            return True
    else:
        return False

#is_valid_walk(['n','s','n','s','n','s','n','s','n','s'])
#is_valid_walk(['w','e','w','e','w','e','w','e','w','e','w','e'])
#is_valid_walk(['e', 'n', 'w', 's', 's', 's', 'e', 'w', 'n', 's'])


def format_duration(seconds):
    numDays = [n/(24*3600)]
    numHours = [(n% (24 *3600))/3600]
    numMinutes = [(n%(24*3600*3600))/60]
    numSeconds = [(n%(24* 3600 * 3600 * 60))/60]

    if seconds == 1:
        print(1 + "1 second")
    elif seconds < 60 and seconds > 1:
        pass



def atm(withdrawal, account):
    if 0 < withdrawal <= 2000 and 0 <= account <= 2000:
        if withdrawal % 5 == 0 and withdrawal <= account:
            account = account - (withdrawal + .50)
            print(format(account,".2f"))
        else:
            print(format(account,".2f"))

#if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    newArr = list(arr)
    tempMax = max(newArr)
    newArr = [x for x in newArr if x != tempMax]
    fin = max(newArr)
    print(fin)

#def solution(arr):
#    for j in range(len(arr):
#        for x in range(j+1):
#solution(['1','2','3','45','3','2','1','2','2'])




class Robot():
    #The init function is used to assign values and properties toward objects
    def __init__(self, name, age, number):
        self.name = name
        self.age = age
        self.number = number

    def greet(self):
        print("Hi my name is " + self.name)

    def none(self):
        pass
#Example of Inheritance with Human inheriting properties and functions from the previous Class, Robot
class Human(Robot):
    #If i add an __init__ function the class will no longer inherit
    pass

p1 = Robot("Aneek", 18, 1294915995)

#p1.greet()
#print(p1)

#x2 = Human("Baba", 52, 123901905)
#x2.greet()


mytuple = ("Apple", "Bananas", "Cherry")
mit = iter(mytuple)
#print(next(mit))

import module
from module import bye

#module.bye("Aneek")



def narcissistic(value):
    yah = len(str(value))
    dub = [int(x) for x in str(value)]
    print(dub)
    ans = []
    for j in dub:
        ans.append(j ** yah)
    if sum(ans) != value:
        return True
    else:
        return False



def order(sentence):
    yah = ''.join(sentence).split()
    du = []
    for i in yah:
        for j in i:
            if j.isalpha() == False:
                du.append(j)

    dictionary = dict(zip(du,yah))
    fin = []
    for i in sorted (dictionary.keys()):
        fin.append(dictionary[i])

    return(" ".join(fin))

#order("is2 Thi1s T4est 3a")


import re
from collections import Counter

def top_3_words(text):
    words = re.findall("[a-z']+", text.lower())
    print([el[0] for el in Counter(words).most_common(3) if re.search('[a-z]', el[0])])


#top_3_words("e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e")
#top_3_words("  //wont won't won't ")
#top_3_words("  '  ")
#top_3_words("yuh buh ruh")
#top_3_words("a a c b b")


















