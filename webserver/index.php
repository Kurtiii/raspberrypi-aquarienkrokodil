<?php
$last_activated = file_get_contents('api/last_activated.txt');
$active = file_get_contents('api/active.txt');
$time = time();

$timestamp = $time - $last_activated;

if ($timestamp < 2400){
  header('Location: sleep');
  exit;
}

file_put_contents("api/last_activated.txt", $time);
file_put_contents("api/active.txt", 1);

header('Location: success')

?>
