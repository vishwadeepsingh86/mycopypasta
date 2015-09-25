#!C:\Strawberry\perl\bin\perl.exe -w
use CGI qw(:standard);
use CGI::Carp qw/fatalsToBrowser warningsToBrowser/;
use CGI::Cookie;

my $q = new CGI;
my $value = $q->cookie('MYCOPYPASTACOOKIE');
print $q->header;
my $err = 0;
my $login = 0;
if($value ne "" && $value eq "1") {
	$login = 1;
}

print '<html lang="en-US">
	<head>
		<title>My Copy-Pasta</title>
		<link rel="shortcut icon" href="images/newlogo.ico">
		<link rel="stylesheet" type="text/css" href="css/style.css">
		<link rel="stylesheet" type="text/css" href="css/viewstyle.css">
		<link rel="stylesheet" type="text/css" href="css/paragraph.css">
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
			<tr>
				<td>
					<img src="images/profile.jpg" alt="Edit" style="width:100%;height:300px;">
				</td>
			</tr>
			<tr>
				<td>
				<p>My Copy-Pasta.
					This creation is inspired by several thoughts. We come across with different information daily, but, we dont keep track of it. As you cannot trust on human mind for storing the information for longer time. As i had seen lot of branches of science and dealing with different set every time, which makes me learn new things daily. But, slowly i started
					forgetting these things and i started loosing track of them. Hence, i thought of building a platform, where you can save anything you want and keep it for future purpose.
				</p>
				</td>
			</tr>
		</table>
	</body>
	<div style="text-align:center"><text style="color:grey;font-size:12px">�2015 Vishwadeep Singh My Copy-Pasta</text></div>
	<hr width="65%">
	<div style="text-align:center"><div class="fb-follow" data-href="https://www.facebook.com/vsdpsingh" data-width="250" data-height="250" data-layout="standard" data-show-faces="true"></div></div>
</html>';


1;