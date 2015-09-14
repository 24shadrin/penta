#!/usr/bin/perl

#$url="url=http://192.168.1.200/web/cur/";
$file="/web/cur/current.jpg";
$url="index.html";

 print "Content-Type: text/html\n\n";
    print "<html>";

    print "<body>";
    print "\n";


system "avconv -y -i 'rtsp://192.168.1.70' -r 10 -f image2 -vframes 1 /var/www/web/cur/current.jpg";


#print "<meta http-equiv='refresh' content=1;$url>";

print "<img src=$file>";


print "<p><a href=$url> <--back</a></p>";

    print "</body>";
    print "</html>";
print "\n";