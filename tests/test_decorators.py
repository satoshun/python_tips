from . import TestCase

from decorators import cached_property


class TestCachedProperty(TestCase):
    def test_cached_property(self):
        l = []

        class A(object):
            @cached_property
            def func(self):
                l.append(1)
                return 100

            def func2(self):
                l.append(1)
                return 100

        a = A()
        a.func
        assert len(l) == 1
        a.func
        assert len(l) == 1

        a.func2()
        assert len(l) == 2
        a.func2()
        assert len(l) == 3
