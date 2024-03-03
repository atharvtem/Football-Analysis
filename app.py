import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Load the dataset
df = pd.read_csv('2022-2023 Football Player Stats.csv', delimiter=';', encoding='latin1')


# Streamlit App
st.title("Football Player Statistics Dashboard")
#
#

selected_league = st.selectbox("Select League:", df['Comp'].unique())
filtered_df = df[df['Comp'] == selected_league]


# Visualization 1: Bar graph showing highest goal scorers (top 20)
top_scorers = filtered_df.nlargest(20, 'Goals')
fig1 = px.bar(top_scorers, x='Player', y='Goals', title='Top 20 Goal Scorers', labels={'Goals': 'Number of Goals'})
fig1.update_traces(hovertemplate='Player: %{x}<br>Goals: %{y}')
st.plotly_chart(fig1)

























# Calculate a metric for goal contribution (e.g., goals + assists)
df['GoalContribution'] = df['Goals'] + df['Assists']

# Select the top 20 players based on goal contribution
top_players = df.nlargest(20, 'GoalContribution')

# Create a scatterplot with size corresponding to goal contribution
fig = px.scatter(top_players, x='Assists', y='Goals', size='GoalContribution',
                 labels={'Assists': 'Number of Assists', 'Goals': 'Number of Goals'},
                 title='Scatterplot: Top 20 Players - Goal Contribution',
                 hover_name='Player')

# Customize the layout for better readability
fig.update_traces(marker=dict(line=dict(width=2, color='DarkSlateGray')), selector=dict(mode='markers'))

# Display the scatterplot
st.plotly_chart(fig)





















# Add a league filter with "All Leagues" option
selected_league = st.selectbox("Select League:", ['All Leagues'] + list(df['Comp'].unique()))
if selected_league == 'All Leagues':
    filtered_df = df
else:
    filtered_df = df[df['Comp'] == selected_league]

# Visualization: Multiline chart for Progressive Passes (PasProg)
positions = ['FW', 'MF', 'DF']

# Create a dataframe with the top 10 players from each position
top_players_df = pd.concat([filtered_df[filtered_df['Pos'] == pos].nlargest(10, 'PasProg') for pos in positions])

# Create a multiline chart
fig = px.line(top_players_df, x='Player', y='PasProg', color='Pos',
              labels={'PasProg': 'Progressive Passes', 'Player': 'Player'},
              title='Top 10 Players - Progressive Passes by Position',
              range_y=[0, 50], render_mode='svg')

# Place dots on the line at each player point
fig.update_traces(mode='markers+lines', hovertemplate='Player: %{x}<br>Progressive Passes: %{y}')

# Show the chart
st.plotly_chart(fig)













# Visualization: Bar graph showing top 20 players with most touches in attacking 3rd
top_players_attacking_3rd = filtered_df.nlargest(20, 'TouAtt3rd')
fig = px.bar(top_players_attacking_3rd, x='Player', y='TouAtt3rd',
             labels={'TouAtt3rd': 'Touches in Attacking 3rd', 'Player': 'Player'},
             title='Top 20 Players - Touches in Attacking 3rd',
             hover_data=['TouAtt3rd'])

# Show the chart
st.plotly_chart(fig)









#
#
# Add interactive elements (e.g., dropdowns, sliders, etc.)
# selected_position = st.selectbox("Select Position:", df['Pos'].unique())
# selected_nation = st.selectbox("Select Nation:", df['Nation'].unique())

# Filter the dataframe based on user selection
# filtered_df = df[(df['Pos'] == selected_position) & (df['Nation'] == selected_nation)]


# You can add more visualizations and interactive elements based on the requirements
# Example: Bar chart for Goals by Position
# Calculate the sum of goals for each playing position
goals_by_position = df.groupby('Pos')['Goals'].sum().reset_index()

# Create a bar graph
fig = px.bar(goals_by_position, x='Pos', y='Goals',
             labels={'Pos': 'Playing Position', 'Goals': 'Number of Goals'},
             title='Number of Goals by Playing Position')

# Customize the layout for better readability
fig.update_layout(xaxis_title='Playing Position', yaxis_title='Number of Goals')

# Display the bar graph
st.plotly_chart(fig)










# Display filtered dataframe
# st.dataframe(filtered_df)












# Calculate the total number of yellow and red cards for each club
discipline_by_club = df.groupby('Squad')[['CrdY', 'CrdR']].sum().reset_index()

# Calculate a total discipline score for each club (sum of yellow and red cards)
discipline_by_club['DisciplineScore'] = discipline_by_club['CrdY'] + discipline_by_club['CrdR']

# Create a treemap
fig = px.treemap(discipline_by_club, 
                 path=['Squad'],
                 values='DisciplineScore',
                 title='Club Discipline - Treemap',
                 labels={'Squad': 'Club', 'DisciplineScore': 'Discipline Score'})

# Customize the layout for better readability
fig.update_layout(margin=dict(l=0, r=0, b=0, t=30))

# Display the treemap
st.plotly_chart(fig)









