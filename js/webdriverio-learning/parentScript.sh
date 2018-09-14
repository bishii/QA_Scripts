export PATH=$PATH:`pwd`/node_modules/.bin
wdio wdio.conf.js
theResult=$?
echo Result of script was: $theResult
marge myfile.json
zip -r html_results.zip mochawesome-report
idnum=`shuf -i 1-100000 -n 1`
echo $idnum
aws s3 cp html_results.zip s3://bji-s3-bucket/public/$idnum-html_results_1.zip
