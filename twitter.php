<?php




$busqueda = $_POST['busqueda'];



$conteo = $_POST['cantidad'];

$analisis = $_POST['recorrido'];

//echo $analisis; die();

$mysqli = new mysqli("localhost", "woobsing_twitter", "julimba1$", "woobsing_tweetAnalize");
$mysqli->set_charset("utf8mb4");

$consultabusqueda= $mysqli->prepare("INSERT INTO busquedas (busqueda) VALUES('".$busqueda."')");

$consultabusqueda->execute();	

$idBusqueda = $mysqli->insert_id;

if (strpos($busqueda, '@') !== false) {

//echo "aqui";
//echo $busqueda;
$busqueda = str_replace('@','',$busqueda);
//echo $conteo;

$url = 'https://api.twitter.com/2/users/by/username/'.$busqueda;

echo $url."<br>";

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => $url,
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'GET',
  CURLOPT_HTTPHEADER => array(
    'Authorization: Bearer AAAAAAAAAAAAAAAAAAAAACGkhAAAAAAANFm%2BCWKqdPRSOUX6Edyg3ekpklg%3D3E1tAHAnjMQZFjIyRerpQ6xSx9pLNznHC7J42bXoXXWetIUBu3',
    'Cookie: guest_id=v1%3A162273890558343460; personalization_id="v1_pnM5aEJksCDqx5xZjj+UGA=="'
  ),
));

$response = curl_exec($curl);

curl_close($curl);
echo $response;
echo "<hr>";
$arr = json_decode($response, true);


$idUsuario = $arr["data"]["id"];

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api.twitter.com/2/users/'.$idUsuario.'/followers?user.fields=created_at,public_metrics&max_results='.$conteo,
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'GET',
  CURLOPT_HTTPHEADER => array(
    'Authorization: Bearer AAAAAAAAAAAAAAAAAAAAACGkhAAAAAAANFm%2BCWKqdPRSOUX6Edyg3ekpklg%3D3E1tAHAnjMQZFjIyRerpQ6xSx9pLNznHC7J42bXoXXWetIUBu3',
    'Cookie: guest_id=v1%3A162273890558343460; personalization_id="v1_pnM5aEJksCDqx5xZjj+UGA=="'
  ),
));

$response = curl_exec($curl);

curl_close($curl);
//echo $response;
//echo "<hr>";
$arr2 = json_decode($response, true);

