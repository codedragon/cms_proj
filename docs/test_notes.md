# Test Notes

Ran 4 tests in 0.075s

OK

```
python manage.py test
python manage.py test -v 2
```

## Coverage report: 70%
created at 2017-05-20 13:29

https://uwpce-pythoncert.github.io/Py300/testing.html

```
coverage run --source='.' --omit cmssite/wsgi.py manage.py test

coverage run my_program.py arg1 arg2
coverage report
coverage html
```


## Integration with coverage.py¶
https://docs.djangoproject.com/en/dev/topics/testing/advanced/#topics-testing-code-coverage

>Code coverage describes how much source code has been tested. It shows which parts of your code are being exercised by tests and which are not. It’s an important part of testing applications, so it’s strongly recommended to check the coverage of your tests.

>Django can be easily integrated with coverage.py, a tool for measuring code coverage of Python programs. First, install coverage.py. Next, run the following from your project folder containing manage.py:


`coverage run --source='.' manage.py test myapp`

>This runs your tests and collects coverage data of the executed files in your project. You can see a report of this data by typing following command:

`coverage report`

>Note that some Django code was executed while running tests, but it is not listed here because of the source flag passed to the previous command.

### TestCase

- PostTestCase
- CategoryTestCase
- FrontEndTestCase

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

What should I test?

How do I test ORM functions?