import streamlit as st
import pandas as pd
import plotly
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
#from webdriver_manager.chrome import ChromeDriverManager
import base64,random
import streamlit_authenticator as stauth
import time,datetime
from pymongo import MongoClient
from pyresparser import ResumeParser
from pdfminer3.layout import LAParams, LTTextBox
from pdfminer3.pdfpage import PDFPage
from pdfminer3.pdfinterp import PDFResourceManager
from pdfminer3.pdfinterp import PDFPageInterpreter
from pdfminer3.converter import TextConverter
import io,random
import spacy


from streamlit_tags import st_tags
from PIL import Image
import pymysql
import sklearn
import yaml
from yaml.loader import SafeLoader
with open('/home/sakthivel.chendilvel/Music/Smart_Resume_Analyser_App/config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

usernames=[]
pages=[]
passwords=[]
if len(passwords) > 0:
    hashed_passwords = stauth.Hasher(passwords).generate()

with open('/home/sakthivel.chendilvel/Music/Smart_Resume_Analyser_App/styles.css') as f:
    css = f.read()

#

import redis

r = redis.Redis(
  host='redis-17990.c11.us-east-1-2.ec2.cloud.redislabs.com',
  port=17990,
  password='u0cxsqUjfX2ROjJ8yFnDnbMFcAf5vdX4')


def _connect_mongo(host, port, username, password, db):
    """ A util for making a connection to mongo """

    if username and password:
        mongo_uri = 'mongodb+srv://sakthivel:sakthi007@atlascluster.t5flwl7.mongodb.net/?retryWrites=true&w=majority' % (username, password, host, port, db)
        conn = MongoClient(mongo_uri)
    else:
        conn = MongoClient(host, port)


    return conn[db]


from pymongo_get_database import get_database
from dateutil import parser
dbname = get_database()
collection_name = dbname["user5"]

#importing database for job applications
from pymongo_get_database2 import get_database
from dateutil import parser
dbname = get_database()
collection_name2 = dbname["jobApplications"]

#importing database for job applications
from pymongo_get_database3 import get_database
from dateutil import parser
dbname = get_database()
collection_name3 = dbname["Admin"]

#importing database for job ApplicantSide
from pymongo_get_database4 import get_database
from dateutil import parser
dbname = get_database()
collection_name4 = dbname["JobApplicantSide"]




st.set_page_config(
   page_title="AI Based WebAPP for Job Application and Talent Sourcing",
   page_icon='./Logo/SRA_Logo.ico',
   


)
   
page_bg_img = '''
<style>
body {
background-image: url("https://dinpattern.com/2019/12/07/dinos/");
background-size: cover;
}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)

#st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

import base64
def add_bg_from_url():
    st.markdown(
    f"""
    <style>
    .stApp {{
    background-image: url("https://dinpattern.com/2019/12/07/dinos/");
    background-attachment: fixed;
    background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_url()
def get_img_as_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

imag = get_img_as_base64("sc1.png")

def s ():
    st.markdown(
    """
    <style>
        [data-testid="stHeader"]{
        background-color:rgba(0,0,0,0);}
        
    </style>
    """,
    unsafe_allow_html=True
    )
s()

def x ():
    st.markdown(
    """
    <style>
      
        [data-testid="stSidebar"]> div:first-child{
        background-image:url("data:image/png;base64,{imag}");
        background-position:center;
        }
        
    </style>
    """,
    unsafe_allow_html=True
    )
st.sidebar.header('')
x()


#st.markdown(page_bg_img,unsafe_allow_html=True)

#connection = pymysql.connect(host='localhost',user='root',password='',db='ra')
#cursor = connection.cursor()
#def insert_data1(name,email,res_score,no_of_pages,skills):
###   insert_sql1 = "insert into " + DB_table_name + """
   #####connection.commit()

# importing required modules
from PyPDF2 import PdfReader
RESERVED_WORDS = [
    'school',
    'college',
    'univers',
    'academy',
    'faculty',
    'institute',
    'faculdades',
    'Schola',
    'schule',
    'lise',
    'lyceum',
    'lycee',
    'polytechnic',
    'kolej',
    'ünivers',
    'okul',
]
 
 



from Courses import ds_course,web_course,android_course,ios_course,uiux_course,resume_videos,interview_videos

import plotly.express as px
###
#def fetch_yt_video(link):
 #   video = pafy.new(link)
#    return video.title

def get_table_download_link(df,filename,text):
    """Generates a link allowing the data in a given panda dataframe to be downloaded
    in:  dataframe
    out: href string
    """
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # some strings <-> bytes conversions necessary here
    # href = f'<a href="data:file/csv;base64,{b64}">Download Report</a>'
    href = f'<a href="data:file/csv;base64,{b64}" download="{filename}">{text}</a>'
    return href

def pdf_reader(file):
    resource_manager = PDFResourceManager()
    fake_file_handle = io.StringIO()
    converter = TextConverter(resource_manager, fake_file_handle, laparams=LAParams())
    page_interpreter = PDFPageInterpreter(resource_manager, converter)
    with open(file, 'rb') as fh:
        for page in PDFPage.get_pages(fh,
                                      caching=True,
                                      check_extractable=True):
            page_interpreter.process_page(page)
            print(page)
        text = fake_file_handle.getvalue()

    # close open handles
    converter.close()
    fake_file_handle.close()
    return text


def show_pdf(file_path):
    with open(file_path, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    # pdf_display = f'<embed src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf">'
    pdf_display = F'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)

def course_recommender(course_list):
    st.subheader("**Courses & Certificates🎓 Recommendations**")
    c = 0
    rec_course = []
    no_of_reco = st.slider('Choose Number of Course Recommendations:', 1, 10, 4)
    random.shuffle(course_list)
    for c_name, c_link in course_list:
        c += 1
        st.markdown(f"({c}) [{c_name}]({c_link})")
        rec_course.append(c_name)
        if c == no_of_reco:
            break
    return rec_course

##cursor = connection.cursor()

#####rec_values = (name, email, str(res_score), timestamp,str(no_of_pages), reco_field, cand_level, skills,recommended_skills,courses)
    ##connection.commit()


def run():
    st.title("Resume Screening AI App")
    st.sidebar.markdown("# Choose User")
    activities = ["Job Applicant", "Recruiter","JobDescription Matching","Form Filling","Admin"]
    choice = st.sidebar.selectbox("Choose among the given options:", activities)
    # link = '[©Developed by Spidy20](http://github.com/spidy20)'
    # st.sidebar.markdown(link, unsafe_allow_html=True)
    #img = Image.open('./Logo/SRA_Logo.jpg')
    #img = img.resize((250,250))
    #st.image(img)

    # Create the DB
    #db_sql = """CREATE DATABASE IF NOT EXISTS SRA;"""
    #cursor.execute(db_sql)

    # Create table
    DB_table_name = 'user_data'
    table_sql = "CREATE TABLE IF NOT EXISTS " + DB_table_name + """
                    (ID INT NOT NULL AUTO_INCREMENT,
                     Name varchar(100) NOT NULL,
                     Email_ID VARCHAR(50) NOT NULL,
                     resume_score VARCHAR(8) NOT NULL,
                     Timestamp VARCHAR(50) NOT NULL,
                     Page_no VARCHAR(5) NOT NULL,
                     Predicted_Field VARCHAR(25) NOT NULL,
                     User_level VARCHAR(30) NOT NULL,
                     Actual_skills VARCHAR(300) NOT NULL,
                     Recommended_skills VARCHAR(300) NOT NULL,
                     Recommended_courses VARCHAR(600) NOT NULL,
                     PRIMARY KEY (ID));
     
                   """
                   #Recommended_skills VARCHAR(300) NOT NULL,
                    #Recommended_courses VARCHAR(600) NOT NULL,
    #cursor.execute(table_sql)
    if choice == 'Job Applicant':
        # st.markdown('''<h4 style='text-align: left; color: #d73b5c;'>* Upload your resume, and get smart recommendation based on it."</h4>''',
        #             unsafe_allow_html=True)

        pdf_file = st.file_uploader("Choose your Resume", type=["pdf"])
        if pdf_file is not None:
            # with st.spinner('Uploading your Resume....'):
            #     time.sleep(4)
            save_image_path = './Uploaded_Resumes/'+pdf_file.name
            with open(save_image_path, "wb") as f:
                f.write(pdf_file.getbuffer())
            show_pdf(save_image_path)
            resume_data = ResumeParser(save_image_path).get_extracted_data()
            if resume_data:
                ## Get the whole resume data
                resume_text = pdf_reader(save_image_path)
                #education = extract_education(resume_text)
                st.header("**Resume Analysis**")
                st.success("Hello "+ resume_data['name'])
                st.subheader("**Data Scraped From Resume**")
                try:
                    st.text('Name: '+resume_data['name'])
                    st.text('Email: ' + resume_data['email'])
                    #st.text('College Name: ' + education)
                    
                    #st.text('Company Name: ' + resume_data['company_names'])
                    #st.text('Designation: ' + resume_data['designation'])
                    #st.text('Years Of Experience: ' + resume_data['degree'])
                    st.text('Contact: ' + resume_data['mobile_number'])
                    st.text('Resume pages: '+str(resume_data['no_of_pages']))
                    st.text('Degree:'+"Bachelor Of Engineering")
                except:
                    pass
                cand_level = ''
                if resume_data['no_of_pages'] == 1:
                    cand_level = "Fresher"
                    st.markdown( '''<h4 style='text-align: left; color: #d73b5c;'>You are looking Fresher.</h4>''',unsafe_allow_html=True)
                elif resume_data['no_of_pages'] == 2:
                    cand_level = "Intermediate"
                    st.markdown('''<h4 style='text-align: left; color: #1ed760;'>You are at intermediate level!</h4>''',unsafe_allow_html=True)
                elif resume_data['no_of_pages'] >=3:
                    cand_level = "Experienced"
                    st.markdown('''<h4 style='text-align: left; color: #fba171;'>You are at experience level!''',unsafe_allow_html=True)

                #st.subheader("**Skills Recommendation💡**")
                ## Skill shows
                keywords = st_tags(label='### Skills that you have',
                #text='See our skills recommendation',
                    value=resume_data['skills'],key = '1')

                ##  recommendation
                ds_keyword = ['tensorflow','keras','pytorch','machine learning','deep Learning','flask','streamlit']
                web_keyword = ['react', 'django', 'node jS', 'react js', 'php', 'laravel', 'magento', 'wordpress',
                               'javascript', 'angular js', 'c#', 'flask']
                android_keyword = ['android','android development','flutter','kotlin','xml','kivy']
                ios_keyword = ['ios','ios development','swift','cocoa','cocoa touch','xcode']
                uiux_keyword = ['ux','adobe xd','figma','zeplin','balsamiq','ui','prototyping','wireframes','storyframes','adobe photoshop','photoshop','editing','adobe illustrator','illustrator','adobe after effects','after effects','adobe premier pro','premier pro','adobe indesign','indesign','wireframe','solid','grasp','user research','user experience']

                recommended_skills = []
                reco_field = ''
                rec_course = ''
                ## Courses recommendation
                for i in resume_data['skills']:
                    ## Data science recommendation
                    if i.lower() in ds_keyword:
                        print(i.lower())
                        reco_field = 'Data Science'
                        st.success("** Our analysis says you are looking for Data Science Jobs.**")
                        recommended_skills = ['Data Visualization','Predictive Analysis','Statistical Modeling','Data Mining','Clustering & Classification','Data Analytics','Quantitative Analysis','Web Scraping','ML Algorithms','Keras','Pytorch','Probability','Scikit-learn','Tensorflow',"Flask",'Streamlit']
                        recommended_keywords = st_tags(label='### Recommended skills for you.',
                        text='Recommended skills generated from System',value=recommended_skills,key = '2')
                        st.markdown('''<h4 style='text-align: left; color: #1ed760;'>Adding this skills to resume will boost🚀 the chances of getting a Job💼</h4>''',unsafe_allow_html=True)
                        rec_course = course_recommender(ds_course)
                        break

                    ## Web development recommendation
                    elif i.lower() in web_keyword:
                        print(i.lower())
                        reco_field = 'Web Development'
                        st.success("** Our analysis says you are looking for Web Development Jobs **")
                        recommended_skills = ['React','Django','Node JS','React JS','php','laravel','Magento','wordpress','Javascript','Angular JS','c#','Flask','SDK']
                        recommended_keywords = st_tags(label='### Recommended skills for you.',
                        text='Recommended skills generated from System',value=recommended_skills,key = '3')
                        st.markdown('''<h4 style='text-align: left; color: #1ed760;'>Adding this skills to resume will boost🚀 the chances of getting a Job💼</h4>''',unsafe_allow_html=True)
                        rec_course = course_recommender(web_course)
                        break

                    ## Android App Development
                    elif i.lower() in android_keyword:
                        print(i.lower())
                        reco_field = 'Android Development'
                        st.success("** Our analysis says you are looking for Android App Development Jobs **")
                        recommended_skills = ['Android','Android development','Flutter','Kotlin','XML','Java','Kivy','GIT','SDK','SQLite']
                        recommended_keywords = st_tags(label='### Recommended skills for you.',
                        text='Recommended skills generated from System',value=recommended_skills,key = '4')
                        st.markdown('''<h4 style='text-align: left; color: #1ed760;'>Adding this skills to resume will boost🚀 the chances of getting a Job💼</h4>''',unsafe_allow_html=True)
                        rec_course = course_recommender(android_course)
                        break

                    ## IOS App Development
                    elif i.lower() in ios_keyword:
                        print(i.lower())
                        reco_field = 'IOS Development'
                        st.success("** Our analysis says you are looking for IOS App Development Jobs **")
                        recommended_skills = ['IOS','IOS Development','Swift','Cocoa','Cocoa Touch','Xcode','Objective-C','SQLite','Plist','StoreKit',"UI-Kit",'AV Foundation','Auto-Layout']
                        recommended_keywords = st_tags(label='### Recommended skills for you.',
                        text='Recommended skills generated from System',value=recommended_skills,key = '5')
                        st.markdown('''<h4 style='text-align: left; color: #1ed760;'>Adding this skills to resume will boost🚀 the chances of getting a Job💼</h4>''',unsafe_allow_html=True)
                        rec_course = course_recommender(ios_course)
                        break

                    ## Ui-UX Recommendation
                    elif i.lower() in uiux_keyword:
                        print(i.lower())
                        reco_field = 'UI-UX Development'
                        st.success("** Our analysis says you are looking for UI-UX Development Jobs **")
                        recommended_skills = ['UI','User Experience','Adobe XD','Figma','Zeplin','Balsamiq','Prototyping','Wireframes','Storyframes','Adobe Photoshop','Editing','Illustrator','After Effects','Premier Pro','Indesign','Wireframe','Solid','Grasp','User Research']
                        recommended_keywords = st_tags(label='### Recommended skills for you.',
                        text='Recommended skills generated from System',value=recommended_skills,key = '6')
                        st.markdown('''<h4 style='text-align: left; color: #1ed760;'>Adding this skills to resume will boost🚀 the chances of getting a Job💼</h4>''',unsafe_allow_html=True)
                        rec_course = course_recommender(uiux_course)
                        break

                #
                ## Insert into table
                ts = time.time()
                cur_date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
                cur_time = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
                timestamp = str(cur_date+'_'+cur_time)

                ### Resume writing recommendation
                #st.subheader("**Resume Tips & Ideas💡**")
                resume_score = 0
                if 'Objective' in resume_text:
                    resume_score = resume_score+20
                    #st.markdown('''<h4 style='text-align: left; color: #1ed760;'>[+] Awesome! You have added Objective</h4>''',unsafe_allow_html=True)
                #else:
                    #st.markdown('''<h4 style='text-align: left; color: #fabc10;'>[-] According to our recommendation please add your career objective, it will give your career intension to the Recruiters.</h4>''',unsafe_allow_html=True)

                if 'Declaration'  in resume_text:
                    resume_score = resume_score + 20
                    #st.markdown('''<h4 style='text-align: left; color: #1ed760;'>[+] Awesome! You have added Delcaration✍/h4>''',unsafe_allow_html=True)
                #else:
                    #st.markdown('''<h4 style='text-align: left; color: #fabc10;'>[-] According to our recommendation please add Declaration✍. It will give the assurance that everything written on your resume is true and fully acknowledged by you</h4>''',unsafe_allow_html=True)

                if 'Hobbies' or 'Interests'in resume_text:
                    resume_score = resume_score + 20
                    #st.markdown('''<h4 style='text-align: left; color: #1ed760;'>[+] Awesome! You have added your Hobbies⚽</h4>''',unsafe_allow_html=True)
                #else:
                    #st.markdown('''<h4 style='text-align: left; color: #fabc10;'>[-] According to our recommendation please add Hobbies⚽. It will show your persnality to the Recruiters and give the assurance that you are fit for this role or not.</h4>''',unsafe_allow_html=True)

                if 'Achievements' in resume_text:
                    resume_score = resume_score + 20
                    #st.markdown('''<h4 style='text-align: left; color: #1ed760;'>[+] Awesome! You have added your Achievements🏅 </h4>''',unsafe_allow_html=True)
                #else:
                    #st.markdown('''<h4 style='text-align: left; color: #fabc10;'>[-] According to our recommendation please add Achievements🏅. It will show that you are capable for the required position.</h4>''',unsafe_allow_html=True)

                if 'Projects' in resume_text:
                    resume_score = resume_score + 20
                    #st.markdown('''<h4 style='text-align: left; color: #1ed760;'>[+] Awesome! You have added your Projects👨‍💻 </h4>''',unsafe_allow_html=True)
                #else:
                    #st.markdown('''<h4 style='text-align: left; color: #fabc10;'>[-] According to our recommendation please add Projects👨‍💻. It will show that you have done work related the required position or not.</h4>''',unsafe_allow_html=True)

                st.subheader("**Resume Score📝**")
                st.markdown(
                    """
                    <style>
                        .stProgress > div > div > div > div {
                            background-color: #d73b5c;
                        }
                    </style>""",
                    unsafe_allow_html=True,
                )
                my_bar = st.progress(0)
                score = 0
                for percent_complete in range(resume_score):
                    score +=1
                    time.sleep(0.1)
                    my_bar.progress(percent_complete + 1)
                st.success('** Your Resume  Score is : ' + str(score)+'**')


                #st.warning("** Note: This score is calculated based on the content that you have added in your Resume. **")
                st.balloons()
                
                #insert_data(resume_data['name'], resume_data['email'], str(resume_score), timestamp,
                 ##            str(recommended_skills), str(rec_course))
                details={"name":resume_data['name'],
                         "email":resume_data['email'],
                         "resume_score ":str(score),
                         "time_of_update":timestamp,
                         "actual_skills":resume_data['skills'],
                         "predicted_field":reco_field,
                         "skills_recommended":recommended_skills,
                         "courses_recommended":str(rec_course)}
                collection_name.insert_one(details)

                st.write("---")
                st.subheader("Just For Fun!!!")
                col1, col2, col3 = st.columns(3)
                col1.metric("Temperature", "70 °F", "1.2 °F")
                col2.metric("Wind", "9 mph", "-8%")
                col3.metric("Humidity", "86%", "4%")
                
                st.write("---")

                st.subheader("Add Your Comments!!")
                name = st.text_input("Enter Your name")
                comments = st.text_area("Upload Comments")

                values = st.slider(
                    'Select a range of values',
                    0, 100, (0, 100))
                st.write('Values:', values)
                st.write("Give you user rating")

                st.subheader("Contact Details")

                tab1, tab2 = st.tabs(["Developer", "Tech Stack"])

                with tab1:
                    #st.image("/home/sakthivel.chendilvel/Music/Smart_Resume_Analyser_App/Background_images/dinos.png", width=200)
                    col1,col2 = st.columns(2)
                    with col1:
                        st.image("/home/sakthivel.chendilvel/Music/Smart_Resume_Analyser_App/Background_images/dinos.png", width=300)
                    with col2:
                        st.write("Sakthivel")
                        st.write("Email: sakthi372000@gmail.com")
                        st.write("Phone no:7871172038")



                with tab2:
                    col1,col2 = st.columns(2)
                    with col1:
                       st.image("/home/sakthivel.chendilvel/Music/Smart_Resume_Analyser_App/Background_images/pexels-markus-spiske-360591.jpg", width=300)
                    with col2:
                        st.write("Streamlit")
                        st.write("Fast API") 
                        st.write("MongoDB")
                        st.write("Redis")

            else:
                st.error('Something went wrong..')
    elif choice == 'Recruiter':
        st.success('Welcome to Admin Side')
        hashed_passwords = stauth.Hasher(passwords).generate()
        import plotly.express as px
        ad_user = st.text_input("Username")
        data = collection_name3.find_one({"Username":ad_user})
        ad_password = st.text_input("Password", type='password')
        datap= collection_name3.find_one({"Password":ad_password})
        pageCheck = collection_name3.find_one({"Page_Authorised":"Recruiter"})
        if st.button('Login'):
            if data is not None and datap is not None :
                st.success("Welcome Sakthivel C")
                data = collection_name.find()
                df= pd.DataFrame(data)
                #print(data)
                st.header("**Applicant's👨‍💻 Data**")
                st.dataframe(df)
                st.markdown(get_table_download_link(df,'User_Data.csv','Download Report'), unsafe_allow_html=True)
                st.snow()
                progress_text = "Operation in progress. Please wait."
    
                with st.spinner('Wait for it...'):
                  time.sleep(2)
                st.success('Done!')
                st.write("---")
                st.subheader("Applicantions Info")
                col1, col2 = st.columns([2,1])

                with col1:
                    st.image("https://www.thebalancemoney.com/thmb/GZgmGPlMTvN5CfquHuuamK6JFgI=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/human-resources--people-and-clipboard-with-job-candidates-list-and-magnifying-glass--employment--job-search--hiring--recruitment--recruiting--hr-concepts--modern-flat-design--vector-illustration-1184240745-fc899337c20349ee819743f198c4e6d2.jpg")
            

                with col2:
                    st.metric(label="Active Applicants", value=int(df.size/12), delta=0.5,
                        delta_color="inverse")

                    st.metric(label="Inactive developers", value=int(df.size()/10)-int(df.size/12), delta=-0.5,
                        delta_color="off")
                   # st.image("https://static.streamlit.io/examples/dog.jpg")
                expander = st.expander("See Explanation")
                expander.write("This field indicates the users who are active and developers who are inactive (i.e) those who dont often visit this webpage")
                import graphviz
                import numpy as np
                st.write("---")
                # Create a graphlib graph object
                st.subheader("**Graphical Representation of 👨Data**")
                graph = graphviz.Digraph()
                graph.edge('Name',"Applicant" )
                graph.edge('resume_score',"Applicant's Eligibiliy")
                graph.edge('Skills', 'resume_score')
                graph.edge('Skills', 'predicted_field')
                graph.edge('recommended-skills', 'predicted_field')
                graph.edge('Job', 'predicted_field')
                graph.edge('predicted_field', 'Recruiters Interest')
                graph.edge('resume_score', 'Overall Rsult')
                
                st.graphviz_chart(graph)
                expander = st.expander("See Explanation")
                expander.write("This is more like a graph or flow of events which occurs to find suitable match for the job description")
                st.write("---")
                st.write("##")
                st.subheader("**Area Plot for predicted Field**")
                data = collection_name.find()

                
                chart_data = pd.DataFrame(
                np.random.randn(100, 3),
                columns=['Predicted Field', 'Applicants', 'Score'])
                
                st.area_chart(chart_data)
                expander = st.expander("See Explanation")
                expander.write("The plot explains about the predicted field of the Applicants")

                import plotly.figure_factory as ff

# Add histogram data
                st.write("---")
                st.subheader("Plot for Job👨‍💻 Roles")
                x1 = np.random.randn(200) - 2
                x2 = np.random.randn(200)
                x3 = np.random.randn(200) + 2

                # Group data together
                hist_data = [x1, x2, x3]

                group_labels = ['Group 1-Software', 'Group 2-Core Engineering', 'Group 3-Data Science']

                # Create distplot with custom bin_size
                fig = ff.create_distplot(
                        hist_data, group_labels, bin_size=[.1, .25, .5])

                # Plot!
                
                st.plotly_chart(fig, use_container_width=True)
                
                st.write("---")
                st.subheader("Just For Fun!!!")
                col1, col2, col3 = st.columns(3)
                col1.metric("Temperature", "70 °F", "1.2 °F")
                col2.metric("Wind", "9 mph", "-8%")
                col3.metric("Humidity", "86%", "4%")
                
                st.write("---")

                st.subheader("Add Your Comments!!")
                name = st.text_input("Enter Your name")
                comments = st.text_area("Upload Comments")

                values = st.slider(
                    'Select a range of values',
                    0, 100, (0, 100))
                st.write('Values:', values)
                st.write("Give you user rating")

                st.subheader("Contact Details")

                tab1, tab2 = st.tabs(["Developer", "Tech Stack"])

                with tab1:
                    #st.image("/home/sakthivel.chendilvel/Music/Smart_Resume_Analyser_App/Background_images/dinos.png", width=200)
                    col1,col2 = st.columns(2)
                    with col1:
                        st.image("/home/sakthivel.chendilvel/Music/Smart_Resume_Analyser_App/Background_images/dinos.png", width=300)
                    with col2:
                        st.write("Sakthivel")
                        st.write("Email: sakthi372000@gmail.com")
                        st.write("Phone no:7871172038")



                with tab2:
                    col1,col2 = st.columns(2)
                    with col1:
                       st.image("/home/sakthivel.chendilvel/Music/Smart_Resume_Analyser_App/Background_images/pexels-markus-spiske-360591.jpg", width=300)
                    with col2:
                        st.write("Streamlit")
                        st.write("Fast API") 
                        st.write("MongoDB")
                        st.write("Redis")

                


            else:
                st.error("Wrong ID & Password Provided")
    elif choice == "JobDescription Matching":
        pdf_file = st.file_uploader("Choose your Resume", type=["pdf"])
        resume_text=""
        jd_text=""
        count =0
        if pdf_file is not None:
            save_image_path = './Uploaded_Resumes/'+pdf_file.name
            with open(save_image_path, "wb") as f:
                f.write(pdf_file.getbuffer())
            show_pdf(save_image_path)
            count+=1
            resume_data = ResumeParser(save_image_path).get_extracted_data()
            resume_text = pdf_reader(save_image_path)
            #print(resume_text)
        pdf_file_jd = st.file_uploader("Choose your the Job Description", type=["pdf"])
        
        if pdf_file_jd is not None:
            # with st.spinner('Uploading your Resume....'):
            #     time.sleep(4)
            save_image_path1 = './Uploaded_Resumes/'+pdf_file_jd.name
            with open(save_image_path1, "wb") as f:
                f.write(pdf_file_jd.getbuffer())
            show_pdf(save_image_path1)
            count+=1
            jd_text = pdf_reader(save_image_path1)


        if count == 2 :
            resume_text = PdfReader('./Uploaded_Resumes/'+pdf_file.name)
            jd_text= PdfReader('./Uploaded_Resumes/'+pdf_file_jd.name)
            progress_text = "Operation in progress. Please wait."
            my_bar = st.progress(0, text=progress_text)

            for percent_complete in range(10):
                time.sleep(0.1)
                my_bar.progress(percent_complete + 1, text=progress_text)
            page = resume_text.pages[0]
            text = page.extract_text()
            page1 = jd_text.pages[0]
            text1 = page1.extract_text()
            ans = [text,text1]
            from sklearn.feature_extraction.text import CountVectorizer
            cv = CountVectorizer()
            count_mat = cv.fit_transform(ans)
            from sklearn.metrics.pairwise import cosine_similarity
            st.write("---")
        
        
            matchPercentage = cosine_similarity(count_mat)[0][1]*100
            matchPercentage = round(matchPercentage,2)
            st.subheader("**Similarity Score📝**")
            st.write(cosine_similarity(count_mat))
            st.markdown(
                    """
                    <style>
                        .stProgress > div > div > div > div {
                            background-color: #d73b5c;
                        }
                    </style>""",
                    unsafe_allow_html=True,
            )
            st.success('** Your similarity  Score is : ' + str(matchPercentage)+'% of the job description''**')
            #st.write("The similarity score is : " + str(matchPercentage) + "% of the job description.")
            #print(matchPercentage)
            db_detailsforApp={"name":resume_data['name'],"email":resume_data["email"],
                              "resume_socre":str(matchPercentage)}
            collection_name4.insert_one(db_detailsforApp)

            data4 = collection_name4.find()
            df4= pd.DataFrame(data4)
            #print(data)
            st.write("---")
            st.subheader("**Applicant's👨‍💻 Data**")
            st.dataframe(df4)
            import numpy as np
            chart_data = df4["name"]
            chart_data2=df4["resume_score"]
            st.write("---")
            st.subheader("For More Info!!!")
            chart = pd.DataFrame(
                 np.random.rand(100,2)
                ,columns=["pages","resume-score"]
            )
            st.bar_chart(chart)

           # resume_data = ResumeParser(save_image_path).get_extracted_data()

           

        #db_sql = """CREATE DATABASE IF NOT EXISTS SRA;"""
        #cursor.execute(db_sql)

        if count ==2:
            # Create table
            DB_table_name = 'jd_data'
            table_sql1 = "CREATE TABLE IF NOT EXISTS " + DB_table_name + """
                            (ID INT NOT NULL AUTO_INCREMENT,
                            Name varchar(100) NOT NULL,
                            Email_ID VARCHAR(50) NOT NULL,
                            resume_score VARCHAR(8) NOT NULL,
                            
                            Page_no VARCHAR(5) NOT NULL,
                            
                            Actual_skills VARCHAR(300) NOT NULL,
                            
                            PRIMARY KEY (ID));
            
                        """
            
            save_image_path = './Uploaded_Resumes/'+pdf_file.name
            with open(save_image_path, "wb") as f:
                    f.write(pdf_file.getbuffer())
            #show_pdf(save_image_path)
                #count+=1
                #resume_data = ResumeParser(save_image_path).get_extracted_data()
            resume_data = ResumeParser(save_image_path).get_extracted_data()
            ###                  str(resume_data['no_of_pages']),str(resume_data['skills']))
            
            #cursor.execute(table_sql1)
           ## cursor.execute('''SELECT*FROM jd_data''')
           # data = cursor.fetchall()
            #st.header("**Applicant's👨‍💻 Data**")
            #df = pd.DataFrame(data, columns=['ID', 'Name', 'Email', 'Resume Score', 
            #'Total Page', 'Actual Skills'])
            #st.dataframe(df)
    
    elif choice =="Form Filling":

        authenticator = stauth.Authenticate(
            config['credentials'],
            config['cookie']['name'],
            config['cookie']['key'],
            config['cookie']['expiry_days'],
            config['preauthorized']
        )
        name, authentication_status, username = authenticator.login('Login', 'main')
        
        if st.session_state['authentication_status']:
            st.write('Welcome *%s*' % (st.session_state['name']))
            
            
        elif st.session_state['authentication_status'] == False:
            st.error('Username/password is incorrect')
        elif st.session_state['authentication_status'] == None:
            st.warning('Please enter your username and password')

        st.header("Job Application Automation")
        pdf_file = st.file_uploader("Choose your Resume", type=["pdf"])
        resume_text=""
        jd_text=""
        count =0
        if pdf_file is not None:
            save_image_path = './Uploaded_Resumes/'+pdf_file.name
            with open(save_image_path, "wb") as f:
                f.write(pdf_file.getbuffer())
            show_pdf(save_image_path)
            count+=1
            resume_data = ResumeParser(save_image_path).get_extracted_data()
            resume_text = pdf_reader(save_image_path)
        
        url = st.text_input("Enter a URL")
        st.markdown(url, unsafe_allow_html=True)
        CompanyName = st.text_input("Enter the Company Name")
        if not url.startswith("http") or not url.startswith("https"):
           st.stop()
        response=False
        if st.button(label="Submit"):
            #driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
            web =webdriver.Chrome()
            web.get(url)
            time.sleep(3)
            first_name = resume_data["name"]
            first = web.find_element("xpath",'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
            first.send_keys(first_name)

            email=resume_data["email"]
            last = web.find_element("xpath",'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
            last.send_keys(email)

            phoneno= resume_data["mobile_number"]
            phone = web.find_element("xpath",'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
            phone.send_keys(phoneno)

            pagesf = resume_data["no_of_pages"]
            pages = web.find_element("xpath",'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input')
            pages.send_keys(pagesf)

            skills = resume_data["skills"]
            skill = web.find_element("xpath",'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[1]/input')
            skill.send_keys(skills)

            degree ="Bachelor Of Engineering"
            deg = web.find_element("xpath",'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input')
            deg.send_keys(degree)
            
            
            submit = web.find_element("xpath",'//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
            submit.click()

            time.sleep(10)
            response =True
        
        if (response == True):
           st.success("Your Response has been submitted Successfully")
        
        ts = time.time()
        cur_date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
        cur_time = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
        timestamp = str(cur_date+'_'+cur_time)
        time.sleep(10)
        details={"URL":url,"Time":timestamp,"Company Name":CompanyName}
        collection_name2.insert_one(details)

        ApplicationData = collection_name2.find()
        df2= pd.DataFrame(ApplicationData)
                #print(data)
        st.header("**Application 👨‍💻 Data**")
        st.dataframe(df2)

    else:
        if 'stage' not in st.session_state:
            st.session_state.stage=0
        
        def set_stage(stage):
            st.session_state.stage=stage
        st.subheader("Admin Page")

        admin_user = st.text_input("Username")
        admin_name = "Sakthivel C"
        admin_password = st.text_input("Password", type='password')
        if (1):
            if admin_user == "x" and admin_password == "x":
                st.success("Welcome to Admin Page "+ admin_name)

                if 'ok_a' not in st.session_state:
                   st.session_state.ok_a = False

                # A upload
                with st.expander("Upload A CSV Files"):
                    uploaded_file = st.file_uploader("Upload A CSV", type=["csv"])
                
                    if uploaded_file is not None:
                        # your stuff

                        # Check error. 
                        if not st.session_state.ok_a:
                            with st.spinner("Checking for error log..."):
                                is_error = False
                        
                                if is_error:
                                    st.dataframe(['log A'])
                                else:
                                    st.success("File A uploaded successfully!")
                                    daf = pd.read_csv(uploaded_file)
                                    st.write(daf)

                                    size = int(daf.size/3)
                                    st.write(size)
                                    curuser=[]
                                    curpass=[]
                                    curpages=[]
                                    hashed=[]
                                # hashed=[]
                                    for i in range (0,size):
                                        usernames.append(daf.loc[i,"Username"])
                                        curuser.append(daf.loc[i,"Username"])
                                    
                                    
                                    for i in range (0,size):
                                        passwords.append(daf.loc[i,"Password"])
                                        curpass.append(daf.loc[i,"Password"])
                                    
                                    
                                    for i in range (0,size):
                                        pages.append(daf.loc[i,"Page-Authorised"])
                                        curpages.append(daf.loc[i,"Page-Authorised"])
                                        
                                    hashed_passwords = stauth.Hasher(curpass).generate()

                                    #hashed = stauth.Hasher(curpass).generate()
                                    

                                    for i in range (0,size):
                                        db_details={"Username":curuser[i],"Password":curpass[i],"Page_Authorised":
                                                curpages[i],"Hashed_Password":hashed_passwords[i]}
                                        collection_name3.insert_one(db_details)
                        else:
                            st.success("File A uploaded successfully!")
                            st.session_state.ok_a = True
   
                            size = int(daf.size/3)
                            st.write(size)
                            
                
                Admindata = collection_name3.find()
                df3= pd.DataFrame(Admindata)
                            #print(data)
                st.header("**Registered User's 👨‍💻 Data**")
                st.dataframe(df3)
                size = int(df3.size/5)
                appCount=0
                recCount=0
                while (size>0):
                    if collection_name3.find({"Page_Authorised":"Recruiter"}):
                        recCount+=1
                    else:           
                        appCount+=1
                    size-=1
                
                st.write("---")
                st.subheader("Users Info")
                col1, col2 = st.columns([2,1])

                with col1:
                    st.image("https://www.thebalancemoney.com/thmb/GZgmGPlMTvN5CfquHuuamK6JFgI=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/human-resources--people-and-clipboard-with-job-candidates-list-and-magnifying-glass--employment--job-search--hiring--recruitment--recruiting--hr-concepts--modern-flat-design--vector-illustration-1184240745-fc899337c20349ee819743f198c4e6d2.jpg")
            

                with col2:
                    st.metric(label="Active Applicants", value=recCount, delta=0.5,
                        delta_color="inverse")

                    st.metric(label="Inactive developers", value=appCount, delta=-0.5,
                        delta_color="off")
                

        

                
            else:
                st.error("Wrong Admin Credentails")


        
run()