//print_r($arr2);die();
//echo "<hr>";
foreach ($arr2["data"] as $item){
	
		
	echo '<span>'.$item['id'].'</span><br>';
	echo '<span>'.$item['public_metrics']['followers_count'].'</span><br>';
	echo '<span>'.$item['username'].'</span><br>';
	echo "<hr>";
	//die();
	$idSeguidor = $item['id'];
	$seguidores = $item['public_metrics']['followers_count'];
	$username = $item['username'];
	$creado = $item['created_at'];
	
	$consultacid= $mysqli->prepare("select * from usuarios where idTwitter = '".$idSeguidor."'");

	$consultacid->execute();
	$categorias2 = $consultacid->get_result();
	$row_cnt = mysqli_num_rows($categorias2);

	if ($row_cnt == 0){
	$consultausuarios= $mysqli->prepare("INSERT INTO usuarios (idTwitter,username,seguidores,created_at) VALUES('".$idSeguidor."','".$username."','".$seguidores."','".$creado."')");
	//echo "INSERT INTO usuarios (idTwitter,username,seguidores) VALUES('".$idSeguidor."','".$username."','".$seguidores."')";
	$consultausuarios->execute();	
	}
	
	$consultausuariosxbusqueda= $mysqli->prepare("INSERT INTO usuariosxbusqueda (idTwitter,idBusqueda) VALUES('".$idSeguidor."','".$idBusqueda."')");
	$consultausuariosxbusqueda->execute();	
	
	
	//die();
	
	
	//	echo $analisis;
		if ($analisis == 1){
	
		$conteoTweets = 100;
		$ciclos = 1;
		$next_token = '';
		echo $ciclos;
		while ($ciclos <= 5){
				
					if ($next_token<>''){
			
					$url = 'https://api.twitter.com/2/users/'.$idSeguidor.'/tweets?max_results='.$conteoTweets.'&tweet.fields=public_metrics,created_at&pagination_token='.$next_token;
					
					}
					else
					{
						$url = 'https://api.twitter.com/2/users/'.$idSeguidor.'/tweets?max_results='.$conteoTweets.'&tweet.fields=public_metrics,created_at';
						if ($ciclos<>1){
								break;
						}
					}
					echo "voy en el ciclo: ".$ciclos."<br>";
					echo $url."<hr>"; 
					$curl = curl_init();
					curl_setopt_array($curl, array(
					CURLOPT_URL => $url,
					CURLOPT_RETURNTRANSFER => true,
					CURLOPT_ENCODING => '',
					CURLOPT_MAXREDIRS => 10,
					CURLOPT_TIMEOUT => 0,
					CURLOPT_FOLLOWLOCATION => true,
					CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
					CURLOPT_CUSTOMREQUEST => 'GET',
					CURLOPT_HTTPHEADER => array(
					'Authorization: Bearer AAAAAAAAAAAAAAAAAAAAACGkhAAAAAAANFm%2BCWKqdPRSOUX6Edyg3ekpklg%3D3E1tAHAnjMQZFjIyRerpQ6xSx9pLNznHC7J42bXoXXWetIUBu3',
					'Cookie: guest_id=v1%3A162273890558343460; personalization_id="v1_pnM5aEJksCDqx5xZjj+UGA=="'
					),
					));

					$response = curl_exec($curl);

					curl_close($curl);
				//	echo $response;
					$arr3 = json_decode($response, true);
					//print_r($arr3);
					
					$next_token = $arr3["meta"]['next_token']; 
					echo $next_token."<hr>";
					foreach ($arr3["data"] as $item3){
					/*	echo '<span>'.$item3['id'].'</span><br>';
						echo '<span>'.$item3['text'].'</span><br>';
						echo '<span>'.$item3['public_metrics']['retweet_count'].'</span><br>';
						echo '<span>'.$item3['public_metrics']['reply_count'].'</span><br>';
						echo '<span>'.$item3['public_metrics']['like_count'].'</span><br>';
						echo '<span>'.$item3['created_at'].'</span><br>';
						echo "<hr>";	*/

						$idTweet = $item3['id'];
						$contenido = $item3['text'];
						$created_at = $item3['created_at'];
						$retweets = $item3['public_metrics']['retweet_count'];
						$likes = $item3['public_metrics']['like_count'];
						$comentarios = $item3['public_metrics']['reply_count'];

						$contenido = str_replace('"', '', $contenido);   
						$contenido = str_replace("'", "", $contenido);   

						$consultacid2= $mysqli->prepare("select * from tweets where idTweet = '".$idTweet."'");

						$consultacid2->execute();
						$categorias3 = $consultacid2->get_result();
						$row_cnt3 = mysqli_num_rows($categorias3);

						if ($row_cnt3 == 0){
						$consultatweet= $mysqli->prepare("INSERT INTO tweets (idTwitter,idTweet,contenido,likes,comentarios,retweets,created_at) VALUES('".$idSeguidor."','".$idTweet."'
						,'".$contenido."','".$likes."','".$comentarios."','".$retweets."','".$created_at."')");
						//echo "INSERT INTO tweets (idTwitter,idTweet,contenido,likes,comentarios,retweets,created_at) VALUES('".$idSeguidor."','".$idTweet."'
						//,'".$contenido."','".$likes."','".$comentarios."','".$retweets."','".$created_at."')";
						$consultatweet->execute();	
						}

						$consultatweetxbusqueda= $mysqli->prepare("INSERT INTO tweetsxbusqueda (idTweet,idBusqueda) VALUES('".$idTweet."','".$idBusqueda."')");
						$consultatweetxbusqueda->execute();	

					}
		
			$ciclos++;
		}
		echo "termino ciclos";
		//die();
	}
	else{
	
	
	if ($conteo < 5){
	$conteo = 5;
	}
	$curl = curl_init();
	curl_setopt_array($curl, array(
	  CURLOPT_URL => 'https://api.twitter.com/2/users/'.$idSeguidor.'/tweets?max_results='.$conteo.'&tweet.fields=public_metrics,created_at',
	  CURLOPT_RETURNTRANSFER => true,
	  CURLOPT_ENCODING => '',
	  CURLOPT_MAXREDIRS => 10,
	  CURLOPT_TIMEOUT => 0,
	  CURLOPT_FOLLOWLOCATION => true,
	  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
	  CURLOPT_CUSTOMREQUEST => 'GET',
	  CURLOPT_HTTPHEADER => array(
		'Authorization: Bearer AAAAAAAAAAAAAAAAAAAAACGkhAAAAAAANFm%2BCWKqdPRSOUX6Edyg3ekpklg%3D3E1tAHAnjMQZFjIyRerpQ6xSx9pLNznHC7J42bXoXXWetIUBu3',
		'Cookie: guest_id=v1%3A162273890558343460; personalization_id="v1_pnM5aEJksCDqx5xZjj+UGA=="'
	  ),
	));

	$response = curl_exec($curl);

	curl_close($curl);
	//echo $response;
	$arr3 = json_decode($response, true);
	//print_r($arr3);
	
	foreach ($arr3["data"] as $item3){
		echo '<span>'.$item3['id'].'</span><br>';
		echo '<span>'.$item3['text'].'</span><br>';
		echo '<span>'.$item3['public_metrics']['retweet_count'].'</span><br>';
		echo '<span>'.$item3['public_metrics']['reply_count'].'</span><br>';
		echo '<span>'.$item3['public_metrics']['like_count'].'</span><br>';
		echo '<span>'.$item3['created_at'].'</span><br>';
		echo "<hr>";	
		
		$idTweet = $item3['id'];
		$contenido = $item3['text'];
		$created_at = $item3['created_at'];
		$retweets = $item3['public_metrics']['retweet_count'];
		$likes = $item3['public_metrics']['like_count'];
		$comentarios = $item3['public_metrics']['reply_count'];
		
		$consultacid2= $mysqli->prepare("select * from tweets where idTweet = '".$idTweet."'");

		$consultacid2->execute();
		$categorias3 = $consultacid2->get_result();
		$row_cnt3 = mysqli_num_rows($categorias3);

		if ($row_cnt3 == 0){
		$consultatweet= $mysqli->prepare("INSERT INTO tweets (idTwitter,idTweet,contenido,likes,comentarios,retweets,created_at) VALUES('".$idSeguidor."','".$idTweet."'
		,'".$contenido."','".$likes."','".$comentarios."','".$retweets."','".$created_at."')");
		//echo "INSERT INTO usuarios (idTwitter,username,seguidores) VALUES('".$idSeguidor."','".$username."','".$seguidores."')";
		$consultatweet->execute();	
		}
		
		$consultatweetxbusqueda= $mysqli->prepare("INSERT INTO tweetsxbusqueda (idTweet,idBusqueda) VALUES('".$idTweet."','".$idBusqueda."')");
		$consultatweetxbusqueda->execute();	
		//die();
	}
	
	}
}



}
else
{
	
$busqueda = urlencode($busqueda);
	
$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api.twitter.com/1.1/search/tweets.json?q='.$busqueda.'&result_type=popular&count='.$conteo.'&lang=es',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'GET',
  CURLOPT_HTTPHEADER => array(
    'Authorization: Bearer AAAAAAAAAAAAAAAAAAAAACGkhAAAAAAANFm%2BCWKqdPRSOUX6Edyg3ekpklg%3D3E1tAHAnjMQZFjIyRerpQ6xSx9pLNznHC7J42bXoXXWetIUBu3',
    'Cookie: guest_id=v1%3A162273890558343460; personalization_id="v1_pnM5aEJksCDqx5xZjj+UGA=="'
  ),
));

