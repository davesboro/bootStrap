<!DOCTYPE html>
<html lang="en">
<head>
    <title>companies</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/css/bootstrap.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
    <script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/js/bootstrap.min.js"></script>
</head>
<body>

    <nav class="navbar navbar-inverse">
        <div class="container-fluid">

            <!-- LOGO -->
            <div class="navbar-header">
                <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#mainNavBar">
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                </button>
                <a href="#" class="navbar-brand">COMPANIES</a>
            </div>

            <!-- MENU ITEMS -->
            <div class="collapse navbar-collapse" id="mainNavBar">
                <ul class="nav navbar-nav">
                    <li class="active"><a href="#">None</a> </li>
                    <li><a href="#">About</a> </li>
                    <li><a href="#">Contact</a> </li>

                    <!-- DROP DOWN MENU -->
                    <li class="dropdown">
                        <a href="#" class="dropdown-toggle" data-toggle="dropdown">My Profile <span class="caret"></span></a>
                        <ul class="dropdown-menu">
                            <li><a href="#">Friends</a> </li>
                            <li><a href="#">Photos</a> </li>
                            <li><a href="#">Settings</a> </li>
                        </ul>
                    </li>
                </ul>

                <!--RIGHT ALIGN-->
                <ul class="nav navbar-nav navbar-right">
                    <li><a href="#">Logout</a> </li>
                </ul>

            </div>

        </div>
    </nav>

    <!--Main Content-->
    <div class="container">

        <h2>Wells sections with borders and gray backgrounds.</h2>

        <div class="well">Basic Well</div>
        <div class="well well-sm">Basic Well</div>

        <div class="alert alert-success">You are successful!</div>

        <div class="alert alert-info"
            <a href="#" class="close" data-dismiss="alert" aria-label="close">&times;</a>Info makes it blue.
        </div>

        <div class="alert alert-danger fade in"
            <a href="#" class="close" data-dismiss="alert" aria-label="close">&times;</a>Danger makes it red.
        </div>


    </div>

</body>
</html>
