//Cntl+C to stop server
//Modulos de Node para diferentes cosas
//Codigo basado en la clase de COMP 2406 de Carleton University del Prof. Lou Nel.
var http = require('http'); //need to http
var fs = require('fs'); //need to read static files
var url = require('url'); //to parse url strings var

//Para realizar la lectura de los sensores desde la base de datos (En proceso)
//sqlite3 = require('sqlite3').verbose();//need to connect with Database
//var db = new sqlite3.Database('data.db'); //need to open Database connection

var ROOT_DIR = 'html'; //directorio de los archivos html

//Para decirle en el mensaje que se envie al navegador que tipo de dato (MIME TYPE) se esta mandando
var MIME_TYPES = {
    'css': 'text/css',
    'gif': 'image/gif',
    'htm': 'text/html',
    'html': 'text/html',
    'ico': 'image/x-icon',
    'jpeg': 'image/jpeg',
    'jpg': 'image/jpeg',
    'js': 'text/javascript', //should really be application/javascript
    'json': 'application/json',
    'png': 'image/png',
    'txt': 'text/plain'
};

//Obtener el tipo de MIME del archivo actual
var get_mime = function(filename) {
    var ext, type;
    for (ext in MIME_TYPES) {
        type = MIME_TYPES[ext];
        if (filename.indexOf(ext, filename.length - ext.length) !== -1) {
            return type;
        }
    }
    return MIME_TYPES['txt'];
};

//Crear el servidor --> Recibe el tipo de request y responde con un archivo response
http.createServer(function (request,response){
     //Ver el URL que se suministr�
     var urlObj = url.parse(request.url, true, false);
     //Imprimir los mensajes
     console.log('\n============================');
         console.log("PATHNAME: " + urlObj.pathname);
     console.log("REQUEST: " + ROOT_DIR + urlObj.pathname);
     console.log("METHOD: " + request.method);
         //Obtener  el archivo de la direccion que se solicita
         var filePath = ROOT_DIR + urlObj.pathname;
        //Direccion por defecto si no se suministra una ruta en el URL
         if(urlObj.pathname === '/') filePath = ROOT_DIR + '/index2.html';
     //Lectura  del archivo
     fs.readFile(filePath, function(err,data){
       if(err){
                  //report error to console
          console.log('ERROR: ' + JSON.stringify(err));
                  //respond with not found 404 to client
		response.writeHead(404);
          response.end(JSON.stringify(err));
          return;
         }
        //Enviar el archivo solicitado con el MIME type correspondiente
         response.writeHead(200, {'Content-Type': get_mime(filePath)});
         response.end(data);
       });

 }).listen(3000); //Se esta escuchando el puerto 3000 del computador

console.log('Server Running at http://127.0.0.1:3000  CNTL-C to quit');
