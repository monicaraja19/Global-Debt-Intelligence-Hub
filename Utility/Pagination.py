import streamlit as st
import math

#
def paginate_dataframe(df, page_size=10, key="table"):

    total_rows = len(df)

    page_key = f"{key}_page"

    if page_key not in st.session_state:
        st.session_state[page_key] = 1

    current_page = st.session_state[page_key]

    if total_rows > page_size:
        total_pages = math.ceil(total_rows / page_size)

        start = (current_page - 1) * page_size
        end = start + page_size

        display_df = df.iloc[start:end]
    else:
        display_df = df
        current_page = 1
        total_pages = 1
        start = 0
        end = total_rows

    return display_df, current_page, total_pages, start, end, total_rows, page_key
def render_table_footer(start, end, total_rows, current_page, total_pages, page_key):
    """
    Professional table footer with pagination arrows
    """

    # Showing text
    st.markdown(
        f"**Showing {start + 1}-{min(end, total_rows)} of {total_rows} records**"
    )

    # Footer layout
    col1, col2, col3 = st.columns([3, 2, 3])

    with col2:
        inner_col1, inner_col2, inner_col3 = st.columns([1, 2, 1])

        with inner_col1:
            if st.button("◀", disabled=current_page == 1, key=f"{page_key}_prev"):
                st.session_state[page_key] -= 1
                st.rerun()

        with inner_col2:
            st.markdown(
                f"<div style='text-align:center;font-weight:600;'>"
                f"Page {current_page} of {total_pages}"
                f"</div>",
                unsafe_allow_html=True
            )

        with inner_col3:
            if st.button("▶", disabled=current_page == total_pages, key=f"{page_key}_next"):
                st.session_state[page_key] += 1
                st.rerun()