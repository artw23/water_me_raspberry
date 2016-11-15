<?php
  $tiempo = $_GET['time'];
  $command = escapeshellcmd('./water.py ' . $tiempo);
  $output = shell_exec($command);
  echo $output;
  echo "La planta se regara " . $tiempo . " segundos";
?>
