/*
Interest.java

class used to manage the interests of a user by representing them
with a category and name

 */
public class Interest{

    public String categoryName;
    public Object category;

    public Interest(String interest, String categoryName) {
        this.categoryName = categoryName;
        if(interest.equals("TV")){
            category = new TV(categoryName);
        }
        else if(interest.equals("Sports")){
            category = new Sports(categoryName);
        }
        else{
            category = null;
        }
    }

    public boolean equals(Object o){
        if (this == o){
            return true;
        }
        if (o == null || getClass() != o.getClass()){
            return false;
        }
        Interest that = (Interest) o;
        return (category != null ? category.equals(that.category) : that.category == null) &&
                (categoryName != null ? categoryName.equals(that.categoryName) : that.categoryName == null);
    }

    public Object getCategory(){return category;}
}
