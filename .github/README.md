# Automatic Tester for self.py Course Exercises

## Intro
[Campus-IL's **self.py** course](https://campus.gov.il/course/course-v1-cs-gov_cs_selfpy101/) is a free Python beginers massive open online course.

It has 10 units with a lot of exercises, many of them are Python code writing tasks. Except for the last exercise, the code writing exercises are not checked by anybody or anything. The students, espasialy as this is a beginers course, don't know if their code fulfilled the exercise requirements. They have no feedback, and might think they did OK even if they have bugs and/or did not implement what they should have.

## What this project does
Using Python's [unittest](https://docs.python.org/3/library/unittest.html) unit testing framework, automatic tests were writen for most of the code writing exercises (Units 5-9). These tests can be used to check student's exercise solution.

## How to use
There is one main test file (**`test_self.py`**) and a few auxiliary files (that are used by some tests). All files should be in the same folder.

The student should:
1. In the folder test_self.py is in, create a new file by the name: **`self.py`**
1. Add the functions you were asked to implemnt (one or more) to **self.py** file (exact function names mast be used).
1. In the command prompt (not Python interpreter/console) run this command:
   * For all tests: `python -m unittest -v test_self.SelfPyTestCase`
   * For a single test: `python -m unittest -v test_self.SelfPyTestCase.test_ex_x_y_z` (x, y, z for exercise x.y.z)

### Example
For **exercise 5.3.7**, function name mast be **`chocolate_maker`**, so add your implementation of the function to **self.py** file:
```
def chocolate_maker(small, big, x):
    ...
```
and run the test [only] for it by: `python -m unittest -v test_self.SelfPyTestCase.test_ex_5_3_7`

If all is OK, this should be the output:
```
test_ex_5_3_7 (test_self.SelfPyTestCase)
Testing chocolate_maker function ... ok

----------------------------------------------------------------------
Ran 1 test in 0.001s

OK
```

## Disclaimer
This content is not affiliated with, endorsed, sponsored, or specifically approved by National Cyber Directorate, [Cyber education center](https://cyber.org.il/) and Campus-IL (or anybody else related to self.py course), and they are not responsible for it.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
