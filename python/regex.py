import re


# name_age = '''
#     Himanshu is 21 and Aman is 18
#     Saket is 50 and Shubham is 31
# '''


# names = re.findall(r'[A-Z][a-z]*', name_age)
# ages = re.findall(r'\d{1,3}', name_age)

# dict_data = {}

# i = 0
# for name in names:
#     dict_data[name] = int(ages[i])
#     i+=1

# for i in range(len(names)):
#     dict_data[names[i]] = int(ages[i])

# for name, age in zip(names, ages):
#     dict_data[name] = int(age)


# print(dict_data)


# if re.search('inform', 'I have a information for you which I will inform you tomorrow'):
#     print('he will got information tomorrow')
#     print(re.search('inform', 'I have a information for you which I will inform you tomorrow'))
# else:
#     print('*****')


# allinform = re.findall(r'[0-z]or', 'I have a information for you which I will inform you tomorrow Bor Tor zor aor kor')
# print(allinform)


# allinform = re.finditer('inform', 'I have a information for you which I will inform you tomorrow')
# for i in allinform:
#     print(i.span())


# data = 'Sat, Tate, Pat, Xat, Date, lat, zat'
# result = re.findall(r'[S-l]at', data)

# for i in range(len(result)):
#     result[i] = result[i][:-1]
    
# print(result)


# data = 'mat rat sat bat cat'
# regex = re.compile(r'[rs]at')
# print(regex)

# result = re.compile(r'[rs]at').sub('food', data)
# print(result)


# data = 'This is \\nimanshu singh'
# print(re.search(r'\\nimanshu', data), '2')

# print(data)


# data = '''
# This is my world
# I can do
# what ever
# I want
# ,everything
# stop me if you
# can !!
# '''

# result = re.compile(r'\n').sub(' ', data)
# print(result)


# data = '123 1234 12345 123 456 1234567 890 20 1 28'
# result = re.findall(r'\d{3,7}', data)
# # result = re.findall(r'[0-3][7-9]', data)
# print(result)

# data = '''
# Phone Numbers
# 444-122-1234
# 123-122-78999
# 111-123-23
# 67-7890-2019
# '''

# result = re.findall(r'\d{3}-\d{3}-\d{4}', data)
# print(result)

# data = 'Thisworld12345_!#!$!'
# result = re.findall(r'[0-9A-Za-z]', data)
# print(result)

# data = 'Himanshu Singh'
# result = re.findall(r'\w{2,20}\s\w{2,20}', data)
# print(result)


# data = 'himan@gmail.com  sk@.com aman2@gmail.co fire@gmail.trio aman@gmail.com '
# result = re.findall(r'[\w]{1,20}@[\w]{2,20}.[A-Za-z]{2,3}', data)
# print(result)


data = "(123) 563-.4701"
result = re.findall(r'\([0-9]{3}\) [0-9]{3}-.[0-9]{3,4}', data)

print(result)