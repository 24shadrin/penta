#!/usr/bin/perl

    local ($buffer, @pairs, $pair, $name, $value, %FORM);
    # Read in text
    $ENV{'REQUEST_METHOD'} =~ tr/a-z/A-Z/;
    if ($ENV{'REQUEST_METHOD'} eq "POST")
    {
        read(STDIN, $buffer, $ENV{'CONTENT_LENGTH'});
    }else {
    $buffer = $ENV{'QUERY_STRING'};
    }
    # Split information into name/value pairs
    @pairs = split(/&/, $buffer);
    foreach $pair (@pairs)
    {
    ($name, $value) = split(/=/, $pair);
    $value =~ tr/+/ /;
    $value =~ s/%(..)/pack("C", hex($1))/eg;
    $FORM{$name} = $value;
    }
    $subject = $FORM{dropdown};

#print "Content-type:text/html\r\n\r\n";
#print "<html>";
#print "<head>";
#print "<title>Dropdown Box - Sixth CGI Program</title>";
#print "</head>";
#print "<body>";
#print "<h2> Selected Subject is $subject</h2>";
#print "</body>";
#print "</html>";

require "sfile";
    print "Content-Type: text/html\n\n";
    print "<html>";

    print "<body>";
    print "\n";


$truedat=$sfile::fullpath;

$p="/home/pi/beward/penta/$truedat/beward_penta/1";

$url="index.html";

system "cd /var/www/web/jpg && rm /var/www/web/jpg/*";

$path="jpg";

system "cd $p && ls  $p |grep jpg |tail -n $subject |xargs cp  --target-directory=/var/www/web/jpg";

system "ls  /var/www/web/jpg > /var/www/web/list";

print "<p><a href=$url> <-back</a></p>";

open(filo, "list") || die "file daz not eksist";
while ($line = <filo>)
{
#print "<img src=$path/$line width=20% align=right>";
print "<img src=$path/$line width=20%>";

#print $line;
}
close(filo);

print "\n";

print "<br>";
"\n";

print "<p><a href=$url> <-back</a></p>";

    print "</body>";
    print "</html>";
print "\n";

1;
