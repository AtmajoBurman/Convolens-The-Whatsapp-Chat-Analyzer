import regex as re
import pandas as pd
def preprocess(data):
    # matches dd/mm/yy or dd/mm/yyyy, time with optional thin space before am/pm
    pattern = r'\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{2}\s?[apAP][mM]\s-\s'

    messages = re.split(pattern, data)[1:]
    dates = re.findall(pattern, data)

    # strip trailing ' - ' from the matched date strings so pandas can infer format
    dates_clean = [d.rstrip(' - ') for d in dates]

    df = pd.DataFrame({'user_message': messages, 'message_date': dates_clean})

    # let pandas infer format; dayfirst=True handles dd/mm/yy and dd/mm/yyyy
    df['message_date'] = pd.to_datetime(df['message_date'], dayfirst=True, errors='coerce')
    df.rename(columns={'message_date': 'date'}, inplace=True)

    users = []
    pure_messages = []

    for msg in df['user_message']:
        parts = re.split(r'^([^:]+):\s', msg, maxsplit=1)
        if len(parts) == 3:
            users.append(parts[1])
            pure_messages.append(parts[2])
        else:
            users.append("group_notification")
            pure_messages.append(parts[0])

    df['user'] = users
    df['message'] = pure_messages
    df.drop(columns=['user_message'], inplace=True)

    df['only_date'] = df['date'].dt.date
    df['year'] = df['date'].dt.year
    df['month_num'] = df['date'].dt.month
    df['month'] = df['date'].dt.month_name()
    df['day'] = df['date'].dt.day
    df['day_name'] = df['date'].dt.day_name()
    df['hour'] = df['date'].dt.hour
    df['minute'] = df['date'].dt.minute

    period = []
    for hour in df[['day_name', 'hour']]['hour']:
        if hour == 23:
            period.append(str(hour) + "-" + str('00'))
        elif hour == 0:
            period.append(str('00') + "-" + str(hour + 1))
        else:
            period.append(str(hour) + "-" + str(hour + 1))

    df['period'] = period
    return df
