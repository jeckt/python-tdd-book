==================================================
Notes on Test Driven Development (TDD) with Python
==================================================

TDD emphasises incrementally building application through testing.

Functional testing is testing how the application functions from the user's
point of view. We do this through the use of Selenium.

Functional test == Accceptance test == End-to-End test == Black box test

On the other side there are unit tests which test the application from the
inside i.e. the programmer's point of view.

Functional tests help build apps with the right functionality and 
guarantees you will never accidentally break it. Unit tests help in writing
code that's clean and bug free.

=============
TDD Work Flow
=============

1. Write functional tests / user story
2. Design code to resolve user story and write one or more
   unit tests to define how the code should behave
3. Write the *smallest amount of application code* to pass
   the unit test. Iterate until enough progress is made
   on the functional test.
4. Rerun functional tests and see if they pass

TEST! TEST! TEST!

======
Django
======

Django generally follows the MVC pattern however its views are more like
controllers while their templates are more like views.

Work Flow
---------
User through the browser provides inputs (GET, POST) which forms a `HTTP
Request` which the Django resolves through the projects urls/app urls and
directs to a Django view which then process the request, access the database
required and returns a HttpResponse which may include a template (HTML).

============
Unit Testing
============

Python standard libraries include a ``unittest`` module which provides
methods such as:

To use the unittest module, create a class that subclasses unittest

::

    class MyTest(unittest.TestCase):
        def setUp(self):
            # set up for each test

        def tearDown(self):
            # clean up code for each test

        def test_dummy(self):
            # some test

    if __name__ == '__main__':
        unittest.main()

Django has it's own unittest module which extends the python standard
library unittest. ``django.test``
