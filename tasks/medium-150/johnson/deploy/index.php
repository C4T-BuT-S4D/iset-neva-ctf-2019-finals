<?php
  error_reporting(E_ERROR | E_PARSE);
  class Foo {
    private $path = "info.txt";
   
    function show_data() {
      return file_get_contents($this->path);
    }
  } 

  $a = new Foo();
  setcookie("some_secret_data", base64_encode(serialize($a)));
?>

<html>
<body>
  <h1> Hello and welcome to our unique website! </h1>
  <h3> It was made to show you example of working in php with files </h3>
</body>
</html>

<?php
  $b = unserialize(base64_decode($_COOKIE["some_secret_data"]));
  $data = $b->show_data();
  $length = strlen($data);
  if ($length > 50)
    $length = 50;
  for ($i = 0; $i < $length; $i++)
    echo $data[$i];
?>