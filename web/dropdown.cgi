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

#$subject = 5;

require "sfile";
    print "Content-Type: text/html\n\n";
    print "<html>";

    print "<body>";
    print "\n";


$truedat=$sfile::fullpath;


$url="index.html";

use File::Copy;

require "sfile";
$truedat=$sfile::fullpath;
$d_path="/var/www/web/jpg";

$p="/home/pi/beward/penta/$truedat/beward_penta/1/*.jpg";
#записываем список файлов источника в массив
@flist = glob $p;


#обнуление счетчика. вычисляем количество элементов в массиве
$i=0;
$x=$#flist+1;
    if ($subject == 0) {
    $j=0;
}
else
{
$j=$x-$subject;
}

print "<p><a href=$url> <--back</a></p>";
print "\n";
    while ($j<$x) {
@mas=split("/",@flist[$j]);
$str=@mas[8];
copy ("@flist[$j]","$d_path/$str" || die "Error $!");
$j++;
print "<img src=jpg/$str width=20%>";
}

    print "<p><a href=$url> <--back</a></p>";
    print "\n";
