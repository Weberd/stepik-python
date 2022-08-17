# class ExtendedStack(list):
#     def sum(self):
#         top1 = self.pop()
#         top2 = self.pop()
#         self.append(top1 + top2)
#
#     def sub(self):
#         top1 = self.pop()
#         top2 = self.pop()
#         self.append(top1 - top2)
#
#     def mul(self):
#         top1 = self.pop()
#         top2 = self.pop()
#         self.append(top1 * top2)
#
#     def div(self):
#         top1 = self.pop()
#         top2 = self.pop()
#         self.append(top1 // top2)
#
# import time
#
# class Loggable:
#     def log(self, msg):
#         print(str(time.ctime()) + ": " + str(msg))
#
# class LoggableList(list, Loggable):
#     def append(self, e):
#         super(LoggableList, self).append(e)
#         self.log(e)
#
# ll = LoggableList()
# ll.append(5)

# import datetime
#
# year, month, day = list(map(int, input().split()))
# days = int(input())
#
# date = datetime.date(year, month, day)
# days = datetime.timedelta(days=days)
# result = date + days
#
# print(result.year, result.month, result.day)


# hierarchy = {}
#
# def search(parent, child):
#     if parent == child:
#         return True
#     if child not in hierarchy:
#         return False
#     if parent in hierarchy[child]['parents']:
#         return True
#     res = False
#     for current_parent in hierarchy[child]['parents']:
#         res = res or search(parent, current_parent)
#     return res
#
# n = int(input())
# for a in range(n):
#     rule = input().split(' : ')
#     child = ''
#     parents = ''
#     if len(rule) > 1:
#         child = rule[0]
#         parents = rule[1]
#     else:
#         child = rule[0]
#     parents = parents.split()
#     if not child in hierarchy:
#         hierarchy[child] = {'parents': []}
#     for parent in parents:
#         if parent not in hierarchy:
#             hierarchy[parent] = {'parents': []}
#         hierarchy[child]['parents'].append(parent)
#
# n = int(input())
# declared = []
#
# for a in range(n):
#     current = input()
#     for d in declared:
#         if search(d, current):
#             print(current)
#             break
#     declared.append(current)

import math

# def is_prime(n):
#     if n in [2, 3, 5, 7, 11]:
#         return True
#     return (math.factorial(n - 1) + 1) % n == 0
#
# def primes():
#     n = 2
#     while True:
#         if is_prime(n):
#             yield n
#         n += 1
#
# p = primes()
# for i in range(31):
#     print(next(p))

# def mod_checker(x, mod=0):
#     return lambda y: y % x == mod
#
# mod_3 = mod_checker(3)
# print(mod_3(3))
# print(mod_3(4))
#
# mod_3_1 = mod_checker(3, 1)
# print(mod_3_1(4)) # True

# s = input()
# a = input()
# b = input()
#
# count = 0
#
# while s.find(a) != -1:
#     s = s.replace(a, b)
#     count += 1
#     if count > 1000:
#         count = 'Impossible'
#         break
#
# print(count)

# import re
# s = input()
# t = input()
# print(len(re.findall('(?=' + t + ')', s)))

# import sys
# import re
#
# for line in sys.stdin:
#     if re.search(r"\bcat\b", line):
#         print(line.rstrip())

# import sys
# import re
#
# for line in sys.stdin:
#     if re.search(r"z.{3}z", line):
#         print(line.rstrip())

# import sys
# import re
#
# for line in sys.stdin:
#     if re.search(r"\\", line):
#         print(line.rstrip())

# import sys
# import re
#
# for line in sys.stdin:
#     if re.search(r"\b(.*)\1\b", line).group() != '':
#         print(line.rstrip())

# import sys
# import re
#
# for line in sys.stdin:
#     print(re.sub('human', 'computer', line).rstrip())

# import sys
# import re
#
# for line in sys.stdin:
#     print(re.sub("a+", "argh", line, 0, re.IGNORECASE).rstrip())

# import sys
# import re
#
# for line in sys.stdin:
#     print(re.sub(r"\b(\w)(\w)(.*?)\b", r"\2\1\3", line).rstrip())


# import sys
# import re
#
# for line in sys.stdin:
#     print(re.sub(r"(\w)\1{1,}", r"\1", line).rstrip())


# import sys
# import re
#
# for line in sys.stdin:
#     match = re.search("0*((1(01*0)*1)*0*)*", line)
#     if match:
#         line = line.rstrip()
#         if match.group() == line:
#             print(line)

# import csv
# from collections import Counter
#
# with open('Crimes.csv') as file:
#     reader = csv.reader(file)
#     data = list(filter(lambda x: x[2].find('/2015') != -1, list(reader)[1:]))
#     crimes = list(zip(*data))[5]
#     print(crimes)
#     crime_counts = Counter(crimes)
#     print(crime_counts.most_common(1))

# import os
#
# with open('result.txt', 'a') as f:
#     for current_dir, dirs, files in os.walk('main'):
#         if list(filter(lambda x: x.endswith('.py'), files)):
#             f.write('{}\n'.format(current_dir))

import re
import urllib.request
from urllib.parse import urlparse

import re
import urllib.request
from urllib.parse import urlparse

# url = input()
# page = urllib.request.urlopen(url)
# content_bytes = page.read()
# content_str = content_bytes.decode("utf8")
# page.close()
#
# content_str = '<a href="http://stepic.org/courses">\n<a href=\'https://stepic.org\'>\n<a href=\'http://neerc.ifmo.ru:1345\'>\n<a href="ftp://mail.ru/distib" >\n<a href="ya.ru">\n<a href="www.ya.ru">\n<a href="../skip_relative_links">'
#
# def parse_link(link):
#     parsed_uri = urlparse(link)
#     if parsed_uri.netloc:
#         res = parsed_uri.netloc
#     else:
#         res = parsed_uri.path
#     try:
#         return res[:res.index(':')]
#     except:
#         return res
#
#
# links = re.findall(r'<a.+href=[\'"]([^./][^\'"]*)[\'"]', content_str)
# [print(link) for link in sorted(list(set(list(map(parse_link, links)))))]

# import re
# import urllib.request
#
# a = input()
# b = input()
#
#
# def get_links(url):
#     try:
#         fp = urllib.request.urlopen(url)
#         content_str = fp.read().decode("utf8")
#         fp.close()
#         links = re.findall(r'<a.*href=[\'"]([^\""]*)[\'"]', content_str)
#     except:
#         return []
#     else:
#         return links
#
#
# links = get_links(a)
# res = False
#
# for link in links:
#     links2 = get_links(link)
#     if b in links2:
#         res = True
#         break
#
# if res:
#     print('Yes')
# else:
#     print('No')

import json

with open('dataset_24476_3.txt') as file:
    for number in file:
        number = number.strip()
        params = {'default': 'Boring number is boring', 'json': True}
        url = 'http://numbersapi.com/{}/math?json=true'.format(number)
        # res = requests.get(url, params=params).text
        fp = urllib.request.urlopen(url)
        content_str = fp.read().decode("utf8")
        fp.close()
        data = json.loads(content_str)
        # print(data)
        if not data['found']:
            print('Boring')
        else:
            print('Interesting')