#Test Notes

##PostTestCase

##CategoryTestCase

##FrontEndTestCase



###Django TestCase Classes

- *SimpleTestCase* is for basic unit testing with no ORM requirements

- *TransactionTestCase* is useful if you need to test transactional actions (commit and rollback) in the ORM

- *TestCase* is used when you require ORM access and a test client

- *LiveServerTestCase* launches the django server during test runs for front-end acceptance tests.

https://docs.djangoproject.com/en/1.11/topics/testing/overview/