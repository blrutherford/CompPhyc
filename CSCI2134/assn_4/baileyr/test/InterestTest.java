import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

public class InterestTest {

    private final String sportsInterest = "Sports Hockey";

    @Test
    void testContructor(){
        Interest interest = new Interest("Sports", "Hockey");
        Interest interest2 = new Interest("TV", "Bridgerton");

        assertEquals("Sports Hockey", interest.category.toString(), "Interest not created");
        assertEquals("TV Bridgerton", interest2.category.toString(), "Interest not created");
    }

    @Test
    void testEquals(){
        Interest interest = new Interest("Sports", "Hockey");
        Interest interest2 = new Interest("Sports", "Hockey");

        Interest interest3 = new Interest("TV", "Bridgerton");
        Interest interest4 = new Interest("TV", "Bridgerton");

        assertEquals(interest, interest2, "Interest not equal");
        assertEquals(interest3, interest4, "Interest not equal");
    }
}
