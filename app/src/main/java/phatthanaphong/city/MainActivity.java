package phatthanaphong.city;

import android.app.ActivityManager;
import android.content.Context;
import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.os.Environment;
import android.support.v7.app.AppCompatActivity;
import android.util.Log;
import android.view.Menu;
import android.view.MenuInflater;
import android.view.MenuItem;
import android.view.View;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.TextView;
import android.widget.Toast;
import com.weiwangcn.betterspinner.library.material.MaterialBetterSpinner;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.io.StreamCorruptedException;
import java.util.Random;

import de.greenrobot.event.EventBus;

public class MainActivity extends AppCompatActivity{
    public static final String TAG = "MainActivity";
    public static final String[] MODELIST = {"Walk", "Bicycle", "Motorcycle", "Car", "Transit", "Running"};
    Button saveButton;
    TextView textView;
    TextView header;
    Intent serviceIntent;
    MyPreference myPreference;
    Button submitButton;
    String mode;
    MaterialBetterSpinner spinner;
    Button startButton;
    DatabaseHandler db;
    int num;
    private EventBus eventBus = EventBus.getDefault();
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        Log.d("TAG", "onCreate");
        setContentView(R.layout.activity_main);
        myPreference = new MyPreference(this);
        db = new DatabaseHandler(this);
        serviceIntent =new Intent(this, LocationService.class);
        myPreference.saveState(0);
        ArrayAdapter<String> arrayAdapter = new ArrayAdapter<String>(this,
                android.R.layout.simple_dropdown_item_1line, MODELIST);
        num = myPreference.getNum();
        spinner = (MaterialBetterSpinner)findViewById(R.id.spinner);
        spinner.setAdapter(arrayAdapter);
        submitButton = (Button)findViewById(R.id.submitButton);
        submitButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                mode = spinner.getText().toString();
                if (mode.equals("")){
                    spinner.setError(getString(R.string.spinner_error));
                }
                else {
                    myPreference.saveState(1);
                    myPreference.saveLabel(mode);
                    setHeader();
                }
            }
        });
        saveButton = (Button) findViewById(R.id.saveButton);
        saveButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                backupDBonSDcard(getApplicationContext(),"GpsLog.db");
            }
        });
        startButton = (Button)findViewById(R.id.startButton);
        startButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if (myPreference.getButtonState()== 0){
                    myPreference.saveButtonState(1);
                    init();
                    updateUI();
                    startService(serviceIntent);
                }else {
                    myPreference.saveButtonState(0);
                    myPreference.saveState(0);
                    init();
                    updateUI();
                    myPreference.saveNum(num+1);
                    stopService(serviceIntent);
                }
            }
        });
        textView = (TextView)findViewById(R.id.textDetail);
        header = (TextView) findViewById(R.id.header);
    }
    private void init(){
        if (myPreference.getButtonState() == 0){
            startButton.setText(getString(R.string.start_text));
        }
        else {
            startButton.setText(getString(R.string.stop_text));
        }
    }

    @Override
    protected void onResume() {
        num = myPreference.getNum();
        Log.d("TAG", "onResume");
        init();
        updateUI();
        if (!eventBus.isRegistered(this)){
            eventBus.register(this);
        }
        Log.d(TAG, "onResume");
        super.onResume();
    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        MenuInflater inflater = getMenuInflater();
        inflater.inflate(R.menu.menu, menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        switch(item.getItemId())
        {
            case R.id.send_log:
                sendEmail(this);
            case R.id.clear_log:
                flushLog();
        }
        return true;
    }

    @Override
    protected void onPause() {
        Log.d("TAG", "onPause");
        eventBus.unregister(this);
        super.onPause();
    }

    @Override
    public void onBackPressed() {
        moveTaskToBack(true);
    }

    public void onEvent(NotifyLocationEvent notifyLocationEvent) {
        updateLocation();
    }

    private void setHeader(){
        String text;
        text = "Transportation mode: "+mode;
        header.setText(text);
        updateUI();
    }

    private void updateUI(){
        if (myPreference.getState() == 1){
            header.setVisibility(View.VISIBLE);
            submitButton.setVisibility(View.GONE);
            spinner.setVisibility(View.GONE);
            startButton.setVisibility(View.VISIBLE);
        }else {
            header.setVisibility(View.GONE);
            submitButton.setVisibility(View.VISIBLE);
            spinner.setVisibility(View.VISIBLE);
            startButton.setVisibility(View.GONE);
        }
    }
    private void updateLocation(){
        saveButton.setVisibility(View.VISIBLE);
        textView.setVisibility(View.VISIBLE);
        LocationModel location = LocationService.locationModel;
        double latitude = location.getLatitude();
        double longitude = location.getLongitude();
        float accuracy = location.getAccuracy();
        float speed = location.getSpeed();
//        Toast.makeText(this, "Update!", Toast.LENGTH_SHORT).show();
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

    private boolean checkDataBase(String fileName) {
        java.io.File dbFile = new java.io.File(fileName);
        return dbFile.exists();
    }

    private void flushLog(){
        db.flushLocation();
    }

    private void sendEmail(Context ctx){
        File backupDB = null;
        backupDB = new File(Environment.getExternalStorageDirectory().getAbsolutePath(), "GpsLog.db");
        Intent emailIntent = new Intent(android.content.Intent.ACTION_SEND);
        emailIntent.setType("*/*");
        emailIntent.putExtra(android.content.Intent.EXTRA_EMAIL,
                new String[] { "phatthanaphong_th@cmu.ac.th" });

        Random r = new Random();

        emailIntent.putExtra(android.content.Intent.EXTRA_SUBJECT,
                "Local db " + r.nextInt());
        emailIntent.putExtra(Intent.EXTRA_STREAM, Uri.fromFile(backupDB));
        ctx.startActivity(Intent.createChooser(emailIntent, "Export database"));
    }
    private void backupDBonSDcard(Context context, String dbName){
        String DB_PATH = context.getDatabasePath(dbName).getPath();
        Log.d("DB_PATH:" , DB_PATH);
        if(checkDataBase(DB_PATH)){
            InputStream myInput;
            try {
                Log.e("DB","[backupDBonSDcard] saving file to SDCARD");
                Toast.makeText(this,"Successful",Toast.LENGTH_SHORT).show();
                myInput = new FileInputStream(DB_PATH);

                // Path to the just created empty db
                String outFileName = Environment.getExternalStorageDirectory().getAbsolutePath() + java.io.File.separator + dbName;

                //Open the empty db as the output stream
                OutputStream myOutput = null;
                try {
                    myOutput = new FileOutputStream(outFileName);
                    //transfer bytes from the inputfile to the outputfile
                    byte[] buffer = new byte[1024];
                    int length;
                    while ((length = myInput.read(buffer))>0){
                        myOutput.write(buffer, 0, length);
                    }
                } catch (IOException e) {
                    // TODO Auto-generated catch block
                    e.printStackTrace();
                } finally {
                    //Close the streams
                    try {

                        if (myOutput != null) {
                            myOutput.flush();
                            myOutput.close();
                        }

                        if (myInput != null)
                            myInput.close();
                    }catch (IOException e){
                        e.printStackTrace();
                    }
                }
            } catch (FileNotFoundException e1) {
                // TODO Auto-generated catch block
                e1.printStackTrace();
            }

        }else{
            Log.d("DB",dbName+" not found");
        }
    }
}