<?php

header('Access-Control-Allow-Origin: *');

header('Access-Control-Allow-Methods: GET, POST');

header("Access-Control-Allow-Headers: X-Requested-With");
error_reporting(E_ALL);
ini_set("display_errors", 1);


include ("../updateStatus.php");

$pin = $_GET['pin'];
#$statut = $_GET['statut'];
$code = $_GET['code'];

$pythonScript = 'python3 /var/www/html/locker/MDSlocker/index.py '.$pin.' '.$code;
#$ledScript = 'python3 /var/www/html/locker/MDSlocker/led.py';


#$commandLed = escapeshellcmd("$ledScript");
//$command = escapeshellcmd("$pythonScript $pin $code");

#$outputLed = shell_exec($commandLed);
$output = shell_exec("$pythonScript");

#echo $outputLed;
//echo $output;

update($code);


?> 
 
