
public class Sports{

    private String category;
    private String categoryName;

    public Sports(String categoryName) {
        category = "Sports";
        this.categoryName = categoryName;
    }


    @Override
    public String toString(){
        return "Sports "+ categoryName;
    }

    @Override
    public boolean equals(Object obj){
        if(this == obj){
            return true;
        }
        if(obj == null || obj.getClass() != this.getClass()){
            return false;
        }
        Sports that = (Sports)obj;
        return (category != null ? category.equals(that.category) : that.category == null) &&
                (categoryName != null ? categoryName.equals(that.categoryName) : that.categoryName == null);
    }


}
