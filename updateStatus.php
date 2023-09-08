<?php
function update($code) {

    $url = 'http://10.54.128.96:8888/projetworkshop/update.php?code='.$code;
    echo $url;
    
    
    
    get_headers($url);
    
    /*
    $ch = curl_init($url);

    $response = curl_exec($ch);

    if ($response === false) {
        echo "Erreur cURL : " . curl_error($ch);
    } else {
        echo $response;
    }
    curl_close($ch);*/
}
?>
