# Automatic Tester for self.py Course Exercises

![CodeQL security analysis](https://github.com/izmirli/self.py_tester/workflows/CodeQL/badge.svg)
![OSSAR analysis](https://github.com/izmirli/self.py_tester/workflows/OSSAR/badge.svg)
![Pylint and pycodestyle](https://github.com/izmirli/self.py_tester/workflows/Pylint%20and%20pycodestyle/badge.svg)

### עברית

* [וידאו הסבר בעברית](https://youtu.be/pzhG9yFcaGg)
* בין הקבצים במאגר יש שני קבצי הוראות בעברית - קצרות ומלאות

## Intro
[Campus-IL's **self.py** course](https://campus.gov.il/course/course-v1-cs-gov_cs_selfpy101/) is a free Python beginners massive open online course.

It has a lot of exercises, many of them are Python code writing tasks. These code writing exercises are not checked by anybody or anything (Except the last, and only for paid upgrade). The students, especially as this is a beginners course, don't know if their code fulfilled the exercise requirements. They have no feedback, and might think they did OK even if they have bugs and/or did not implement what they should have.

## What this project does
Using Python's [unittest](https://docs.python.org/3/library/unittest.html) unit testing framework, automatic tests were writen for most of the code writing exercises that have functions (Units 5-9). These tests can be used to check student's exercise solution.

## How to use
[More information can be found in Wiki](https://github.com/izmirli/self.py_tester/wiki/Usage)

### Setup

There is one main test file (**`test_self.py`**) and a few auxiliary files - all files should be in the same folder.

In the above folder (test_self.py is in) create a new (empty) file by the name: **`self.py`**

Some external modules should be installed. Though not mandatory, it enhances the tests and easy to do. 
In the command prompt, at the above folder, run this command:

```python -m pip install -r requirements.txt```

### Usage

For each exercise:
1. Add the functions you were asked to implement (one or more) to **self.py** file (exact function names mast be used).
2. In the command prompt (cmd) run this command:
`python test_self.py`
3. Read tests output.

### Example

#### Testing 1st exercise

For **exercise 5.3.4** (the 1st exercise checked in these automated tests), function name mast be **`last_early`**, so add your implementation of the function to **self.py** file:
```
def last_early(my_str):
    ...
```
Open command prompt (cmd) and run the tests with: `python test_self.py`

If all is OK, output should look something like this:
```
Exercise 5.3.4 (last_early): OK
----------------------------------------------------------------------
Ran 38 tests in 0.004s

OK (skipped=37)
 1 exercises done successfully
32 exercises left to do
        Next exercises: 5.3.5 (distance), 5.3.6 (filter_teens), 5.3.7 (chocolate_maker)
```

#### Testing 2nd exercise

For the next exercise, **5.3.5**, function name mast be **`distance`**. Add it to **self.py** file (after the previous function from Exercise 5.3.4):
```
def distance(num1, num2, num3):
    ...
```
Now run the tests with same command as before: `python test_self.py`

If all is OK, output should look something like this:
```
Exercise 5.3.4 (last_early): OK
Exercise 5.3.5 (distance): OK
----------------------------------------------------------------------
Ran 38 tests in 0.000s

OK (skipped=36)
 2 exercises done successfully
31 exercises left to do
        Next exercises: 5.3.6 (filter_teens), 5.3.7 (chocolate_maker), 5.4.1 (func)

```
If you'll have a bug in your function, a test for this exercise might fail and the output may look like this:
```
Exercise 5.3.4 (last_early): OK
Exercise 5.3.5 (distance): FAIL
---
True != False : Failed on: num1=4, num2=5, num3=3
---
----------------------------------------------------------------------
Ran 38 tests in 0.007s

FAILED (failures=1, skipped=36)
 1 exercises have problems
 1 exercises done successfully
31 exercises left to do
        Next exercises: 5.3.6 (filter_teens), 5.3.7 (chocolate_maker), 5.4.1 (func)
```

## Disclaimer
This content is not affiliated with, endorsed, sponsored, or specifically approved by National Cyber Directorate, Cyber education center and Campus-IL (or anyone else related to self.py course), and they are not responsible for it.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
