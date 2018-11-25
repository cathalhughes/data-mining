import numpy as np
import pandas as pd
from datetime import datetime as dt
import itertools

loc = "D:/data_mining/data_mining2/Datasets/"

data1 = pd.read_csv(loc + '2000-01.csv', error_bad_lines=False)
data2 = pd.read_csv(loc + '2001-02.csv', error_bad_lines=False)
data3 = pd.read_csv(loc + '2002-03.csv', error_bad_lines=False)
data4 = pd.read_csv(loc + '2003-04.csv', error_bad_lines=False)
data5 = pd.read_csv(loc + '2004-05.csv', error_bad_lines=False)
data6 = pd.read_csv(loc + '2005-06.csv', error_bad_lines=False)
data7 = pd.read_csv(loc + '2006-07.csv', error_bad_lines=False)
data8 = pd.read_csv(loc + '2007-08.csv', error_bad_lines=False)
data9 = pd.read_csv(loc + '2008-09.csv', error_bad_lines=False)
data10 = pd.read_csv(loc + '2009-10.csv', error_bad_lines=False)
data11 = pd.read_csv(loc + '2010-11.csv', error_bad_lines=False)
data12 = pd.read_csv(loc + '2011-12.csv', error_bad_lines=False)
data13 = pd.read_csv(loc + '2012-13.csv', error_bad_lines=False)
data14 = pd.read_csv(loc + '2013-14.csv', error_bad_lines=False)
data15 = pd.read_csv(loc + '2014-15.csv', error_bad_lines=False)
data16 = pd.read_csv(loc + '2015-16.csv', error_bad_lines=False)
data17 = pd.read_csv(loc + '2016-17.csv', error_bad_lines=False)
data18 = pd.read_csv(loc + '2017-18.csv', error_bad_lines=False)



def get_date(date):
    if date == '':
        return None
    else:
        return dt.strptime(date, '%d/%m/%y').date()

def get_date_other(date):
    if date == '':
        return None
    else:
        return dt.strptime(date, '%d/%m/%Y').date()
    

data1.Date = data1.Date.apply(get_date)    
data2.Date = data2.Date.apply(get_date)    
data3.Date = data3.Date.apply(get_date_other)         # The date format for this dataset is different  
data4.Date = data4.Date.apply(get_date)    
data5.Date = data5.Date.apply(get_date)    
data6.Date = data6.Date.apply(get_date)    
data7.Date = data7.Date.apply(get_date)    
data8.Date = data8.Date.apply(get_date)    
data9.Date = data9.Date.apply(get_date)    
data10.Date = data10.Date.apply(get_date)
data11.Date = data11.Date.apply(get_date)
data12.Date = data12.Date.apply(get_date)
data13.Date = data13.Date.apply(get_date)
data14.Date = data14.Date.apply(get_date)
data15.Date = data15.Date.apply(get_date)
data16.Date = data16.Date.apply(get_date)
data17.Date = data17.Date.apply(get_date)
data18.Date = data18.Date.apply(get_date)

#Gets all the statistics related to gameplay
                      
columns_required = ['Date','HomeTeam','AwayTeam','FTHG','FTAG','FTR']

stats1 = data1[columns_required]                      
stats2 = data2[columns_required]
stats3 = data3[columns_required]
stats4 = data4[columns_required]
stats5 = data5[columns_required]
stats6 = data6[columns_required]
stats7 = data7[columns_required]
stats8 = data8[columns_required]
stats9 = data9[columns_required]
stats10 = data10[columns_required]
stats11 = data11[columns_required]   
stats12 = data12[columns_required]
stats13 = data13[columns_required]
stats14 = data14[columns_required]
stats15 = data15[columns_required]
stats16 = data16[columns_required]
stats17 = data17[columns_required]
stats18 = data18[columns_required]

