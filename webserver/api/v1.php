<?php
$active = file_get_contents('active.txt');
if ($active == 1){
  http_response_code(201);
  file_put_contents("active.txt", 0);
  exit;
}else{
  http_response_code(200);
  exit;
}
