<!DOCTYPE html>
<html lang="en">
<head>
    <title>thenewboston</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/css/bootstrap.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
    <script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/js/bootstrap.min.js"></script>
    <link rel="stylesheet" href="sidebar.css">
</head>
<body>

    <div id="wrapper">

        <!--SIDEBAR-->
        <div id="sidebar-wrapper">
            <ul class="sidebar-nav">
                <li><a href="#">Account</a></li>
                <li><a href="#">Settings</a></li>
                <li><a href="#">Logout</a></li>
            </ul>
        </div>

        <!--MAIN CONTENT-->
        <div id="page-content-wrapper">
            <div class="container-fluid">
                <div class="row">
                    <div class="col-lg-12">
                        <a href="#" class="btn btn-success" id="menu-toggle">Toggle Menu</a>
                        <h1>Sidebar Layouts</h1>
                        <p>I love to eat good food.
                        I like to eat healthy food.</p>
                    </div>
                </div>
            </div>
        </div>

    </div>

    <!--Menu Toggle Script-->
    <script>
        $("#menu-toggle").click( function (e){
            e.preventDefault();
            $("#wrapper").toggleClass("toggled");
        });
    </script>

</body>
</html>
