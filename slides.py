import streamlit as st
import qrcode
import graphviz as graphviz


st.set_page_config(page_title='2022-12-8元智大學Python課演講', layout='wide')
topic = st.sidebar.selectbox(
	'',
	[
		'選擇要分享的內容',
		'為何改用Python進行研究工作？',
		'可以用Python解決哪些問題？',
		'如何藉由Python與天文維持關係？',
		'揪團用Python拉近群眾與星空的距離'
	]
)

if topic == '選擇要分享的內容':
	st.title('離開天文所後，我如何藉由Python與天文繼續維持關係')
	st.header('蘇羿豪@元智大學 2022-12-8')

	if st.button('開始'):
		_, col, _ = st.columns(3)
		with col:
			qr = qrcode.QRCode()
			qr.add_data(
				data='https://hackmd.io/D1cCtPqYQ3KYMKKnVd4fWg'
			)
			qr_img = qr.make_image(fill='black', back_color='white')
			qr_img.save('./qrcode_notes.png')
			st.subheader('這堂課的共筆')
			st.image('./qrcode_notes.png')

if topic == '為何改用Python進行研究工作？':
	st.header('為何改用Python進行研究工作？')
	with st.expander('為何進行天文研究工作需要寫程式？'):
		st.subheader('為何進行天文研究工作需要寫程式？')
		st.text('天文研究是藉由分析觀測資料或電腦模擬以了解天文現象，所以需要寫程式下載觀測資料、過濾資料、分析資料、視覺化資料、數值模擬天文物理現象。')

	with st.expander('我的程式語言經歷'):
		st.subheader('我的程式語言經歷')
		graph = graphviz.Digraph()
		graph.edge('C、Linux shell script', 'IDL')
		graph.edge('IDL', 'HTML、CSS、JavaScript、PHP、SQL')
		graph.edge('IDL', 'MATLAB')
		graph.edge('MATLAB', 'Python')
		st.graphviz_chart(graph)

	with st.expander('在研究工作上改用Python的契機與成果'):
		st.subheader('在研究工作上改用Python的契機與成果')
		st.markdown('* 在國際天文會議及workshop耳聞Python')
		st.markdown('* 修「電波天文學」時用來分析資料的軟體CASA需要用到Python')
		st.markdown('* 看到[Why Astronomers Should Program in Python](http://bellm.org/blog/2011/05/27/why-astronomers-should-program-in-python/)這篇文章')
		st.markdown('* 2015年暑假為了帶高能天文物理實驗室新生，編寫教材「[Python 基本語法與科學計算套件的使用](https://github.com/Astrohackers-TW/IANCUPythonAdventure/wiki/Python-%E5%9F%BA%E6%9C%AC%E8%AA%9E%E6%B3%95%E8%88%87%E7%A7%91%E5%AD%B8%E8%A8%88%E7%AE%97%E5%A5%97%E4%BB%B6%E7%9A%84%E4%BD%BF%E7%94%A8)」')
		st.markdown('* 2015年參與紐約天文黑客松[Astro Hack Week](http://astrohackweek.org/2020/)的小成就：[Python Wrapper for Hilbert–Huang Transform MATLAB Package](https://github.com/HHTpy/HHTpywrapper)')
		st.markdown('* 基於開放科學精神，企圖將博班研究工作整理成[QPOpytracker](https://github.com/YihaoSu/QPOpytracker)')

