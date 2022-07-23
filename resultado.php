<?php

$busqueda = $_GET['id'];


$mysqli = new mysqli("localhost", "woobsing_twitter", "julimba1$", "woobsing_tweetAnalize");
$mysqli->set_charset("utf8mb4");

function array_sort($array, $on, $order=SORT_DESC)
{
    $new_array = array();
    $sortable_array = array();

    if (count($array) > 0) {
        foreach ($array as $k => $v) {
            if (is_array($v)) {
                foreach ($v as $k2 => $v2) {
                    if ($k2 == $on) {
                        $sortable_array[$k] = $v2;
                    }
                }
            } else {
                $sortable_array[$k] = $v;
            }
        }

        switch ($order) {
            case SORT_ASC:
                asort($sortable_array);
            break;
            case SORT_DESC:
                arsort($sortable_array);
            break;
        }

        foreach ($sortable_array as $k => $v) {
            $new_array[$k] = $array[$k];
        }
    }

    return $new_array;
}

?>

<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
    <title>CONSULTA DE TWITTER</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css" integrity="sha512-dTfge/zgoMYpP7QbHy4gWMEGsbsdZeCXz7irItjcC3sPUFtf0kuFbDz/ixG7ArTxmDjLXDmezHubeNikyKGVyQ==" crossorigin="anonymous">
    <link rel="stylesheet" href="https://cdn.datatables.net/1.10.25/css/dataTables.bootstrap4.min.css" >
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
			
		<link rel="stylesheet" href="//code.jquery.com/ui/1.12.1/themes/base/jquery-ui.css">
			<script src="https://code.jquery.com/jquery-1.12.4.js"></script>
		<script src="https://code.jquery.com/ui/1.12.1/jquery-ui.js"></script>
		<script src="https://cdn.datatables.net/1.10.25/js/jquery.dataTables.min.js"></script>
		<script src="https://cdn.datatables.net/1.10.25/js/dataTables.bootstrap4.min.js"></script>



		

<style>
.row {
    margin-bottom: 18px;
}
</style>
</head>
<body>
<nav class="navbar navbar-default">
  <div class="container-fluid">
    <div class="navbar-header">
      <a class="navbar-brand" href="#">Consulta de Twitter</a>
    </div>
    
  </div>
</nav>
<div class="container">

<?php
$consulta2= $mysqli->prepare("SELECT * from busquedas where idBusqueda=".$busqueda);
$consulta2->execute();
$categorias2 = $consulta2->get_result();
$row2 = $categorias2->fetch_assoc()

?>

<h1>RESULTADOS DE LA BUSQUEDA "<?php echo $row2['busqueda']; ?>" </h1>


<h2>PALABRAS MAS IMPORTANTES EN EL TEMA</H2>

<?php

$query = $mysqli->prepare("SELECT COUNT(*) as `count` FROM palabrasxbusqueda");

// Since there will always be exactly 1 row, fetch it.}
$query->execute();
$result = $query->get_result();
$row = $result->fetch_assoc();

$cantidadPalabras = $row['count'];

$queryx = $mysqli->prepare("SELECT COUNT(*) as `count` FROM palabrasxbusqueda where idBusqueda=".$busqueda."");

// Since there will always be exactly 1 row, fetch it.}
$queryx->execute();
$resultx = $queryx->get_result();
$rowx = $resultx->fetch_assoc();

$cantidadPalabrasBusqueda = $rowx['count'];




