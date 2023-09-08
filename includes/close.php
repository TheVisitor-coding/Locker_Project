<?php
include ("../updateStatus.php");

header('Access-Control-Allow-Origin: *');

header('Access-Control-Allow-Methods: GET, POST');

header("Access-Control-Allow-Headers: X-Requested-With");

$pin = $_GET['pin'];
$code = $_GET['code'];

$pythonScript = 'python3 /var/www/html/locker/MDSlocker/close.py '.$pin;
$output = shell_exec("$pythonScript");
update($code);


?>
