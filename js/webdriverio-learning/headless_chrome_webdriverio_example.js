var webdriverio = require('webdriverio');
var options = {
    desiredCapabilities: {
        browserName: 'chrome',
        chromeOptions: {
        args: ['--headless', '--disable-gpu', '--window-size=1280,800']//,
                //binary: '/usr/bin/chromedriver'
        }
    }
}

webdriverio
    .remote(options)
    .init()
    .url('http://brentishiidigital.us-west-2.elasticbeanstalk.com/test/test_1')
    .element("HUMANS").getText("NAME" ).then(function(theObj) {
        console.log(theObj)
        })
    .end()
    .catch(function(err) {
        console.log(err);
    });
