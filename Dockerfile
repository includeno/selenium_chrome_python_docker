FROM python:3.9.4

WORKDIR /app
#Ubuntu系统
RUN /bin/sh -c 'apt-get update  && apt-get upgrade -y  && apt-get install wget -y && apt-get install git -y &&apt-get install unzip  -y  && apt-get install fonts-liberation  -y  && apt-get install libasound2  -y  && apt-get install libatk-bridge2.0-0  -y  && apt-get install libatk1.0-0  -y  && apt-get install libatspi2.0-0  -y  && apt-get install libcairo2  -y && apt-get install libcups2  -y && apt-get install libdbus-1-3  -y && apt-get install libdrm2  -y && apt-get install libgbm1  -y && apt-get install libgdk-pixbuf2.0-0  -y && apt-get install libglib2.0-0  -y && apt-get install libgtk-3-0  -y && apt-get install libnspr4  -y && apt-get install libnss3  -y && apt-get install libpango-1.0-0  -y && apt-get install libxcomposite1  -y && apt-get install libxdamage1  -y && apt-get install libxfixes3  -y && apt-get install libxkbcommon0  -y && apt-get install libxshmfence1  -y && apt-get install xdg-utils  -y  '

#下载安装chrome驱动 位置/
RUN /bin/sh -c 'mkdir /tools &&wget http://npm.taobao.org/mirrors/chromedriver/89.0.4389.23/chromedriver_linux64.zip &&unzip -d /tools chromedriver_linux64.zip'
#chrome_linux64_stable_89.0.4389.90

#https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
#下载安装chrome https://blog.csdn.net/weixin_42170439/article/details/100927676
RUN /bin/sh -c 'cd /tools && wget -P /tools https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && dpkg -i chrome.deb'

