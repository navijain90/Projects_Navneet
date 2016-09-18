import greenfoot.*;  // (World, Actor, GreenfootImage, Greenfoot and MouseInfo)

/**
 * Write a description of class GreenPicker here.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */
public class GreenPicker extends Picker
{
    /**
     * Act - do whatever the GreenPicker wants to do. This method is called whenever
     * the 'Act' or 'Run' button gets pressed in the environment.
     */
    public void act() 
    {
        // Add your action code here.
    }
    // Create a Green Gumball and add the object to the world
    public void create_GumBall()
    {
        getWorld().addObject( new GreenGumball(), 600,700) ;    
        Message objMessage = new Message();
        objMessage.setText("Green Gumball");
        getWorld().addObject(objMessage,750,750);
    }
}
