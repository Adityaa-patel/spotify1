from spotify1.panda import songs_only_df
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams.update({
    'axes.facecolor': '#282c34',
    'axes.edgecolor': '#abb2bf',
    'axes.labelcolor': '#ffffff',
    'xtick.color': '#ffffff',
    'ytick.color': '#ffffff',
    'grid.color': '#4b5263',
    'figure.facecolor': '#1c1e24',
    'legend.facecolor': '#282c34',
    'legend.edgecolor': '#abb2bf',
    'text.color': '#ffffff',
})

def plot_weekly_listening(artists, df):
    df = df.copy()
    df.loc[:, 'ts'] = pd.to_datetime(df['ts'])
    df = df.sort_values('ts')
    conversion_factor = 1000 * 60 * 60  

    plt.figure(figsize=(12, 6))
    for artist in artists:
                artist_data = df[df['master_metadata_album_artist_name'] == artist]
                weekly_data = artist_data.set_index('ts').resample('W')['ms_played'].sum().reset_index()
                weekly_data['hours_played'] = weekly_data['ms_played'] / conversion_factor

                plt.plot(weekly_data['ts'], weekly_data['hours_played'],
                 label=artist, alpha=0.4, linewidth=2)


    total_data = df.set_index('ts').resample('W')['ms_played'].sum().reset_index()
    total_data['hours_played'] = total_data['ms_played'] / conversion_factor
    plt.plot(total_data['ts'], total_data['hours_played'],
             label='Total Listening Time', color='black', linestyle='--', linewidth=2, alpha=0.5)

    plt.title('Weekly Listening Time Graph', fontsize=16, weight='bold', color='#61dafb')
    plt.xlabel('Week', fontsize=12, weight='bold')
    plt.ylabel('Hours Played (Smoothed)', fontsize=12, weight='bold')
    plt.legend(framealpha=0.8, fontsize=10, loc='upper left')
    plt.grid(alpha=0.5)
    plt.show()

def plot_weekly_percentage(artists, df):

    df = df.copy()
    df.loc[:, 'ts'] = pd.to_datetime(df['ts'])
    df = df.sort_values('ts')
    conversion_factor = 1000 * 60 * 60  

    total_data = df.set_index('ts').resample('W')['ms_played'].sum().reset_index()
    total_data['hours_played_total'] = total_data['ms_played'] / conversion_factor

    plt.figure(figsize=(12, 6))
    for artist in artists:
        artist_data = df[df['master_metadata_album_artist_name'] == artist]
        weekly_data = artist_data.set_index('ts').resample('W')['ms_played'].sum().reset_index()
        weekly_data['hours_played_artist'] = weekly_data['ms_played'] / conversion_factor

        merged = pd.merge(weekly_data, total_data, on='ts', how='inner')

        merged['percentage'] = (merged['hours_played_artist'] / merged['hours_played_total']) * 100

        plt.plot(merged['ts'], merged['percentage'],
                 label=f'{artist} (%)', alpha=0.4, linewidth=2)

    plt.title('Weekly Percentage per Artist', fontsize=16, weight='bold', color='#61dafb')
    plt.xlabel('Week', fontsize=12, weight='bold')
    plt.ylabel('Percentage of Total Listening (%)', fontsize=12, weight='bold')
    plt.legend(framealpha=0.8, fontsize=10, loc='upper left')
    plt.grid(alpha=0.5)
    plt.show()

artists = ["Eminem", "Nirvana", "The Beatles","Miki Matsubara"]

plot_weekly_listening(artists, songs_only_df)
plot_weekly_percentage(artists, songs_only_df)
