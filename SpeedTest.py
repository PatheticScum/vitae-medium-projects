# pip install speedtest-cli

# import Speedtest()

st = Speedtest()
download = st.download()
upload = st.upload()
st.get_servers([])
ping = st.results.ping
