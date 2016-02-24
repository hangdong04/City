package phatthanaphong.city;

import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity{
    Button btnShowLocation;
    GPSTracker gps;
    TextView textView;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        // check if GPS enabled
        btnShowLocation = (Button) findViewById(R.id.btnShowLocation);
        textView = (TextView)findViewById(R.id.textDetail);

        // show location button click event
        btnShowLocation.setOnClickListener(new View.OnClickListener() {

            @Override
            public void onClick(View arg0) {
                // create class object
                gps = new GPSTracker(MainActivity.this);

                // check if GPS enabled
                if(gps.canGetLocation()){

                    double latitude = gps.getLatitude();
                    double longitude = gps.getLongitude();
                    double altitude = gps.getAltitude();
                    float accuracy = gps.getAccuracy();
                    float speed = gps.getSpeed();
                    long time = gps.getTime();
                    textView.setText("Your Location is - \nLat: " + latitude + "\nLong: " + longitude +"\nAlti"+altitude + "\nAcc"+accuracy+"\nSpeed"+speed+"\nTime"+time);

                }else{
                    // can't get location
                    // GPS or Network is not enabled
                    // Ask user to enable GPS/network in settings
                    gps.showSettingsAlert();
                }

            }
        });
    }
}