country_mapping = {
    'AFG': 'Afghanistan',
    'ALB': 'Albania',
    'ALG': 'Algeria',
    'AND': 'Andorra',
    'ANG': 'Angola',
    'ANT': 'Antigua and Barbuda',
    'ARG': 'Argentina',
    'ARM': 'Armenia',
    'ARU': 'Aruba',
    'AUS': 'Australia',
    'AUT': 'Austria',
    'AZE': 'Azerbaijan',
    'BAH': 'Bahamas',
    'BHR': 'Bahrain',
    'BAN': 'Bangladesh',
    'BRB': 'Barbados',
    'BLR': 'Belarus',
    'BEL': 'Belgium',
    'BLZ': 'Belize',
    'BEN': 'Benin',
    'BER': 'Bermuda',
    'BHU': 'Bhutan',
    'BOL': 'Bolivia',
    'BIH': 'Bosnia and Herzegovina',
    'BOT': 'Botswana',
    'BRA': 'Brazil',
    'BRN': 'Bahrain',
    'BUL': 'Bulgaria',
    'BUR': 'Burundi',
    'CAM': 'Cameroon',
    'CAN': 'Canada',
    'CPV': 'Cape Verde',
    'CAF': 'Central African Republic',
    'CHI': 'Chile',
    'CHN': 'China',
    'COL': 'Colombia',
    'COM': 'Comoros',
    'CGO': 'Congo',
    'CRC': 'Costa Rica',
    'CIV': "Côte d'Ivoire",
    'CRO': 'Croatia',
    'CUB': 'Cuba',
    'CUW': 'Curaçao',
    'CYP': 'Cyprus',
    'CZE': 'Czech Republic',
    'DEN': 'Denmark',
    'DJI': 'Djibouti',
    'DMA': 'Dominica',
    'DOM': 'Dominican Republic',
    'ECU': 'Ecuador',
    'EGY': 'Egypt',
    'SLV': 'El Salvador',
    'ENG': 'United Kingdom',
    'EQG': 'Equatorial Guinea',
    'ERI': 'Eritrea',
    'EST': 'Estonia',
    'ETH': 'Ethiopia',
    'FAR': 'Faroe Islands',
    'FIJ': 'Fiji',
    'FIN': 'Finland',
    'FRA': 'France',
    'GAB': 'Gabon',
    'GAM': 'Gambia',
    'GEO': 'Georgia',
    'GER': 'Germany',
    'GHA': 'Ghana',
    'GRE': 'Greece',
    'GRN': 'Grenada',
    'GUM': 'Guam',
    'GUA': 'Guatemala',
    'GUI': 'Guinea',
    'GNB': 'Guinea-Bissau',
    'GUY': 'Guyana',
    'HAI': 'Haiti',
    'HON': 'Honduras',
    'HKG': 'Hong Kong',
    'HUN': 'Hungary',
    'ISL': 'Iceland',
    'IND': 'India',
    'IDN': 'Indonesia',
    'IRN': 'Iran',
    'IRQ': 'Iraq',
    'IRL': 'Ireland',
    'ISR': 'Israel',
    'ITA': 'Italy',
    'JAM': 'Jamaica',
    'JPN': 'Japan',
    'JOR': 'Jordan',
    'KAZ': 'Kazakhstan',
    'KEN': 'Kenya',
    'KIR': 'Kiribati',
    'KOR': 'Korea Republic',
    'KOS': 'Kosovo',
    'KUW': 'Kuwait',
    'KGZ': 'Kyrgyzstan',
    'LAO': 'Laos',
    'LAT': 'Latvia',
    'LIB': 'Lebanon',
    'LES': 'Lesotho',
    'LBR': 'Liberia',
    'LBY': 'Libya',
    'LIE': 'Liechtenstein',
    'LTU': 'Lithuania',
    'LUX': 'Luxembourg',
    'MKD': 'North Macedonia',
    'MAD': 'Madagascar',
    'MWI': 'Malawi',
    'MAS': 'Malaysia',
    'MDV': 'Maldives',
    'MLI': 'Mali',
    'MLT': 'Malta',
    'MHL': 'Marshall Islands',
    'MTN': 'Mauritania',
    'MRI': 'Mauritius',
    'MEX': 'Mexico',
    'MDA': 'Moldova',
    'MCO': 'Monaco',
    'MGL': 'Mongolia',
    'MNE': 'Montenegro',
    'MAR': 'Morocco',
    'MOZ': 'Mozambique',
    'MYA': 'Myanmar',
    'NAM': 'Namibia',
    'NRU': 'Nauru',
    'NEP': 'Nepal',
    'NED': 'Netherlands',
    'NZL': 'New Zealand',
    'NCA': 'Nicaragua',
    'NIG': 'Niger',
    'NGA': 'Nigeria',
    'NOR': 'Norway',
    'OMA': 'Oman',
    'PAK': 'Pakistan',
    'PLW': 'Palau',
    'PLE': 'Palestine',
    'PAN': 'Panama',
    'PNG': 'Papua New Guinea',
    'PAR': 'Paraguay',
    'PER': 'Peru',
    'PHI': 'Philippines',
    'POL': 'Poland',
    'POR': 'Portugal',
    'PUR': 'Puerto Rico',
    'QAT': 'Qatar',
    'ROU': 'Romania',
    'RUS': 'Russia',
    'RWA': 'Rwanda',
    'SKN': 'Saint Kitts and Nevis',
    'LCA': 'Saint Lucia',
    'SAM': 'Samoa',
    'SMR': 'San Marino',
    'STP': 'Sao Tome and Principe',
    'SAU': 'Saudi Arabia',
    'SCO': 'Scotland',
    'SEN': 'Senegal',
    'SRB': 'Serbia',
    'SEY': 'Seychelles',
    'SLE': 'Sierra Leone',
    'SIN': 'Singapore',
    'SVK': 'Slovakia',
    'SVN': 'Slovenia',
    'SOL': 'Solomon Islands',
    'SOM': 'Somalia',
    'RSA': 'South Africa',
    'SSD': 'South Sudan',
    'ESP': 'Spain',
    'SRI': 'Sri Lanka',
    'SDN': 'Sudan',
    'SUR': 'Suriname',
    'SWZ': 'Swaziland',
    'SWE': 'Sweden',
    'SUI': 'Switzerland',
    'SYR': 'Syria',
    'TPE': 'Chinese Taipei',
    'TJK': 'Tajikistan',
    'TAN': 'Tanzania',
    'THA': 'Thailand',
    'TLS': 'Timor-Leste',
    'TOG': 'Togo',
    'TGA': 'Tonga',
    'TRI': 'Trinidad and Tobago',
    'TUN': 'Tunisia',
    'TUR': 'Turkey',
    'TKM': 'Turkmenistan',
    'TCA': 'Turks and Caicos Islands',
    'UGA': 'Uganda',
    'UKR': 'Ukraine',
    'UAE': 'United Arab Emirates',
    'USA': 'United States',
    'URU': 'Uruguay',
    'UZB': 'Uzbekistan',
    'VAN': 'Vanuatu',
    'VEN': 'Venezuela',
    'VIE': 'Vietnam',
    'VIR': 'Virgin Islands (U.S.)',
    'WAL': 'Wales',
    'YEM': 'Yemen',
    'ZAM': 'Zambia',
    'ZIM': 'Zimbabwe',
}