if topic == '可以用Python解決哪些問題？':
	st.header('可以用Python解決哪些問題？')
	st.subheader('從天文所網頁工讀生轉職為承接網站開發及資料科學相關案子的遠距工作者')
	st.markdown('* PTT SOHO板上的[徵才文](https://www.ptt.cc/bbs/soho/M.1417694394.A.7F7.html)')
	st.markdown('* [卡米爾公司](https://cameo.tw/tw/)')

	st.subheader('從遠距工作經驗分享可以用Python解決哪些問題')
	with st.expander('網頁資料擷取(網路爬蟲)'):
		st.markdown('* 台經院的[FINDIT](https://findit.org.tw/index.aspx)網站需要抓取國內外群眾募資網站資料來分析趨勢')
		st.markdown('* 相關Python套件： [requests](https://docs.python-requests.org/en/latest/)、[BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)、[Selenium](https://selenium-python.readthedocs.io/)、[Scrapy](https://scrapy.org/)')

	with st.expander('網站及API開發'):
		st.markdown('* 澎湖民宿[屋光拾舍Hygge](https://hygge.tw/)的網站')
		st.markdown('* 「[探索科博尋寶趣](https://cobofun.nmns.edu.tw/index.html)」app的內容上稿後台')
		st.markdown('* 文化資產災害示警系統')
		st.markdown('* 相關Python套件： [Django](https://www.djangoproject.com/)、[Django REST framework](https://www.django-rest-framework.org/)、[Flask](https://flask.palletsprojects.com/en/2.0.x/)、[FastAPI](https://fastapi.tiangolo.com/)')

	with st.expander('資料分析及視覺化'):
		st.markdown('* 分析IoT資料找出空氣、噪音、水質汙染事件')
		st.markdown('* 相關Python套件： [Pandas](https://pandas.pydata.org/)、[GeoPandas](https://geopandas.org/en/stable/)、[Plotly](https://plotly.com/python/)、[Streamlit](https://streamlit.io/)')

	with st.expander('更多應用'):
		st.markdown('* 自動寄發Email及Line通知、自動讀寫Google Sheets([gspread](https://docs.gspread.org/en/v5.7.0/))和Drive([PyDrive2](https://docs.iterative.ai/PyDrive2/))上的檔案資料、...')
		st.markdown('* 歡迎參加[台灣Python年會](https://tw.pycon.org/2022/zh-hant)')

if topic == '如何藉由Python與天文維持關係？':
	st.header('如何藉由Python與天文維持關係？')
	with st.expander('PyCon Taiwan 2017'):
		st.subheader('天文黑客們的Python大冒險')
		st.markdown('* [簡報](https://hackmd.io/@astrobackhacker/rJhGJeNzZ)')
		st.markdown('* 演講錄影：')
		st.video('https://www.youtube.com/watch?v=MX-cur3_ZgA')

	with st.expander('PyCon Taiwan 2018'):
		st.subheader('以Astroquery套件擷取線上天文觀測資料')
		st.markdown('* [簡報](https://hackmd.io/@astrobackhacker/B1pDk2iAf)')
		st.markdown('* 演講錄影：')
		st.video('https://www.youtube.com/watch?v=sPUVD4XWOvE')

	with st.expander('PyCon Taiwan 2019'):
		st.subheader('用Python拉近群眾與星空的距離：Astrohackers in Taiwan社群介紹')
		st.markdown('* [簡報](https://hackmd.io/@astrobackhacker/ByWuFL1DB)')
		st.markdown('* 演講錄影：')
		st.video('https://www.youtube.com/watch?v=SbcbHFpGtY0')

	with st.expander('PyCon Taiwan 2020'):
		st.subheader('重力波調查員：鄉民都來分析重力波觀測資料')
		st.markdown('* [簡報](https://hackmd.io/@astrobackhacker/rkZ4n-0MD)')
		st.markdown('* 演講錄影：')
		st.video('https://www.youtube.com/watch?v=i36y82mIQtA')

	with st.expander('PyCon Taiwan 2021'):
		st.subheader('搭上Streamlit特快車遊沐星光程式')
		st.markdown('* [簡報](https://hackmd.io/@astrobackhacker/r1sEG3eeF)')
		st.markdown('* 演講錄影：')
		st.video('https://www.youtube.com/watch?v=n0PdS7cehZM')

	with st.expander('PyCon APAC 2022'):
		st.subheader('鄉民如何用Python協作貢獻天文教育')
		st.markdown('* [簡報](https://hackmd.io/@astrobackhacker/BJ4XYe4jq)')
		st.markdown('* 演講錄影：')
		st.video('https://www.youtube.com/watch?v=2FGwasV6Nrg')

if topic == '揪團用Python拉近群眾與星空的距離':
	st.header('揪團用Python拉近群眾與星空的距離')
	st.subheader('[g0v零時小學校](https://sch001.g0v.tw/) 2021-22 Demo Day的提案：「[鄉民都來開拓公民天文學家的地圖[0]：從互動式開源教材開始](https://sch001.g0v.tw/dash/prj/2Sk_LR05YD05j20AmR02l9dxC)」')

	if st.button('加入我們'):
		_, col, _ = st.columns(3)
		with col:
			st.subheader('謝謝大家！')
			qr = qrcode.QRCode()
			qr.add_data(
				data='https://www.facebook.com/groups/1022708484514663'
			)
			qr_img = qr.make_image(fill='black', back_color='white')
			qr_img.save('./qrcode_python_group.png')
			st.subheader('「Python在天文領域的應用」FB社團')
			st.image('./qrcode_python_group.png')
