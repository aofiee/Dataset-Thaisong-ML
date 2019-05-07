<?php
  $fn = fopen("songdb-clean-name.csv","r");
  
  while(! feof($fn))  {
	$result = fgets($fn);
    $ar = array();
    $ar = explode(",",$result);
    if(count($ar) == 2){
        $lyric = str_replace("'","\'",$ar[1]);
        list($song_name,$artist) = explode("-",$ar[0]);
        $song_name = trim($song_name);
        $artist = trim($artist);
        $lyric = str_replace("เพลง : ".$song_name,"",$lyric);
        $lyric = str_replace("ศิลปิน : ".$artist,"",$lyric);
        $lyric = str_replace("อัลบั้ม : ".$artist,"",$lyric);
        $lyric = str_replace("อัลบั้ม : ".$song_name,"",$lyric);
        $lyric = str_replace("**","",$lyric);
        $lyric = str_replace("*","",$lyric);
        $lyric = str_replace("(","",$lyric);
        $lyric = str_replace(")","",$lyric);
        $lyric = str_replace("."," ",$lyric);
        // echo $song_name.",".$artist.",".$lyric;
        // echo "\r\n--------------------\r\n";
        $fp = fopen('songdb-clean-name2.csv', 'a');
        fwrite($fp,$song_name.",".$artist.",".$lyric);
        fclose($fp);
    }
  }

  fclose($fn);
?>