import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime as dt
import itertools
from pandas.plotting import table

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

columns_required = ['Date','HomeTeam','AwayTeam','FTHG','FTAG','FTR','HS','AS',
               'HST','AST','HF','AF','HC','AC','HY','AY','HR','AR']

               
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


playing_stats = pd.concat([stats1, stats2, stats3, stats4,
                                stats5, stats6, stats7, stats8,
                                stats9, stats10, stats11,stats12, 
                                stats13, stats14, stats15, stats16, stats17, stats18])


#Average of wins 
def get_result_stats(playing_stats, year):
    return pd.DataFrame(data = [ len(playing_stats[playing_stats.FTR == 'H']),
                                 len(playing_stats[playing_stats.FTR == 'A']),
                                 len(playing_stats[playing_stats.FTR == 'D'])],
                        index = ['Home Wins', 'Away Wins', 'Draws'],
                        columns =[year]
                       ).T

result_stats_agg = get_result_stats(playing_stats, 'Overall')


print(len(playing_stats))

total_games = len(playing_stats)

labels = 'Home Wins', 'Away Wins', 'Draws'
sizes = [(result_stats_agg['Home Wins'][0]/ total_games) * 100 , (result_stats_agg['Away Wins'][0]/ total_games) * 100, (result_stats_agg['Draws'][0]/ total_games) * 100]

fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.savefig("winsPieChart.png")

#Effect of last 3 games 

def get_match_results(playing_stat):
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


results1 = get_match_results(stats1)
results2 = get_match_results(stats2)
results3 = get_match_results(stats3)
results4 = get_match_results(stats4)
results5 = get_match_results(stats5)
results6 = get_match_results(stats6)
results7 = get_match_results(stats7)
results8 = get_match_results(stats8)
results9 = get_match_results(stats9)
results10 = get_match_results(stats10)
results11 = get_match_results(stats11)
results12 = get_match_results(stats12)
results13 = get_match_results(stats13)
results14 = get_match_results(stats14)
results15 = get_match_results(stats15)
results16 = get_match_results(stats16)
results17 = get_match_results(stats17)
results18 = get_match_results(stats18)

results_list = [results1, results2, results3, results4, results5, results6, results7, results8,
                 results9, results10, results11, results12, results13, results14, results15, results16, results17, results18]

def get_match_location(playing_stat):
    # Create a dictionary with team names as keys
    teams = {}
    for i in playing_stat.groupby('HomeTeam').mean().T.columns:
        teams[i] = []
    
    # the value corresponding to keys is a list containing the match location
    for i in range(len(playing_stat)):
        teams[playing_stat.iloc[i].HomeTeam].append('H')
        teams[playing_stat.iloc[i].AwayTeam].append('A')
        
    return pd.DataFrame(data=teams, index = [i for i in range(1,39)]).T


match_loc_1 = get_match_location(stats1)
match_loc_2 = get_match_location(stats2)
match_loc_3 = get_match_location(stats3)
match_loc_4 = get_match_location(stats4)
match_loc_5 = get_match_location(stats5)
match_loc_6 = get_match_location(stats6)
match_loc_7 = get_match_location(stats7)
match_loc_8 = get_match_location(stats8)
match_loc_9 = get_match_location(stats9)
match_loc_10 = get_match_location(stats10)
match_loc_11 = get_match_location(stats11)
match_loc_12 = get_match_location(stats12)
match_loc_13 = get_match_location(stats13)
match_loc_14 = get_match_location(stats14)
match_loc_15 = get_match_location(stats15)
match_loc_16 = get_match_location(stats16)
match_loc_17 = get_match_location(stats17)
match_loc_18 = get_match_location(stats18)

match_location_list = [match_loc_1, match_loc_2, match_loc_3, match_loc_4, match_loc_5, match_loc_6, match_loc_7, 
              match_loc_8, match_loc_9, match_loc_10, match_loc_11, match_loc_12, match_loc_13, match_loc_14,
              match_loc_15,match_loc_16,match_loc_17,match_loc_18]

def get_past_form(form_list,match_loc_list, size):
    perm_dict = {}
    for i in range(len(form_list)):
        df = form_list[i].T
        m_df = match_loc_list[i].T
        
        for team in df.columns:
            i = 0
            while i != (38-size):
                n = 0 
                comb = ''
                while n < size:
                    comb = comb + df[team].iloc[i+n]
                    n+=1
                result = df[team].iloc[i+size]
                side = m_df[team].iloc[i+size]
                if comb in perm_dict:
                    perm_dict[comb].append([result,side])
                else:
                    perm_dict[comb] = []
                    perm_dict[comb].append([result,side])
                i = i+1
                
    return perm_dict

past_form_comb_3 = get_past_form(results_list, match_location_list, 3)

# Calculates wins/losses/draws for home/away side