$consulta= $mysqli->prepare("SELECT palabrasxbusqueda.idPalabra, palabra, COUNT(*) as conteo
FROM palabrasxbusqueda
inner join palabras on palabras.idPalabra = palabrasxbusqueda.idPalabra
where idBusqueda=".$busqueda."
GROUP BY idPalabra
ORDER BY COUNT(*) DESC");
$consulta->execute();
$categorias = $consulta->get_result();
$i = 1;
$array = [];
while($row = $categorias->fetch_assoc()) {
	$iddPalabra = $row['idPalabra'];
	
	$palabrita = $row['palabra'];
	
	$counta =  substr_count($palabrita, ' ');
	
	//echo $palabrita . "-".$counta;
	//echo "<br>";
	if ($counta < 1){
	
	$query2 = $mysqli->prepare("SELECT COUNT(*) as `count` FROM palabrasxbusqueda where idPalabra = '".$iddPalabra."'" );

	// Since there will always be exactly 1 row, fetch it.}
	$query2->execute();
	$result2 = $query2->get_result();
	$row2 = $result2->fetch_assoc();
	
	$cantidadPalabrasCluster = $row2['count'];
	
	$cantidadPal = $row['conteo'];
	
	$umbral = ($cantidadPal*10000)/$cantidadPalabrasBusqueda;
	$umbral = round($umbral); 
	if ($umbral > 3){

	$pesoPalabra = (($cantidadPal*100)/$cantidadPalabrasCluster)/(($cantidadPalabrasCluster*100)/$cantidadPalabras);
	
	$pesoPalabra;
	$array[] = [
		'word' => $palabrita,
		'peso' => $pesoPalabra
	];
	}
	}
}
//print_r(array_sort($array, 'peso'));

$array2 = array_sort($array, 'peso');
$d = 0;
foreach ($array2 as $row) {
	?>
	<span class="badge bg-warning text-dark" style="margin-right:10px;"><?echo $row['word'];?></span>
 <?
	$d++;
	if ($d == 50)
	{
	break;
	}
}

?>


<h2>DENSIDAD POR PALABRAS</H2>

<table id="example"  class="table table-striped">
  <thead>
    <tr>
      <th scope="col">#</th>
      <th scope="col">PALABRA</th>
      <th scope="col">CONTEO</th>
    </tr>
  </thead>
  <tbody>
<?php
$consulta= $mysqli->prepare("SELECT palabrasxbusqueda.idPalabra, palabra, COUNT(*) as conteo
FROM palabrasxbusqueda
inner join palabras on palabras.idPalabra = palabrasxbusqueda.idPalabra
where idBusqueda=".$busqueda."
GROUP BY idPalabra
ORDER BY COUNT(*) DESC");
$consulta->execute();
$categorias = $consulta->get_result();
$i = 1;
while($row = $categorias->fetch_assoc()) {
?>
    <tr>
      <th scope="row"><?php echo $i; ?></th>
      <td><?php echo $row['palabra']; ?></td>
      <td><?php echo $row['conteo']; ?></td>
    </tr>
	
<? 
$i++; 
}
?>
   </tbody>
</table>	

<h2>MENCIONES</H2>

<table  id="example2"  class="table table-striped">
  <thead>
    <tr>
      <th scope="col">#</th>
      <th scope="col">HASHTAG</th>
      <th scope="col">CONTEO</th>
    </tr>
  </thead>
  <tbody>
<?php
$consulta= $mysqli->prepare("SELECT mencionesxbusqueda.idMencion, mencion, COUNT(*) as conteo
FROM mencionesxbusqueda
inner join menciones on menciones.idMencion = mencionesxbusqueda.idMencion
where idBusqueda=".$busqueda." and menciones.mencion like '%#%'
GROUP BY idMencion
ORDER BY COUNT(*) DESC");
$consulta->execute();
$categorias = $consulta->get_result();
$i = 1;
while($row = $categorias->fetch_assoc()) {
?>
    <tr>
      <th scope="row"><?php echo $i; ?></th>
      <td><?php echo $row['mencion']; ?></td>
      <td><?php echo $row['conteo']; ?></td>
    </tr>
	
<? 
$i++; 
}
?>
   </tbody>
</table>	

<table  id="example4"  class="table table-striped">
  <thead>
    <tr>
      <th scope="col">#</th>
      <th scope="col">MENCION</th>
      <th scope="col">CONTEO</th>
    </tr>
  </thead>
  <tbody>
<?php
$consulta= $mysqli->prepare("SELECT mencionesxbusqueda.idMencion, mencion, COUNT(*) as conteo
FROM mencionesxbusqueda
inner join menciones on menciones.idMencion = mencionesxbusqueda.idMencion
where idBusqueda=".$busqueda." and menciones.mencion like '%@%'
GROUP BY idMencion
ORDER BY COUNT(*) DESC");

$consulta->execute();
$categorias = $consulta->get_result();
$i = 1;
while($row = $categorias->fetch_assoc()) {
?>
    <tr>
      <th scope="row"><?php echo $i; ?></th>
      <td><?php echo $row['mencion']; ?></td>
      <td><?php echo $row['conteo']; ?></td>
    </tr>
	
<? 
$i++; 
}
?>
   </tbody>
</table>	


<h2>URLS</H2>

<table id="example3"  class="table table-striped">
  <thead>
    <tr>
      <th scope="col">#</th>
      <th scope="col">URL</th>
      <th scope="col">CONTEO</th>
    </tr>
  </thead>
  <tbody>
<?php
$consulta= $mysqli->prepare("SELECT urlsxbusqueda.idUrl, url, COUNT(*) as conteo
FROM urlsxbusqueda
inner join urls on urls.idUrl = urlsxbusqueda.idUrl
where idBusqueda=".$busqueda."
GROUP BY idUrl
ORDER BY COUNT(*) DESC");
$consulta->execute();
$categorias = $consulta->get_result();
$i = 1;
while($row = $categorias->fetch_assoc()) {
?>
    <tr>
      <th scope="row"><?php echo $i; ?></th>
      <td><a href="<?php echo $row['url']; ?>" target="_blank"><?php echo $row['url']; ?></a></td>
      <td><?php echo $row['conteo']; ?></td>
    </tr>
	
<? 
$i++; 
}
?>
   </tbody>
</table>			
					
</div>
<script>

$(document).ready(function() {
    $('#example').DataTable();
    $('#example2').DataTable();
    $('#example3').DataTable();
    $('#example4').DataTable();
} );

</script>
</body>
</html>

