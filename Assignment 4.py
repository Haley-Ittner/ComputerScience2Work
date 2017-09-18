from __future__ import print_function
from sys import stdin
import unittest

class family_tree:
    def __init__ (self, init = None):
        self.__value = self.__name = self.__parent = None
        self.__left = self.__right = None

        if init:
            try:
                for i in init:
                    self.add(i[0], i[1])
            except TypeError:
                self.add(init[0], init[0])

    def __iter__(self):
        if self.__left:
            for node in self.__left:
                yield(node)

        yield(self.__value, self.__name)

        if self.__right:
            for node in self.__right:
                yield(node)

    """ Return a preorder list """
    def pre_order(self):
        result = []
        result += [(self.__value, self.__name)]
        if self.__left:
            result += self.__left.pre_order()
        if self.__right:
            result += self.__right.pre_order()
        return result

    """ Return an inorder list """
    def in_order(self):
        result = []
        if self.__left:
            result += self.__left.in_order()
        result += [(self.__value, self.__name)]
        if self.__right:
            result += self.__right.in_order()
        print(result)
        return result

    """ Return a postorder list """
    def post_order(self):
        result = []
        if self.__left:
            result += self.__left.post_order()
        if self.__right:
            result += self.__right.post_order()
        result += [(self.__value, self.__name)]
        return result

    def __str__(self):
        return(','.join(str(node) for node in self))

    def add(self, value, name):
        if self.__value == self.__left == self.__right == None:
            self.__value = value
            self.__name = name
            self.__parent = None
            return

        if value < self.__value:
            if not self.__left:
                self.__left = family_tree()
                self.__left.__parent = self
                self.__left.__value = value
                self.__left.__name = name
            else:
                self.__left.add(value, name)
        else:
            if not self.__right:
                self.__right = family_tree()
                self.__right.__parent = self
                self.__right.__value = value
                self.__right.__name = name
            else:
                self.__right.add(value, name)

    """ Given a value, return the node with that value. Useful in the
    next two methods """
    def __find(self, value):
        if self.__value == value: return self

        if self.__value > value:
            if self.__left:
                return self.__left.__find(value)
            else:
                raise(LookupError)

        if self.__value < value:
            if self.__right:
                return self.__right.__find(value)
            else:
                raise(LookupError)

    """ Given a value, return the name of that node's parent """
    def find_parent(self, value):
        person = self.__find(value)
        if not person:
            return None
        if not person.__parent:
            return None
        else:
            return person.__parent.__name

    """ Given a value, return the name of that node's grand parent """
    def find_grand_parent(self, value):
        person = self.__find(value)
        if not person:
            return None
        older_person = person.__parent
        if not older_person:
            return None
        else:
            return self.find_parent(older_person.__value)



    """ Create a list of lists, where each of the inner lists
        is a generation """
    """ First, create a list 'this_level' with the root,
                and three empty lists: 'next_level', 'result', and
                'names' """
    """ While 'this_level' has values """
    """ Get the first element and append its name to 'names' """

    """ If the first element has a left, append it to 'next_level'
                Do the same for the right """
    def generations(self):
        """ If 'this_level' is now empty """
        """ Append 'names' to 'result', set "this_level' to
        'next_level', and 'next_level' and 'names' to empty
                    lists """
        this_level = [self]
        next_level = []
        result = []
        names = []
        while this_level != []:
            curr = this_level.pop(0)
            names.append(curr.__name)
            if curr.__left:
                next_level.append(curr.__left)
            if curr.__right:
                next_level.append(curr.__right)
            if not len(this_level):
                result.append(names)
                this_level = next_level
                next_level = []
                names = []
        return result

