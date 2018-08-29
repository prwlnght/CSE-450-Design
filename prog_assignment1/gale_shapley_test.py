'''
copyright CSE450@asu 


todo

'''

import os, sys, platform
import pickle
import sys


#setting current working directory to this directory 
working_directory = os.getcwd()
os.chdir(os.path.dirname(os.path.abspath(__file__)))

sys.path.append('../')


if platform.system() == 'Windows':
    import resources_windows as resources
else:
    import resources_unix as resources

import prog_assignment1.gale_shapley as gs
# import prog_assignment1.impl.gale_shapley_impl as gs

workspace_dir = resources.workspace_dir
test_dir = os.path.join(workspace_dir, 'prog_assignment1', 'test_files')

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

        hospitals_dict, student_dict, total_proposals = gs.gale_shapley_matching(hospital_prefs, student_prefs)

        # test case 0 : sanity check
        stable_matching = False

        try:
            assert len(hospital_prefs.values()) == len(student_prefs.keys())
            assert len(hospitals_dict.keys()) == len(hospital_prefs.keys())
            print('All were returned')
            total_score += 0
        except AssertionError as e:
            print(str(e))

        # test case 1: perfect matching
        try:
            assert len(set(hospitals_dict.values())) == len(student_prefs.keys())
            assert len(set(hospitals_dict.keys())) == len(hospital_prefs.keys())
            print('+2: Perfect matching')
            total_score += 2
        except AssertionError as e:
            print(str(e))

       #test case 2: stable matching
        try:
            for m_hospital in hospitals_dict.keys():
                matched_student = hospitals_dict[m_hospital]
                if matched_student != hospital_prefs[m_hospital][0]:
                    for m_student in student_prefs.keys():
                        matched_hospital = student_dict[m_student]
                        if hospital_prefs[m_hospital].index(m_student) < hospital_prefs[m_hospital].index(matched_student): #if hospital prefers another student to matched one
                            assert not student_prefs[m_student].index(m_hospital) < student_prefs[m_student].index(matched_hospital)
            print('+2: Stable Matching found!')
            stable_matching = True
            total_score += 4
        except AssertionError as e:
            print('+0: Matching is not stable!')
            print(str(e))

        #test case 3: Total Proposals not more than n^2
        if stable_matching:
            try:
                assert total_proposals <= len(hospital_prefs.keys())**2
                assert total_proposals >= len(hospital_prefs.keys())
                print('+2: Algorithm makes less than n^2 proposals')
                total_score += 4
            except AssertionError as e:
                print(str(e))
                print('+0: Proposal count not implemented correctly, or algorithm does not run as expected')
        else:
            print('+0: This test case is run only if stable matching is found!')

print('Total score obtained for ', test_file_counter, ' test_files:', total_score)
print('Total score for assignment: ', total_score)

