import greenfoot.*;  // (World, Actor, GreenfootImage, Greenfoot and MouseInfo)
import java.awt.*;

/**
 * Write a description of class Message here.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */
public class Message extends Actor
{
    public void setText(String text)
    {
        updateImage(text);
    }
    private void updateImage(String text)
    {
        setImage(new GreenfootImage(text,36,Color.BLACK,Color.GREEN));
    }
}
