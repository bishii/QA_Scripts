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
sudo chown ubuntu automation/
cd automation

sudo apt install git
sudo mkdir git
cd git
git clone https://github.com/bishii/QA_Scripts.git

apt install npm
npm init
npm install webdriverio

sudo ln -s /usr/bin/nodejs /usr/bin/node
export PATH=$PATH:/home/ubuntu/automation/node_modules/.bin/

sudo npm install wdio-mochawesome-reporter
sudo npm install wdio-mocha-framework
sudo npm install mochawesome-report-generator
sudo apt install awscli
sudo apt install zip

###TODO: Figure out how to set the .aws/credentials (username and pwd)

cp git/QA_Scripts/js/webdriverio-learning/parentScript.js automation/
cp git/QA_Scripts/js/webdriverio-learning/wdio.conf.js automation/

#cp ../QA_Scripts/js/webdriverio-learning/headless_chrome_webdriverio_example.js .
#runuser -l ubuntu -c 'cd automation; nodejs headless_chrome_webdriverio_example.js'
