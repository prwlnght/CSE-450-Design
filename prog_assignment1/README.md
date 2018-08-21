Assignment 1
Description Document

Steps:
1.	Start by cloning (or downloading) the github repository into a workspace folder on your workstation (how) from the following link
2.	Modify ‘resources_unix.py’ or ‘resources_windows.py’ to put the correct value of ‘workspace_dir’ according to your workstation setup.
a.	If you are using a windows machine modify resources_windows.py
b.	If you are using a unix (linux or mac) machine modify resources_unix.py
c.	For the absolute path for  my CSE-450-Design folder is ‘C:\Users\ppaudyal\workspace\CSE-450-Design’ so I set
i.	workspace_dir = os.path.join('C:\\', 'Users', 'ppaudyal', 'workspace', 'CSE-450-Design')
3.	Make your changes to ‘prog_assignment1 > gale_shapley.py’

Github repository url: https://github.com/prwlnght/CSE-450-Design.git

Input:

1.	A hospital preference dictionary
2.	A student preference dictionary

Input format:
1.	One python .pickle with with two dictionaries one for hospital preferences and one for student preferences


Output:
1.	A single dictionary with hospital number as key and matched student as value
2.	A single dictionary with student number as key and matched hospital as value
3.	An int that keeps track of total proposals made in the algorithm.


Reading Materials:
1.	Brush up on python (dictionaries, pickle)
2.	Learn how to clone a git repository from url.
3.	Book chapter on Gale-Shapley

Grading Criteria:
1.	Pass all test cases (3 per test file) . All test cases are specified in galey_shapley_test.py. Run this file to get current score.
2.	10 total files will be tested with (5 sample files are provided)
3.	Unseen but similar preference files will be used
4.	The output on our test files will be your score
5.	Automated testing will be used, so please follow submission instructions below correctly

Test cases: (For each of 10 test files)
1.	Perfect matching (2 points)
2.	Stable matching (4 points)
3.	Efficient Algorithm (4 points)
4.	You can make as many test files as you want by running helpers > generate_pickles.py and changing the arguments in the main function
5.


Submission Instructions:
1.	Modify only the python file ‘gale_shapley.py’
2.	Run ‘gale-shapley-test.py’ with different test files (generate from helper>generate_testfiles.py for more tests), the output of the file is your score for one test file, or just have multiple test files in the test_files folder.
3.	Use python 3.x for all coding
4.	All directory paths should be relative (test by running after moving CSE-450-Design folder into another directory)
5.	Clear all test_files you generated
6.	Create an archive of the following format:
a.	[ASURITEID_lastname].zip
b.	Please do not use any other archive formats


