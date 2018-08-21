'''
copyright @cse 450 Arizona State University




'''

import os, platform
import pickle
import time

if platform.system() == 'Windows':
    import resources_windows as resources
else:
    import resources_unix as resources

workspace_dir = resources.workspace_dir
test_files_dir = os.path.join(workspace_dir, 'prog_assignment1', 'test_files')


def gale_shapley_matching(hospital_prefs, student_prefs):
    '''Input: One dictionary for hospital preferences and another for student preferences
     Output:
     1. One dictionary with hospital ids as keys and corresponding matched students as ids (type: {})
     2. One dictionary with student ids as keys and corresponding matched hospitals as ids (type: {})
     3. Integer value for total number of proposals made throughout the algorithms (type: int)

     '''

    hospital_ids = hospital_prefs.keys()
    student_ids = student_prefs.keys()
    hospitals_dict = dict.fromkeys(hospital_ids)
    students_dict = dict.fromkeys(student_ids)
    proposals_count = 0  # increment every time a proposal is made
    start = time.time() * 1000.0

    '''
    Enter code here
    
    
    
    Do not modify given code or the automated test cases will fail 
    '''

    end = time.time() * 1000.0
    print('Took', str(end - start), 'to process: ', len(hospital_ids))

    return hospitals_dict, students_dict, proposals_count


'''



'''


def run_unit_tests(m_test_files):
    for m_file in os.listdir(m_test_files):
        if m_file.startswith('.'):
            continue
        in_file = os.path.join(m_test_files, m_file)
        if m_file.startswith('.'):
            continue
        with open(in_file, 'rb') as f:
            pref_dict = pickle.load(f)

        # Each pickle file will have the hospital preferences as a dictionary and the student preferences as a dictionary
        hospitals_prefs = pref_dict['hospitals']
        students_prefs = pref_dict['students']

        hospitals_dict, students_dict, proposals_count = gale_shapley_matching(hospitals_prefs, students_prefs)

        print('Hospital mathces: ', hospitals_dict)
        print('Student matches: ', students_dict)
        print('Total proposals: ', proposals_count)


if __name__ == '__main__':
    run_unit_tests(os.path.join(test_files_dir))
