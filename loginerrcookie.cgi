#!C:\Strawberry\perl\bin\perl.exe

use DBI;
use CGI;
use CGI::Carp qw/fatalsToBrowser warningsToBrowser/;
use CGI::Cookie;
use CGI::Session;

# new cgi query
my $q = new CGI;
# fetching cookie
my $ssid = $q->cookie('MYCOPYPASTACOOKIE');
$session = CGI::Session->load($ssid) or die "$!";
$session->delete();
$session->flush();
# SETTING LOGIN COOKIES
$cookie1 = CGI::Cookie->new(-name=>'MYCOPYPASTACOOKIE',-value=>'0');
print $q->header(-cookie=>[$cookie1]);
my $url="login.cgi";
my $t=0; # time until redirect activates
print "<META HTTP-EQUIV=refresh CONTENT=\"$t;URL=$url\">\n";
1;