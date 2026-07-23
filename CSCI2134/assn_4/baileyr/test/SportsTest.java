import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

public class SportsTest {

    @Test
    public void testSports() {
        Sports sportsInterest = new Sports("Hockey");

        assertEquals("Sports Hockey", sportsInterest.toString(), "Interest not created");
    }

    @Test
    public void testSportsToString() {
        Sports sportsInterest = new Sports("Hockey");

        assertEquals("Sports Hockey", sportsInterest.toString(), "Interest could not be converted to string");
    }

    @Test
    public void testSportsEquals() {
        Sports sportsInterest = new Sports("Hockey");
        Sports sportsInterest2 = new Sports("Hockey");

        assertEquals(sportsInterest, sportsInterest2, "Interest not equal");
    }
}
