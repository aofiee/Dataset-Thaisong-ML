<?php
header('Content-Type: text/html; charset=utf-8');
$dom = new DOMDocument();
libxml_use_internal_errors(true);
$dom->loadHTMLFile('http://www.lyric.in.th/listsong.php?cs=9');
$data = $dom->getElementsByTagName("li");
$fullUrl = 'http://www.lyric.in.th/';
$dataset = array();
$fp = fopen('songdb.csv', 'a');
foreach($data as $li ) {
    foreach($li->childNodes as $nodename){
        if($nodename->nodeName == 'a'){
            $url = trim($nodename->getAttribute('href'));
            $title = utf8_decode(trim($nodename->nodeValue));

            $loadLyric = new DOMDocument();
            $loadLyric->loadHTMLFile($fullUrl.$url);
            $dataLyric = $loadLyric->getElementsByTagName("p");
            foreach($dataLyric as $tmp){
                $lyric = strip_tags($tmp->textContent);
                $lyric = preg_replace("/[\n\r]/","",$lyric);
                $lyric = str_replace(",","",$lyric);
                $lyric = preg_replace("/[\t]/","",$lyric);
                $lyric = utf8_decode(trim($lyric));
                echo $lyric;
                // $dataset[] = array(
                //     'name' => $title,
                //     'lyric' => $lyric
                // );
                fwrite($fp,$title.','.$lyric."\r\n");
                // exit;
            }
            
        }
    }
}
fclose($fp);
?>