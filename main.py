import streamlit as st
import preprocessor
import helper
import matplotlib.pyplot as plt

st.sidebar.title("CONVOLENS -The Whatsapp Chat Analyzer")

uploaded_file = st.sidebar.file_uploader("Choose a file")

if uploaded_file is not None:

    bytes_data = uploaded_file.getvalue()
    data = bytes_data.decode("utf-8")
    df = preprocessor.preprocess(data)



    # fetch unique users
    user_list = df['user'].unique().tolist()
    user_list.remove('group_notification')
    user_list.sort()
    user_list.insert(0,"Overall")

    selected_user = st.sidebar.selectbox("Show analysis wrt",user_list)

    if st.sidebar.button("Show Analysis"):
        st.title("In-Depth Analysis of Whatsapp Chat")

        num_messages, words, media, links = helper.fetch_stats(selected_user, df)

        col1,col2,col3,col4=st.columns(4)
        
        with col1:
            st.header("Total Messages")
            st.title(num_messages)

        with col2:
            st.header("Total Words")
            st.title(words)      

        with col3:
            st.header("Media shared")
            st.title(media)      

        with col4:
            st.header("Links shared")
            st.title(links) 

        # monthly timeline
        st.title("Monthly Timeline")
        timeline = helper.monthly_timeline(selected_user,df)
        fig,ax = plt.subplots()
        ax.plot(timeline['time'], timeline['message'],color='green')
        plt.xticks(rotation='vertical')
        st.pyplot(fig)

        # daily timeline
        st.title("Daily Timeline")
        daily_timeline = helper.daily_timeline(selected_user, df)
        fig, ax = plt.subplots()
        ax.plot(daily_timeline['only_date'], daily_timeline['message'], color='blue')
        plt.xticks(rotation='vertical')
        st.pyplot(fig)

        st.title("Activity Map")
        col1, col2 = st.columns(2)  

        with col1:
            st.header("Most Busy Day")
            busy_day = helper.week_activity_map(selected_user,df)
            fig,ax=plt.subplots()
            ax.bar(busy_day.index,busy_day.values,color='orange')
            plt.xticks(rotation='vertical')
            st.pyplot(fig)
 
        with col2:
            st.header("Most Busy Month")
            busy_month = helper.month_activity_map(selected_user,df)
            fig,ax=plt.subplots()
            ax.bar(busy_month.index,busy_month.values,color='pink')
            plt.xticks(rotation='vertical')
            st.pyplot(fig)
        

        st.title("Weekly Activity Map")
        user_heatmap = helper.activity_heatmap(selected_user, df)

        fig, ax = plt.subplots(figsize=(10, 4))

        # Draw heatmap
        cax = ax.imshow(user_heatmap, cmap='cividis', aspect='auto')

        # Add colorbar
        cbar = plt.colorbar(cax)

        # Add label to colorbar showing Least Active → Most Active
        cbar.set_label("Activity Level (Least Active → Most Active)", rotation=90, labelpad=15)
        # Add labels from DataFrame
        ax.set_xticks(range(len(user_heatmap.columns)))
        ax.set_xticklabels(user_heatmap.columns, rotation=45, ha='right')

        ax.set_yticks(range(len(user_heatmap.index)))
        ax.set_yticklabels(user_heatmap.index)

        ax.set_xlabel("Period")
        ax.set_ylabel("Day Name")
        ax.set_title("Weekly Activity Heatmap")

        st.pyplot(fig)




        # busiest users
        if selected_user == 'Overall':
            st.title('Busiest Users')
            x, new_df = helper.busiest_users(df)

            fig, ax = plt.subplots()
            col1, col2 = st.columns(2)

            with col1:
                ax.bar(x.index, x.values, color='green')
                plt.xticks(rotation='vertical')
                st.pyplot(fig)

            with col2:
                st.dataframe(new_df)

        else:
            # Show message contribution for selected user
            percentage, is_busiest = helper.user_contribution(selected_user, df)

            msg = f"**{selected_user} contributes {percentage}% of total messages in the group.**"

            if is_busiest:
                msg += " 🎉 **Being the busiest user in the chat!**"

            st.header(msg)


        # WordCloud
        st.title("WordCloud")
        wc = helper.create_wordcloud(selected_user, df)
        fig, ax = plt.subplots()
        ax.imshow(wc, interpolation='bilinear')
        ax.axis('off')
        st.pyplot(fig)

        # Most common words
        st.title("Most Common Words")
        common_words = helper.most_common_words(selected_user, df)
        fig, ax = plt.subplots()
        ax.bar(common_words[0], common_words[1], color='purple')
        plt.xticks(rotation='vertical')
        st.pyplot(fig)

        # Emojis
        st.title("Most Used Emojis")    
        emoji_df = helper.most_used_emojis(selected_user, df)
        st.dataframe(emoji_df)