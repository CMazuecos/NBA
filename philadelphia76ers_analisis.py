import requests
import pandas as pd
from fpdf import FPDF

def extract():
    url = 'https://api.sportsdata.io/v3/nba/projections/json/PlayerSeasonProjectionStatsByTeam/2022/PHI' 
    with open ('config.txt') as f: #cogemos la key
        key = f.read().strip()
    link = requests.get(url + key) #hacemos el request
    philadelphia = link.json() #lo convertimos en json
    return philadelphia

def transform(philadelphia):
    df = pd.DataFrame(philadelphia) #lo convertimos en dataframe
    with open('philadelphia.csv', 'w') as f:
        f.write(df.to_csv(index=False)) #lo guardamos en csv
    return df

def load(df):
    pdf = FPDF() #creamos el pdf
    pdf.add_page() #creamos la portada
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(200, 10, txt = 'Philadelphia 76ers Stats 2022', ln = 1, align = 'C')
    pdf.image('logo.png', x = 20, y = 40, w = 170)
    pdf.set_font('Arial', '', 10)
    pdf.cell(200, 10, txt = 'Hecho por Carlos Mazuecos', ln = 1, align = 'C')
    df = df.sort_values(by=['Points'], ascending=False) # ordenamos por puntos (el que más puntos tiene, se suele considerar el mejor para ir analizando de mejor a peor)
    for i in range(len(df)):
        pdf.add_page()
        pdf.cell(40, 10, 'Player: ' + df['Name'].iloc[i])       
        pdf.set_fill_color(200, 255, 200)
        pdf.set_line_width(0.3)
        pdf.set_font('Times', 'B', 10)
        pdf.ln(10) #creamos una tabla con las estadisticas generales
        pdf.cell(50, 5, txt = 'Position', border = 1, align = 'C', fill = True)
        pdf.cell(50, 5, txt = df['Position'].iloc[i], border = 1, align = 'C', fill = True)
        pdf.ln()
        pdf.cell(50, 5, txt = 'Games', border = 1, align = 'C', fill = True)
        pdf.cell(50, 5, txt = str(df['Games'].iloc[i]), border = 1, align = 'C', fill = True)
        pdf.ln()
        pdf.cell(50, 5, txt = 'Minutes ', border = 1, align = 'C', fill = True)
        pdf.cell(50, 5, txt = str(df['Minutes'].iloc[i]), border = 1, align = 'C', fill = True)
        pdf.ln()        
        pdf.cell(50, 5, txt = 'Points ', border = 1, align = 'C', fill = True)
        pdf.cell(50, 5, txt = str(df['Points'].iloc[i]), border = 1, align = 'C', fill = True)
        pdf.ln()        
        pdf.cell(50, 5, txt = 'Rebounds ', border = 1, align = 'C', fill = True)
        pdf.cell(50, 5, txt = str(df['Rebounds'].iloc[i]), border = 1, align = 'C', fill = True)
        pdf.ln()        
        pdf.cell(50, 5, txt = 'Offensive Rebounds ', border = 1, align = 'C', fill = True)
        pdf.cell(50, 5, txt = str(df['OffensiveRebounds'].iloc[i]), border = 1, align = 'C', fill = True)
        pdf.ln()        
        pdf.cell(50, 5, txt = 'Defensive Rebounds ', border = 1, align = 'C', fill = True)
        pdf.cell(50, 5, txt = str(df['DefensiveRebounds'].iloc[i]), border = 1, align = 'C', fill = True)
        pdf.ln()        
        pdf.cell(50, 5, txt = 'Assists ', border = 1, align = 'C', fill = True)
        pdf.cell(50, 5, txt = str(df['Assists'].iloc[i]), border = 1, align = 'C', fill = True)
        pdf.ln()        
        pdf.cell(50, 5, txt = 'Steals ', border = 1, align = 'C', fill = True)
        pdf.cell(50, 5, txt = str(df['Steals'].iloc[i]), border = 1, align = 'C', fill = True)
        pdf.ln()        
        pdf.cell(50, 5, txt = 'Blocks ', border = 1, align = 'C', fill = True)
        pdf.cell(50, 5, txt = str(df['BlockedShots'].iloc[i]), border = 1, align = 'C', fill = True)
        pdf.ln()        
        pdf.cell(50, 5, txt = 'Turnovers ', border = 1, align = 'C', fill = True)
        pdf.cell(50, 5, txt = str(df['Turnovers'].iloc[i]), border = 1, align = 'C', fill = True)
        pdf.ln()        
        pdf.cell(50, 5, txt = 'Personal Fouls ', border = 1, align = 'C', fill = True)
        pdf.cell(50, 5, txt = str(df['PersonalFouls'].iloc[i]), border = 1, align = 'C', fill = True)
        pdf.ln()        
        pdf.cell(50, 5, txt = 'Double Doubles', border = 1, align = 'C', fill = True)
        pdf.cell(50, 5, txt = str(df['DoubleDoubles'].iloc[i]), border = 1, align = 'C', fill = True)
        pdf.ln()        
        pdf.cell(50, 5, txt = 'Triple Doubles', border = 1, align = 'C', fill = True)
        pdf.cell(50, 5, txt = str(df['TripleDoubles'].iloc[i]), border = 1, align = 'C', fill = True)
        pdf.ln()        
        pdf.cell(50, 5, txt = 'Plus Minus', border = 1, align = 'C', fill = True)
        pdf.cell(50, 5, txt = str(df['PlusMinus'].iloc[i]), border = 1, align = 'C', fill = True)
        pdf.ln()
        pdf.cell(200, 10, txt = 'Shooting stats', ln = 1, align = 'L') #creamos una tabla con las estadisticas de tiro
        pdf.cell(50, 5, txt = 'Field Goals Made', border = 1, align = 'C', fill = True)
        pdf.cell(50, 5, txt = str(df['FieldGoalsMade'].iloc[i]), border = 1, align = 'C', fill = True)
        pdf.ln()
        pdf.cell(50, 5, txt = 'Field Goals Attempted', border = 1, align = 'C', fill = True)
        pdf.cell(50, 5, txt = str(df['FieldGoalsAttempted'].iloc[i]), border = 1, align = 'C', fill = True)
        pdf.ln()
        pdf.cell(50, 5, txt = '3 Pointers Made', border = 1, align = 'C', fill = True)
        pdf.cell(50, 5, txt = str(df['ThreePointersMade'].iloc[i]), border = 1, align = 'C', fill = True)
        pdf.ln()
        pdf.cell(50, 5, txt = '3 Pointers Attempted', border = 1, align = 'C', fill = True)
        pdf.cell(50, 5, txt = str(df['ThreePointersAttempted'].iloc[i]), border = 1, align = 'C', fill = True)
        pdf.ln()
        pdf.cell(50, 5, txt = 'Free Throws Made', border = 1, align = 'C', fill = True)
        pdf.cell(50, 5, txt = str(df['FreeThrowsMade'].iloc[i]), border = 1, align = 'C', fill = True)
        pdf.ln()
        pdf.cell(50, 5, txt = 'Free Throws Attempted', border = 1, align = 'C', fill = True)
        pdf.cell(50, 5, txt = str(df['FreeThrowsAttempted'].iloc[i]), border = 1, align = 'C', fill = True)
        pdf.ln()
        pdf.cell(50, 5, txt = '2 Pointers Made', border = 1, align = 'C', fill = True)
        pdf.cell(50, 5, txt = str(df['TwoPointersMade'].iloc[i]), border = 1, align = 'C', fill = True)
        pdf.ln()
        pdf.cell(50, 5, txt = '2 Pointers Attempted', border = 1, align = 'C', fill = True)
        pdf.cell(50, 5, txt = str(df['TwoPointersAttempted'].iloc[i]), border = 1, align = 'C', fill = True)
        pdf.ln()
        pdf.cell(50, 5, txt = 'True Shooting Attemps', border = 1, align = 'C', fill = True)
        pdf.cell(50, 5, txt = str(df['TrueShootingAttempts'].iloc[i]), border = 1, align = 'C', fill = True)
        pdf.ln()
        pdf.cell(200, 10, txt = 'Percentage stats', ln = 1, align = 'L') #creamos una tabla con las estadisticas de porcentaje

        pdf.cell(50, 5, txt = 'Field Goals Percentage', border = 1, align = 'C', fill = True)
        pdf.cell(50, 5, txt = str(df['FieldGoalsPercentage'].iloc[i]), border = 1, align = 'C', fill = True)
        pdf.ln()
        pdf.cell(50, 5, txt = 'Free Throw Percentage', border = 1, align = 'C', fill = True)
        pdf.cell(50, 5, txt = str(df['FreeThrowsPercentage'].iloc[i]), border = 1, align = 'C', fill = True)
        pdf.ln()
        pdf.cell(50, 5, txt = '2 Point Percentage', border = 1, align = 'C', fill = True)
        pdf.cell(50, 5, txt = str(df['TwoPointersPercentage'].iloc[i]), border = 1, align = 'C', fill = True)
        pdf.ln()
        pdf.cell(50, 5, txt = 'Effective Field Goal Percentage', border = 1, align = 'C', fill = True)
        pdf.cell(50, 5, txt = str(df['EffectiveFieldGoalsPercentage'].iloc[i]), border = 1, align = 'C', fill = True)
        pdf.ln()
        pdf.cell(50, 5, txt = '3 Point Percentage', border = 1, align = 'C', fill = True)
        pdf.cell(50, 5, txt = str(df['ThreePointersPercentage'].iloc[i]), border = 1, align = 'C', fill = True)
        pdf.ln()
        pdf.cell(50, 5, txt = 'True Shooting Percentage', border = 1, align = 'C', fill = True)
        pdf.cell(50, 5, txt = str(df['TrueShootingPercentage'].iloc[i]), border = 1, align = 'C', fill = True)
        pdf.ln()
        

    pdf.output('philadelphia.pdf', 'F') #guardamos el pdf
    

if __name__ == '__main__':
    philadelphia = extract() #formato etl
    philadelphia = transform(philadelphia)
    load(philadelphia)
    