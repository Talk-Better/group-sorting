import pandas as pd

def preprocess(df):
    ## More cleaning of data and preperation for sorting ##
    talk_codes = {'Not very talkative at all': 1, 'Not talkative': 2, 'Somewhat talkative': 3, 'Talkative': 4, 'Very talkative': 5}
    attendance_codes = {'No': 1, 'Maybe': 2, 'Yes': 3}
    leaning_codes = {"Right": 1, 'Center': 2, "Left": 3}

    df['Talkativeness'] = df['Talkativeness'].replace(talk_codes)
    df['Attendance'] = df['Attendance'].replace(attendance_codes)
    df['Leaning'] = df['Leaning'].replace(leaning_codes)

    df = df.sort_values(['Leaning', 'Familiarity', 'Talkativeness', "Attendance"], ascending=[False, False, False, False])
    #df.to_csv("alldata.csv")
    
    return df

def makeGroups(df, k):
    groups = []
    for i in range(0, len(df)):
        group_num = (i % k) + 1
        groups.append(group_num)
    
    df["Group"] = groups
    df = df.sort_values(["Group"], ascending=[True])

    return df
    
