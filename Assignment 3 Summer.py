from __future__ import print_function
import unittest

'''
Description: Stupid things go here.
Author: Someone Dumb
Version: 1.0
Help received from: My brain (people, URLs, etc.)
Help provided to: Me
'''

def findandreplace(find, replace, string):
    '''
        Replace all instances of find with replace in string.

        Recursive approach:
        If the string starts with find, return replace and findandreplace
        with the rest of the string, else return the first character of the
        string and findandreplace with the rest of the string
        '''
    print("String: ", string, "Find: ", find, "Replace: ", replace)
    if string == "":
        print("Empty String!")
        return ""
    if string == None:
        print("None String!")
        return None
    if find == "":
        return string
    if find == None and string != None:
        return string
    if replace == None:
        return string
    if find == string[:len(find)]:
        print("Found a match!")
        return replace + findandreplace(find, replace, string[len(find):])
    else:
        print("Continuing to search!")
        return string[:len(find)] + findandreplace(find, replace, string[len(find):])



class TestFindAndReplace(unittest.TestCase):
    def test_all_none(self):
        self.assertEqual(findandreplace(None, None, None), None)
    def test_find_none(self):
        self.assertEqual(findandreplace(None, "a", "aabb"), "aabb")
    def test_find_empty(self):
        self.assertEqual(findandreplace("", "a", "aabb"), "aabb")
    def test_replace_none(self):
        self.assertEqual(findandreplace("a", None, "aabb"), "aabb")
    def test_string_none(self):
        self.assertEqual(findandreplace("a", "b", None), None)
    def test_simple(self):
        self.assertEqual(findandreplace("a", "b", "aabb"), "bbbb")
    def test_remove(self):
        self.assertEqual(findandreplace(" ", "", " a abb"), "aabb")
    def test_gettysburg(self):
        self.assertEqual(findandreplace("Four score", "Twenty", \
            "Four score and seven years ago"), "Twenty and seven years ago")
    def test_something(self):
        self.assertEqual(findandreplace("Chickens", "Turkeys", "Chickens, wooooo"), "Turkeys, wooooo")
    def test_another(self):
        self.assertEqual(findandreplace("b", "a", "kinjbsba"), "kinjasaa")