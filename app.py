import streamlit as st
import preprocessor,helper
import matplotlib.pyplot as plt
import seaborn as sns

st.sidebar.title("Whatsapp Chat Analyzer")

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

        # Stats Area
        num_messages, words, num_media_messages, num_links = helper.fetch_stats(selected_user,df)
        st.title("Top Statistics")
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.header("Total Messages")
            st.subheader(num_messages)
        with col2:
            st.header("Total Words")
            st.subheader(words)
        with col3:
            st.header("Media Shared")
            st.subheader(num_media_messages)
        with col4:
            st.header("Links Shared")
            st.subheader(num_links)

        # monthly timeline
        st.title("Monthly Timeline")
        timeline = helper.monthly_timeline(selected_user,df)
        fig,ax = plt.subplots()
        ax.plot(timeline['time'], timeline['message'],color='green')
        plt.xticks(rotation='vertical')
        plt.xlabel('Months', color='green')
        plt.ylabel('No. of messages', color='green')
        st.pyplot(fig)

        # daily timeline
        st.title("Daily Timeline")
        daily_timeline = helper.daily_timeline(selected_user, df)
        fig, ax = plt.subplots()
        ax.plot(daily_timeline['only_date'], daily_timeline['message'], color='gold')
        plt.xticks(rotation='vertical')
        plt.xlabel('Date', color='gold')
        plt.ylabel('No. of messages', color='gold')
        st.pyplot(fig)

        # activity map
        st.title('Activity Map')
        col1,col2 = st.columns(2)

        with col1:
            st.header("Most busy day")
            busy_day = helper.week_activity_map(selected_user,df)
            fig,ax = plt.subplots()
            ax.bar(busy_day.index,busy_day.values,color='purple')
            plt.xticks(rotation='vertical')
            plt.xlabel('Days', color='purple')
            plt.ylabel('No. of messages', color='purple')
            st.pyplot(fig)

        with col2:
            st.header("Most busy month")
            busy_month = helper.month_activity_map(selected_user, df)
            fig, ax = plt.subplots()
            ax.bar(busy_month.index, busy_month.values,color='hotpink')
            plt.xticks(rotation='vertical')
            plt.xlabel('Months', color='hotpink')
            plt.ylabel('No. of messages', color='hotpink')
            st.pyplot(fig)

        st.title("Weekly Activity Map")
        user_heatmap = helper.activity_heatmap(selected_user,df)
        fig,ax = plt.subplots()
        ax = sns.heatmap(user_heatmap)
        st.pyplot(fig)

        # finding the most active users in the group(Group level)
        if selected_user == 'Overall':
            st.title('Most Active Users')
            x,new_df = helper.most_active_users(df)
            fig, ax = plt.subplots()

            col1, col2 = st.columns(2)

            with col1:
                ax.bar(x.index, x.values,color='sandybrown')
                plt.xticks(rotation='vertical')
                plt.xlabel('Users', color='sandybrown')
                plt.ylabel('No. of messages', color='sandybrown')
                st.pyplot(fig)
            with col2:
                st.dataframe(new_df)

        # WordCloud
        st.title("Wordcloud")
        df_wc = helper.create_wordcloud(selected_user,df)
        fig,ax = plt.subplots()
        ax.imshow(df_wc)
        st.pyplot(fig)

        # most common words
        most_common_df = helper.most_common_words(selected_user,df)

        fig,ax = plt.subplots()

        ax.barh(most_common_df[0],most_common_df[1], color='cyan')
        plt.xticks(rotation='vertical')
        plt.xlabel('Frequency', color='cyan')
        plt.ylabel('Words', color='cyan')
        st.title('Most commmon words')
        st.pyplot(fig)

        # emoji analysis
        emojis, emoji_df = helper.emoji_helper(selected_user,df)
        st.title("Emoji Analysis")
        if len(emojis):
            col1,col2 = st.columns(2)

            with col1:
                st.dataframe(emoji_df)
            with col2:
                fig,ax = plt.subplots()
                ax.pie(emoji_df["Frequency"].head(),labels=emoji_df["Emoji"].head(),autopct="%0.2f")
                st.pyplot(fig)
    
        else:
            st.info("No emoji found in the conversation!")
        

        #sentiment analysis
        positive, negative, neutral, sentiment = helper.sentiments_of_users(selected_user,df)
        st.title("Sentiment Analysis")
        if selected_user=="Overall":
            selected_user="Group"

            
        if sentiment=="pos":
            st.info("Sentiment of " + selected_user + " is POSITIVE.")
        elif sentiment=="neg":
            st.info("Sentiment of " + selected_user + " is NEGATIVE.")
        elif sentiment=="neu":
            st.info("Sentiment of " + selected_user + " is NEUTRAL.")

        st.info(selected_user + " is rated as " + str(positive*100) + " % positive.")
        st.info(selected_user + " is rated as " + str(negative*100) + " % negative.")
        st.info(selected_user + " is rated as " + str(neutral*100) + " % neutral.")
        











