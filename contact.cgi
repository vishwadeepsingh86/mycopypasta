#!C:\Strawberry\perl\bin\perl.exe -w
use CGI qw(:standard);
use CGI::Carp qw/fatalsToBrowser warningsToBrowser/;
use CGI::Cookie;
use CGI::Session;
use DBI;
use HTML::Entities;

# new cgi query
my $q = new CGI;
# fetching cookie
my $ssid = $q->cookie('MYCOPYPASTACOOKIE');
# printing header
print $q->header;
# login error or not
my $err = 0;
# proper logged in?
my $login = 0;

if($ssid eq "") {
	# empty/no cookie found. Hence not logged in
} else {
	# cookie has some value, hence loading session from $ssid
	$session = CGI::Session->load($ssid) or die "$!";
	if($session->is_expired || $session->is_empty) {
		# if session is expired/empty, need to relogin
	} else {
		my $value = $session->param('logged_in_status_mycp');
		if ($value eq "1") {
			# properly logged in
			$login = 1;
		}
	}
}

print '<html lang="en-US">
	<head>
		<title>My Copy-Pasta</title>
		<link rel="shortcut icon" href="images/newlogo.ico">
		<link rel="stylesheet" type="text/css" href="css/style.css">
		<link rel="stylesheet" type="text/css" href="css/viewstyle.css">
		<link rel="stylesheet" type="text/css" href="css/paragraph.css">
		<link rel="stylesheet" type="text/css" href="css/registerpasta.css">
			<link rel="stylesheet" type="text/css" href="css/addpasta.css">
		<div id="fb-root"></div>
		<script>(function(d, s, id) {
			  var js, fjs = d.getElementsByTagName(s)[0];
			  if (d.getElementById(id)) return;
			  js = d.createElement(s); js.id = id;
			  js.src = "//connect.facebook.net/en_GB/sdk.js#xfbml=1&version=v2.4&appId=173510282674533";
			  fjs.parentNode.insertBefore(js, fjs);
			}(document, \'script\', \'facebook-jssdk\'));
		</script>
	</head>
	
	<body>
		<table class="box" align="center" width="65%">
			<tr>
				<td>
					<div style="text-align:center"><img src="images/banner.jpg" alt="Edit" style="width:100%;height:250px;"></div>
				</td>
			</tr>
			<tr>
				<td>
				    <div id="centeredmenu">
				      <ul>
				        <li><a href="index.cgi">Home</a></li>';
				        if ($login) {
					        print '<li><a href="addpasta.cgi">Add Copy-Pasta</a></li>';
				        }
				        print '<li><a href="view.cgi">My Copy-Pasta</a></li>
				        <li><a href="tutorial.cgi">Tutorials</a></li>
				        <li><a href="search.cgi">Search Copy-Pasta</a></li>
				        <li><a href="contact.cgi">Contact Us</a></li>';
				        if ($login) {
				        	my $getuser = $session->param('logged_in_userid_mycp');
					        print '<li><a href="logout.cgi">Logout</a></li>';
					        print "<li><a href=\"profile.cgi?id=$getuser\">Profile</a></li>";
				        } else {
				        	print '<li><a href="login.cgi">Login</a></li>';
				        }
				      print '</ul>
				    </div>
				</td>
			</tr>
		<tr><td>
		<!-- Facebook Badge START -->
		<a href="https://www.facebook.com/mycopypasta" title="My Copy-Pasta" style="font-family: &quot;lucida grande&quot;,tahoma,verdana,arial,sans-serif; font-size: 11px; font-variant: normal; font-style: normal; font-weight: normal; color: #3B5998; text-decoration: none;" target="_TOP">My Copy-Pasta</a>
		<br /><a href="https://www.facebook.com/mycopypasta" title="My Copy-Pasta" target="_TOP">
		<img class="img" src="https://badge.facebook.com/badge/1505964906363256.11050.193534457.png" style="border: 1px;" alt="" /></a><!-- Facebook Badge END -->
		</td>
		
		</tr>
		</table>';
		my $dsn = "DBI:mysql:database=mycopypasta;host=localhost";
		my $dbh = DBI->connect($dsn,"root","");
		$sth = $dbh->prepare("SELECT category,count FROM categoryinfo");
		$sth->execute();
		print "</table><section class=\"registerdata\">
						<div class=\"loginbox\">Total Category Inputs by all of you</div><form>";
		my %categoryinfo;
		while (my $ref = $sth->fetchrow_hashref()) {
			$categoryinfo{$ref->{'category'}} = $categoryinfo{$ref->{'category'}}+$ref->{'count'};
		}
		foreach $key (sort(keys %categoryinfo)) {
			my $string = "categoryview.cgi?showmycategory=$key";
			encode_entities($string);
	        print "<a href =\"$string\"><text class=\"fontdec\">$key</text></a>
    				&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
    			<input type=\"text\" style=\"width:60%\" value=\"$categoryinfo{$key}\" readonly><br /><br />";
	    }
	    print "</form>
			   </div>
		</div>
	    </section>";
	    
	    $sth = $dbh->prepare("SELECT tag,tagcount FROM taginfo");
		$sth->execute();		
		print "<section class=\"registerdata\">
						<div class=\"loginbox\">Total Tag Inputs by all of you</div><form>";
		my %taginfo;
		while (my $ref = $sth->fetchrow_hashref()) {
			$taginfo{$ref->{'tag'}} = $taginfo{$ref->{'tag'}}+$ref->{'tagcount'};
		}
		foreach $key (sort(keys %taginfo)) {
			my $string = "categoryview.cgi?showmycategory=$key";
			encode_entities($string);
	        print "<a href =\"$string\"><text class=\"fontdec\">$key</text></a>
    				&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
    			<input type=\"text\" style=\"width:60%\" value=\"$taginfo{$key}\" readonly><br /><br />";
	    }
	    print "</form>
			   </div>
		</div>
	    </section>";
		
	print '</body>
	<div style="text-align:center"><text style="color:grey;font-size:12px;font:status-bar">&copy;2015 <a href="mailto:myblueskylabs@gmail.com ?Subject=Reg:Hello" target="_top">My Blue Sky Labs (myblueskylabs@gmail.com)</a>, powered by Vishwadeep Singh</text></div>
	<hr width="65%">
	<div style="text-align:center"><div class="fb-follow" data-href="https://www.facebook.com/vsdpsingh" data-width="250" data-height="250" data-layout="standard" data-show-faces="true"></div></div>
</html>';


1;