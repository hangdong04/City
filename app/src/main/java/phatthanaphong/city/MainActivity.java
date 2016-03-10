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

import com.github.clans.fab.FloatingActionButton;
import com.github.clans.fab.FloatingActionMenu;

import de.greenrobot.event.EventBus;

public class MainActivity extends AppCompatActivity{
    public static final String TAG = "MainActivity";
    Button saveButton;
    Button startButton;
    TextView textView;
    TextView header;
    String title;
    Intent serviceIntent;
    Boolean start = false;
    public static String label;
    FloatingActionMenu mainMenu;
    FloatingActionButton walkButton;
    FloatingActionButton biButton;
    FloatingActionButton motorButton;
    FloatingActionButton carButton;
    FloatingActionButton transitButton;
    FloatingActionButton runningButton;
    MyPreference myPreference;

    private EventBus eventBus = EventBus.getDefault();
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        myPreference = new MyPreference(this);
        serviceIntent = new Intent(this, BackgroundService.class);
        mainMenu = (FloatingActionMenu) findViewById(R.id.mainMenu);
        saveButton = (Button) findViewById(R.id.saveButton);
        saveButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                eventBus.post(new BackupDatabaseEvent(BackupDatabaseEvent.BACKUP_DATABASE));
            }
        });
        textView = (TextView)findViewById(R.id.textDetail);
        header = (TextView) findViewById(R.id.header);
        walkButton = (FloatingActionButton)findViewById(R.id.walkButton);
        walkButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                title = getString(R.string.header_mode)+getString(R.string.walk_mode);
                header.setText(title);
                myPreference.saveLabel(getString(R.string.walk_mode));
            }
        });
        biButton = (FloatingActionButton)findViewById(R.id.bicycleButton);
        biButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                title = getString(R.string.header_mode)+getString(R.string.bicycle_mode);
                header.setText(title);
                myPreference.saveLabel(getString(R.string.bicycle_mode));
            }
        });
        motorButton = (FloatingActionButton)findViewById(R.id.motorcycleButton);
        motorButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                title = getString(R.string.header_mode)+getString(R.string.motorcycle_mode);
                header.setText(title);
                myPreference.saveLabel(getString(R.string.motorcycle_mode));
            }
        });
        carButton = (FloatingActionButton)findViewById(R.id.carButton);
        carButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                title = getString(R.string.header_mode)+getString(R.string.car_mode);
                header.setText(title);
                myPreference.saveLabel(getString(R.string.car_mode));
            }
        });
        transitButton = (FloatingActionButton)findViewById(R.id.transitButton);
        transitButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                title = getString(R.string.header_mode)+getString(R.string.transit_mode);
                header.setText(title);
                myPreference.saveLabel(getString(R.string.transit_mode));
            }
        });
        runningButton = (FloatingActionButton)findViewById(R.id.runButton);
        runningButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                title = getString(R.string.header_mode)+getString(R.string.running_mode);
                header.setText(title);
                myPreference.saveLabel(getString(R.string.running_mode));
            }
        });

    }

    @Override
    protected void onResume() {
        if (!eventBus.isRegistered(this)){
            eventBus.register(this);
        }
        if (!isMyServiceRunning(BackgroundService.class)){
            startService(serviceIntent);
        }
        Log.d(TAG, "onResume");
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
        float accuracy = BackgroundService.gps.getAccuracy();
        float speed = BackgroundService.gps.getSpeed();
        Toast.makeText(this, "Update!", Toast.LENGTH_SHORT).show();
        textView.setText("Your Location is \nLatitude: " + latitude + "\nLongitude: " + longitude +"\nAccuracy: "+accuracy+"\nSpeed: "+speed);
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
