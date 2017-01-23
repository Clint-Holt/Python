import unicodecsv
from datetime import date

enrollments_file = 'C:\Users\clint\Downloads\enrollments.csv'
daily_engagements_file = 'C:\Users\clint\Downloads\daily_engagement_full.csv'
project_submissions_file = 'C:\Users\clint\Downloads\project_submissions.csv'


def read_file(file_name):
    """ Reads a csv file into a list. """
    with open(file_name, 'rb') as f:
        reader = unicodecsv.DictReader(f)
        return list(reader)


def get_students(list_name):
    """ Creates a set of all students, eliminating duplicates."""
    student_set = set()
    for row in list_name:
        student_set.add(row['account_key'])
    return student_set


def convert_to_date(dict):
    for row in dict:
        for key in row.keys():
            if 'date' in key:
                value = row[key]
                try:
                    row[key] = date(int(value[:4]), int(value[5:7]), int(value[8:]))
                except:
                    row[key] = None
    return dict


def get_paid_students(student_list):
    """ Finds which students have already paid. This is any student in
        'student_list' who has been enrolled for more than 7 days. """
    paid_students = {}
    for student in student_list:
        date1 = student['join_date']
        date2 = student['cancel_date']
        if date2:
            if (date2 - date1).days > 7:
                paid_students[student['account_key']] = date1
        else:
            paid_students[student['account_key']] = date1

    return paid_students


def main():
    enrollment_list = convert_to_date(read_file(enrollments_file))
    # daily_engagements = convert_to_date(read_file(daily_engagements_file))
    project_submissions = convert_to_date(read_file(project_submissions_file))
    print enrollment_list[:3]
    print 'L57'
    # Clean up data
    new_enrollment_list = []
    for row in enrollment_list:
        if (row['days_to_cancel'] != u'0') and (row['is_udacity'] != u'True'):
            new_enrollment_list.append(row)

    # new_daily_engagements = []
    # for row in daily_engagements:
    #     row['account_key'] = row['acct']
    #     del row['acct']
    #
    #     if row['is_udacity'] != u'True':
    #         new_daily_engagements.append(row)



    # Get the student account IDs
    enrollment_students = get_students(new_enrollment_list)
    # engagement_students = get_students(new_daily_engagements)
    submission_students = get_students(project_submissions)

    paid_students = get_paid_students(new_enrollment_list)
    print len(paid_students)


if __name__ == '__main__':
    main()


