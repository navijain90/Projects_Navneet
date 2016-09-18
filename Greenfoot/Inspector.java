import greenfoot.*;  // (World, Actor, GreenfootImage, Greenfoot and MouseInfo)
import java.util.*;


/**
 * Write a description of class Inspector here.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */
public class Inspector extends Alien
{
    public Actor coin;
    Message objMessage=new Message();
    /**
     * Act - do whatever the Inspector wants to do. This method is called whenever
     * the 'Act' or 'Run' button gets pressed in the environment.
     */
    public void act() 
    {
        // Add your action code here.
    }
    public void inspect_coin(){
        //getWorld().removeObjects(getWorld().getObjects(Gumball.class)); // Remove all Gumballs from the world
        if(coin instanceof Penny){
            //getWorld().addObject( new Penny(), 65, 77 ) ;
            objMessage.setText("Penny Inserted");
            getWorld().addObject(objMessage,700,550);
        }
        else if(coin instanceof FakeQuarter){
            //getWorld().addObject( new FakeQuarter(), 65, 380 ) ;
            objMessage.setText("Fake Quarter Inserted");
            getWorld().addObject(objMessage,700,550);
        }
        else if(coin instanceof Quarter){
            objMessage.setText("Quarter Inserted");
            getWorld().addObject(objMessage,700,550);
            int normal = Greenfoot.getRandomNumber(10); // Generate a random number to select a Picker
            if(normal <5)
            {
                GreenPicker picker=getWorld().getObjects(GreenPicker.class).get(0);
                picker.create_GumBall();
            }
            else
            {
                RandomPicker picker=getWorld().getObjects(RandomPicker.class).get(0);
                picker.create_GumBall();
            }
        }
    }
    public void saveCoin(Actor coinInput)
    {
        coin=coinInput;
    }
}
