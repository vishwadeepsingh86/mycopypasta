#!C:\Strawberry\perl\bin\perl.exe -w
use CGI qw(:standard);
use CGI::Carp qw/fatalsToBrowser warningsToBrowser/;
use CGI::Cookie;
use DBI;

my $q = new CGI;
my $value = $q->cookie('MYCOPYPASTACOOKIE');
print $q->header;
my $err = 0;
my $login = 0;
if($value ne "" && $value eq "1") {
	$login = 1;
} else {
	my $url="login.cgi";
	my $t=0; # time until redirect activates
	print "<META HTTP-EQUIV=refresh CONTENT=\"$t;URL=$url\">\n";
}
print '<html lang="en-US">
	<head>
		<title>My Copy-Pasta</title>
		<link rel="shortcut icon" href="images/newlogo.ico">
		<link rel="stylesheet" type="text/css" href="css/style.css">
		<link rel="stylesheet" type="text/css" href="css/viewstyle.css">
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
					        print '<li><a href="logout.cgi">Logout</a></li>
					        <li><a href="profile.cgi">Profile</a></li>';
				        } else {
				        	print '<li><a href="login.cgi">Login</a></li>';
				        }
				      print '</ul>
				    </div>
				</td>
			</tr>
		</table>';
		
		print '<section class="adddata">
			<div class="loginbox">Add Copy-Pasta</div>
			<form action="adddone.cgi" method="post">
			Category: <select>';
			
		my $dsn = "DBI:mysql:database=mycopypasta;host=localhost";
		my $dbh = DBI->connect($dsn,"root","");
		my $sth = $dbh->prepare("SELECT distinct(category) FROM categoryinfo");
		$sth->execute();
		while (my $ref = $sth->fetchrow_hashref()) {
			if ($ref->{'category'} ne "") {
				print " <option value=\"$ref->{'category'}\">$ref->{'category'}</option>";
			}
		}	
		print '</select><br />
		    	<input type="text" required title="Topic" placeholder="Topic"><br />
		    	<textarea class="discussion"></textarea>
		    	<input type="text" required title="Sources" placeholder="Sources (add them comma separated)"><br />
		    	<input type="text" required title="Tags" placeholder="Tags (add them comma separated)"><br />
		    	Share: <select>
		    	<option value="public">public</option>
		    	<option value="private">private</option>
		    	</select>
		    	<input type="submit" class="submitbox" name="submit" alt="search" value="Submit your Copy-Pasta">
		    </form>
		</section>
	</body>
	<div style="text-align:center"><text style="color:grey;font-size:12px">�2015 Vishwadeep Singh My Copy-Pasta</text></div>
	<hr width="65%">
	<div style="text-align:center"><div class="fb-follow" data-href="https://www.facebook.com/vsdpsingh" data-width="250" data-height="250" data-layout="standard" data-show-faces="true"></div></div>
</html>';


1;