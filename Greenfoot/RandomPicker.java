import greenfoot.*;  // (World, Actor, GreenfootImage, Greenfoot and MouseInfo)

/**
 * Write a description of class RandomPicker here.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */
public class RandomPicker extends Picker
{
    /**
     * Act - do whatever the RandomPicker wants to do. This method is called whenever
     * the 'Act' or 'Run' button gets pressed in the environment.
     */
    public void act() 
    {
        // Add your action code here.
    }
    // Create Gumball and add the object to the world
    public void create_GumBall()
    { 
        Message objMessage = new Message();
        int normal = Greenfoot.getRandomNumber(10);
        if(normal < 5)
        {
            getWorld().addObject( new RedGumball(), 600,100) ; 
            objMessage.setText("Red Gumball");
            getWorld().addObject(objMessage,750,150);
        }
        else
        {
            getWorld().addObject( new BlueGumball(), 600,100) ; 
            objMessage.setText("Blue Gumball");
            getWorld().addObject(objMessage,750,150);
        }
    }
}
