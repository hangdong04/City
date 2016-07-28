package phatthanaphong.city;

/**
 * Created by phatthanaphong on 25/2/2559.
 */
public class LocationModel {
    private double latitude;
    private double longitude;
    private float speed;
    private float accuracy;
    private long time;
    private int id;
    private int num;

    private float angle;
    private String label;

    public LocationModel(String label, int id,double latitude,double longitude,float speed,float accuracy,long time,float angle){
        this.label = label;
        this.id = id;
        this.latitude = latitude;
        this.longitude = longitude;
        this.speed = speed;
        this.accuracy = accuracy;
        this.time = time;
        this.angle = angle;
    }


    public LocationModel(int num, String label, double latitude, double longitude, float speed, float accuracy, long time, float angle){
        this.num = num;
        this.label = label;
        this.latitude = latitude;
        this.longitude = longitude;
        this.speed = speed;
        this.accuracy = accuracy;
        this.time = time;
        this.angle = angle;
    }

    public int getNum() {
        return num;
    }

    public void setNum(int num) {
        this.num = num;
    }

    public float getAngle() {
        return angle;
    }

    public void setAngle(float angle) {
        this.angle = angle;
    }

    public int getId() {
        return id;
    }

    public long getTime() {
        return time;
    }

    public double getLatitude() {
        return latitude;
    }

    public double getLongitude() {
        return longitude;
    }

    public float getSpeed() {
        return speed *3.6f;
    }
    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }

    public float getAccuracy() {
        return accuracy;
    }
}