# Gets the goals scored agg arranged by teams and matchweek
def get_goals_scored(playing_stat):
    # Create a dictionary with team names as keys
    teams = {}
    for i in playing_stat.groupby('HomeTeam').mean().T.columns:
        teams[i] = []
    
    # the value corresponding to keys is a list containing the match location.
    for i in range(len(playing_stat)):
        HTGS = playing_stat.iloc[i]['FTHG']
        ATGS = playing_stat.iloc[i]['FTAG']
        teams[playing_stat.iloc[i].HomeTeam].append(HTGS)
        teams[playing_stat.iloc[i].AwayTeam].append(ATGS)
    
    # Create a dataframe for goals scored where rows are teams and cols are matchweek.
    GoalsScored = pd.DataFrame(data=teams, index = [i for i in range(1,39)]).T
    GoalsScored[0] = 0
    # Aggregate to get uptil that point
    for i in range(2,39):
        GoalsScored[i] = GoalsScored[i] + GoalsScored[i-1]
    return GoalsScored

# Gets the goals conceded agg arranged by teams and matchweek
def get_goals_conceded(playing_stat):
    # Create a dictionary with team names as keys
    teams = {}
    for i in playing_stat.groupby('HomeTeam').mean().T.columns:
        teams[i] = []
    
    # the value corresponding to keys is a list containing the match location.
    for i in range(len(playing_stat)):
        ATGC = playing_stat.iloc[i]['FTHG']
        HTGC = playing_stat.iloc[i]['FTAG']
        teams[playing_stat.iloc[i].HomeTeam].append(HTGC)
        teams[playing_stat.iloc[i].AwayTeam].append(ATGC)
    
    # Create a dataframe for goals scored where rows are teams and cols are matchweek.
    GoalsConceded = pd.DataFrame(data=teams, index = [i for i in range(1,39)]).T
    GoalsConceded[0] = 0
    # Aggregate to get uptil that point
    for i in range(2,39):
        GoalsConceded[i] = GoalsConceded[i] + GoalsConceded[i-1]
    return GoalsConceded


def get_gss(playing_stat):
    GC = get_goals_conceded(playing_stat)
    GS = get_goals_scored(playing_stat)
   
    j = 0
    HTGS = []
    ATGS = []
    HTGC = []
    ATGC = []

    for i in range(380):
        ht = playing_stat.iloc[i].HomeTeam
        at = playing_stat.iloc[i].AwayTeam
        HTGS.append(GS.loc[ht][j])
        ATGS.append(GS.loc[at][j])
        HTGC.append(GC.loc[ht][j])
        ATGC.append(GC.loc[at][j])
        
        if ((i + 1)% 10) == 0:
            j = j + 1
        
    playing_stat['HTGS'] = HTGS
    playing_stat['ATGS'] = ATGS
    playing_stat['HTGC'] = HTGC
    playing_stat['ATGC'] = ATGC
    
    return playing_stat


# Apply to each dataset
stats1 = get_gss(stats1)
stats2 = get_gss(stats2)
stats3 = get_gss(stats3)
stats4 = get_gss(stats4)
stats5 = get_gss(stats5)
stats6 = get_gss(stats6)
stats7 = get_gss(stats7)
stats8 = get_gss(stats8)
stats9 = get_gss(stats9)
stats10 = get_gss(stats10)
stats11 = get_gss(stats11)
stats12 = get_gss(stats12)
stats13 = get_gss(stats13)
stats14 = get_gss(stats14)
stats15 = get_gss(stats15)
stats16 = get_gss(stats16)
stats17 = get_gss(stats17)
stats18 = get_gss(stats18)

def get_points(result):
    if result == 'W':
        return 3
    elif result == 'D':
        return 1
    else:
        return 0
    

def get_cuml_points(matchres):
    matchres_points = matchres.applymap(get_points)
    for i in range(2,39):
        matchres_points[i] = matchres_points[i] + matchres_points[i-1]
        
    matchres_points.insert(column =0, loc = 0, value = [0*i for i in range(20)])
    return matchres_points