$response = curl_exec($curl);

curl_close($curl);
//echo $response;



$arr = json_decode($response, true);

//print_r($arr);

echo "<hr>";
foreach ($arr["statuses"] as $item){
	
	echo '<span>'.$item['user']['id'].'</span><br>';
	echo '<span>'.$item['user']['followers_count'].'</span><br>';
	echo '<span>'.$item['user']['screen_name'].'</span><br>';
	echo "<hr>";
	

	$idSeguidor = $item['user']['id'];
	$seguidores = $item['user']['followers_count'];
	$username = $item['user']['screen_name'];
	$creado = $item['user']['createt_at'];
	
	$consultacid= $mysqli->prepare("select * from usuarios where idTwitter = '".$idSeguidor."'");

	$consultacid->execute();
	$categorias2 = $consultacid->get_result();
	$row_cnt = mysqli_num_rows($categorias2);

	if ($row_cnt == 0){
	$consultausuarios= $mysqli->prepare("INSERT INTO usuarios (idTwitter,username,seguidores,created_at) VALUES('".$idSeguidor."','".$username."','".$seguidores."','".$creado."')");
	//echo "INSERT INTO usuarios (idTwitter,username,seguidores) VALUES('".$idSeguidor."','".$username."','".$seguidores."')";
	$consultausuarios->execute();	
	}
	
	$consultausuariosxbusqueda= $mysqli->prepare("INSERT INTO usuariosxbusqueda (idTwitter,idBusqueda) VALUES('".$idSeguidor."','".$idBusqueda."')");
	$consultausuariosxbusqueda->execute();	
	

	
		if ($analisis == 1){
	
		$conteoTweets = 100;
		$ciclos = 1;
		$next_token = '';
		echo $ciclos;
		while ($ciclos <= 5){
				
					if ($next_token<>''){
			
					$url = 'https://api.twitter.com/2/users/'.$idSeguidor.'/tweets?max_results='.$conteoTweets.'&tweet.fields=public_metrics,created_at&pagination_token='.$next_token;
					
					}
					else
					{
						$url = 'https://api.twitter.com/2/users/'.$idSeguidor.'/tweets?max_results='.$conteoTweets.'&tweet.fields=public_metrics,created_at';
						if ($ciclos<>1){
								break;
						}
					}
					echo "voy en el ciclo: ".$ciclos."<br>";
					echo $url."<hr>"; 
					$curl = curl_init();
					curl_setopt_array($curl, array(
					CURLOPT_URL => $url,
					CURLOPT_RETURNTRANSFER => true,
					CURLOPT_ENCODING => '',
					CURLOPT_MAXREDIRS => 10,
					CURLOPT_TIMEOUT => 0,
					CURLOPT_FOLLOWLOCATION => true,
					CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
					CURLOPT_CUSTOMREQUEST => 'GET',
					CURLOPT_HTTPHEADER => array(
					'Authorization: Bearer AAAAAAAAAAAAAAAAAAAAACGkhAAAAAAANFm%2BCWKqdPRSOUX6Edyg3ekpklg%3D3E1tAHAnjMQZFjIyRerpQ6xSx9pLNznHC7J42bXoXXWetIUBu3',
					'Cookie: guest_id=v1%3A162273890558343460; personalization_id="v1_pnM5aEJksCDqx5xZjj+UGA=="'
					),
					));

					$response = curl_exec($curl);

					curl_close($curl);
				//	echo $response;
					$arr3 = json_decode($response, true);
					//print_r($arr3);
					
					$next_token = $arr3["meta"]['next_token']; 
					echo $next_token."<hr>";
					foreach ($arr3["data"] as $item3){
					/*	echo '<span>'.$item3['id'].'</span><br>';
						echo '<span>'.$item3['text'].'</span><br>';
						echo '<span>'.$item3['public_metrics']['retweet_count'].'</span><br>';
						echo '<span>'.$item3['public_metrics']['reply_count'].'</span><br>';
						echo '<span>'.$item3['public_metrics']['like_count'].'</span><br>';
						echo '<span>'.$item3['created_at'].'</span><br>';
						echo "<hr>";	*/

						$idTweet = $item3['id'];
						$contenido = $item3['text'];
						$created_at = $item3['created_at'];
						$retweets = $item3['public_metrics']['retweet_count'];
						$likes = $item3['public_metrics']['like_count'];
						$comentarios = $item3['public_metrics']['reply_count'];

						$contenido = str_replace('"', '', $contenido);   
						$contenido = str_replace("'", "", $contenido);   

						$consultacid2= $mysqli->prepare("select * from tweets where idTweet = '".$idTweet."'");

						$consultacid2->execute();
						$categorias3 = $consultacid2->get_result();
						$row_cnt3 = mysqli_num_rows($categorias3);

						if ($row_cnt3 == 0){
						$consultatweet= $mysqli->prepare("INSERT INTO tweets (idTwitter,idTweet,contenido,likes,comentarios,retweets,created_at) VALUES('".$idSeguidor."','".$idTweet."'
						,'".$contenido."','".$likes."','".$comentarios."','".$retweets."','".$created_at."')");
						//echo "INSERT INTO tweets (idTwitter,idTweet,contenido,likes,comentarios,retweets,created_at) VALUES('".$idSeguidor."','".$idTweet."'
						//,'".$contenido."','".$likes."','".$comentarios."','".$retweets."','".$created_at."')";
						$consultatweet->execute();	
						}

						$consultatweetxbusqueda= $mysqli->prepare("INSERT INTO tweetsxbusqueda (idTweet,idBusqueda) VALUES('".$idTweet."','".$idBusqueda."')");
						$consultatweetxbusqueda->execute();	

					}
		
			$ciclos++;
		}
		echo "termino ciclos";
		//die();
	}
	else{
	
	
	
	
	if ($conteo < 5){
	$conteo = 5;
	}
	$curl = curl_init();
	curl_setopt_array($curl, array(
	  CURLOPT_URL => 'https://api.twitter.com/2/users/'.$idSeguidor.'/tweets?max_results='.$conteo.'&tweet.fields=public_metrics,created_at',
	  CURLOPT_RETURNTRANSFER => true,
	  CURLOPT_ENCODING => '',
	  CURLOPT_MAXREDIRS => 10,
	  CURLOPT_TIMEOUT => 0,
	  CURLOPT_FOLLOWLOCATION => true,
	  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
	  CURLOPT_CUSTOMREQUEST => 'GET',
	  CURLOPT_HTTPHEADER => array(
		'Authorization: Bearer AAAAAAAAAAAAAAAAAAAAACGkhAAAAAAANFm%2BCWKqdPRSOUX6Edyg3ekpklg%3D3E1tAHAnjMQZFjIyRerpQ6xSx9pLNznHC7J42bXoXXWetIUBu3',
		'Cookie: guest_id=v1%3A162273890558343460; personalization_id="v1_pnM5aEJksCDqx5xZjj+UGA=="'
	  ),
	));

	$response = curl_exec($curl);

	curl_close($curl);
	//echo $response;
	$arr3 = json_decode($response, true);
	print_r($arr3);
	
		foreach ($arr3["data"] as $item3){
			/*echo '<span>'.$item3['id'].'</span><br>';
			echo '<span>'.$item3['text'].'</span><br>';
			echo '<span>'.$item3['public_metrics']['retweet_count'].'</span><br>';
			echo '<span>'.$item3['public_metrics']['reply_count'].'</span><br>';
			echo '<span>'.$item3['public_metrics']['like_count'].'</span><br>';
			echo '<span>'.$item3['created_at'].'</span><br>';
			echo "<hr>";	*/
			
			$idTweet = $item3['id'];
			$contenido = $item3['text'];
			$created_at = $item3['created_at'];
			$retweets = $item3['public_metrics']['retweet_count'];
			$likes = $item3['public_metrics']['like_count'];
			$comentarios = $item3['public_metrics']['reply_count'];
			
			$contenido = str_replace('"', '', $contenido);   
			$contenido = str_replace("'", "", $contenido);   
			
			$consultacid2= $mysqli->prepare("select * from tweets where idTweet = '".$idTweet."'");

			$consultacid2->execute();
			$categorias3 = $consultacid2->get_result();
			$row_cnt3 = mysqli_num_rows($categorias3);

			if ($row_cnt3 == 0){
			$consultatweet= $mysqli->prepare("INSERT INTO tweets (idTwitter,idTweet,contenido,likes,comentarios,retweets,created_at) VALUES('".$idSeguidor."','".$idTweet."'
			,'".$contenido."','".$likes."','".$comentarios."','".$retweets."','".$created_at."')");
			//echo "INSERT INTO tweets (idTwitter,idTweet,contenido,likes,comentarios,retweets,created_at) VALUES('".$idSeguidor."','".$idTweet."'
			//,'".$contenido."','".$likes."','".$comentarios."','".$retweets."','".$created_at."')";
			$consultatweet->execute();	
			}
			
			$consultatweetxbusqueda= $mysqli->prepare("INSERT INTO tweetsxbusqueda (idTweet,idBusqueda) VALUES('".$idTweet."','".$idBusqueda."')");
			$consultatweetxbusqueda->execute();	

		}
	}
}


}

echo "<a href='parseador.php?id=".$idBusqueda."'>Procesar Contenido</a><br><br> ó";
echo "<a href='analisis.php?id=".$idBusqueda."'>Ver Analisis de cuentas</a>";
?>