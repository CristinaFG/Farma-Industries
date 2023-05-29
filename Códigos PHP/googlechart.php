  <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
  <div id="chart_div"></div>
  <div id="chart_div2"></div>
  <div id="chart_div3"></div> 
  <div id="chart_div4"></div>
  <div id="chart_div5"></div>
  <div id="chart_div6"></div>
  <div id="chart_div7"></div>
  
  <?php 
	include ('connectBD.php');
	include ('funciones.php');
    // ConexiÃ³n con la base de datos
    $conexion = conectarBD();
    
    $valor_temp1 = obtener_valores(1, $conexion);
    //var_dump ($valor_temp1);die();
    $valor_temp2 = obtener_valores(2, $conexion);
    $valor_temp3 = obtener_valores(3, $conexion);
    $valor_temp4 = obtener_valores(4, $conexion);
    $valor_temp5 = obtener_valores(5, $conexion);
    $valor_temp6 = obtener_valores(6, $conexion);
    $valor_temp7 = obtener_valores(7, $conexion);
    
	desconectarBD($conexion);
  ?>
<script>
    google.charts.load('current', {packages: ['corechart', 'line']});
    google.charts.setOnLoadCallback(drawBasic1);
    google.charts.load('current', {packages: ['corechart', 'line']});
    google.charts.setOnLoadCallback(drawBasic2);
    google.charts.load('current', {packages: ['corechart', 'line']});
    google.charts.setOnLoadCallback(drawBasic3);
    google.charts.load('current', {packages: ['corechart', 'line']});
    google.charts.setOnLoadCallback(drawBasic4);
    google.charts.load('current', {packages: ['corechart', 'line']});
    google.charts.setOnLoadCallback(drawBasic5);
    google.charts.load('current', {packages: ['corechart', 'line']});
    google.charts.setOnLoadCallback(drawBasic6);
    google.charts.load('current', {packages: ['corechart', 'line']});
    google.charts.setOnLoadCallback(drawBasic7);


function drawBasic1() {

      var data = new google.visualization.DataTable();
      data.addColumn('string', 'datetime');
      data.addColumn('number', 'cm');
	  data.addRows(<?php echo $valor_temp1;?>);

      var options = {
        title: 'URJC',
        curveType: 'function',
  
        
        vAxis: {
          title: 'Distancia',
          viewWindow: {
              max:400,
              min:0
            }
        }
      };

      var chart = new google.visualization.LineChart(document.getElementById('chart_div'));
      chart.draw(data, options);
            
    }   

function drawBasic2() {

      var data = new google.visualization.DataTable();
      data.addColumn('string', 'Time of Day');
      data.addColumn('number', 'Pa');
	  data.addRows(<?php echo $valor_temp2;?>);

      var options = {
        
        vAxis: {
          title: 'Presion'
        }
      };

      var chart = new google.visualization.LineChart(document.getElementById('chart_div2'));
      chart.draw(data, options);
            
    } 

function drawBasic3() {

      var data = new google.visualization.DataTable();
      data.addColumn('string', 'Time of Day');
      data.addColumn('number', '%');
	  data.addRows(<?php echo $valor_temp3;?>);

      var options = {
        
        vAxis: {
          title: 'Humedad'
        }
      };

      var chart = new google.visualization.LineChart(document.getElementById('chart_div3'));
      chart.draw(data, options);
            
    }    

function drawBasic4() {

      var data = new google.visualization.DataTable();
      data.addColumn('string', 'Time of Day');
      data.addColumn('number', 'particulas');
	  data.addRows(<?php echo $valor_temp4;?>);

      var options = {
        
        vAxis: {
          title: 'Particulas 0.5 um'
        }
      };

      var chart = new google.visualization.LineChart(document.getElementById('chart_div4'));
      chart.draw(data, options);
            
    } 

function drawBasic5() {

      var data = new google.visualization.DataTable();
      data.addColumn('string', 'Time of Day');
      data.addColumn('number', 'particulas');
	  data.addRows(<?php echo $valor_temp5;?>);

      var options = {
        
        vAxis: {
          title: 'Particulas 5 um'
        }
      };

      var chart = new google.visualization.LineChart(document.getElementById('chart_div5'));
      chart.draw(data, options);
            
    } 

function drawBasic6() {

      var data = new google.visualization.DataTable();
      data.addColumn('string', 'Time of Day');
      data.addColumn('number', 'g');
	  data.addRows(<?php echo $valor_temp6;?>);

      var options = {
        
        vAxis: {
          title: 'Peso'
        }
      };

      var chart = new google.visualization.LineChart(document.getElementById('chart_div6'));
      chart.draw(data, options);
            
    } 

function drawBasic7() {

      var data = new google.visualization.DataTable();
      data.addColumn('string', 'Time of Day');
      data.addColumn('number', 'ºC');
	  data.addRows(<?php echo $valor_temp7;?>);

      var options = {
        
        vAxis: {
          title: 'Temperatura'
        }
      };

      var chart = new google.visualization.LineChart(document.getElementById('chart_div7'));
      chart.draw(data, options);
            
    } 
</script>