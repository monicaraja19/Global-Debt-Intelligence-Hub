import streamlit as st
import pandas as pd
from DatabaseConnectionAndQuery.assesment_query import show_advanced_query,show_basic_query,show_intermediate_query
from Utility.Pagination import paginate_dataframe, render_table_footer

#pagination
def apply_pagination_summary(filtered_df,option):
    if filtered_df.empty:
        st.write("No data available.")
    else:
        # Pagination
        display_df, current_page, total_pages, start, end, total_rows, page_key = paginate_dataframe(filtered_df,page_size=10,key=f"{option}")
        row_height = 35
        header_height = 38
        dynamic_height = header_height + (len(display_df) * row_height)
        st.dataframe(display_df,
            use_container_width=True,
            hide_index=True,
            height=min(dynamic_height, 600)  # max limit
        )
        # Pagination Footer
        render_table_footer(start,end,total_rows,current_page,total_pages,page_key)
        
#assesment query
def show_query():
    st.set_page_config(page_title="GDIH-About",page_icon="Assets/gdih_logo.png",layout="wide")
    query_result_1,query_result_2,query_result_3,query_result_4,query_result_5,query_result_6,query_result_7,query_result_8,query_result_9,query_result_10 = show_basic_query()
    query_result_11,query_result_12,query_result_13,query_result_14,query_result_15,query_result_16,query_result_17,query_result_18,query_result_19,query_result_20 = show_intermediate_query()
    query_result_21,query_result_22,query_result_23,query_result_24,query_result_25,query_result_26,query_result_27,query_result_28,query_result_29,query_result_30 = show_advanced_query()
    queryList = ["1.Retrieve all distinct country names from the dataset.","2.Count the total number of countries available.",
                 "3.Find the total number of indicators present.","4.Display the first 10 records of the dataset.","5.Calculate the total global debt.",
                 "6.List all unique indicator names.","7.Find the number of records for each country.",
                 "8.Display all records where debt is greater than 1 billion USD.","9.Find the minimum, maximum, and average debt values.","10.Count total number of records in the dataset.",
                 "11.Find the total debt for each country.","12.Display the top 10 countries with the highest total debt.",
                 "13.Find the average debt per country.","14.Calculate total debt for each indicator.","15.Identify the indicator contributing the highest total debt.",
                 "16.Find the country with the lowest total debt.","17.Calculate total debt for each country and indicator combination.",
                 "18.Count how many indicators each country has.","19.Display countries whose total debt is above the global average.","20.Rank countries based on total debt (highest to lowest).",
                 "21.Find the top 5 indicators contributing most to global debt.","22.Calculate percentage contribution of each country to total global debt.",
                 "23.Identify the top 3 countries for each indicator based on debt.","24.Find the difference between maximum and minimum debt for each country.","25.Create a view for the top 10 countries with highest debt.",
                 "26.Categorize countries into:High debt,Low debt,Medium debt(based on threshold)","27.Use window functions to calculate cumulative debt per country.",
                 "28.Find indicators where average debt is higher than overall average debt.","29.Identify countries contributing more than 5% of global debt.","30.Find the most dominant indicator (highest contribution) for each country."]
    selected_query = st.selectbox("Select Query",options= queryList)
    query_num = int(selected_query.split(".")[0])
    if query_num == 1:
        st.write("All distinct country names from the Countries_debt dataset.")
        filtered_df=query_result_1
    elif query_num == 2:
        st.write("Total number of countries available.")
        filtered_df = query_result_2
    elif query_num == 3:
        st.write("Total number of indicators present.")
        filtered_df = query_result_3
    elif query_num == 4:
        st.write("The first 10 records of the Countries_debt dataset.")
        filtered_df = query_result_4
    elif query_num == 5:
        st.write("The total global debt.")
        filtered_df = query_result_5
    elif query_num == 6:
        st.write("All unique indicator names.")
        filtered_df = query_result_6
    elif query_num == 7:
        st.write("The number of records for each country.")
        filtered_df = query_result_7
    elif query_num == 8:
        st.write("All records where debt is greater than 1 billion USD.")
        filtered_df = query_result_8
    elif query_num == 9:
        st.write("The minimum, maximum, and average debt values.")
        filtered_df= query_result_9
    elif query_num == 10:
        st.write("Total number of records in the Countries_debt dataset.")
        filtered_df = query_result_10
    elif query_num == 11:
        st.write("The total debt for each country.")
        filtered_df = query_result_11
    elif query_num == 12:
        st.write("The top 10 countries with the highest total debt.")
        filtered_df = query_result_12
    elif query_num == 13:
        st.write("The average debt per country.")
        filtered_df = query_result_13
    elif query_num == 14:
        st.write("Total debt for each indicator.")
        filtered_df = query_result_14
    elif query_num == 15:
        st.write("Indicator contributing the highest total debt.")
        filtered_df = query_result_15
    elif query_num == 16:
        st.write("The country with the lowest total debt.")
        filtered_df = query_result_16
    elif query_num == 17:
        st.write("Total debt for each country and indicator combination.")
        filtered_df = query_result_17
    elif query_num == 18:
        st.write("Count of indicators each country has.")
        filtered_df = query_result_18
    elif query_num == 19:
        st.write("Countries whose total debt is above the global average.")
        filtered_df=query_result_19
    elif query_num == 20:
        st.write("Ranked countries based on total debt (highest to lowest).")
        filtered_df = query_result_20
    elif query_num == 21:
        st.write("The top 5 indicators contributing most to global debt.")
        filtered_df = query_result_21
    elif query_num == 22:
        st.write("Percentage contribution of each country to total global debt.")
        filtered_df = query_result_22
    elif query_num == 23:
        st.write("The top 3 countries for each indicator based on debt.")
        filtered_df = query_result_23
    elif query_num == 24:
        st.write("The difference between maximum and minimum debt for each country.")
        filtered_df = query_result_24
    elif query_num == 25:
        st.write("View table for the top 10 countries with highest debt.")
        filtered_df = query_result_25
    elif query_num == 26:
        st.write("Categorized countries into:High debt,Low debt,Medium debt(based on threshold)")
        filtered_df = query_result_26
    elif query_num == 27:
        st.write("Used window functions to calculate cumulative debt per country.")
        filtered_df= query_result_27
    elif query_num == 28:
        st.write("Indicators where average debt is higher than overall average debt.")
        filtered_df = query_result_28
    elif query_num == 29:
        st.write("Countries contributing more than 5% of global debt.")
        filtered_df = query_result_29
    elif query_num == 30:
        st.write("The most dominant indicator (highest contribution) for each country.")
        filtered_df = query_result_30
    #applying pagination to the filtered dataframe based on the selected query
    apply_pagination_summary(filtered_df,query_num)