# Replace short country names with full names
df['Nation'] = df['Nation'].map(country_mapping)

# Calculate the number of players from each country
players_by_country = df['Nation'].value_counts().reset_index()
players_by_country.columns = ['Country', 'Number of Players']

# Create a map plot with a blue color scale
fig = px.choropleth(players_by_country, 
                    locations='Country',
                    locationmode='country names',
                    color='Number of Players',
                    color_continuous_scale='Blues',  # Use the 'Blues' color scale
                    title='Number of Players from Each Country')

# Customize the layout for better readability
fig.update_layout(geo=dict(showframe=True, showcoastlines=True, projection_type='equirectangular'))

# Display the map plot
st.plotly_chart(fig)











# Count the number of players based on playing positions
position_count = df['Pos'].value_counts().reset_index()
position_count.columns = ['Playing Position', 'Count']

# Create a donut chart for playing positions
fig = go.Figure(go.Pie(labels=position_count['Playing Position'], values=position_count['Count'], hole=0.3, name='Playing Positions'))
fig.update_layout(title_text=f'Donut Chart for Playing Positions', showlegend=True)

# Display the donut chart
st.plotly_chart(fig)










# Get the top 5 clubs with the most shots on target
top_clubs_shots_on_target = df.groupby('Squad')['SoT'].sum().nlargest(5).reset_index()

# Create a funnel chart for the top 5 clubs
fig = px.funnel(top_clubs_shots_on_target, x='SoT', y='Squad',
                title="Top 5 Clubs with the Most Shots on Target",
                labels={'SoT': 'Total Shots on Target', 'Squad': 'Club'})

# Display the funnel chart
st.plotly_chart(fig)


# Get the top 5 clubs with the best passing accuracy
top_clubs_passing_accuracy = df.groupby('Squad')['PasTotCmp%'].mean().nlargest(5).reset_index()

# Create a funnel chart for the top 5 clubs
fig = px.funnel(top_clubs_passing_accuracy, x='PasTotCmp%', y='Squad',
                title="Top 5 Clubs with the Best Passing Accuracy",
                labels={'PasTotCmp%': 'Passing Accuracy', 'Squad': 'Club'})

# Display the funnel chart
st.plotly_chart(fig)


# Get the top 5 clubs with the best records of tackles won
top_clubs_tackles = df.groupby('Squad')['TklWon'].sum().nlargest(5).reset_index()

# Create a funnel chart for the top 5 clubs
fig = px.funnel(top_clubs_tackles, x='TklWon', y='Squad', 
                title="Top 5 Clubs with the Best Records of Tackles Won",
                labels={'TklWon': 'Total Tackles Won', 'Squad': 'Club'})

# Display the funnel chart
st.plotly_chart(fig)