boolean overBox = false;
boolean locked = false;
PFont myFont;
public class Create_Button{
  private int bx;
  private int by;
  private int boxWidth;
  private int boxLength;
  public Create_Button(int x,int y,int wid,int len){
    this.bx=x;
    this.by=y;
    this.boxWidth=wid;
    this.boxLength=len;
  }
  public void drawButton(boolean value)
  {
    rect(this.bx,this.by,this.boxWidth,this.boxLength);
    fontCreation(value);
  }
  private void fontCreation(boolean bvalue){
    fill(255,0,0);
    myFont = createFont("ACaslonPro-Bold", 36);
    textFont(myFont);
    textAlign(CENTER,CENTER);
    if(bvalue == true){
      text("Insert Quarter",this.bx+this.boxWidth/2,this.by+this.boxLength/2);
    }else {
      text("Turn Crank",this.bx+this.boxWidth/2,this.by+this.boxLength/2);
    }
    
}
  
  public void mouseDrag(){
   if((mouseX > this.bx) && (mouseX < this.bx+this.boxWidth) &&
      (mouseY > this.by) && (mouseY < this.by+this.boxLength))
    {
      overBox=true;
      if(!locked) {
        stroke(120,10,120); 
        fill(126);
      } 
    } else {
      stroke(120,10,120);
      fill(255);
      overBox = false;
    }  
  }
}