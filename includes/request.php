<?php
header('Access-Control-Allow-Origin: *');

header('Access-Control-Allow-Methods: GET, POST');

header("Access-Control-Allow-Headers: X-Requested-With");

    $filename = $_GET['url'].'?'.$_GET['params'];

    $handle = fopen( $filename , 'r' );

    $contents = fread( $handle, 200000);

    fclose($handle);

    echo $contents;
