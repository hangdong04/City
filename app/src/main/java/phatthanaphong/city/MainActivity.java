package phatthanaphong.city;

import android.app.ActivityManager;
import android.content.Context;
import android.content.Intent;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;
import android.widget.Toast;

import de.greenrobot.event.EventBus;

public class MainActivity extends AppCompatActivity{
    public static final String TAG = "MainActivity";
    Button button;
    TextView textView;
    Intent serviceIntent;
    private EventBus eventBus = EventBus.getDefault();
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        // check if GPS enabled.
        serviceIntent = new Intent(this, BackgroundService.class);
        button = (Button) findViewById(R.id.button);
        button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                eventBus.post(new BackupDatabaseEvent(BackupDatabaseEvent.BACKUP_DATABASE));
            }
        });
        textView = (TextView)findViewById(R.id.textDetail);

    }

    @Override
    protected void onResume() {
        if (!eventBus.isRegistered(this)){
            eventBus.register(this);
        }
        Log.d(TAG, "onResume");
        if (!isMyServiceRunning(BackgroundService.class)) {
            Log.d(TAG, "onResume: StartBackkkkkkkkkkkkk");
            startService(serviceIntent);
        }
        super.onResume();
    }

    @Override
    protected void onPause() {
        eventBus.unregister(this);
        super.onPause();
    }

    public void onEvent(NotifyLocationEvent notifyLocationEvent) {
        updateUI();
    }
    private void updateUI(){
        double latitude = BackgroundService.gps.getLatitude();
        double longitude = BackgroundService.gps.getLongitude();
        double altitude = BackgroundService.gps.getAltitude();
        float accuracy = BackgroundService.gps.getAccuracy();
        float speed = BackgroundService.gps.getSpeed();
        long time = BackgroundService.gps.getTime();
        Toast.makeText(this, "Update!", Toast.LENGTH_LONG).show();
        textView.setText("Your Location is - \nLat: " + latitude + "\nLong: " + longitude +"\nAlti"+altitude + "\nAcc"+accuracy+"\nSpeed"+speed+"\nTime"+time);
    }

    private boolean isMyServiceRunning(Class<?> serviceClass) {
        ActivityManager manager = (ActivityManager) getSystemService(Context.ACTIVITY_SERVICE);
        for (ActivityManager.RunningServiceInfo service : manager
                .getRunningServices(Integer.MAX_VALUE)) {
            if (serviceClass.getName().equals(service.service.getClassName())) {
                return true;
            }
        }

        return false;
    }
}
