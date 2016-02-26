package phatthanaphong.city;

/**
 * Created by phatthanaphong on 25/2/2559.
 */
public class LocationModel {
    private double latitude;
    private double longitude;
    private double altitude;
    private float speed;
    private float accuracy;
    private long time;
    private int id;

    public LocationModel(int id,double latitude,double longitude,double altitude,float speed,float accuracy,long time){
        this.id = id;
        this.latitude = latitude;
        this.longitude = longitude;
        this.altitude = altitude;
        this.speed = speed;
        this.accuracy = accuracy;
        this.time = time;
    }

    public LocationModel(double latitude,double longitude,double altitude,float speed,float accuracy,long time){
        this.latitude = latitude;
        this.longitude = longitude;
        this.altitude = altitude;
        this.speed = speed;
        this.accuracy = accuracy;
        this.time = time;
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

    public double getAltitude() {
        return altitude;
    }

    public float getSpeed() {
        return speed;
    }

    public float getAccuracy() {
        return accuracy;
    }
}
