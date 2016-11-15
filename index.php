<?php
  $tiempo = $_GET['time'];
  $output = passthru("python water.py $tiempo");
  echo $output;
  echo "La planta se regara " . $tiempo . " segundos";
?>
