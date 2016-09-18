import greenfoot.*;  // (World, Actor, GreenfootImage, Greenfoot and MouseInfo)
import java.io.*;
import java.awt.*;
import java.lang.Object.*;

/**
 * Write a description of class GumballMachine here.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */
public class GumballMachine extends Actor
{
    public static boolean bisCoinInserted = false;
    Message objMessage=new Message();
    
    public GumballMachine()
    {
        GreenfootImage image = getImage() ;
        image.scale( 550, 650 ) ; 
    }

    public void act() 
    {
        World world=getWorld();
        Inspector inspector = world.getObjects(Inspector.class).get(0);
        Actor coin=getOneObjectAtOffset(0,0,Coin.class);
              
        if(coin != null)
        {
            getWorld().removeObjects(getWorld().getObjects(Message.class));
            getWorld().removeObjects(getWorld().getObjects(Gumball.class)); 
            bisCoinInserted= true;
            inspector.saveCoin(coin);
            world.removeObject(coin);
            objMessage.setText("Have Coin Turn Crank");
            world.addObject(objMessage,400,300);
        } 
        if(Greenfoot.mousePressed(this)&&bisCoinInserted)
        {
            inspector.inspect_coin();
            world.removeObject(objMessage);
            bisCoinInserted=false;
            Message InsertCoin=new Message();
            InsertCoin.setText("Insert Coin");
            world.addObject(InsertCoin,400,400);
            Message TurnCrank=new Message();
            TurnCrank.setText("Turn Crank");
            world.addObject(TurnCrank,400,620);
        }
        

    }
}
