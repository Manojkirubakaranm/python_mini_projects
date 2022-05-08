import speedtest
speed=speedtest.Speedtest()
download_speed=speed.download()
upload_speed=speed.upload()
download_speed=float(download_speed*10**-6)
upload_speed=float(upload_speed*10**-6)
print(f'dwn speed is{download_speed}')
print(f'UP speed is{upload_speed}')

