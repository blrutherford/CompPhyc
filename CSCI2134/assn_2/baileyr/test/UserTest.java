import static org.junit.jupiter.api.Assertions.*;

import java.util.ArrayList;
import java.util.Scanner;

import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.Test;

class UserTest {
  private static String[] friendNames = {"Alice", "Bob", "Carol"};

  // clear the static users HashMap before each test
  @AfterEach
  void clearUsers() {
    User.users.clear();
  }

  // Test constructing a user adds them to the HashMap
  @Test
  void testConstructor() {
    User u = new User(friendNames[0]);
    assertEquals(friendNames[0], u.name, "Incorrect name");
    assertEquals(1, User.users.size(), "Incorrect size");
    assertEquals(u, User.users.get(friendNames[0]), "User not in HashMap");
  }

  /**
   *Tests a username is returned for a given user
   */
  @Test
  void testFind() {
    User user = new User(friendNames[0]);
    User found = User.find("Alice");
      assertEquals(user, found, "User not found");
  }

  /**
   * Test to make sure if no user exists, return null
   */
  @Test
  void testFind_noUser(){
    User found = User.find("Dave");
    assertNull(found, "This user was found");
  }

  /**
   *Tests if a user successfully friended another user
   */
  @Test
  void testFriend() {
    User user1 = new User(friendNames[0]);
    User user2 = new User(friendNames[1]);

    int user1AdjSize = user1.adj.size();
    int user2AdjSize = user2.adj.size();

    User friend = user1.friend(friendNames[1]);

    assertEquals(user2, friend, friendNames[0]+" did not friend "+friendNames[1]);
    assertEquals(user1AdjSize+1, user1.adj.size(), "User2 was not added to User1's network");
    assertEquals(user2AdjSize+1, user2.adj.size(), "User1 was not added to User2's network");
  }

  /**
   * Tests if user friendship stays the same when they are already friends
   */
  @Test
  void testFriend_alreadyFriends(){
    User user1 = new User(friendNames[0]);
    User user2 = new User(friendNames[1]);
    user1.friend(friendNames[1]);

    int user1SizeAdjBefore = user1.adj.size();
    int user2SizeAdjBefore = user2.adj.size();

    user1.friend(friendNames[1]);

    assertEquals(user1SizeAdjBefore, user1.adj.size(),
            "User1 map size should not change when the users are already friends");
    assertEquals(user2SizeAdjBefore, user2.adj.size(),
            "User2 map size should not change when the users are already friends");

    assertTrue(user1.adj.containsKey(friendNames[1]),
            "User1 should still be friend with User2");
    assertTrue(user2.adj.containsKey(friendNames[0]),
            "User2 should still be friend with User1");
  }

  /**
   * Tests if unfriending a user is successful
   */
  @Test
  void testUnfriend() {
    User user1 = new User(friendNames[0]);
    User user2 = new User(friendNames[1]);
    user1.friend(friendNames[1]);

    assertEquals(user2, user1.unfriend(friendNames[1]), "User1 did not unfriend User2");
    assertEquals(0, user1.adj.size(), "User1 should remove User2 from network");
    assertEquals(0, user2.adj.size(), "User2 should remove User1 from network");
  }

  /**
   * Tests if unfriending a user who is not a friend is allowed
   */
  @Test
  void testUnFriend_notFriends(){
    User user1 = new User(friendNames[0]);
    User user2 = new User(friendNames[1]);

    int user1SizeAdjBefore = user1.adj.size();
    int user2SizeAdjBefore = user2.adj.size();

    user1.unfriend(friendNames[1]);

    assertEquals(user1SizeAdjBefore, user1.adj.size());
    assertEquals(user2SizeAdjBefore, user2.adj.size());
  }

  /**
   * Tests if user was removed from the network with no friends
   */
  @Test
  void testLeave() {
    User user1 = new User(friendNames[0]);

    user1.leave();

    assertFalse(user1.adj.containsKey(friendNames[0]), "User1 should not be in the network");
  }

  /**
   * Tests if user was removed from friends network
   */
  @Test
  void testLeave_withFriends(){
    User user1 = new User(friendNames[0]);
    User user2 = new User(friendNames[1]);

    user1.friend(friendNames[1]);

    int user1SizeAdjBefore = user1.adj.size();

    user1.leave();

    assertEquals(user1SizeAdjBefore-1, user1.adj.size());
    assertTrue(user1.adj.containsKey(friendNames[1]), "User1 should not be in the network");
    assertFalse(user2.isFriend(user1), "User1 should be removed from friends list");
  }

  /**
   * Tests if user is friends with another user
   */
  @Test
  void testIsFriend() {
    User user1 = new User(friendNames[0]);
    User user2 = new User(friendNames[1]);

    user1.friend(friendNames[1]);

    assertTrue(user1.isFriend(user2), "User1 should be friends with User 2");
  }

  /**
   * Tests if user is friends with a user they are not friends with
   */
  @Test
  void testIsFriend_notFriends(){
    User user1 = new User(friendNames[0]);
    User user2 = new User(friendNames[1]);
    User user3 = new User(friendNames[2]);

    user1.friend(friendNames[1]);

    assertTrue(user1.isFriend(user3), "User1 should not be friends with User 3");
  }

  // add more tests as needed using white-box, black-box or a mix of testing strategies
  // Note: you need to add multiple tests for each method in User.java
}