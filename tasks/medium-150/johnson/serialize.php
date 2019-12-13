<?php
  class Foo {
    private $path = "flag.txt";
   
    function show_data() {
      return file_get_contents($this->path);
    }
  } 

  $a = new Foo();
  echo base64_encode(serialize($a));
?>