class test_family_tree (unittest.TestCase):
    """
      20
     /  \
    10  30
       /  \
      25  35
    """
    def test_empty(self):
        self.assertEquals(str(family_tree()), '(None, None)')

    def setUp(self):
        self.tree = family_tree([(20, "Grandpa"), (10, "Herb"), \
        (30, "Homer"),(25, "Bart"), (35, "Lisa")])
        self.expected = "(10, 'Herb'),(20, 'Grandpa'),(25, 'Bart'),\
(30, 'Homer'),(35, 'Lisa')"

    def test_add(self):
        bt = family_tree()
        bt.add(20, "Grandpa")
        bt.add(10, "Herb")
        bt.add(30, "Homer")
        bt.add(25, "Bart")
        bt.add(35, "Lisa")
        self.assertEquals(str(bt), self.expected)

    def test_init(self):
        self.assertEquals(str(self.tree), self.expected)

    def test_parent(self):
        self.assertEquals(self.tree.find_parent(35), "Homer")

    def test_grand_parent(self):
        self.assertEquals(self.tree.find_grand_parent(35), "Grandpa")

    def test_generations(self):
        self.assertEquals(self.tree.generations(), \
            [['Grandpa'], ['Herb', 'Homer'], ['Bart', 'Lisa']])
    """Used the discussion board to help write unit tests."""
    def test_preorder(self):
        self.assertEquals(self.tree.pre_order(), \
            [(20, 'Grandpa'),(10, 'Herb'), (30, 'Homer'),(25, 'Bart'),(35, 'Lisa')])

    def test_inorder(self):
        self.assertEquals((self.tree.in_order()), \
                          [(10,'Herb'), (20,'Grandpa'), (25,'Bart'), (30,'Homer'), (35,'Lisa')])

    def test_postorder(self):
        self.assertEquals((self.tree.post_order()), \
                          [(10,'Herb'), (25,'Bart'), (35,'Lisa'), (30,'Homer'), (20,'Grandpa')])

    def test_tree_again(self):
        pp = family_tree()
        pp.add(15, "Chad")
        pp.add(20, "Chase")
        pp.add(25, "Chelsea")
        pp.add(30, "Charles")
        pp.add(35, "Charlie")
        pp.add(40, "Chicken")
        pp.add(45, "Cheetah")
        pp.add(50, "Cheese")
        self.assertEqual(str(pp), "(15, 'Chad'),(20, 'Chase'),(25, 'Chelsea'),(30, 'Charles'),(35, 'Charlie'),(40, 'Chicken'),(45, 'Cheetah'),(50, 'Cheese')")
    def test_in_order_new(self):
        pp = family_tree()
        pp.add(15, "Chad")
        pp.add(20, "Chase")
        pp.add(25, "Chelsea")
        pp.add(30, "Charles")
        pp.add(35, "Charlie")
        pp.add(40, "Chicken")
        pp.add(45, "Cheetah")
        pp.add(50, "Cheese")
        self.assertEqual(pp.in_order(), [(15, 'Chad'),(20, 'Chase'),(25, 'Chelsea'),(30, 'Charles'),(35, 'Charlie'),(40, 'Chicken'),(45, 'Cheetah'),(50, 'Cheese')])

    def test_generations_new(self):
        pp = family_tree()
        pp.add(15, "Chad")
        pp.add(20, "Chase")
        pp.add(25, "Chelsea")
        pp.add(30, "Charles")
        pp.add(35, "Charlie")
        pp.add(40, "Chicken")
        pp.add(45, "Cheetah")
        pp.add(50, "Cheese")
        self.assertEqual(pp.generations(), [['Chad'], ['Chase'], ['Chelsea'], ['Charles'], ['Charlie'], ['Chicken'], ['Cheetah'], ['Cheese']])

    def test_just_the_root_pre(self):
        qq = family_tree()
        qq.add(9, "Crazy")
        self.assertEqual(qq.pre_order(), [(9, 'Crazy')])

    def test_just_the_root_in(self):
        qq = family_tree()
        qq.add(9, "Crazy")
        self.assertEqual(qq.in_order(), [(9, "Crazy")])

    def test_just_the_root_post(self):
        qq = family_tree()
        qq.add(9, "Crazy")
        self.assertEqual(qq.post_order(), [(9, "Crazy")])

    def test_father_and_son_pre(self):
        ww = family_tree()
        ww.add(8, "Glegory")
        ww.add(2, "Ray")
        self.assertEqual(ww.pre_order(), [(8, "Glegory"), (2, "Ray")])

    def test_father_and_son_in(self):
        ww = family_tree()
        ww.add(8, "Glegory")
        ww.add(2, "Ray")
        self.assertEqual(ww.in_order(), [(2, "Ray"), (8, "Glegory")])

    def test_father_and_son_post(self):
        ww = family_tree()
        ww.add(8, "Glegory")
        ww.add(2, "Ray")
        self.assertEqual(ww.post_order(), [(2, "Ray"), (8, "Glegory")])

    """ Write your own tests for inorder etc. here """

if '__main__' == __name__:
    """ Read a file with lines of '# name'. Add each to a
    familty tree, and print out the resulting generations. """
    ft = family_tree()
    for line in stdin:
        a = line.strip().split(" ")
        ft.add(a[0], a[1])
    print(ft.generations())