apt-get update
apt-get install -y unzip xvfb libxi6 libgconf-2-4
apt-get install default-jdk

curl -sS -o - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add
echo "deb [arch=amd64]  http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list


apt-get -y update
apt-get -y install google-chrome-stable

wget https://chromedriver.storage.googleapis.com/2.41/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
mv chromedriver /usr/bin/chromedriver
chown root:root /usr/bin/chromedriver
chmod +x /usr/bin/chromedriver

wget https://selenium-release.storage.googleapis.com/3.13/selenium-server-standalone-3.13.0.jar

#xvfb-run java -Dwebdriver.chrome.driver=/usr/bin/chromedriver -jar selenium-server-standalone-3.13.0.jar
#java -Dwebdriver.chrome.driver=/usr/bin/chromedriver -jar selenium-server-standalone-3.13.0.jar &

runuser -l ubuntu -c 'java -Dwebdriver.chrome.driver=/usr/bin/chromedriver -jar selenium-server-standalone-3.13.0.jar &'


mkdir automation
cd automation
apt install npm
npm init
npm install webdriverio

cp ../QA_Scripts/js/webdriverio-learning/headless_chrome_webdriverio_example.js .

runuser -l ubuntu -c 'cd automation; nodejs headless_chrome_webdriverio_example.js'
