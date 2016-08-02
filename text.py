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

    <div class = "container-fluid">

        <h1>Column Layout</h1>
        <div class="row">
           <div class="col-md-4" style="background-color: #FF9999">Left</div>
           <div class="col-md-4" style="background-color: #99CCFF">Middle</div>
           <div class="col-md-4" style="background-color: #00CC99">Right</div>
        </div>
        <p>You can highlight with <mark>mark tags</mark></p>

        <blockquote>
            <p>The road is anywhere you want, except the freezer.</p>
            <footer>Nobody</footer>
        </blockquote>

        <h4>List of Stuff</h4>
        <dl>
            <dt>Inside</dt>
                <dd>computer</dd>
                <dd>television</dd>
            <dt>Outside</dt>
                <dd>Go back inside</dd>
        </dl>

        <p>To set the users weight use <code>setUserWeight(374):</code> with an integer</p>

        <p>For multi-line code use the pre tags</p>
        <pre>
            for n in range(101):
                if(n % 4 is 0):
                    print(n)
        </pre>

        <p>This is supposed to be keyboard input.<kbd>CTRL + ALT + DEL</kbd></p>

        <h4>Built in color classes</h4>
        <p class="text-muted">Grey Text</p>
        <p class="text-success">Green Text</p>
        <p class="text-danger">Red Text</p>

        <p class="bg-muted">Grey Background</p>
        <p class="bg-success">Green Background</p>
        <p class="bg-danger">Red Background</p>

    </div>

</body>
</html>
