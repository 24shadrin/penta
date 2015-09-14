#!/usr/bin/perl
#use strict;

@flist = glob "fortm/*.jpg";
$$j=@flist[0];
$i=$#flist;
$j=@flist[$i];


print $j;
#print $i;

print "\n";