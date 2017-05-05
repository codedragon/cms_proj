# Test Notes

## PostTestCase

## CategoryTestCase

## FrontEndTestCase



### Django TestCase Classes

- _SimpleTestCase_ is for basic unit testing with no ORM requirements

- _TransactionTestCase_ is useful if you need to test transactional actions (commit and rollback) in the ORM

- _TestCase_ is used when you require ORM access and a test client

- _LiveServerTestCase_ launches the django server during test runs for front-end acceptance tests.

https://docs.djangoproject.com/en/1.11/topics/testing/overview/


    POST = Create
    GET = Read
    PUT = Update
    DELETE = Delete
