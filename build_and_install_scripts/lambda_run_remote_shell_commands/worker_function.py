import boto3
import paramiko
import datetime

def getDate():
	return datetime.datetime.today().now().strftime("%A, %d. %B %Y %I:%M%p")

def worker_handler(event, context):

    s3_Resource = boto3.resource('s3')
    s3_Resource.Bucket('bi-s3-key-bucket').download_file('aws-eb', '/tmp/aws-eb') 

    #Download private key file from secure S3 bucket
    #s3_client.download_file('bi-s3-key-bucket','aws-eb', '/tmp/aws-eb')

    k = paramiko.RSAKey.from_private_key_file("/tmp/aws-eb","")
    c = paramiko.SSHClient()
    c.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    #host=event['IP']
    host = "34.220.130.66"
    print("%s Connecting to %s" % (getDate(),host))
    c.connect( look_for_keys=False, hostname = host, password="", username = "ubuntu", pkey = k )
    print("%s Connected to %s" % (getDate(),host))

    commands = [
        "ls; pwd; whoami; cd automation; pwd; ls; nodejs headless_chrome_webdriverio_example.js"
        ]

    	
    standardOut="%s ============== Starting Standard Out LOG ================\n" % getDate()
    standardOut += "%s Starting script remotely...\n" % getDate()
    standardErr="%s ============== Starting ERROR LOG ================\n" % getDate()
    for command in commands:
        standardOut += (("%s EXECUTING: {}\n" % getDate()).format(command))
        stdin , stdout, stderr = c.exec_command(command)
        standardOut += "%s %s" % (getDate(), stdout.read())
	standardErr += "%s %s" % (getDate(), stderr.read())
    standardOut += "============== END OF STANDARD OUT LOG ================\n\n\n\n"
    standardErr += "============== END OF ERROR LOG ================\n\n\n"

    keyToUse='logs/automation-%s-1234-event-COMPLETED-PASS' % str(hash(datetime.datetime.now()))

    s3_Resource.Bucket('bji-s3-bucket').put_object(Key=keyToUse,Body=standardOut + standardErr + "End of log.")

    return
    {
        'message' : "Script execution completed. See Cloudwatch logs for complete output"
    }
