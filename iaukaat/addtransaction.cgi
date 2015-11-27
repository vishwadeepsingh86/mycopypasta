#!C:\Strawberry\perl\bin\perl.exe -w
use CGI qw(:standard);
use CGI::Carp qw/fatalsToBrowser warningsToBrowser/;
use CGI::Cookie;
use CGI::Session;
use DBI;

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
		<title>iAukaat</title>
			<link rel="shortcut icon" href="images/newlogo.ico">
			<link rel="stylesheet" type="text/css" href="css/style.css">
			<link rel="stylesheet" type="text/css" href="css/viewstyle.css">
			<link rel="stylesheet" type="text/css" href="css/paragraph.css">
			<link rel="stylesheet" type="text/css" href="css/registerpasta.css">
		<div id="fb-root"></div>
		<script>(function(d, s, id) {
			  var js, fjs = d.getElementsByTagName(s)[0];
			  if (d.getElementById(id)) return;
			  js = d.createElement(s); js.id = id;
			  js.src = "//connect.facebook.net/en_GB/sdk.js#xfbml=1&version=v2.4&appId=173510282674533";
			  fjs.parentNode.insertBefore(js, fjs);
			}(document, \'script\', \'facebook-jssdk\'));
		</script>
		<script type="text/javascript">
			function changetextbox()
			{
			    document.getElementById("new_category").disabled=\'\';
				if (document.getElementById("selectcategory").value != "Create New Category") {
				    document.getElementById("new_category").disabled=\'true\';
				} else {
				    document.getElementById("new_category").disabled=\'\';
				}
			}
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
					        print '<li><a href="addtransaction.cgi">Add Transaction</a></li>';
				        }
				        print '<li><a href="view.cgi">iAukaat</a></li>
				        <li><a href="tutorial.cgi">Tutorials</a></li>
				        <li><a href="search.cgi">Search Transaction</a></li>
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
		</table>';
			print '<section class="registerdata">
				<div class="loginbox">Add transaction in iAukaat</div>
				<form action="addtransactionme.cgi" onsubmit="return myFunction()" METHOD="post" ENCTYPE="multipart/form-data">
					<table>
					<tr><td><text class="fontdec">Amount</text></td>
			    		<td><input type="text" title="amount" placeholder="only digits allowed" style="width:100%" name="amount" maxlength="64" required></td></tr>
					<tr><td><text class="fontdec">Transaction Type</text></td>
			    		<td><input type="text" title="ttype" placeholder="minimum 6 characters" style="width:100%" name="ttype" id="ttype" maxlength="64" required></td></tr>
			    	<tr><td><text class="fontdec">Account</text></td>
			    		<td><input type="text" title="account" placeholder="your name" style="width:100%" name="name" id="account" maxlength="256" required></td></tr>
			    	<tr><td><text class="fontdec">Category</text></td>
						<td><select id="selectcategory" name="selectcategory" onChange="changetextbox();"><option selected value="Create New Category">Create New Category</option>';
				
					my $dsn = "DBI:mysql:database=mycopypasta;host=localhost";
					my $dbh = DBI->connect($dsn,"root","");
					my $sth = $dbh->prepare("SELECT distinct(category) FROM categoryinfo");
					$sth->execute();
					while (my $ref = $sth->fetchrow_hashref()) {
						if ($ref->{'category'} ne "") {
							print " <option value=\"$ref->{'category'}\">$ref->{'category'}</option>";
						}
					}
					print '</select><input required type="text" title="New_Category" placeholder="New Category (max 128 characters)" id="new_category" name="new_category" maxlength="128"/></td></tr>
					<tr><td><text class="fontdec">Tags</text></td>
			    		<td><input type="text" title="tags" placeholder="tags" style="width:100%" name="identitylock" id="tags" maxlength="512" placeholder="maximum 64 characters, no special characters" required></td></tr>
					</table><br />
			    	<input type="submit" class="submitbox" name="submit" alt="search" value="Register">
			    </form>
			</section>';
	print '</body>
	<div style="text-align:center"><text style="color:grey;font-size:12px;font:status-bar">&copy;2015 <a href="mailto:myblueskylabs@gmail.com ?Subject=Reg:Hello" target="_top">My Blue Sky Labs (myblueskylabs@gmail.com)</a>, powered by Vishwadeep Singh</text></div>
	<hr width="65%">
	<div style="text-align:center"><div class="fb-follow" data-href="https://www.facebook.com/vsdpsingh" data-width="250" data-height="250" data-layout="standard" data-show-faces="true"></div></div>
</html>';


1;