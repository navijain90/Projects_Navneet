import greenfoot.*;  // (World, Actor, GreenfootImage, Greenfoot and MouseInfo)

/**
 * Write a description of class GumballWorld here.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */
public class GumballWorld extends World
{

    /**
     * Constructor for objects of class GumballWorld.
     * 
     */
    public GumballWorld()
    {    
        // Create a new world with 600x400 cells with a cell size of 1x1 pixels.
        super(1000, 900, 1); 
        prepare();
    }

    /**
     * Prepare the world for the start of the program. That is: create the initial
     * objects and add them to the world.
     */
    private void prepare()
    {
        GumballMachine gumballmachine = new GumballMachine();
        addObject(gumballmachine, 400, 400);
        addObject( new Penny(), 65, 77 ) ;
        addObject( new Quarter(), 65, 220) ;
        addObject( new Quarter(), 65, 600) ;
        addObject( new Quarter(), 65, 800) ;
        addObject( new FakeQuarter(), 65, 380 ) ;
        Message InsertCoin=new Message();
        InsertCoin.setText("Insert Coin");
        addObject(InsertCoin,400,400);
        Message TurnCrank=new Message();
        TurnCrank.setText("Turn Crank");
        addObject(TurnCrank,400,620);
        Inspector inspector = new Inspector();
        addObject(inspector, 680, 400);
        RandomPicker randompicker = new RandomPicker();
        addObject(randompicker, 700, 104);
        randompicker.setLocation(810, 110);
        GreenPicker greenpicker = new GreenPicker();
        addObject(greenpicker, 700, 654);
        greenpicker.setLocation(810, 700);
    }
}
