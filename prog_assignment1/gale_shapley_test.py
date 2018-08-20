'''
copyright CSE450@asu 


todo

'''

import os
import pickle

import prog_assignment1.gale_shapley as gs

this_dir = os.getcwd()

test_dir = os.path.join(this_dir, 'test_files')

# run tests for each test_file

total_score = 0
test_file_counter = 0
for m_file in os.listdir(test_dir):
    if m_file.endswith('.pkl'):
        test_file_counter += 1
        with open(os.path.join(test_dir, m_file), 'rb') as f:
            pref_dict = pickle.load(f)

        # Each pickle file will have the hospital preferences as a dictionary and the student preferences as a dictionary
        hospital_prefs = pref_dict['hospitals']
        student_prefs = pref_dict['students']

        ordered_hospital_prefs, ordered_students_prefs = gs.gale_shapley_matching(hospital_prefs, student_prefs)

        # test cases
        try:
            assert len(ordered_hospital_prefs) == len(hospital_prefs)
            assert len(ordered_students_prefs) == len(student_prefs)
            total_score += 1
        except AssertionError as e:
            print(str(e))

        # write more test cases

print('Total score obtained for ', test_file_counter, ' test_files:', total_score)
print('Total socre for assignment: ', total_score)

