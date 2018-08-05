package chapter4.exercises;

import junit.framework.TestCase;

/**
 * Unit test for simple App.
 */
public class Excercise4_1_Test 
    extends TestCase
{

	public Excercise4_1_Test( String testName )
    {
        super( testName );
    }

    public void testItsBalancedWhenHasNoChilds()
    {
    		Tree tree = new Tree(1);
        assertTrue( tree.is_balanced() );
        assertEquals(1, tree.level());
    }
    
    public void testItsBalancedWhenHasTwoChildWithThreeChildsEach()
    {
    		// Set up fixture
    		Tree tree = new Tree(1);
        assertTrue( tree.is_balanced() );
        
        Tree subLevel1Node1 = new Tree(2);
        Tree subLevel1Node2 = new Tree(2);
        
        Tree subLevel2Node1 = new Tree(3);
        Tree subLevel2Node2 = new Tree(3);
        Tree subLevel2Node3 = new Tree(3);

        Tree subLevel2Node4 = new Tree(3);
        Tree subLevel2Node5 = new Tree(3);
        Tree subLevel2Node6 = new Tree(3);

        subLevel1Node1.addChild(subLevel2Node1);
        subLevel1Node1.addChild(subLevel2Node2);
        subLevel1Node1.addChild(subLevel2Node3);

        subLevel1Node2.addChild(subLevel2Node4);
        subLevel1Node2.addChild(subLevel2Node5);
        subLevel1Node2.addChild(subLevel2Node6);
        
        tree.addChild(subLevel1Node1);
        tree.addChild(subLevel1Node2);
        
        assertTrue( tree.is_balanced() );
        assertEquals(3, tree.level());
    }
    
    public void testItsNotBalancedWhenHasTwoChildWithThreeChildsEach()
    {
    		// Set up fixture
    		Tree tree = new Tree(1);
        assertTrue( tree.is_balanced() );
        
        Tree subLevel1Node1 = new Tree(2);
        Tree subLevel1Node2 = new Tree(2);
        
        Tree subLevel2Node1 = new Tree(3);
        
        Tree subLevel4Node = new Tree(4);
                
        subLevel2Node1.addChild(subLevel4Node);

        subLevel1Node1.addChild(subLevel2Node1);
        
        tree.addChild(subLevel1Node1);
        tree.addChild(subLevel1Node2);
        
        assertFalse( tree.is_balanced() );
        assertEquals(4, tree.level());
    }

}