def get_matches(playing_stat):
    # Create a dictionary with team names as keys
    teams = {}
    for i in playing_stat.groupby('HomeTeam').mean().T.columns:
        teams[i] = []

    # the value corresponding to keys is a list containing the match result
    for i in range(len(playing_stat)):
        if playing_stat.iloc[i].FTR == 'H':
            teams[playing_stat.iloc[i].HomeTeam].append('W')
            teams[playing_stat.iloc[i].AwayTeam].append('L')
        elif playing_stat.iloc[i].FTR == 'A':
            teams[playing_stat.iloc[i].AwayTeam].append('W')
            teams[playing_stat.iloc[i].HomeTeam].append('L')
        else:
            teams[playing_stat.iloc[i].AwayTeam].append('D')
            teams[playing_stat.iloc[i].HomeTeam].append('D')
            
    return pd.DataFrame(data=teams, index = [i for i in range(1,39)]).T

def get_agg_points(playing_stat):
    matchres = get_matches(playing_stat)
    cum_pts = get_cuml_points(matchres)
    HomeTeamPoints = []
    AwayTeamPoints = []
    j = 0
    for i in range(380):
        ht = playing_stat.iloc[i].HomeTeam
        at = playing_stat.iloc[i].AwayTeam
        HomeTeamPoints.append(cum_pts.loc[ht][j])
        AwayTeamPoints.append(cum_pts.loc[at][j])

        if ((i + 1)% 10) == 0:
            j = j + 1
            
    playing_stat['HTP'] = HomeTeamPoints
    playing_stat['ATP'] = AwayTeamPoints
    return playing_stat
    
# Apply to each dataset
stats1 = get_agg_points(stats1)
stats2 = get_agg_points(stats2)
stats3 = get_agg_points(stats3)
stats4 = get_agg_points(stats4)
stats5 = get_agg_points(stats5)
stats6 = get_agg_points(stats6)
stats7 = get_agg_points(stats7)
stats8 = get_agg_points(stats8)
stats9 = get_agg_points(stats9)
stats10 = get_agg_points(stats10)
stats11 = get_agg_points(stats11)
stats12 = get_agg_points(stats12)
stats13 = get_agg_points(stats13)
stats14 = get_agg_points(stats14)
stats15 = get_agg_points(stats15)
stats16 = get_agg_points(stats16)
stats17 = get_agg_points(stats17)
stats18 = get_agg_points(stats18)

def get_form(playing_stat,num):
    form = get_matches(playing_stat)
    form_final = form.copy()
    for i in range(num,39):
        form_final[i] = ''
        j = 0
        while j < num:
            form_final[i] += form[i-j]
            j += 1           
    return form_final

def add_form(playing_stat,num):
    form = get_form(playing_stat,num)
    h = ['M' for i in range(num * 10)]  # since form is not available for n MW (n*10)
    a = ['M' for i in range(num * 10)]
    
    j = num
    for i in range((num*10),380):
        ht = playing_stat.iloc[i].HomeTeam
        at = playing_stat.iloc[i].AwayTeam
        
        past = form.loc[ht][j]               # get past n results
        h.append(past[num-1])                    # 0 index is most recent
        
        past = form.loc[at][j]               # get past n results.
        a.append(past[num-1])                   # 0 index is most recent
        
        if ((i + 1)% 10) == 0:
            j = j + 1

    playing_stat['HM' + str(num)] = h                 
    playing_stat['AM' + str(num)] = a

    
    return playing_stat


def add_form_df(playing_statistics):
    playing_statistics = add_form(playing_statistics,1)
    playing_statistics = add_form(playing_statistics,2)
    playing_statistics = add_form(playing_statistics,3)
    playing_statistics = add_form(playing_statistics,4)
    playing_statistics = add_form(playing_statistics,5)
    return playing_statistics    
    