def get_form_stats(past_form_c):
    past_form_res = {}
    for key in past_form_c.keys():
        total = len(past_form_c[key])
        HW = 0
        HL = 0
        AW = 0 
        AL = 0
        HD = 0
        AD = 0
        for result,loc in past_form_c[key]:
            if loc == 'H':
                if result == 'W':
                    HW += 1 
                elif result == 'L':
                    HL += 1
                else:
                    HD += 1
            else:
                if result == 'W':
                    AW += 1 
                elif result == 'L':
                    AL += 1
                else:
                    AD += 1
        past_form_res[key] = [HW, HL, HD, AW, AL, AD, HW+AW, HL+AL, HD+AD, total]

    past_form_prob = pd.DataFrame(past_form_res).T

    # Change column names to correct ones
    past_form_prob = pd.DataFrame(past_form_res).T
    past_form_prob.rename(columns = {0:'HomeWin', 1:'HomeLoss', 2:'HomeDraw', 3:'AwayWin', 4:'AwayLoss', 5:'AwayDraw',
                                     6:'TotalWins', 7:'TotalLosses', 8:'TotalDraws', 9:'TotalMatches' }, inplace=True)

    # Convert the numbers to probability
    for col in ['HomeWin', 'HomeLoss', 'HomeDraw', 'AwayWin', 'AwayLoss', 'AwayDraw', 'TotalWins', 'TotalLosses', 'TotalDraws']:
        past_form_prob[col] = past_form_prob[col] / past_form_prob['TotalMatches']
    
    # Change column names again
    past_form_prob.rename(columns = {'HomeWin':'P(W/H)', 'HomeLoss': 'P(L/H)', 'HomeDraw': 'P(D/H)', 'AwayWin': 'P(W/A)',
                                     'AwayLoss': 'P(L/A)','AwayDraw': 'P(D/A)','TotalWins': 'P(W)', 'TotalLosses': 'P(L)',
                                     'TotalDraws': 'P(D)'}, inplace=True)
    return past_form_prob

past_form_prob_3 = get_form_stats(past_form_comb_3)

with open("index.html", "w") as f:
	f.write(past_form_prob_3.to_html())
	f.close()


##League Points justification

def get_points(result):
    if result == 'W':
        return 3
    elif result == 'D':
        return 1
    else:
        return 0

def get_cuml_points(matchres):
    resultspoints = matchres.applymap(get_points)
    for i in range(2,39):
        resultspoints[i] = resultspoints[i] + resultspoints[i-1]
        
    resultspoints.insert(column =0, loc = 0, value = [0*i for i in range(20)])
    return resultspoints

cuml_pts_1 = get_cuml_points(results1)
cuml_pts_2 = get_cuml_points(results2)
cuml_pts_3 = get_cuml_points(results3)
cuml_pts_4 = get_cuml_points(results4)
cuml_pts_5 = get_cuml_points(results5)
cuml_pts_6 = get_cuml_points(results6)
cuml_pts_7 = get_cuml_points(results7)
cuml_pts_8 = get_cuml_points(results8)
cuml_pts_9 = get_cuml_points(results9)
cuml_pts_10 = get_cuml_points(results10)
cuml_pts_11 = get_cuml_points(results11)
cuml_pts_12 = get_cuml_points(results12)
cuml_pts_13 = get_cuml_points(results13)
cuml_pts_14 = get_cuml_points(results14)
cuml_pts_15 = get_cuml_points(results15)
cuml_pts_16 = get_cuml_points(results16)
cuml_pts_17 = get_cuml_points(results17)
cuml_pts_18 = get_cuml_points(results18)


# (2) Gets the difference between the points of any two teams in any matchweek.
def get_diff(ht,at,week,cuml_pts):
    ht_pts = cuml_pts[week-1].loc[ht]
    at_pts = cuml_pts[week-1].loc[at]
    diff = ht_pts - at_pts
    return diff

# def points_diff(playing_stat, cuml_pts):
#     point_diff_overall = {}
#     matches = 0
#     for week in range(1,39):
#         point_diff = []
#         for match in range(matches,matches+10):
#             ht = playing_stat.iloc[match].HomeTeam
#             at = playing_stat.iloc[match].AwayTeam
#             res = playing_stat.iloc[match].FTR
#             diff = get_diff(ht,at,week,cuml_pts)
            
#             if res == 'H':
#                 point_diff.append([diff, 'HW'])
#             elif res == 'A':
#                 point_diff.append([diff, 'AW'])
#             else:
#                 point_diff.append([diff, 'D'])
#         point_diff_overall[week] = point_diff
#         matches += 10
#     return point_diff_overall


def points_diff(playing_stat, cuml_pts):
    point_diff_overall = {}
    matches = 0
    for week in range(1,39):                       # 38 matchweeks in a season
        point_diff = {}
        for match in range(matches,matches+10):
            ht = playing_stat.iloc[match].HomeTeam
            at = playing_stat.iloc[match].AwayTeam
            res = playing_stat.iloc[match].FTR
            diff = get_diff(ht,at,week,cuml_pts)
            if res == 'H':
                if diff not in point_diff:
                    point_diff[diff] = ['HW']
                else:
                    point_diff[diff].append('HW')
            elif res == 'A':
                if diff not in point_diff:
                    point_diff[diff] = ['AW']
                else:
                    point_diff[diff].append('AW')
            else:
                if diff not in point_diff:
                    point_diff[diff] = ['D']
                else:
                    point_diff[diff].append('D')
        point_diff_overall[week] = point_diff
        matches += 10
    return point_diff_overall


