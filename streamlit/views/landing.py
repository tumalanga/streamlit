from pathlib import Path
import streamlit as st
from PIL import Image
from utils.path_helper import from_root

css_path = from_root("styles", "main.css")
# --- PATH SETTINGS ----
# current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
# css_file = "styles/main.css"
css_path = from_root("styles", "main.css")
# profile_file = "assets/pp.jpg"
profile_file = from_root("assets", "me.jpg")
# resume_file = "assets/DonovanAbednego_cv.pdf"
resume_file = from_root("assets", "DonovanAbednego_cv.pdf")

# --- GENERAL SETTINGS ----
PAGE_TITLE = "Digital CV | Donovan Abednego"
PAGE_ICON = ":wave:"
NAME = "Donovan Abednego"
DESCRIPTION = "Seeking opportunities to apply analytical expertise and automation skills in a dynamic professional setting."
EMAIL = "donovan.abednego@gmail.com"
SOCIAL_MEDIA = {"LinkedIn":"linkedin.com/in/dabednego"}

# --- header. WAJIB DI ATAS! ----
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --- CSS, pdf and prof pic ----
with open(css_path) as f:
    css = f.read()
    st.markdown("<style>{}</style>".format(css), unsafe_allow_html=True)
with open(resume_file,"rb") as pdf_file:
    PDFbyte = pdf_file.read()
# profile_pic = Image.open(profile_file)
profile_pic = Image.open(profile_file)

# --- mukadimah ----
col1,col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)
with col2:
    st.title(NAME)
    st.write(DESCRIPTION)

    st.download_button(
        label = "Download Resume",
        data=PDFbyte,
        file_name="DonovanAbednego_cv.pdf",
        mime="application/octet-stream"
    )
    st.write("Email",EMAIL)


# ---Social Links ----
st.write("#")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (plaftorm,link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{plaftorm}]({link})")

st.write("#")
st.subheader("Experience")
st.write("""- 💼 Experienced in on-site, remote, and hybrid work environments.
- 📈 Passionate about data-driven decision-making and process automation, with a strong focus on optimizing dataflows and reporting through scripting and advanced analytical tools to enhance efficiency.
- 👟 Skilled in collaborating with clients and stakeholders, managing upward communication, and addressing ad-hoc data requirements to support business objectives.""")

st.write("#")
st.subheader("Hard Skills")
st.write("""- Programming: Python, SQL, Bigquery
- Data Visualization: Tableau, Data Studio
- Other supporting tools: Hubspot, Google Sheets, Google Slides
- Languages: Bahasa Indonesia (native), English (CEFR B2), Mandarin Taiwan (On progress)""")

st.write("#")
st.subheader("Working Experience")
st.write("---")
st.write("**Liven PTY LTD | Data Analyst**")
st.write("Jun 2023 - Aug 2024 | Bali, Indonesia")
st.write("""
- • Automate Monthly Revenue Reporting, Commission Report, Team Sales Report and Individual commission report for the sales team.
- • Maintaining weekly revenue reporting for venue and product to determine which region has the best performance, tracking each sales performance is also possible.
- • Reducing data reporting time from 3 working days to just 3 working days.
- • Create Dataflow and datamart from the API to data platform. Prepared data from data platform to be distributed into several platforms i.e Google Sheets and Mosaic. Datamart has made data easier to be accessed efficiently by users from 3 hours request into just few minutes.
- • Designed and implemented Dataflow and Datamart to optimize data integration from the API to the data platform. Facilitated seamless data preparation and distribution to multiple platforms, including Google Sheets and Mosaic. The deployment of Datamart significantly enhanced data accessibility, reducing request processing time from three hours to just a few minutes.
- • Inhouse tools, Databricks and Hubspot to get the data, Google Colab and Google Sheets are our daily day to day tools. Looker is used in order to introducing data to user and help them cater their day to day data needs.""")
st.write("#")
st.write("**Tokocrypto | Social Media Data Analyst**")
st.write("Feb 2022 - Sep 2022 | Jakarta, Indonesia")
st.write("""- • Automate the flow and analyze the data source to stakeholders and help them to make data driven decisions.
- • Efficiency had been created for company since weekly Work in Progress (WIP) for Social Media and Corporate Communication team has made.
- • Cut the process of making weekly report from 5 days to just 3 days. Hence, improving campaign performance and got insides from data team is a big leap for Social Media team.•Used Brandwatch (formerly falcon.io), Google Colab, Google Sheets, Google Slides as daily day to day tools.
- • Used Brandwatch (formerly falcon.io), Google Colab, Google Sheets, Google Slides as daily day to day tools.""")

st.write("#")
st.write("**Redcomm Asia Inc. | Data Analyst Executive**")
st.write("Aug 2020 - Jan 2022 | Jakarta, Indonesia")
st.write("""
- • Automate Reporting process in order to support Business unit’s Data analyst and reduced 30% of reporting process.
- • Creating a dashboard of historical post to help Creative and Strategy team looking for inspirations for design, copy- writing and post schedule social media post for clients.
- • Tools involved: Fanpage Karma, Google Bigquery, Google Sheet, Tableau. Google Data Studio.""")

st.write("#")
st.write("**Redcomm Asia Inc. | Data Analyst Freelancer for Funnel Dashboard for Telco Company**")
st.write("May 2020 - Jul 2020 | Jakarta, Indonesia")
st.write("""
- • Established a funnel dashboard to enable clients to monitor and oversee the progress of their marketing and sales efforts.
- • Tableau was the main tool to conduct the dashboard, along with sample data via google sheets and excel file.""")

st.write("#")
st.write("**Conversant Solutions, Pte. Ltd. | Strategic Sales Executive**")
st.write("Mar 2017 - Mar 2020 | Jakarta, Indonesia")
st.write("""
- •Providing IT Solution in Content Delivery Network (CDN), Transcoding, game accelerator and Cache for company.
- • While using products, clients had made efficiency regarding the requests to their original servers by about 20% to 30%.
- • Partnering with Telkom International (Telin), Parolamas Insurance, Tado, Suara.com, RCTI Plus and other existing companies.""")

st.write("#")
st.subheader("Education")
st.write("""**Bina Nusantara University | Sep 2011 - Sep 2016**""")
st.write("""Bachelor of Accounting and Information Systems | Jakarta, Indonesia""")

st.write("#")
st.subheader("Other Course")
st.write("---")
# st.write("#")
st.write("""**National Taiwan Normal University | Sep 2024 - Feb 2025**""")
st.write("""Mandarin Training Center Non-Degree Program | Taipei, Taiwan""")
st.write("""
- • Huayu Enrichment Scholarship (HES) Recipient""")

st.write("""**Algoritma Data Science School | Bootcamp Data Analyst and Data Science Using R**""")
st.write("""Jan 2019 - Mar 2019 | Jakarta, Indonesia""")
st.write("""**Algoritma Data Science School | Bootcamp Data Analyst using Python**""")
st.write("""Sep 2019 - Oct 2019 | Jakarta, Indonesia""")