# Make changes to df
stats1 = add_form_df(stats1)
stats2 = add_form_df(stats2)
stats3 = add_form_df(stats3)
stats4 = add_form_df(stats4)
stats5 = add_form_df(stats5)
stats6 = add_form_df(stats6)
stats7 = add_form_df(stats7)
stats8 = add_form_df(stats8)
stats9 = add_form_df(stats9)
stats10 = add_form_df(stats10)
stats11 = add_form_df(stats11)
stats12 = add_form_df(stats12)
stats13 = add_form_df(stats13)
stats14 = add_form_df(stats14)
stats15 = add_form_df(stats15)    
stats16 = add_form_df(stats16)
stats17 = add_form_df(stats17)
stats18 = add_form_df(stats18)

# Rearranging columns
cols = ['Date', 'HomeTeam', 'AwayTeam', 'FTHG', 'FTAG', 'FTR', 'HTGS', 'ATGS', 'HTGC', 'ATGC', 'HTP', 'ATP', 'HM1', 'HM2', 'HM3',
        'HM4', 'HM5', 'AM1', 'AM2', 'AM3', 'AM4', 'AM5' ]

stats1 = stats1[cols]
stats2 = stats2[cols]
stats3 = stats3[cols]
stats4 = stats4[cols]
stats5 = stats5[cols]
stats6 = stats6[cols]
stats7 = stats7[cols]
stats8 = stats8[cols]
stats9 = stats9[cols]
stats10 = stats10[cols]
stats11 = stats11[cols]
stats12 = stats12[cols]
stats13 = stats13[cols]
stats14 = stats14[cols]
stats15 = stats15[cols]
stats16 = stats16[cols]
stats17 = stats17[cols]
stats18 = stats18[cols]

Standings = pd.read_csv(loc + "EPLStandings.csv")
Standings.set_index(['Team'], inplace=True)
Standings = Standings.fillna(20)

def get_last(playing_stat, Standings, year):
    HomeTeamLP = []
    AwayTeamLP = []
    for i in range(380):
        ht = playing_stat.iloc[i].HomeTeam
        at = playing_stat.iloc[i].AwayTeam
        HomeTeamLP.append(Standings.loc[ht][year])
        AwayTeamLP.append(Standings.loc[at][year])
    playing_stat['HomeTeamLP'] = HomeTeamLP
    playing_stat['AwayTeamLP'] = AwayTeamLP
    return playing_stat

stats1 = get_last(stats1, Standings, 0)
stats2 = get_last(stats2, Standings, 1)
stats3 = get_last(stats3, Standings, 2)
stats4 = get_last(stats4, Standings, 3)
stats5 = get_last(stats5, Standings, 4)
stats6 = get_last(stats6, Standings, 5)
stats7 = get_last(stats7, Standings, 6)
stats8 = get_last(stats8, Standings, 7)
stats9 = get_last(stats9, Standings, 8)
stats10 = get_last(stats10, Standings, 9)
stats11 = get_last(stats11, Standings, 10)
stats12 = get_last(stats12, Standings, 11)
stats13 = get_last(stats13, Standings, 12)
stats14 = get_last(stats14, Standings, 13)
stats15 = get_last(stats15, Standings, 14)
stats16 = get_last(stats16, Standings, 15)
stats17 = get_last(stats17, Standings, 16)
stats18 = get_last(stats18, Standings, 17)

def get_mw(playing_stat):
    j = 1
    MatchWeek = []
    for i in range(380):
        MatchWeek.append(j)
        if ((i + 1)% 10) == 0:
            j = j + 1
    playing_stat['MW'] = MatchWeek
    return playing_stat

stats1 = get_mw(stats1)
stats2 = get_mw(stats2)
stats3 = get_mw(stats3)
stats4 = get_mw(stats4)
stats5 = get_mw(stats5)
stats6 = get_mw(stats6)
stats7 = get_mw(stats7)
stats8 = get_mw(stats8)
stats9 = get_mw(stats9)
stats10 = get_mw(stats10)
stats11 = get_mw(stats11)
stats12 = get_mw(stats12)
stats13 = get_mw(stats13)
stats14 = get_mw(stats14)
stats15 = get_mw(stats15)
stats16 = get_mw(stats16)
stats17 = get_mw(stats17)
stats18 = get_mw(stats18)

