<!DOCTYPE html>
<html>
<head>
<title>Expressions litérales</title>
<style>
body {
    background-color: #e6fbff;
    }
    
main {
      height: calc(100vh - 60px);
    }
    
    
h1 {
	text-align: center;
    }




.progress {
	  display: inline-block;
      border: 5px solid #0dff00;
      border-radius: 5px;
      width: 0%;
      margin-bottom: 10px;
      margin-top: 10px;
      transition: width 1s;
       
    }
    
.total {
	  display: inline-block;
      position: absolute;
      left: 10px;
  	  z-index: -1;
      border: 5px solid #edfff0;
      border-radius: 5px;
      width: calc(100% - 80px);
      margin-bottom: 10px;
      margin-top: 10px;
    }
    
.percent {
 	  color: #067300;
	  display: inline-block;
      position: absolute;
  	  right: 10px;
      margin-bottom: 10px;
      margin-top: 5px;
      
    }
    
    
    
</style>
</head>
<body>

<main>
<h1>Développer et réduire l'éxpression suivante:</h1>
<p id='p'>A = 3(x + 6) - 2</p>

</main>
<nobr class='progress' id='bar'></nobr>
<nobr class='total'></nobr>
<nobr class='percent' id='percent'>0 / 20</nobr>
</body>
<script>
function bar(nb){
	const percent = nb / 20 * 100;
    const px = nb / 20 * 61;
	document.getElementById("bar").style.width = 'calc('+ percent + '% - ' + px + 'px)';
    document.getElementById("percent").innerHTML = nb + ' / 20';
    }
    
    
    
    

function random_bool(){
	return Math.random() < 0.5
}

function random_letter(){
    let letter = Math.floor(Math.random() * 5) + 1
    if (letter == 1) {
      return 'x'
    }
    else if (letter == 2) {
      return 'y'
    }
    else if (letter == 3) {
      return 'xy'
    }
    else if (letter == 4) {
      return 'x²'
    }
    else if (letter == 5) {
      return 'y²'
    }
}

function random_nb2(){
	return Math.floor(Math.random() * 10) + 1
}

function random_nb() {
	let nb_or_letter = Math.floor(Math.random() * 3) + 1
    if (nb_or_letter == 1) {
    	let number = random_nb2()
        return number
    }
    
    else if (nb_or_letter == 2) {
    	let letter = random_letter()
        return letter
    }
    
    else if (nb_or_letter == 3) {
    	let number = random_nb2()
    	let letter = random_letter()
        return number + letter
    }
}

function plus_minus(){
	if (random_bool()){
    	return ' + '
    }
    else {
    	return ' - '
    }
}


function generate(){
	let str = ""
    let result = ""
	let plusdevant = random_bool()
    if (plusdevant) {
    	let rn = random_nb()
        let pm = plus_minus()
    	str = str + rn
        str = str + pm
        result = result + rn
        result = result + pm
    }
    
    let k = random_nb()
    let a = random_nb()
    let b = random_nb()
    let sign = plus_minus()
    str = str + k
    str = str + '('
    str = str + a
    str = str + sign
    str = str + b
    str = str + ')'
    result = result + k
    result = result + '×'
    result = result + a
    result = result + sign
    result = result + k
    result = result + '×'
    result = result + b
    
    if (plusdevant == false) {
    	let pm = plus_minus()
        let rn = random_nb()
    	str = str + pm
        str = str + rn
        result = result + pm
        result = result + rn
    }
    
    
    // make a better result
    result = result.replaceAll(" ", "")
    resultplus = result.split("+"); // return list
    resultminus = result.split("-"); // return list
    result = resultplus.split("-"); // return list
    
    for (let x in result) {
    	for (let caracter of x){
        	
    }
    
    
    return [str, result]
    
}




document.getElementById("p").innerHTML = generate()
</script>
</html>