points_diff_1 = points_diff(stats1, cuml_pts_1)
points_diff_2 = points_diff(stats2, cuml_pts_2)
points_diff_3 = points_diff(stats3, cuml_pts_3)
points_diff_4 = points_diff(stats4, cuml_pts_4)
points_diff_5 = points_diff(stats5, cuml_pts_5)
points_diff_6 = points_diff(stats6, cuml_pts_6)
points_diff_7 = points_diff(stats7, cuml_pts_7)
points_diff_8 = points_diff(stats8, cuml_pts_8)
points_diff_9 = points_diff(stats9, cuml_pts_9)
points_diff_10 = points_diff(stats10, cuml_pts_10)
points_diff_11 = points_diff(stats11, cuml_pts_11)
points_diff_12 = points_diff(stats12, cuml_pts_12)
points_diff_13 = points_diff(stats13, cuml_pts_13)
points_diff_14 = points_diff(stats14, cuml_pts_14)
points_diff_15 = points_diff(stats15, cuml_pts_15)
points_diff_16 = points_diff(stats16, cuml_pts_16)
points_diff_17 = points_diff(stats17, cuml_pts_17)
points_diff_18 = points_diff(stats18, cuml_pts_18)

points_diff_list = [points_diff_1, points_diff_2, points_diff_3, points_diff_4, points_diff_5, points_diff_6,
                    points_diff_7, points_diff_8, points_diff_9, points_diff_10, points_diff_11, points_diff_12,
                    points_diff_13, points_diff_14, points_diff_15,points_diff_16,points_diff_17,points_diff_18]


points_diff = {}
for key in range(1,39):
    points_diff[key] = {}
    
def merge_dicts(target_dict, dicts_to_merge):
    for points_diff_n in dicts_to_merge:
        for mw in [i for i in range(1,39)]:
            differences = points_diff_n[mw].keys()
            for diff in differences:
                if diff in points_diff[mw]:
                    points_diff[mw][diff] = points_diff[mw][diff] + points_diff_n[mw][diff]
                else:
                    points_diff[mw][diff] = points_diff_n[mw][diff]
    return target_dict

points_diff = merge_dicts(points_diff, points_diff_list)

mw_dist = {}

for mw in points_diff.keys():
    differences = {}
    for diff in points_diff[mw].keys():
        homewins = 0
        awaywins = 0
        draws = 0
        results = [0,0,0]
        
        for result in points_diff[mw][diff]:
            matches = len(points_diff[mw][diff])
            if result == 'HW':
                homewins += 1
            elif result == 'AW':
                awaywins += 1
            else:
                draws += 1
        
        differences[diff] = [homewins, awaywins, draws]
    mw_dist[mw] = differences



print(mw_dist[2])

df = pd.DataFrame(mw_dist[2], index=['HomeWins', 'AwayWins', 'Draws'])

#Plotting above dataframe
df.T.loc[sorted(list(mw_dist[2].keys()))].plot(kind='bar', stacked = True, figsize=[30,10], color = ['steelblue','sandybrown', 'turquoise'])
plt.legend(loc=1,prop={'size':20})
plt.title('Difference in Points & Corresponding Results for Match Week ' + str(2), size = 20)
plt.xlabel('Difference', size =20)
plt.ylabel('Frequency', size =20)
plt.xticks(rotation=0)
plt.tick_params(axis='both', which='major', labelsize=17)
plt.tick_params(axis='both', which='minor', labelsize=17)
plt.savefig("PointsDifferenceWeek2.png")

df = pd.DataFrame(mw_dist[19], index=['HomeWins', 'AwayWins', 'Draws'])

#Plotting above dataframe
df.T.loc[sorted(list(mw_dist[19].keys()))].plot(kind='bar', stacked = True, figsize=[30,10], color = ['steelblue','sandybrown', 'turquoise'])
plt.legend(loc=1,prop={'size':20})
plt.title('Difference in Points & Corresponding Results for Match Week ' + str(19), size = 20)
plt.xlabel('Difference', size =20)
plt.ylabel('Frequency', size =20)
plt.xticks(rotation=0)
plt.tick_params(axis='both', which='major', labelsize=17)
plt.tick_params(axis='both', which='minor', labelsize=17)
plt.savefig("PointsDifferenceWeek19.png")


##
data = pd.read_csv('Datasets/relevant_data/cleanedDataset.csv', index_col = 0)
test_data = pd.read_csv('Datasets/relevant_data/cleanedTestDataset.csv', index_col = 0)

leaguePositionCorrect = 0

for index, row in data.iterrows():
	winner = row.FTR
	if winner == 'H' or winner == "D":
		if row.DiffLP > 0:
			leaguePositionCorrect += 1
	if winner == 'A' or winner == 'D':
		if row.DiffLP < 0:
			leaguePositionCorrect += 1


print((leaguePositionCorrect/len(data)) * 100)

