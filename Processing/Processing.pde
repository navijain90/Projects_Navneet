GumballMachine gumballMachine = new GumballMachine(5);
Screen_output objScreenOutput = new Screen_output();
Create_Button objCreateButton1 = new Create_Button(100,680,250,60);  // Create Button 1 object
Create_Button objCreateButton2 = new Create_Button(400,680,250,60);  // Create Button 2 object
boolean insert_quarter=false;
boolean turnedCrank=false;
void setup() 
{
  size(800, 800) ;
  background(255) ;
  smooth() ;
  strokeWeight(3);
  strokeCap(ROUND);
  // load font
  PFont font;
  font = loadFont("BookAntiqua-48.vlw");
  textFont(font, 36);
  fill(0);  
  text("The Gumball Machine", 250, 60);
  PImage image = loadImage("gumball.jpg");
  image(image, (width-image.width)/2, (height-image.height)/2);
}

void draw() {
  objCreateButton1.mouseDrag();
  objCreateButton1.drawButton(true);
  objCreateButton2.mouseDrag();
  objCreateButton2.drawButton(false);
}
public void mousePressed(){
  if(mouseX>100 && mouseX<350 && mouseY>680 && mouseY<740){
    stroke(120,10,120); 
    fill(0);
    objCreateButton1.drawButton(true);
    insert_quarter=true;
    runTest();
  }else if(mouseX>400 && mouseX<650 && mouseY>680 && mouseY<740){
    stroke(120,10,120); 
    fill(0);
    objCreateButton2.drawButton(false);
    turnedCrank=true;
    runTest();
  }

}
public void runTest() {
  if(insert_quarter==true){
     gumballMachine.insertQuarter();
     insert_quarter=false;
  }
  if(turnedCrank==true){
    gumballMachine.turnCrank();
    turnedCrank=false;
  }
  System.out.println(gumballMachine);
}