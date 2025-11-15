from urlextract import URLExtract

ext = URLExtract()


def fetch_stats(selected_user,df):

    if selected_user != "Overall":
       df=df[df['user'] == selected_user]

    # 1. Number of messages
    num_messages = df.shape[0]
    # 2. Number of Words
    words=[]
    for message in df['message']:
        words.extend(message.split())  
    # 3. Number of media files sent
    media=df[df['message']=="<Media omitted>\n"].shape[0] 
    # 4. Number of Links
    links=[]
    for mess in df['message']:
        links.extend(ext.find_urls(mess))    

    return num_messages,len(words),media,len(links)

def busiest_users(df):
    df = df[df['user'] != 'group_notification']
    n = 5 if df['user'].nunique() < 50 else 10
    x = df['user'].value_counts().head(n)
    df = round((df['user'].value_counts() / df.shape[0]) * 100, 2).reset_index()

    df.columns = ['User', 'Percentage']        # change column names
    df.index = df.index + 1                    # 1-based indexing
    df['Percentage'] = df['Percentage'].astype(str) + '%'   # add % sign
    return x,df

def create_wordcloud(selected_user,df):
    from wordcloud import WordCloud

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    temp = df[df['message'] != '<Media omitted>\n']
    wc = WordCloud(width=500, height=500, min_font_size=10, background_color='white')
    wc.generate(temp['message'].str.cat(sep=" "))

    return wc

def most_common_words(selected_user,df):
    from collections import Counter
    import pandas as pd

    f=open('combined_stopwords.txt','r')
    stop_words=f.read().split()
    f.close()

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    temp = df[df['user'] != 'group_notification']
    temp = temp[temp['message'] != '<Media omitted>\n']

    words = []
    for message in temp['message']:
        for word in message.lower().split():
            if word not in stop_words:
                words.append(word)

    most_common_df = pd.DataFrame(Counter(words).most_common(20))
    return most_common_df

def most_used_emojis(selected_user,df):
    import pandas as pd
    from collections import Counter
    import emoji

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    emojis = []
    for message in df['message'].dropna():
        # EMOJI_DATA may not exist in some emoji versions; guard with getattr
        emoji_data = getattr(emoji, 'EMOJI_DATA', {})
        emojis.extend([c for c in message if c in emoji_data])

    counter = Counter(emojis)

    if not counter:
        return pd.DataFrame(columns=['Emoji', 'Count', 'Percentage Usage'])

    emoji_df = pd.DataFrame(counter.most_common()).rename(
        columns={0: 'Emoji', 1: 'Count'}
    )

    emoji_df['Percentage Usage'] = round(
        (emoji_df['Count'] / emoji_df['Count'].sum()) * 100, 2
    ).astype(str) + '%'

    emoji_df.index = emoji_df.index + 1    # 1-based indexing

    return emoji_df

def monthly_timeline(selected_user,df):

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    timeline = df.groupby(['year', 'month_num', 'month']).count()['message'].reset_index()

    time = []
    for i in range(timeline.shape[0]):
        time.append(timeline['month'][i] + "-" + str(timeline['year'][i]))

    timeline['time'] = time

    return timeline

def daily_timeline(selected_user,df):

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    daily_timeline = df.groupby('only_date').count()['message'].reset_index()

    return daily_timeline

def activity_heatmap(selected_user,df):

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    user_heatmap = df.pivot_table(index='day_name', columns='period', values='message', aggfunc='count').fillna(0)


    return user_heatmap

def week_activity_map(selected_user,df):

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    return df['day_name'].value_counts()

def month_activity_map(selected_user,df):

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    return df['month'].value_counts()

def user_contribution(selected_user, df):
    df2 = df[df['user'] != 'group_notification']

    total_messages = df2.shape[0]

    user_count = df2[df2['user'] == selected_user].shape[0]

    percentage = round((user_count / total_messages) * 100, 2)

    # Check if this user is the busiest
    busiest_user = df2['user'].value_counts().idxmax()

    is_busiest = (selected_user == busiest_user)

    return percentage, is_busiest
