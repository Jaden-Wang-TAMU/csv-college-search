import csv


def highest_in_state(state):
    """
    Returns the name and cost of the most expensive university in state

    We're using the TUITIONFEE_IN field as cost and INSTNM as the school
    name.

    Be careful on data types on this one. 
    """
    csv_file = csv.DictReader(open('university-data.csv'))
    maxTu=0
    maxSch=""
    for row in csv_file:
        if row['STABBR']==state and row['TUITIONFEE_IN']!="-" and int(row['TUITIONFEE_IN'])>maxTu:
            maxTu=int(row['TUITIONFEE_IN'])
            maxSch=row['INSTNM']
        
    return maxTu, maxSch
