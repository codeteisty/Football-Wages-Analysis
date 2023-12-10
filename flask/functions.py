import pandas as pd
df = pd.read_csv('../SalaryPrediction2.csv')

def response(a):
    if a in df['Nation'].unique():
        resp = df[df['Nation'] == a]['Wage'].mean().astype('int')
        str_resp = f'Average wage of {a} players is:\n{resp} euros per year,\n{int(resp/12)} euros per month,\n{int(resp/(12*30))} euros per day,\n{int(resp/(12*30*24))} euros per hour,\n{int(resp/(12*30*24*60))} euros per minute.'
        return str_resp
    elif a in df['Position'].unique():
        resp = df[df['Position'] == a]['Wage'].mean().astype('int')
        str_resp = f'Average wage of players whose position is {a} is equal to:\n{resp} euros per year,\n{int(resp / 12)} euros per month,\n{int(resp / (12 * 30))} euros per day,\n{int(resp / (12 * 30 * 24))} euros per hour,\n{int(resp / (12 * 30 * 24 * 60))} euros per minute.'
        return str_resp

    elif a in df['League'].unique():
        resp = df[df['League'] == a]['Wage'].mean().astype('int')
        str_resp = f'Average wage of players who play in {a} is:\n{resp} euros per year,\n{int(resp / 12)} euros per month,\n{int(resp / (12 * 30))} euros per day,\n{int(resp / (12 * 30 * 24))} euros per hour,\n{int(resp / (12 * 30 * 24 * 60))} euros per minute.'
        return str_resp
    elif len(a.split()) == 2:
        str_resp = f'Here is the list of leagues:\n{df.League.unique()}'
        return str_resp
    elif len(a) == 3:
        str_resp = f'Here is the list of nations:\n{df.Nation.unique()}'
        return str_resp
    elif len(a) > 3:
        str_resp = f'Here is the list of positions:\n{df.Position.unique()}'
        return str_resp
    else:
        str_resp = "That doesn't make ane sense!"
        return str_resp
