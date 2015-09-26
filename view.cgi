#!C:\Strawberry\perl\bin\perl.exe -w
use CGI qw(:standard);
use CGI::Carp qw/fatalsToBrowser warningsToBrowser/;
use CGI::Cookie;
use CGI::Session;

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
		</table>
				<table class="box" align="center" width="65%">
			<tr>
				<td>
					<p class="one">
						<img src="images/note.jpg" alt="Note View" style="width:20px;height:20px;">
						<a href="view.html" class="heading_link"><text class="headings">452152. How to add image in html?</text></a><a class="edit_button" href="view.html">
						<img src="images/edit.jpg" alt="Edit" style="width:10px;height:10px;padding-right:3px">Edit</a>
						<br>
						<text class="date">13 May 2011 at 11:04 by <a href="profile.html" class="heading_link">Vishwadeep Singh</a> (Shared: Private)</text>
						<br>
						<a class="category_button" href="view.html">Category: HTML Programming (2,147 related topics found)</a>
						<br>
						<br>
							<textarea readonly class="discussion">In HTML, images are defined with the <img> tag.<br>
								The <img> tag is empty, it contains attributes only, and does not have a closing tag.<br>
								The src attribute specifies the URL (web address) of the image<br>
							</textarea>
						<br>
						<text class="information">
							Sources:
						</text>
						<a class="source_button" href="http://www.w3schools.com/tags/att_body_background.asp">http://www.w3schools.com/tags/att_body_background.asp</a>
						<a class="source_button" href="http://www.w3schools.com/tags/att_body_background.asp">http://www.w3schools.com/tags/att_body_background.asp</a>
						<br>
						<text class="information">
							Tags:
						</text>
							<a class="tag_button">#HTML</a>
							<a class="tag_button">#Programming</a>
						<br>
					</p>
				</td>
			</tr>
			<tr>
				<td>
					<p class="two">
						<img src="images/note.jpg" alt="Note View" style="width:20px;height:20px;">
						<a href="view.html" class="heading_link"><text class="headings">452152. How to add image in html?</text></a><a class="edit_button" href="view.html">
						<img src="images/edit.jpg" alt="Edit" style="width:10px;height:10px;padding-right:3px">Edit</a>
						<br>
						<text class="date">13 May 2011 at 11:04 by <a href="profile.html" class="heading_link">Vishwadeep Singh</a> (Shared: Private)</text>
						<br>
						<a class="category_button" href="view.html">Category: HTML Programming (2,147 related topics found)</a>
						<br>
						<br>
							<textarea readonly class="discussion">In HTML, images are defined with the <img> tag.<br>
								The <img> tag is empty, it contains attributes only, and does not have a closing tag.<br>
								The src attribute specifies the URL (web address) of the image<br>
							</textarea>
						<br>
						<text class="information">
							Sources:
						</text>
						<a class="source_button" href="http://www.w3schools.com/tags/att_body_background.asp">http://www.w3schools.com/tags/att_body_background.asp</a>
						<a class="source_button" href="http://www.w3schools.com/tags/att_body_background.asp">http://www.w3schools.com/tags/att_body_background.asp</a>
						<br>
						<text class="information">
							Tags:
						</text>
							<a class="tag_button">#HTML</a>
							<a class="tag_button">#Programming</a>
						<br>
					</p>
				</td>
			</tr>
			<tr>
				<td>
					<p class="one">
						<img src="images/note.jpg" alt="Note View" style="width:20px;height:20px;">
						<a href="view.html" class="heading_link"><text class="headings">452152. How to add image in html?</text></a><a class="edit_button" href="view.html">
						<img src="images/edit.jpg" alt="Edit" style="width:10px;height:10px;padding-right:3px">Edit</a>
						<br>
						<text class="date">13 May 2011 at 11:04 by <a href="profile.html" class="heading_link">Vishwadeep Singh</a> (Shared: Private)</text>
						<br>
						<a class="category_button" href="view.html">Category: HTML Programming (2,147 related topics found)</a>
						<br>
						<br>
							<textarea readonly class="discussion">In HTML, images are defined with the <img> tag.<br>
								The <img> tag is empty, it contains attributes only, and does not have a closing tag.<br>
								The src attribute specifies the URL (web address) of the image<br>
							</textarea>
						<br>
						<text class="information">
							Sources:
						</text>
						<a class="source_button" href="http://www.w3schools.com/tags/att_body_background.asp">http://www.w3schools.com/tags/att_body_background.asp</a>
						<a class="source_button" href="http://www.w3schools.com/tags/att_body_background.asp">http://www.w3schools.com/tags/att_body_background.asp</a>
						<br>
						<text class="information">
							Tags:
						</text>
							<a class="tag_button">#HTML</a>
							<a class="tag_button">#Programming</a>
						<br>
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