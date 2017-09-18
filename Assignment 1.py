class linked_list:
    front = back = None
    current = None  # used in iterator

    def push_front(self, value):
        if self.empty():
            self.front = self.back = self.node(value, None)
        else:
            george = self.front
            self.front = self.node(value, None)
            self.front.next = george
    def push_back(self, value):
        if self.empty():
            self.front = self.back = self.node(value, None)
        else:
            joe = self.node(value, None)
            self.back.next = joe
            self.back = joe
    def pop_front(self):
        if self.empty():
            raise RuntimeError
        elif self.front == self.back:
            madKing = self.front.value
            self.front = self.back = None
            return madKing
        else:
            ray = self.front.value
            self.front = self.front.next
            return ray
    def pop_back(self):
        if self.empty():
            raise RuntimeError
        elif self.front== self.back:
            micoo = self.front.value
            self.front = self.back = None
            return micoo
        else:
            gavy = self.back.value
            q = self.front
            while q.next != self.back:
                q = q.next
            self.back = q
            self.back.next = None
        return gavy
    def empty(self):
        if self.front == self.back == None:
            return True
        else:
            return False

    class node:
        def __init__ (self, value, next):
            self.value = value
            self.next = next

import unittest
class test_linked_list (unittest.TestCase):
    def test_none(self):
        self.assertTrue(linked_list().empty())
    def test_pop_front_empty(self):
        self.assertRaises(RuntimeError, lambda: linked_list().pop_front())
    def test_pop_back_empty(self):
        self.assertRaises(RuntimeError, lambda: linked_list().pop_back())
    def test_push_back_pop_front(self):
        ll = linked_list()
        ll.push_back(1)
        ll.push_back(2)
        ll.push_back(3)
        self.assertFalse(ll.empty())
        self.assertEquals(ll.pop_front(), 1)
        self.assertEquals(ll.pop_front(), 2)
        self.assertEquals(ll.pop_front(), 3)
        self.assertTrue(ll.empty())
    def test_push_front_pop_front(self):
        ll = linked_list()
        ll.push_front(1)
        ll.push_front(2)
        ll.push_front(3)
        self.assertEquals(ll.pop_front(), 3)
        self.assertEquals(ll.pop_front(), 2)
        self.assertEquals(ll.pop_front(), 1)
        self.assertTrue(ll.empty())
    def test_push_front_pop_back(self):
        ll = linked_list()
        ll.push_front(1)
        ll.push_front(2)
        ll.push_front(3)
        self.assertFalse(ll.empty())
        self.assertEquals(ll.pop_back(), 1)
        self.assertEquals(ll.pop_back(), 2)
        self.assertEquals(ll.pop_back(), 3)
        self.assertTrue(ll.empty())
    def test_push_back_pop_back(self):
        ll = linked_list()
        ll.push_back(1)
        ll.push_back("foo")
        ll.push_back([3,2,1])
        self.assertFalse(ll.empty())
        self.assertEquals(ll.pop_back(),[3,2,1])
        self.assertEquals(ll.pop_back(), "foo")
        self.assertEquals(ll.pop_back(), 1)
        self.assertTrue(ll.empty())
    def test_push_backness(self):
        oo = linked_list()
        oo.push_back(1)
        oo.push_back(2)
        oo.push_back(3)
        oo.push_back(4)
        oo.push_back(5)
        self.assertEqual(oo.pop_front(), 1)

class factorial:
    def fact(self, a):
        if a < 0: raise ValueError("Less than zero")
        if a == 0 or a == 1: return 1

        stack = linked_list()
        while a > 1:
            stack.push_front(a)
            a -= 1

        result = 1
        while not stack.empty():
            result *= stack.pop_front()

        return result

class test_factorial (unittest.TestCase):
    def test_less_than_zero(self):
        self.assertRaises(ValueError, lambda: factorial().fact(-1))
    def test_zero(self):
        self.assertEquals(factorial().fact(0), 1)
    def test_one(self):
        self.assertEquals(factorial().fact(1), 1)
    def test_two(self):
        self.assertEquals(factorial().fact(2), 2)
    def test_10(self):
        self.assertEquals(factorial().fact(10), 10*9*8*7*6*5*4*3*2*1)

if __name__ == '__main__':
        print (factorial().fact(1))
        print (factorial().fact(2))
        print (factorial().fact(100))