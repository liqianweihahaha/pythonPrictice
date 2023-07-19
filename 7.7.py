# from fpdf import FPDF
#
# Pdf = FPDF()
#
#
# list_of_images = ["2.jpg","3.png","4.jpg"]
#
# for i in list_of_images:
#     Pdf.add_page()
#     Pdf.image(i,x=100,y=100,w=200,h=200)
#     Pdf.output("result.pdf","F")


import speedtest as st

# Set Best Server
server = st.Speedtest()
server.get_best_server()

# Test Download Speed
down = server.download()
down = down / 1000000
print(f"Download Speed: {down} Mb/s")

# Test Upload Speed
up = server.upload()
up = up / 1000000
print(f"Upload Speed: {up} Mb/s")

# Test Ping
ping = server.results.ping
print(f"Ping Speed: {ping}")