playing_stat = pd.concat([stats1,
                          stats2,
                          stats3,
                          stats4,
                          stats5,
                          stats6,
                          stats7,
                          stats8,
                          stats9,
                          stats10,
                          stats11,
                          stats12,
                          stats13,
                          stats14,
                          stats15,
                          stats16,
                          stats17,
                          stats18], ignore_index=True)

# Gets the form points.
def get_form_points(string):
    sum = 0
    for letter in string:
        sum += get_points(letter)
    return sum

playing_stat['HTFormPtsStr'] = playing_stat['HM1'] + playing_stat['HM2'] + playing_stat['HM3'] + playing_stat['HM4'] + playing_stat['HM5']
playing_stat['ATFormPtsStr'] = playing_stat['AM1'] + playing_stat['AM2'] + playing_stat['AM3'] + playing_stat['AM4'] + playing_stat['AM5']

playing_stat['HTFormPts'] = playing_stat['HTFormPtsStr'].apply(get_form_points)
playing_stat['ATFormPts'] = playing_stat['ATFormPtsStr'].apply(get_form_points)

# Identify Win/Loss Streaks if any.
def get_3game_ws(string):
    if string[-3:] == 'WWW':
        return 1
    else:
        return 0
    
def get_5game_ws(string):
    if string == 'WWWWW':
        return 1
    else:
        return 0
    
def get_3game_ls(string):
    if string[-3:] == 'LLL':
        return 1
    else:
        return 0
    
def get_5game_ls(string):
    if string == 'LLLLL':
        return 1
    else:
        return 0
    
playing_stat['HTWinStreak3'] = playing_stat['HTFormPtsStr'].apply(get_3game_ws)
playing_stat['HTWinStreak5'] = playing_stat['HTFormPtsStr'].apply(get_5game_ws)
playing_stat['HTLossStreak3'] = playing_stat['HTFormPtsStr'].apply(get_3game_ls)
playing_stat['HTLossStreak5'] = playing_stat['HTFormPtsStr'].apply(get_5game_ls)

playing_stat['ATWinStreak3'] = playing_stat['ATFormPtsStr'].apply(get_3game_ws)
playing_stat['ATWinStreak5'] = playing_stat['ATFormPtsStr'].apply(get_5game_ws)
playing_stat['ATLossStreak3'] = playing_stat['ATFormPtsStr'].apply(get_3game_ls)
playing_stat['ATLossStreak5'] = playing_stat['ATFormPtsStr'].apply(get_5game_ls)

print(playing_stat.keys())

# Get Goal Difference
playing_stat['HTGD'] = playing_stat['HTGS'] - playing_stat['HTGC']
playing_stat['ATGD'] = playing_stat['ATGS'] - playing_stat['ATGC']

# Diff in points
playing_stat['DiffPts'] = playing_stat['HTP'] - playing_stat['ATP']
playing_stat['DiffFormPts'] = playing_stat['HTFormPts'] - playing_stat['ATFormPts']

# Diff in last year positions
playing_stat['DiffLP'] = playing_stat['HomeTeamLP'] - playing_stat['AwayTeamLP']

# Scale DiffPts , DiffFormPts, HTGD, ATGD by Matchweek.
cols = ['HTGD','ATGD','DiffPts','HTP','ATP']
playing_stat.MW = playing_stat.MW.astype(float)

# for col in cols:
    
#     playing_stat[col] = playing_stat[col] / playing_stat.MW


# playing_stat['DiffFormPts'] = playing_stat['DiffFormPts'] / 9

def only_hw(string):
    if string == 'H':
        return 'H'
    else:
        return 'NH'

    
#playing_stat['FTR'] = playing_stat.FTR.apply(only_hw)

print(len(playing_stat))

# playing_stat_test = playing_stat[6790:]
# playing_stat = playing_stat[0:6790]


print(playing_stat)

playing_stat.to_csv(loc + "final_dataset_project_full_no_normalisation.csv")
#playing_stat_test.to_csv(loc+"test_project_full_new_normalisation.csv")