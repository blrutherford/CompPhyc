import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

public class TVTest {

    @Test
    public void testTV() {
        TV tvInterest = new TV("Bridgerton");

        assertEquals("TV Bridgerton", tvInterest.toString(), "Interest could not be created");
    }

    @Test
    public void testTVToString() {
        TV tv = new TV("Bridgerton");

        assertEquals("TV Bridgerton", tv.toString(), "Interest could not be converted to String");
    }

    @Test
    public void testTVEquals() {
        TV tv = new TV("Bridgerton");
        TV tv2 = new TV("Bridgerton");

        assertEquals(tv, tv2, "Interest are not equals");
    }
}
