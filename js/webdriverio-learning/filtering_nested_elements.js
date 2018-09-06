var webdriverio = require('webdriverio');
var assert = require('assert')
var options = {
    desiredCapabilities: {
        browserName: 'firefox'
    }
};

webdriverio
    .remote(options)
    .init()
    .url('http://eb-new-two.us-west-2.elasticbeanstalk.com/test/test_1')
    .element("HUMANS").getText("NAME" ).then(function(theObj) {
	assert.equal(theObj.length, 3)
	console.log("Verified:")
	console.log(theObj)
	})
    .element("ALIENS").getText("NAME[nickname='green blooded computer'").then(function(theObj) {
	assert.equal(theObj, "Mr. Spock")
	console.log("Verified:")
	console.log(theObj)
	})
    .end()
    .catch(function(err) {
        console.log(err);
    });
