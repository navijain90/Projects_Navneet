var express=require("express"); // Include express dependency
var bodyParser=require('body-parser'); //Include body parser to format data received from thr post request
var app=express(); //Initialize a node.js app
app.use(bodyParser.json()); // app use json body parser

var meows=["Hello I am Navneet Jain",
		"My cat is running around",
		"My dog is running around"];  // Array to display data

app.get('/meows',function(req,res,next){

	res.send(meows);
});  //Implementation of get function

app.post('/meows',function(req,res,next){
	console.log(req.body)  // Log at the server end
	meows.push(req.body.newMeow) // Push the new meow to the array
	res.send(meows);
});  // Implementation of post function
app.use(express.static("public"))  // Allows app to use the front end from the public folder in the src
app.listen(3000,function(){
	console.log("Example Runing on port 3000")
});  // Make the server live at the localhost and port