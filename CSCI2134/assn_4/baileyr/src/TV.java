public class TV{

    private String categoryName;
    private String category;

    public TV(String categoryName){
        category = "TV";
        this.categoryName = categoryName;
    }

    @Override
    public String toString(){
        return "TV "+categoryName;
    }

    @Override
    public boolean equals(Object obj){
        if(this == obj){
            return true;
        }
        if(obj == null || obj.getClass() != this.getClass()){
            return false;
        }
        TV that = (TV)obj;
        return (category != null ? category.equals(that.category) : that.category == null) &&
                (categoryName != null ? categoryName.equals(that.categoryName) : that.categoryName == null);
    }
}
